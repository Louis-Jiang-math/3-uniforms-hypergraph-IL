# 十分钟研究者速览

读完本页后，应能回答项目最关键的七个问题。

## 1. 主定理是否已经证明？

没有。

目标仍是证明三一致等块分块超图在

\[
\Delta(H)<\left(\frac14-o(1)\right)b^2
\]

时存在独立横截。当前转向 Route B：临界稳定性。

## 2. 当前唯一 active 的主链命题是什么？

**S1 / Q-0018：faithful global execution and natural defect。**

目标不是把全部 residual 送入收费账本，而是从任意块极小无 IT 反例构造：

1. 保存真实边、块、root projection、pivot、genealogy 和未来坐标的全局执行对象；
2. 一个自然非负 defect；
3. defect 趋零时仍保存 actual support 的极限对象。

Route A 的 Q-0002/Q-0015 暂时搁置。

## 3. 为什么不再以“全部 heavy excess 被支付”为主目标？

因为 \(1/4\) 不必是 \(100\%\) residual-conversion theorem。更合理的稳定性逻辑是：

\[
\text{正 defect}
\Longrightarrow
\text{耗散},
\qquad
\text{defect}\to0
\Longrightarrow
\text{临界结构},
\]

再由临界结构产生真实 \(1/4\) link、IT 或完整块矛盾。

逐质量收费仍是合法辅助方法，但不是 Route B 的验收标准。

## 4. Route B 的精确目标是什么？

先证明零缺陷对象属于

\[
\text{binary regeneration forest}
+
\text{reversible exact-future cores}.
\]

然后证明每个 reversible core 在 actual support 上：

- splice 饱和并乘积化；
- 或进入 single-pivot critical link；
- 或产生完整真实块终局；
- 或具有正 defect。

最后才做固定 \(\varepsilon\) 的定量稳定化。

## 5. 本轮新增的有限证据是什么？

脚本 `enumerate/q4_splice_pay_cylinder_validation.py` 穷举：

- 272 个 \(Q_4\) 坐标完美匹配；
- 8 个正常匹配；
- 192 个正常独立 one-hole states；
- 768 个 future-complete release policies。

分类结果：

- 384 个 edge-disjoint splice candidates；
- 192 个 unavoidable real-edge reuse；
- 192 个 local same-pivot cylinders。

所有 384 个 splice candidates 的最小 splice 都使用全部 8 条真实边。因此
splice 不能被当作免费可重复闭包。该结果仅是 bounded exhaustive evidence。

## 6. 哪些错误必须避免？

- 把 \(1/4\) 解释成全部 residual 必须收费；
- 用 desired terminal structure 定义 defect；
- 把 local same-pivot 当成 global cylinder；
- 把 reversibility、phase 或 genealogy 可恢复性当成 product support；
- 假设 common-base diamond 自动存在；
- 把 splice 当成免费操作；
- 对 partial support 使用块极小性；
- 用有限枚举替代一般定理。

## 7. Route A 的结果还能使用吗？

可以。以下仍是可靠辅助模块：

- configuration auditor 和三份独立账本；
- future-complete lift；
- old-anchor Lyapunov；
- aggregate normalization；
- pair-flat/heavy-excess decomposition；
- orientation progress；
- F-0034、F-0042 的条件关闭判据；
- Hall orthogonalization 和 exchange-flow 工具。

但这些模块不得自动把 active node 改回 Q-0015。

## 接下来读什么？

1. `../HANDOFF_CURRENT.md`
2. `PROJECT_STATE.yaml`
3. `PROOF_DAG.md`
4. `framework/FW-60_CRITICAL_STABILITY_ROUTE.md`
5. `../knowledge/DECISIONS.md`
6. `../knowledge/FACTS.md`
7. `../knowledge/FAILURES.md`
8. `../knowledge/QUESTIONS.md`
9. `../evidence/proofs/ROUTE_B_REORIENTATION_AUDIT.md`
