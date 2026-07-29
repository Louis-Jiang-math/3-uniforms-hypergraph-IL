# 十分钟研究者速览

读完本页后，应能回答项目最关键的七个问题。

## 1. 主定理是否已经证明？

没有。

目标是证明三一致等块分块超图在

\[
\Delta(H)<\left(\frac14-o(1)\right)b^2
\]

时存在独立横截。当前仍缺一般近无损配置入口、persistent-blocker 正常形、
因果 incidence 再生和最终稳定计数。

## 2. 当前唯一 active 的主链命题是什么？

**G1c / Q-0015：E-exit 与 aggregate heavy-excess 的定量控制。**

已知一个 Q-0015 实根障碍要么在有限前缀产生命名 E 出口，要么可无损提升为
future-complete persistent blocker。另有 aggregate route 将实际二步失败写成

\[
\mathcal B_k\le(1+\eta)\Delta(H)A_{k-2}+\mathfrak H_k.
\]

现在必须控制最短 E 质量或等价地控制全部 heavy-pair 正部总量：

- 证明它们是小误差；
- 或用正确的 root-budget、slot、real-edge 账本支付；
- 或输出可复算结构割；
- 剩余质量才能进入下游 persistent-blocker 分析。

## 3. 它依赖哪些已证结果？

可以直接使用：

- configuration auditor、root-pivot LP、slot flow、real-edge Hall flow；
- F-0029 等回归反例；
- 实际 pivot-switch/reroot lift；
- finite escape Hall/reuse 二分；
- future-complete lift 形式二分；
- 在已假设逐节点 \(11/27\) 收缩时的 \(27/16\) 森林摊还。

不能把 AMCG、transition capping 或有限深度枚举当作一般入口定理。

## 4. 什么结果算关闭当前节点？

需要给出一个一般定理，作用于低度、块极小、无 IT 的实际 Q-0015 根障碍，并且：

1. 原路线：对所有相关最短 E 证书给出统一质量控制；或
2. aggregate 路线：证明 \(\mathcal B_k\le c_\varepsilon b^2A_{k-2}\)，其中 \(c_\varepsilon<1/4\)；
3. 明确使用哪一份容量账本，不重复真实边、slot 或根预算；
4. 所有 quotient 必须 future-compatible，并输出可接受结构出口；
5. 或给出满足全部真实执行条件的严格反模型。

只在新接口中定义 E 可支付，不算关闭。

## 5. 什么反例会杀死它？

一个有效反例必须同时给出：

- 真实三一致分块超图；
- 低度、块极小、无 IT；
- 实际可达根记录与失败义务；
- 完整 root projection 和 genealogy；
- 三份容量账本；
- 正质量最短 E 证书；
- 证明该 E 质量既非小误差，也不能合法支付，又不产生规定结构割。

压缩状态、相位模型或手工抽象树不足以构成反例。

## 6. 哪些脚本可以测试有限模型？

从 `enumerate/` 开始，优先查看：

- Q-0015 configuration auditor；
- root-pivot LP / dual certificate；
- slot-flow auditor；
- real-edge Hall-flow auditor；
- F-0029 和 genealogy collision 回归；
- depth-two splitter enumeration；
- reset-compensation 的三块二元完整枚举。

计算结果必须保存参数、输入、输出、日志、随机种子和 SHA-256。
“未找到反例”不是一般证明；unresolved state 也不是反例。

## 7. 哪些路线已经被永久排除？

至少包括：

- 所有失败义务共享一个预置 pivot；
- 删除第一 blocker 的一个端点后不重新检查独立性；
- 静态 switch 自动产生合法 reroot；
- 压缩迹相同即可合并 genealogy；
- trivial monodromy 或 phase 一致自动推出 product support；
- 投影满推出完整真实块支持；
- partial support 直接调用块极小性；
- incidence 增殖直接推出 \(1/4\) 集中；
- ordinary transition capping 自动创造真实边收费权；
- 有限 LP/MILP 或小参数枚举替代一般定理。

## 接下来读什么？

1. `../HANDOFF_CURRENT.md`
2. `PROOF_DAG.md`
3. `framework/FW-10_CONFIGURATION_ENTRY.md`
4. `framework/FW-40_FUTURE_COMPLETE_LIFT.md`
5. `../agent.md`
6. 根目录 `knowledge/FACTS.md`、`knowledge/FAILURES.md`、`knowledge/QUESTIONS.md`
