# Decisions

## D-0001 — Keep one active proof node

- **Status:** superseded by D-0006
- **Former decision:** `G1c / Q-0015` was the only active main-proof node.
- **Reason for supersession:** the near-lossless charging contract was found to
  conflate a sufficient recurrence mechanism with the expected mechanism of the
  \(1/4\) stability theorem.

## D-0002 — Keep three capacity ledgers separate

- **Status:** active
- **Decision:** root/configuration budget, projection-sensitive slot capacity,
  and global real-edge capacity are different resource types.
- **Reason:** feasibility in one ledger does not imply feasibility in another.
- **Consequences:** code uses distinct types and tests cross-ledger misuse.

## D-0003 — Treat raw conversations as immutable sources

- **Status:** active
- **Decision:** move raw conversations to `sources/raw/conversations/` and do not
  rewrite them.
- **Reason:** corrections belong in canonical registries and audits, while source
  chronology must remain inspectable.

## D-0004 — Reject status promotion from transition capping

- **Status:** active
- **Decision:** ordinary transition capping is not accepted as a proof of Q-0016
  or Q-0017.
- **Reason:** the required independent charging right has not been derived.
- **Related:** `knowledge/FAILURES.md`,
  `docs/framework/FW-50_PERSISTENT_BLOCKER.md`.

## D-0005 — Generated artifacts are script-owned

- **Status:** active
- **Decision:** committed experiment baselines and reports must identify their
  generator, parameters, result type, source commit, and payload hash.
- **Reason:** generated evidence must be reproducible and must not be manually
  edited.

## D-0006 — Make Route B the active proof strategy

- **Status:** active
- **Decision:** `S1 / Q-0018` is the only active main-proof node. Route B studies
  faithful global execution, exact zero-defect structure, reversible-core
  saturation, and quantitative stability.
- **Reason:** \(1/4\) need not be a \(100\%\) residual-charging theorem. Large
  unresolved mass may be evidence of a rigid critical structure rather than a
  debt that must receive an independent capacity entitlement.
- **Consequences:**
  - Q-0002/Q-0015 and the F-0042 heavy-excess recurrence are suspended as a main
    route;
  - Q-0017 is retargeted to zero-defect global normal form;
  - Q-0016 is retargeted to actual-support reversible-core saturation;
  - Q-0003–Q-0007 move into the main stability spine.
- **Reactivation rule:** Route A may be reactivated only by a new explicit
  decision and synchronized updates to `AGENTS.md`, `README.md`,
  `docs/PROJECT_STATE.yaml`, `docs/PROOF_DAG.md`, `knowledge/QUESTIONS.md`,
  `tools/check_repository.py`, and `HANDOFF_CURRENT.md`.

## D-0007 — Prove the exact theorem before the epsilon theorem

- **Status:** active
- **Decision:** Route B must first classify zero-defect faithful execution
  objects. Quantitative \(\varepsilon\)-stability is downstream.
- **Reason:** otherwise each new anomaly class risks becoming another unproved
  charging obligation, reproducing the Route-A drift.
- **Consequences:** a new defect definition is accepted only if its terms are
  natural and independently auditable; the desired binary forest, product
  support, or terminal contradiction cannot be inserted into the definition.

## D-0008 — Preserve Route-A results as supporting modules

- **Status:** active
- **Decision:** F-0034 and F-0036–F-0044 remain valid within their stated
  hypotheses and may be used inside Route B.
- **Reason:** changing the proof strategy does not refute exact mass identities,
  faithful lifts, Lyapunov laws, Hall orthogonalization, or conditional
  recurrence criteria.
- **Consequences:** using one of these modules does not reactivate the
  near-lossless charging acceptance criterion.
