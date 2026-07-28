# FW-50 — Persistent-blocker critical normal form

- **Status:** open
- **Question:** Q-0017
- **DAG node:** G2

## Input contract

输入必须来自 G1 的真实近无损配置流或 FW-40 的无 E 剩余，并保存：

- root projection；
- pivot；
- genealogy；
- ordinary/switch/multi-defect 分类；
- 三份容量；
- 完整未来 tuple 支持。

## Desired theorem

persistent blocker 要么进入 augmentation、fresh、reuse/Hall、exact quotient、
内部完整块闭合等命名出口，要么归约为

\[
\sum_{u\in\operatorname{ch}(v)}\mu_u
\le
\left(\frac{11}{27}+o_\varepsilon(1)\right)\mu_v.
\]

## Known conditional result

F-0034 证明：一旦上述逐节点收缩成立，截断森林满足最佳常数 \(27/16\) 的摊还。
这不是正常形定理本身。

## Rejected transition-capping route

不能将超出 \(11/27\) 的 ordinary continuation 自动定义为 transition charge。
需要先证明它拥有独立、未消费、非循环的真实边收费权。当前没有该引理。

## Active prerequisites

- G1c E-exit control；
- 一般配置入口；
- 一个不制造容量的单调量、结构割或真实反模型。
