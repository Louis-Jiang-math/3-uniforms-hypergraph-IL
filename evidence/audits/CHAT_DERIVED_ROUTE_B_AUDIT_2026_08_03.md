# Chat-derived Route-B audit — 2026-08-03

## 1. Scope lock

```text
Task:
  Consolidate the mathematically audited discussion after F-0055 into the local
  repository and remove repeated renaming of the same Core Endgame gap.
Mode:
  implementation; supporting-fact/failure registration only
Base version:
  a7243dde288965b629948756fde42a9da2780d47
Target:
  Route-B supporting lemmas, actual recurrent-core structure, and the precise
  remaining actual-incidence obstruction.
Inputs:
  the local repository and the self-contained derivations recorded in this audit
Outputs:
  proof/audit evidence, canonical facts/failures/decisions, updated current state
Allowed paths:
  evidence/, knowledge/, docs/framework/, docs/PROJECT_STATE.yaml,
  docs/PROOF_DAG.md, README.md, HANDOFF_CURRENT.md
Forbidden paths:
  sources/raw/, history/, src/, tests/, enumerate/, generated baselines
Expected status change:
  no theorem or open question closed; supporting facts/failures only
Acceptance criteria:
  every promoted fact has a self-contained proof; every negative conclusion has
  an explicit counterexample or semantic failure; Q-0016 remains open
Required checks:
  repository required checks and git diff --check
Non-goals:
  no E1/E2/E3 closure, no Route-A reactivation, no one-quarter theorem claim
```

## 2. Classification

| Change | Object | Classification | Canonical effect |
|---|---|---|---|
| finite Markov state determines exact future interface | F-0056 | ADD, verified-conditional | supporting only |
| uniform sampling kills eventually-same-edge tails | F-0057 | ADD, verified-conditional | supporting only |
| fixed-pivot target-following | F-0058 | ADD, verified | supporting Core module |
| literal coordinate-splice closure is Cartesian | F-0059 | ADD, verified | supporting zero-set lemma |
| harmonic degree-budget compression | F-0060 | ADD, verified | exploratory algebra only |
| release-complete no-copy split | F-0061 | ADD, verified | repairs execution semantics |
| clean-epoch contraction and transient decay | F-0062 | ADD, verified-conditional | transient supporting theorem |
| all-release core completion identities | F-0063–F-0066 | ADD, verified | actual Core structure |
| maximal-reuse synchronization–dispersion theorem | F-0067 | ADD, verified | exact matching dichotomy |
| global E1/E2 closure from conditional objects | A-0036 | ADD, failed | no status promotion |
| policy-generated pivot switch as natural defect | A-0037 | ADD, failed | release branches must be retained |
| degree-budget/shadow relaxation as harmonic proof | A-0038 | ADD, refuted | pairing data required |
| open-hole queue as actual release dynamics | A-0039 | ADD, failed | wrong state semantics |
| Core target-follow ledger identified with F-0051 \(G_A\) | A-0040 | ADD, failed | separate second-stage ledger |
| switch-map dispersion implies spare edge capacity | A-0041 | ADD, refuted-formal | Latin-square array |
| repeated aliases for the same Core gap | A-0042 | ADD, strategy drift | freeze Q-0016 vocabulary |

## 3. What is genuinely new

The completion–switch representation gives, for each maximum-multiplicity real
edge \(e\), a family of injections
\[
\pi_W:S(e)\longrightarrow E(H)
\qquad (W\in\Omega_e)
\]
whose average is a fractional matching.  This yields a rigorous
synchronization–dispersion dichotomy and a strong exact-synchronization
structure.

The discussion also produced exact all-release recurrent-core identities:
triangle decomposition, weighted context regularity, common-state
multiplicities, target-following forced off-pivot mass, and a static bound for
pairwise incompatible real-edge families.

These are real additions.  They do not prove the final conversion
\[
\text{high actual context reuse}
\Longrightarrow
\text{large link, complete-block reduction, exact cover, or recurrence loss}.
\]

## 4. What is not new

The phrases

- causal Hall/reuse conversion;
- actual-incidence mixing;
- context compression;
- maximal-reuse synchronization;
- Actual Latin-Mixing Conversion;

have all referred to the same unresolved implication at different resolutions.
Introducing a new name does not change the proof DAG.  The canonical location is
Q-0016, Actual-support Core Endgame.

## 5. Frozen working bottleneck

The current strict subproblem inside Q-0016 is:

> Given a maximum-context-multiplicity edge whose completion–switch fractional
> matching is saturated, use the actual three-vertex incidence, reversible
> switch maps, and no-IT/block-minimal hypotheses to obtain a real terminal
> outcome or a quantitative recurrence loss.

Matrix dispersion alone is insufficient: the cyclic array
\[
\pi_t(s)=s+t\pmod q
\]
is fully dispersed while every label column is saturated.  Conversely, exact
synchronization alone yields bijective context transport and common fixed
endpoint pairs, but not product support without an actual expansion theorem.

## 6. Status judgment

No canonical proof node is promoted.  Q-0016, Q-0017, Q-0018, and the
one-quarter theorem remain open.  The update narrows Q-0016 and prevents further
taxonomy drift.
