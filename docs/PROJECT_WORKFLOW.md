# Project research workflow

This file adds project-specific sequencing to the general rules in `../agent.md` and `../WORKFLOW.md`.

## Start

1. Read `HANDOFF_CURRENT.md` and `docs/PROOF_DAG.md`.
2. Select the single active node.
3. Read its entries in `knowledge/FACTS.md`, `knowledge/FAILURES.md`, and `knowledge/QUESTIONS.md`.
4. Read the relevant framework, implementation, tests, and evidence.
5. Create a scoped change manifest before a substantial write.

## Work-product order

Prefer:

1. full theorem or implementation with tests;
2. strict counterexample;
3. formal normalization or certificate dichotomy;
4. precise smaller lemma;
5. bounded computational observation.

The fifth category cannot be promoted to the first.

## Project integrity audit

For each mathematical or computational step, check:

- real object identity and actual reachability;
- root projection and genealogy;
- separation of the three capacity ledgers;
- complete versus projected support;
- original question answer criterion;
- relevant failure signatures.

## Finish

Update evidence and registries first. Update `docs/PROOF_DAG.md`, `docs/PROJECT_STATE.yaml`, and `HANDOFF_CURRENT.md` only after the evidence passes validation. Handoff is rewritten as a current snapshot, not appended as a log.
