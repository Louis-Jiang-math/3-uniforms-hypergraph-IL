# Q-0015 immediate reset-compensation attack

## Classification

- **Result type:** exhaustive-bounded
- **Role:** refutation of an immediate-reset claim
- **General positive theorem:** none
- **Repository base:** `1da38011d28643eb8a3d35aa727d5fb206aacf41`
- **Generator:** `enumerate/q0015_reset_compensation.py`
- **Deterministic scope:** all transversal-edge subsets on three blocks of size two
- **Random seed:** none

## Command

```bash
python enumerate/q0015_reset_compensation.py \
  --generated-at 2026-07-29T12:00:00Z \
  --output artifacts/runs/q0015/reset_compensation_results.json
```

The generated JSON uses the repository `research-artifact-v1` envelope and a
SHA-256 hash of its payload.

## Claim attacked

\[
\text{carrier changes}
+
\text{no new blocker edge}
+
\text{no new carrier support}
\Longrightarrow
\text{immediate repetition of the full labelled state}.
\]

A full labelled state retains the hole block, selected one-hole partial
transversal, tested vertex, actual blocker edge and carrier pair.

## Minimal witness

Use three blocks of size two and the single edge

\[
e=\{0_0,1_0,2_0\}.
\]

| step | hole | selected | test | carrier |
|---:|---:|---|---|---|
| 0 | \(B_0\) | \(\{1_0,2_0\}\) | \(0_0\) | \(\{1_0,2_0\}\) |
| 1 | \(B_1\) | \(\{0_0,2_0\}\) | \(1_0\) | \(\{0_0,2_0\}\) |
| 2 | \(B_2\) | \(\{0_0,1_0\}\) | \(2_0\) | \(\{0_0,1_0\}\) |

All states use the same real edge. Before the last listed transition, both
endpoints of the next carrier have appeared, yet the destination is a new full
labelled state. A further move repeats the first orientation.

## Exhaustive result

There are \(2^8=256\) possible transversal-edge subsets.

- tested: 256;
- immediate counterexamples: 255;
- non-counterexamples: 1, the empty hypergraph.

This proves the immediate claim false in the stated finite model. It does not
bound orientation budgets in larger systems.

## Correct replacement

With resources fixed, each nonrepeating reset must consume a previously unused
future-compatible orientation token. If no token is consumed, a sound quotient
token repeats.

Future compatibility is essential: current trace, edge set or support alone is
not a valid quotient signature.
