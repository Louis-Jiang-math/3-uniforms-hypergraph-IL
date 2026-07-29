# Proof DAG

## 1. Purpose

这是唯一的主证明依赖图。路线、定义、计算和条件模型只有在关闭某个节点或排除某个
命题时，才算主线净进展。

## 2. Graph

```text
M0  One-quarter theorem
└── G4  Terminal structure and epsilon stability
    ├── G3  Causal incidence regeneration (Q-0016)
    │   └── G2  Persistent-blocker normal form (Q-0017)
    │       └── G1d Near-lossless configuration entry (Q-0002/Q-0015)
    │           ├── G1c E-exit / aggregate heavy-excess control [ACTIVE]
    │           ├── G1b Future-complete lift dichotomy          [PROVED-FORMAL]
    │           └── G1a Configuration auditor infrastructure [PROVED-FORMAL]
    └── independent stability/link inputs (Q-0003–Q-0007)
```

Q-0016 与 Q-0017 的具体证明可能互相反馈，但二者都必须作用于由 G1 产生的真实、
近无损、带完整账本的执行对象。

## 3. Node contracts

### G1a — Configuration auditor infrastructure

- **Status:** proved-formal
- **Input:** 实际根记录和失败义务。
- **Output:** 合法配置枚举、root-pivot LP、slot flow、real-edge Hall flow、机器证书。
- **Does not prove:** 一般低度实例存在近无损可行流。
- **Evidence:** F-0030、`src/hypergraph_il/`、`tests/` 与 `evidence/experiments/q0015/`。

### G1b — Future-complete lift dichotomy

- **Status:** proved-formal
- **Input:** 已经具备实际可达根 cylinder、genealogy、三份账本的 Q-0015 实根障碍。
- **Output:** 有限命名 E 出口，或无损未来完备 persistent-blocker 提升。
- **Does not prove:** E 质量小、入口存在、\(11/27\)、集中或完整子核心。
- **Normative text:** `framework/FW-40_FUTURE_COMPLETE_LIFT.md`。

### G1c — E-exit and aggregate heavy-excess control

- **Status:** active
- **Input:** G1b 的最短 E 证书，或 F-0039 的实际二步 aggregate cylinders。
- **Proved supporting output:** F-0040 给出 pair-flat \(\Delta(H)\)-支付与精确 heavy-excess 余项 \(\mathfrak H_k\)；F-0041 给出 future-compatible orientation-budget reset compensation。
- **Required output:** 支付/忽略全部 \(\mathfrak H_k\)，或输出保存真实对象与账本的结构割/反模型；原逐 source E-flow 仍可作为另一充分路线。
- **Acceptance criterion:** 原近无损 configuration/escape flow 成立，或 aggregate 路线产生统一 \(c_\varepsilon<1/4\) 递推；所有支付使用正确独立账本，所有 quotient 是 future-compatible。
- **Counterexample criterion:** 满足低度、块极小、无 IT、实际可达与全账本条件，但原 flow 与 aggregate heavy-excess criterion 均失败的真实模型。
- **Normative text:** `framework/FW-15_AGGREGATE_PAIR_CYLINDER.md`。

### G1d — Near-lossless configuration entry

- **Status:** open
- **Input:** 任意目标低度、块极小、无 IT 实例。
- **Output:** 跨深度、跨 root projection 的近无损配置/escape 流。
- **Acceptance criterion:** Q-0002/Q-0015 原 answer criterion 全部满足。
- **Depends on:** G1c 及配置预算/slot/real-edge 的联合结构定理。

### G2 — Persistent-blocker critical normal form

- **Status:** open
- **Question:** Q-0017
- **Input:** G1d 输出的真实 persistent blocker。
- **Output:** 命名出口，或逐层 continuation 至多 \(11/27+o(1)\) 的正常形。
- **Known conditional input:** F-0034 只在该收缩假设下给出摊还。
- **Forbidden shortcut:** ordinary transition capping 未获独立收费权。

### G3 — Causal incidence regeneration

- **Status:** open
- **Question:** Q-0016
- **Input:** 无 reuse、无 augmentation、无 exact-future quotient 的真实未来闭合区域。
- **Output:** fresh 容量、旧锚集中/高点度数、完整真子核心、未覆盖未来选择或命名证书。
- **Known limit:** F-0035 只给 incidence 集中或顶点增殖；对角分散模型阻止直接推出 \(1/4\)。

### G4 — Terminal structure and epsilon stability

- **Status:** blocked
- **Questions:** Q-0003、Q-0005–Q-0007。
- **Input:** G1–G3 已关闭。
- **Output:** terminal counting、完整块终局、固定 \(\varepsilon\) 稳定化及最终递推。

### M0 — One-quarter theorem

- **Status:** blocked
- **Acceptance criterion:** 完整、无条件、保留真实对象和容量的证明；不能依赖未经复核的外部常数或机器报告。

## 4. Progress rule

以下工作不自动改变节点状态：

- 新定义；
- 条件模型中的漂亮常数；
- 小参数枚举；
- 新 atlas/phase/quotient；
- “若闭合则有核心”的充分条件；
- 未连接原问题入口的 Hall 定理。

它们应分别登记为 definition、proved-conditional、computational-observation 或 supporting result。
