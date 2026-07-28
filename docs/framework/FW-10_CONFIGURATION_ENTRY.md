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

## 3. Active gap

当前不是继续扩展抽象 genealogy，而是定量控制 E 类最短前缀：

- 哪些是预算/slot/edge 可支付；
- 哪些是 \(o_\varepsilon(1)\) 异常；
- 哪些给出真实低度结构割；
- 哪些留下无损 persistent blocker。

## 4. Nonclaims

本模块尚未证明：

- 一般低度实例存在近无损配置流；
- 跨 root projection 联合预算；
- ordinary transition 拥有额外收费权；
- Q-0017 的 \(11/27\) 正常形；
- Q-0016 的因果集中；
- \(1/4\) 定理。
