# Q-0019 rank-two rollback/zipper patch scope

- **Base commit:** `326425f`
- **Write mode:** implementation (no status promotion of Q-0019 or the main theorem)
- **Task:** integrate the mathematically meaningful results from the supplied proof-gap conversations and the current rank-two numerical investigation into auditable repository evidence, registries, experiments, and the current handoff.
- **Target DAG node:** `S1 / Q-0019`
- **Inputs:** the repository at `326425f`; the supplied proof-gap conversation exports; the current conversation's rank-two incidence calculations.
- **Outputs:** one self-contained proof/route note; one compression audit; one deterministic finite generator with tests; one generated experiment artifact/report/manifest; synchronized facts, failures, decision, Q-0019, DAG/state/handoff/status/README, and changelog.
- **Allowed paths:** `README.md`, `HANDOFF_CURRENT.md`, `docs/`, `knowledge/`, `evidence/`, `enumerate/`, `tests/`, `tools/check_generated_artifacts.py`, `history/CHANGELOG.md`.
- **Forbidden paths:** `sources/raw/`, `old/`, unrelated source modules, manuscript theorem claims, Git history.
- **Expected status change:** none for the theorem or Q-0019. New finite results may be recorded as `observed`; elementary self-contained lemmas may be recorded as formal/conditional facts within their exact hypotheses.
- **Acceptance criteria:** preserve the fork--inverse-fiber--anchor umbrella route; make the current rank-two frontier explicit; record refuted shortcuts; distinguish proof from finite computation; provide reproducible bounded evidence; do not claim `P^2 -> P` or close Q-0019.
- **Required checks:** `python -m compileall -q src enumerate tools tests`; `python -m pytest -q`; `python tools/check_repository.py`; `python tools/check_generated_artifacts.py`; run the new rank-two generator and compare its key payload to the committed baseline.
- **Non-goals:** proving the one-quarter theorem; promoting bounded computations to an asymptotic theorem; restoring deprecated migration-taxonomy or direct-macro routes; editing raw conversations.
- **Final status:** validated
