# Route-B LP/atlas bounded validation

## Metadata

- **Generator:** `enumerate/route_b_lp_atlas_validation.py`
- **Command:** `python enumerate/route_b_lp_atlas_validation.py --exact 200 --general4 200 --general5 50 --generated-at 2026-07-30T16:34:00Z --output evidence/experiments/route_b/baselines/route_b_lp_atlas_validation.json`
- **Result type:** `mixed-exhaustive-and-bounded-random`
- **Source baseline:** `cfadd24b52546d4d5800c4a3c5a75a2add86f928`
- **Generated at:** `2026-07-30T16:34:00Z`
- **Python:** `3.13.5`
- **Payload SHA-256:** `cf4aa0da128d738bb81bed13de51ace0bc81611c9290107f8577dd8afd2dfb9b`
- **Seeds:** `{'exact': 20260737, 'general4': 20260738, 'general5': 20260734}`

## Complete four-block binary spaces

The star-forest search is exhaustive over edge-minimal covers of the 4-cube:

```json
{
  "block_minimal": 50524,
  "multi_blocker_M": 50256,
  "nonnormal_N": 260,
  "normal_Q4": 8,
  "not_block_minimal": 4,
  "star_forests_total": 50528
}
```

After exposing `M` and nonnormal `N`, exactly the 8 normal Q4 models remain as
unexplained critical models in this bounded class.

The existing normal-Q4 release-policy generator was run in the same artifact:

```json
{
  "categories": {
    "edge-disjoint splice": 384,
    "same-pivot cylinder": 192,
    "unavoidable real-edge reuse": 192
  },
  "coordinate_perfect_matchings": 272,
  "future_complete_release_policies": 768,
  "minimum_distinct_real_edges_per_splice": {
    "8": 384
  },
  "normal_independent_states": 192,
  "normal_matchings": 8,
  "per_state_patterns": {
    "edge-disjoint splice | edge-disjoint splice | same-pivot cylinder | unavoidable real-edge reuse": 192
  }
}
```

## Fixed-seed b=3 searches

### Four-block exact covers

```json
{
  "attempts": 202,
  "classification": {
    "N_covered_or_same_edge_R_only": 200,
    "raw_q_cycle": 54,
    "reduced_q_cycle": 0
  },
  "raw_kernel_sizes": {
    "3 states/6 moves": 54
  },
  "target": 200,
  "unique_block_minimal_exact_covers": 200
}
```

Raw `Q` cycles in this sample are three-state/six-move kernels around one real
blocker edge. The actual-edge-history `R` reduction removes all of them.

### Four-block general edge-minimal covers

```json
{
  "attempts": 200,
  "classification": {
    "covered_after_MN_and_same_edge_reduction": 200,
    "reduced_q_only_cycle": 0,
    "reduced_residual_cycle": 0
  },
  "edge_count_distribution": {
    "27": 4,
    "28": 6,
    "29": 24,
    "30": 33,
    "31": 55,
    "32": 52,
    "33": 24,
    "34": 2
  },
  "target": 200,
  "unique_block_minimal_covers": 200
}
```

### Five-block general edge-minimal covers

```json
{
  "attempts": 50,
  "classification": {
    "covered_after_WMAN_and_R": 50,
    "reduced_q_core": 0,
    "reduced_residual_core": 0
  },
  "edge_count_distribution": {
    "27": 2,
    "28": 6,
    "29": 6,
    "30": 9,
    "31": 9,
    "32": 5,
    "33": 4,
    "34": 4,
    "35": 2,
    "36": 2,
    "37": 1
  },
  "seed": 20260734,
  "target": 50,
  "unique_models": 50
}
```

## Interpretation and nonclaims

Supported bounded observations:

- nonnormal unique-blocker Q4 recurrence must be treated as an `N` module;
- same-edge release oscillation must be removed before searching for a genuine
  residual multi-edge core;
- the committed fixed-seed b=3 sample contains no new reduced residual core.

Not supported:

- a general finite-atlas theorem;
- a general classification of reversible or codebook cores;
- a proof that no b=3 residual core exists;
- the one-quarter theorem.
