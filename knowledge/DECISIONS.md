# Decisions

## D-0001 — Keep one active proof node

- **Status:** active
- **Decision:** `G1c / Q-0015` is the only active main-proof node.
- **Reason:** downstream conditional work cannot replace the missing near-lossless entrance and E-exit control.
- **Consequences:** handoff and immediate actions must focus on E-exit control unless this decision is explicitly superseded with evidence.

## D-0002 — Keep three capacity ledgers separate

- **Status:** active
- **Decision:** root/configuration budget, projection-sensitive slot capacity, and global real-edge capacity are different resource types.
- **Reason:** feasibility in one ledger does not imply feasibility in another.
- **Consequences:** code uses distinct types and tests cross-ledger misuse.

## D-0003 — Treat raw conversations as immutable sources

- **Status:** active
- **Decision:** move raw conversations to `sources/raw/conversations/` and do not rewrite them.
- **Reason:** corrections belong in canonical registries and audits, while source chronology must remain inspectable.

## D-0004 — Reject status promotion from transition capping

- **Status:** active
- **Decision:** ordinary transition capping is not accepted as a proof of Q-0016 or Q-0017.
- **Reason:** the required independent charging right has not been derived.
- **Related:** `knowledge/FAILURES.md`, `docs/framework/FW-50_PERSISTENT_BLOCKER.md`.

## D-0005 — Generated artifacts are script-owned

- **Status:** active
- **Decision:** committed experiment baselines and reports must identify their generator, parameters, result type, source commit, and payload hash.
- **Reason:** generated evidence must be reproducible and must not be manually edited.
