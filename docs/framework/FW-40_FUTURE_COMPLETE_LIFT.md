# FW-40 — Future-complete lift of a Q-0015 root obstacle

- **Status:** proved-formal
- **DAG node:** G1b
- **Source:** latest dialogue `sources/raw/conversations/chatgpt-export_深度二分析执行.txt`, final corrected argument

## 0. Contract

### Input

一个 Q-0015 **实根障碍**，已经包含：

- 两两不交的实际可达根 cylinder；
- 根记录 \((U,\rho,p,M,\gamma)\)；
- 根义务与合法配置数据；
- root-pivot、slot、global real-edge 三份账本；
- 每个根选择的非空完整真实未来块集 \(\mathcal J_r\subsetneq\mathcal P\)。

### Output

以下严格二分之一：

1. 某个正质量分支在有限最短前缀进入命名 E 出口；
2. 障碍可在质量与账本无损的条件下提升为未来完备执行森林，并包含真实
   persistent-blocker 分支。

## 1. Future tuple space

对每个根 \(r\)，令

\[
X_r=\prod_{B\in\mathcal J_r} B.
\]

规范提升保留每个 \(x\in X_r\) 的忠实副本。未来块中的当前顶点只能是指定坐标
\(x_B\)；ordinary move 可以释放该坐标，但不能偷偷改取同块另一顶点。

## 2. C/I/E classification

每个忠实单块尝试严格分类为：

- **C — faithful continuation:** 实际合法后继，保存 tuple、projection、genealogy 与账本；
- **I — internal real blocker:** 存在 \(e\subseteq T(x)\)，且 \(e\) 完全位于完整未来块集内部；
- **E — named exit:** no-configuration、boundary、projection failure、multi-defect、
  switch 无 reroot lift、预算/slot/edge cut、外部旧锚 blocker、exact quotient、
  augmentation/survivor 或最短未分类执行失败。

## 3. Theorem

### Theorem FW-40.1

对每个 Q-0015 实根障碍，恰有：

\[
\text{finite named E exit}
\quad\vee\quad
\text{mass/ledger-preserving future-complete lift}.
\]

提升保持：

- 全未来 tuple 支持；
- 实际 root coverage；
- 完整 genealogy；
- C/I/E 完备分类；
- 三份容量不复制；
- 最小割 source side 对 C 结构弧闭合。

### Proof idea

取原执行空间与有限未来 tuple 的乘积，并将每个根 cylinder 的质量均匀分配到
其 tuple 副本。按固定真实边/块/合法动作全序确定性展开。第一个无法进入 C 或 I
的前缀定义 E；若所有正质量分支均无 E，则得到完整 future lift。

为网络中的 C 结构弧赋容量 \(L>M\)，有限容量只放在真实资源和 I/E 终端。
任何容量至多 \(M\) 的最小割不能穿过 C 弧，因此 source side 对忠实执行后继闭合。

## 4. Block-minimal consequence

若 \(H\) 块极小且无 IT，并且某个正质量根的所有 future tuples 都在有限时间进入 I，
则完整真块集 \(\mathcal J_r\) 的每个横截都含内部真实边，形成无 IT 真子核心，
与块极小性矛盾。

因此在无 E 的分支中至少存在一个无限 C 链，即真实 persistent blocker。

## 5. Nonclaims

FW-40.1 不证明：

- 输入实根障碍由任意目标实例近乎无损产生；
- E 出口质量可控；
- 所有分支都 persistent；
- persistent blocker 满足 \(11/27\)；
- incidence 再生集中；
- 完整子核心必然出现；
- Q-0015、Q-0017 或 Q-0016 已关闭。

## 6. Current use

FW-40 将 Q-0015 的剩余工作压缩为：

\[
\text{定量控制 E 类}
\quad+\quad
\text{对无 E persistent blocker 证明 Q-0017/Q-0016}.
\]
