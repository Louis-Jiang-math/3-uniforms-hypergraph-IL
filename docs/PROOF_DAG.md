# Proof DAG

## 1. Purpose

这是唯一的主证明依赖图。当前主线是 Route B：先从原实例构造 faithful
Round-or-Core 入口，再把 actual recurrent cores 送入一次性 Core Endgame。
F-0038/F-0051/F-0042 保留为条件 stability backend；在 exact 或 vanishing-loss
Round 输出下，它不再被视为第四个独立结构 gap。Route A 的收费—递推节点保留为
辅助模块，但不再是主线验收标准。

## 2. Graph

```text
M0  One-quarter theorem
└── S5  Quantitative epsilon closure check (Q-0007)
    ├── S4  Exact terminal contradiction
    │   ├── S3a Critical-link product theorem        (Q-0003)
    │   ├── S3b Binary-regeneration terminal theorem (Q-0005/Q-0006)
    │   └── S3c Actual-support Core Endgame          (Q-0016/Q-0004/Q-0009/Q-0010)
    └── S2  Zero-defect global normal form            (Q-0017)
        └── S1  Faithful global Round-or-Core entrance (Q-0018) [ACTIVE]
            ├── R1  Faithful local/global modules      [PROVED-FORMAL]
            └── R2  Global entrance / overflow conversion [OPEN]

Parked Route A:
Q-0002/Q-0015 near-lossless charging,
F-0034 11/27 contraction,
F-0042 aggregate heavy-excess recurrence.
```

Q-0016 与 Q-0017 是耦合的结构问题。二者必须作用于 S1 产生的真实、
future-complete、保留 genealogy 与真实支持的执行对象，但不要求该对象先被
近无损地送入收费流。


## 3. Current bottleneck compression

The logical DAG is unchanged, but D-0012 fixes the implementation sequence:

1. **Root-only entrance:** use F-0070 on original two-step failure atoms and
   reduce the explicit canonical excess \(\Xi_I\) to clean-chart mismatch,
   F-0038 deficit, fresh saturated leaves, and repeat/core mass. Root capacity
   does not refresh along descendants.
2. **Actual core module:** prove the Q-0016 actual switch-cube defect theorem.
   F-0068 excludes cross-context slot migration and F-0069 makes perfect
   monodromy trivial; the open step is the first-nonliteral bounded-multiplicity
   count on the actual three-switch cube.
3. **Fresh forest:** apply F-0041 to split fresh saturated leaves into new
   edge/support/token/repeat outcomes. Repeat goes to the core module; pure
   token mass must be converted by the actual three-cylinder regeneration
   theorem.
4. **Backend:** substitute the resulting gain/boundary estimate into the fixed
   interval master inequality and invoke F-0042/Q-0007.

The normative implementation map is `MAIN_PROOF_ROUTE.md`. F-0055 still closes
only the finite/exact network interface, and no open node is closed by this
compression.

## 4. Node contracts

### R1 — Faithful supporting modules

- **Status:** proved-formal/supporting.
- **Contents:** F-0036–F-0041、F-0043–F-0044、F-0048–F-0055，以及经审计的
  F-0056–F-0070。
- **Output:** 质量守恒的 future lift、no-configuration 重标、old-anchor
  Lyapunov、aggregate orthogonalization、orientation progress、局部 Hall
  deficiency、same-load exchange flow，以及 finite signature atlas、实际边
  history LP/core 接口、M-event release/fan 分解、clean product-chart ledger，
  以及 exact execution tree 上的 pathwise dynamic Round-or-Core-or-Overflow 接口。
- **Does not prove:** 全局 defect 很小、零缺陷分类、product support、全局
  single-pivot cylinder 或 \(1/4\)。

### R2 — Root-excess reduction, fresh forest, and overflow conversion

- **Status:** open.
- **Input:** 任意目标低度、块极小、无 IT 实例，以及 R1 的有限接口。
- **Required output:** 从 F-0070 的 root-only canonical excess \(\Xi_I\) 出发，
  构造与 F-0055/F-0038/F-0051/F-0042 同单位的 clean-chart reduction；对 fresh
  saturated leaves 保留 first owner 与三份账本，完成 edge/support/token/repeat
  conversion；并把 F-0053 的 unbounded overflow 转化为命名结构、上述实际资源
  增长或 positive-mass actual core。
- **Forbidden shortcuts:** 只对压缩 phase graph 或当前 trace 取极限；把
  critical-profile/heavy-pair mismatch 重新命名为 generic defect；把 unstable
  signatures 静默商化；沿 release descendants 刷新 F-0070 的 root capacity；
  用 fixed-instance token-universe finiteness 代替统一 conversion。

### S1 — Faithful global Round-or-Core entrance and natural defect

- **Status:** active.
- **Question:** Q-0018.
- **Input:** 任意目标低度、块极小、无 IT 实例。
- **Output:** 一个统一的 faithful global execution object \(\mathcal X\)，
  适用 F-0055 的 no-copy pathwise Round-or-Core-or-Overflow 接口，以及自然非负
  defect \(\operatorname{Def}(\mathcal X)\)。
- **Natural means:** defect 项来自实际不可逆信息损失、F-0038 的精确
  near-equality deficit、真实支持拼接失败、非正常局部交换或其他独立可审计
  偏差；不得把“不是 binary forest”直接定义成 defect。
- **Acceptance criterion:** 从原实例验证 F-0055 的 entrance/owner/candidate
  hypotheses 与 Round compatibility；若 \(\operatorname{Def}\to0\)，可抽取保存
  actual genealogy、edge/support identity 的零缺陷极限；unbounded overflow
  有命名结构或 actual-core 后果。
- **Normative text:** `framework/FW-60_CRITICAL_STABILITY_ROUTE.md`。

### S2 — Zero-defect global normal form

- **Status:** open.
- **Question:** Q-0017.
- **Input:** S1 的零缺陷 faithful execution object。
- **Required output:**
  \[
  \text{binary regeneration forest}
  +
  \text{reversible exact-future cores}.
  \]
- **Does not require:** 每层 \(11/27\) 收缩。
- **Known auxiliary:** F-0055 已在 exact tree + stable atlas 前提下给出
  pathwise Round / named exit / `R` / actual multi-edge core 分解；F-0034 可处理
  已经具有 \(11/27\) 收缩的非临界分支。全局 entrance 与 overflow 仍未闭合。

### S3a — Critical-link product theorem

- **Status:** open.
- **Question:** Q-0003.
- **Input:** 零缺陷或近零缺陷的 actual single-pivot component。
- **Output:** 增广、正 defect、近平衡真实 link 乘积或高点度数。
- **Forbidden shortcut:** local same-pivot window 不等于 global cylinder。

### S3b — Binary-regeneration terminal theorem

- **Status:** open.
- **Questions:** Q-0005、Q-0006.
- **Input:** binary regeneration forest 的 terminal components。
- **Output:** 增广叶、真实 \(1/4\) link、完整真实块子核心之一。

### S3c — Actual-support Core Endgame

- **Status:** open.
- **Question:** Q-0016；相关 Q-0004、Q-0009、Q-0010。
- **Input:** 保存 actual support 的正质量 reversible exact-future core。
- **Output:** 对每个 positive-mass actual core 给出 augmentation/survivor、
  real near-\(1/4\) single-pivot link、complete real-block no-IT subinstance 或
  strictly positive natural defect。
- **Known supporting structure:** F-0058 与 F-0063–F-0067 给出 target-follow、
  all-release core 三角形/context identities、incompatible-family bound 和
  maximal-reuse switch-matching 二分。F-0068 证明 actual output edge 的全局
  switch-slot 唯一性，F-0069 证明 perfect-transition monodromy 恒等与 sheet
  分解。
- **Current strict subproblem:** D-0011/D-0012 的 actual switch-cube defect。
  必须在 ordered three-coordinate switches 上保留全部 intermediate actual
  supports，并把坏 instruction 赋给第一处 nonliteral context-slot，得到
  bounded multiplicity 与自然正 defect。
- **Known limits:** common-base diamond 原命题为假；splice 不是免费重复操作；
  phase/reversibility 不自动推出 product support；A-0041 排除“switch-map
  dispersion 自动给 spare capacity”。

### S4 — Exact terminal contradiction

- **Status:** blocked by S2–S3.
- **Output:** 每个零缺陷 terminal object 都给出 IT、\(\Delta(H)\ge
  (1/4-o(1))b^2\) 或完整真子无 IT 核心。

### S5 — Quantitative epsilon closure check

- **Status:** blocked by S1/S4; conditional backend available.
- **Question:** Q-0007.
- **Input:** exact 或 uniformly vanishing-loss faithful Round-or-Core，以及完整
  Core Endgame。
- **Available backend:** F-0038 的精确 deficit identity、F-0051 的条件
  clean-chart ledger、F-0042 的条件递推关闭。
- **Output:** 在 S1/S4 的实际输出上验证统一 loss/normalization 参数，使最终
  二阶系数严格小于 \(1/4\)。
- **Order rule:** 不得另起一套 anomaly taxonomy；未验证 global input 时也不得
  把条件 chart 结论提升为 unconditional stability theorem。

### M0 — One-quarter theorem

- **Status:** blocked.
- **Acceptance criterion:** 完整、无条件、保留真实对象和容量的证明；不能
  依赖未经复核的外部常数或有限机器报告。

## 5. Parked Route A

以下节点仍是合法的条件路线，但当前不 active：

- G1a/G1b：配置审计与 future-complete lift；
- Q-0002/Q-0015：near-lossless configuration/escape flow 与 aggregate
  heavy-excess dissipation；
- F-0034：假设 \(11/27\) 收缩后的森林摊还；
- F-0042：假设小 \(\mathfrak H_k\) 后的递推关闭。

任何重新激活必须先修改 `knowledge/DECISIONS.md`。单独证明一个新收费
子类、Hall cut 或 token bound 不构成路线切换。

## 6. Progress rule

以下工作不自动改变节点状态：

- 新定义或新 defect 名称；
- 条件模型中的漂亮常数；
- 小参数枚举；
- 新 atlas/phase/quotient/cut；
- “若闭合则有核心”的充分条件；
- 未连接 actual support 的熵或紧性陈述；
- 未证明全局粘合的 local same-pivot 分类；
- Route A 中更精细的余项切割。

主线净进展必须至少完成一项：

1. S1 的自然 defect 或紧性接口；
2. S2 的精确零缺陷分类；
3. S3 的 actual-support 饱和/终局定理；
4. S5 的统一稳定模量；
5. 一个满足全部真实条件的反模型，排除相应节点。
