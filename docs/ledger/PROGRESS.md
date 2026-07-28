# Net progress log

只记录证明状态的净变化，不记录“新增文档行数”或一般探索。

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

