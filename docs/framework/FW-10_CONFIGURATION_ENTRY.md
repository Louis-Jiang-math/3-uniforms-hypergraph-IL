# FW-10 — Configuration entry

- **Status:** active
- **Questions:** Q-0002, Q-0015
- **DAG nodes:** G1a–G1d

## 0. Contract

### Input

任意低度、块极小、无 IT 实例中的实际搜索失败义务。

### Desired output

近无损、实际可达的配置流，保存：

- 全部合法真实两步配置；
- root projection；
- pivot 与 root edge；
- genealogy；
- root-pivot 总预算；
- slot capacity；
- global real-edge capacity；
- ordinary/switch/multi-defect/augmentation 分类。

若不可行，输出可复算的真实结构割。

## 1. Proved infrastructure

Q-0015 审计器已经实现：

- 合法配置枚举；
- root-pivot 原始/对偶 LP；
- 固定预算 slot flow；
- 独立 real-edge Hall flow；
- F-0029、九边修复、genealogy collision 等回归。

这是 G1a，状态 `proved-formal`。

## 2. New formal progress

G1b 已得到规范未来完备提升：

\[
\text{Q-0015 实根障碍}
\Longrightarrow
E\text{ 有限命名出口}
\;\vee\;
\text{future-complete persistent blocker}.
\]

详见 `FW-40_FUTURE_COMPLETE_LIFT.md`。

G1c 还得到一条 aggregate supporting route：

\[
\mathcal B_k
\le
(1+\eta)\Delta(H)A_{k-2}
+
\mathfrak H_k,
\]

其中 \(\mathfrak H_k\) 是真实 pair-cylinder 质量超过
\((1+\eta)W_N/b^2\) 的正部总量。该归约同时包含 old-anchor 与
fresh/configurable failures，并且不会复制 sibling genealogy 质量。

详见 `FW-15_AGGREGATE_PAIR_CYLINDER.md`。

## 3. Active gap

当前精确缺口是 quantitative heavy-pair dissipation：

- 把全部 \(\mathfrak H_k\) 无损分解到 carrier trajectories；
- 以新真实边、新 anchor support 或可控 orientation token 支付；
- 或把 sound token repetition 提升为 accepted exact-future quotient；
- 达到 F-0042 所需的 \(c_\varepsilon<1/4\) 递推。

原逐 source configuration-flow 路线仍是充分路线，但不是唯一可能接口。

## 4. Nonclaims

本模块尚未证明：

- 一般低度实例存在近无损配置流；
- 跨 root projection 联合预算；
- ordinary transition 拥有额外收费权；
- Q-0017 的 \(11/27\) 正常形；
- Q-0016 的因果集中；
- \(1/4\) 定理。
