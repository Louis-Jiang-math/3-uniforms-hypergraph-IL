# Net progress log

只记录证明状态的净变化，不记录“新增文档行数”或一般探索。


## 2026-08-04 — Root-excess and actual switch-cube route clarification

### Proved-formal supporting

- F-0068: a fixed actual switch output edge can arise from at most one slot of a
  fixed input edge, uniformly over all completion contexts;
- F-0069: perfect transition cycles have trivial monodromy and decompose into
  completion sheets;
- F-0070: legal-interval two-step root failures satisfy the exact root-only
  canonical excess normalization.

### Strategy clarification

D-0012 fixes the implementation route:

\[
\text{root-only canonical excess}
\to
\text{actual switch-cube core defect}
\to
\text{F-0041 fresh-leaf split}
\to
\text{three-cylinder regeneration}
\to
\text{F-0042}.
\]

Root capacity is not refreshed on release descendants. Dynamic descendant
charging, static core Hall compression, abstract Latin dispersion, and finite
token-universe exhaustion are not main-route substitutes.

### Canonical status

Q-0016, Q-0017, Q-0018, S1--S5, and the one-quarter theorem remain open. The
switch-cube defect inequality, clean-chart reduction of \(\Xi_I\), and
three-cylinder fresh-token conversion are not promoted.

## 2026-07-29 — Q-0015 aggregate heavy-excess reduction

### Proved-formal

- no-configuration 义务无损重标为 surviving external-old-anchor blocker；
- old-anchor profile 精确稳定恒等式与 genealogy 内 temporal Lyapunov；
- 实际二步失败的 aggregate-cylinder 质量恒等式；
- 统一 old/fresh pair-flat 界及精确 heavy-excess 余项 \(\mathfrak H_k\)；
- future-compatible orientation-budget reset compensation。

### Refuted-bounded-exhaustive

- “无新 blocker edge、无新 carrier support 则第一次 reset 立即闭合”；
- 三块二元的全部 \(2^8\) 模型中，255 个非空模型给出反例。

### Conditional reduction

若能以 \(\rho\) 支付或 telescoping 全部 \(\mathfrak H_k\)，且

\[
(1+\eta)(1/4-\varepsilon)+\rho<1/4,
\]

则直接得到 \(c_\varepsilon<1/4\) 的二阶递推。

### Canonical status

Q-0015/G1c 保持 active；Q-0016、Q-0017 和 one-quarter theorem 保持 open。

## 2026-07-28 — Documentation and latest-dialogue audit

### Proved-formal

- 建立 Q-0015 实根障碍的规范未来完备提升二分：
  有限命名 E 出口，或质量/账本无损的 future-complete persistent blocker。
- 明确 C/I/E 单步分类与最小割对 C 结构弧闭合。
- 在无 E 且块极小无 IT 时，至少存在真实 persistent-blocker 分支。

### Definitions/specifications

- AMCG 被整理为质量守恒与 provenance 的审计规格。
- 规范无原子细化可实现分数质量拆分，但不创造收费权。

### Claims withdrawn or narrowed

- 撤回“AMCG + ordinary transition capping 已证明 Q-0016/Q-0017”。
- ordinary transition 的额外 real-edge charging right 尚未证明。
- Q-0016、Q-0017 保持 open。
- 深度二 \(Q_4\) 枚举只登记为 computational observation。

### Critical-path change

当前工作从孤立扩展 Q-0016/Q-0017 抽象模型，回到 G1c：
定量控制 Q-0015 的 E 类最短前缀质量。

### Main theorem nodes closed

无。

## 2026-07-28 — Repository workflow restructure

### Governance and reproducibility

- separated the reusable agent protocol from project-specific instructions;
- moved canonical registries, evidence, raw sources, and historical monoliths into distinct layers;
- introduced atomic experiment output, provenance metadata, payload hashes, and deterministic baselines;
- fixed nondeterministic ordering in Hall cut certificates and added a regression test.

### Canonical mathematical status

No theorem or question status changed. G1c/Q-0015 remains active; Q-0016 and Q-0017 remain open.

