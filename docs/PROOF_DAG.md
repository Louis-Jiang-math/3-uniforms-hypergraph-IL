# Proof DAG

## 1. Purpose

这是唯一的主证明依赖图。当前主线是 Route B：先分类零缺陷临界对象，再做
固定 \(\varepsilon\) 稳定化。Route A 的收费—递推节点保留为辅助模块，但不再是
主线验收标准。

## 2. Graph

```text
M0  One-quarter theorem
└── S5  Quantitative epsilon stability (Q-0007)
    ├── S4  Exact terminal contradiction
    │   ├── S3a Critical-link product theorem        (Q-0003)
    │   ├── S3b Binary-regeneration terminal theorem (Q-0005/Q-0006)
    │   └── S3c Reversible-core saturation/gluing    (Q-0016/Q-0004/Q-0009/Q-0010)
    └── S2  Zero-defect global normal form            (Q-0017)
        └── S1  Faithful execution and natural defect (Q-0018) [ACTIVE]
            ├── R1  Faithful local/global modules      [PROVED-FORMAL]
            └── R2  Tightness/compactness interface    [OPEN]

Parked Route A:
Q-0002/Q-0015 near-lossless charging,
F-0034 11/27 contraction,
F-0042 aggregate heavy-excess recurrence.
```

Q-0016 与 Q-0017 是耦合的结构问题。二者必须作用于 S1 产生的真实、
future-complete、保留 genealogy 与真实支持的执行对象，但不要求该对象先被
近无损地送入收费流。

## 3. Node contracts

### R1 — Faithful supporting modules

- **Status:** proved-formal/supporting.
- **Contents:** F-0036–F-0041，以及 F-0043–F-0044。
- **Output:** 质量守恒的 future lift、no-configuration 重标、old-anchor
  Lyapunov、aggregate orthogonalization、orientation progress、局部 Hall
  deficiency 和 same-load exchange flow。
- **Does not prove:** 全局 defect 很小、零缺陷分类、product support、全局
  single-pivot cylinder 或 \(1/4\)。

### R2 — Tightness and compactness interface

- **Status:** open.
- **Input:** 有界深度 faithful execution laws，保留实际块、边、pivot、
  root projection、genealogy 与未来坐标。
- **Required output:** 一个不会因 refinement、reroot 或历史展开而丢失实际
  身份的紧性/极限接口。
- **Forbidden shortcut:** 只对压缩 phase graph 或当前 trace 取极限。

### S1 — Faithful execution and natural defect

- **Status:** active.
- **Question:** Q-0018.
- **Input:** 任意目标低度、块极小、无 IT 实例。
- **Output:** 一个统一的 faithful global execution object \(\mathcal X\) 和
  自然非负 defect \(\operatorname{Def}(\mathcal X)\)。
- **Natural means:** defect 项来自实际不可逆信息损失、F-0038 的精确
  near-equality deficit、真实支持拼接失败、非正常局部交换或其他独立可审计
  偏差；不得把“不是 binary forest”直接定义成 defect。
- **Acceptance criterion:** 若 \(\operatorname{Def}\to0\)，可抽取保存实际
  genealogy、边身份和支持的零缺陷极限；若 defect 有固定正密度，则该部分有
  一个独立已证明的耗散后端。
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
- **Known auxiliary:** F-0034 可处理已经具有 \(11/27\) 收缩的非临界分支。

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

### S3c — Reversible-core saturation and gluing

- **Status:** open.
- **Question:** Q-0016；相关 Q-0004、Q-0009、Q-0010。
- **Input:** 保存 actual support 的正质量 reversible exact-future core。
- **Output:** splice saturation/product support、same-pivot critical link、
  完整块终局或正 defect。
- **Known limits:** common-base diamond 原命题为假；splice 不是免费重复操作；
  phase/reversibility 不自动推出 product support。

### S4 — Exact terminal contradiction

- **Status:** blocked by S2–S3.
- **Output:** 每个零缺陷 terminal object 都给出 IT、\(\Delta(H)\ge
  (1/4-o(1))b^2\) 或完整真子无 IT 核心。

### S5 — Quantitative epsilon stability

- **Status:** blocked by S4.
- **Question:** Q-0007.
- **Input:** 精确零缺陷分类。
- **Output:** 对固定 \(\varepsilon\) 的统一稳定模量，排除
  \(\Delta(H)\le(1/4-\varepsilon)b^2\) 的块极小无 IT 序列。
- **Order rule:** 不得在 S4 前把逐类异常收费当作完整稳定性证明。

### M0 — One-quarter theorem

- **Status:** blocked.
- **Acceptance criterion:** 完整、无条件、保留真实对象和容量的证明；不能
  依赖未经复核的外部常数或有限机器报告。

## 4. Parked Route A

以下节点仍是合法的条件路线，但当前不 active：

- G1a/G1b：配置审计与 future-complete lift；
- Q-0002/Q-0015：near-lossless configuration/escape flow 与 aggregate
  heavy-excess dissipation；
- F-0034：假设 \(11/27\) 收缩后的森林摊还；
- F-0042：假设小 \(\mathfrak H_k\) 后的递推关闭。

任何重新激活必须先修改 `knowledge/DECISIONS.md`。单独证明一个新收费
子类、Hall cut 或 token bound 不构成路线切换。

## 5. Progress rule

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
