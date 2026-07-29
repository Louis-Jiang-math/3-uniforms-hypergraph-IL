# Normal-\(Q_4\) splice/pay/cylinder validation

## Metadata

- **Generator:** `enumerate/q4_splice_pay_cylinder_validation.py`
- **Command:** `python enumerate/q4_splice_pay_cylinder_validation.py`
- **Result type:** `bounded exhaustive`
- **Random seed:** none
- **Patch base:** `b56fe56d3fd7d4bf09c9b48113f50890d727aba7`
- **Historical source baseline:** `cfadd24b52546d4d5800c4a3c5a75a2add86f928`
- **Proposal run date:** 2026-07-30
- **Standalone generator SHA-256:** `7e4288e2057746589d3949c2a16a41ec8c927a7ac864b3a1c4fceb47be81627c`
- **Standalone payload SHA-256:** `0bb71f9c56b2f96d6f24a0b35ea38b03da5621f7a5b1e209eb41f934bec23236`

The hashes refer to the proposal-run files used to create this patch. Rerun the
committed generator after applying the patch; do not treat the hashes as a
post-commit source hash.

## Exhausted space

The script enumerates:

1. all 272 coordinate perfect matchings of the 4-cube;
2. all 8 normal matchings;
3. all 192 normal independent one-hole states;
4. all 768 future-complete pairs of release policies.

For each policy pair it checks:

- equality of the actual pivot;
- existence of a reconvergence using edge-simple paths;
- whether the two genealogies can be edge-disjoint;
- the minimum number of distinct actual edges used by an edge-disjoint splice.

## Results

```json
{
  "coordinate_perfect_matchings": 272,
  "normal_matchings": 8,
  "normal_independent_states": 192,
  "future_complete_release_policies": 768,
  "categories": {
    "same-pivot cylinder": 192,
    "edge-disjoint splice": 384,
    "unavoidable real-edge reuse": 192
  },
  "per_state_patterns": {
    "edge-disjoint splice | edge-disjoint splice | same-pivot cylinder | unavoidable real-edge reuse": 192
  },
  "minimum_distinct_real_edges_per_splice": {
    "8": 384
  }
}
```

Thus every normal state has the same \(2+1+1\) local policy pattern, and every
edge-disjoint splice candidate uses all eight real edges of the model.

## Interpretation

Supported bounded conclusions:

- the local splice/reuse/same-pivot classification is exhaustive in this model;
- splice is not a free repeatable closure operation;
- local same-pivot data is a distinct branch, not an automatic global cylinder.

Not supported:

- a general classification theorem;
- a positive global cylinder-mass theorem;
- a real-edge charging entitlement;
- a proof of Q-0016, Q-0017, Q-0018, or the one-quarter theorem.
