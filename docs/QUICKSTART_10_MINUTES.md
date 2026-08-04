# 十分钟研究者速览

读完本页后，应能定位当前唯一主线、可直接使用的模块和剩余证明义务。

## 1. 主定理是否已经证明？

没有。目标仍是

\[
\Delta(H)<\left(\frac14-o(1)\right)b^2
\Longrightarrow
H\text{ 有独立横截}.
\]

当前策略是 Route B：critical stability。

## 2. 当前 active 节点是什么？

逻辑 DAG 的唯一 active 节点仍是：

> **S1 / Q-0018 — faithful global Round-or-Core entrance and natural defect.**

Q-0016 是 actual-support Core Endgame，Q-0017 是 zero-defect forest/core
normal form。三者均 open。

## 3. 当前固定的实现路线是什么？

D-0012 固定：

\[
\boxed{
\text{root-only canonical excess}
\to
\text{actual switch-cube core defect}
\to
\text{fresh saturated-leaf conversion}
\to
\text{F-0042}.
}
\]

详见 `MAIN_PROOF_ROUTE.md`。

## 4. 第一阶段：root-only canonical excess

F-0070 已证明，在合法区间 \(I\) 上

\[
\frac{\sum_{k\in I}\mathcal B_k}{b^2S_I}
\le
(1+\eta)\frac{\Delta(H)}{b^2}+\Xi_I.
\]

这里的容量只属于原始二步 failure roots。release 后出现的 blocker 不会
自动刷新一份新容量。

当前 Q-0018 要证明：

\[
\Xi_I
\le
\operatorname{ChartMis}_I
+2\mathcal D_I^\sharp
+\Phi_I
+\mathcal R_I,
\]

并保持 root、slot、actual-edge 与 recurrence units 一致。

## 5. 第二阶段：actual switch-cube core defect

F-0063--F-0067 给出 finite unique-blocker all-release core 与
completion-switch matching。新增支持事实：

- F-0068：固定 \(e,f\) 时，\(f\) 跨 contexts 只能来自一个固定 switch
  slot；
- F-0069：perfect-transition monodromy 为恒等，完美 component 分解为
  completion sheets。

它们排除单步 actual Latin-column migration，但不关闭 Q-0016。

当前 candidate theorem 是 actual switch-cube defect：在 ordered
three-coordinate switches 上保留全部 intermediate actual supports，把坏
instruction 赋给第一处 nonliteral context-slot，并证明 bounded
multiplicity。成功后，每个 positive-mass core 产生 Route B 接受的自然正
actual-support defect。

## 6. 第三阶段：fresh saturated leaves

对 \(\Phi_I\) 使用 F-0041 的 no-copy split：

\[
\Phi_I=
\Phi_I^{\rm edge}
+\Phi_I^{\rm support}
+\Phi_I^{\rm token}
+\Phi_I^{\rm repeat}.
\]

固定后端：

- repeat \(\to\) actual core \(\to\) switch-cube defect；
- support \(\to\) actual \(S\) witness 或 hereditary coordinate expansion；
- edge \(\to\) first-certifying bounded-multiplicity actual-edge ledger；
- token \(\to\) actual three-cylinder critical regeneration。

固定实例 token universe 有限不够；需要 interval-level 的实际转化。

## 7. 最后如何闭合？

得到

\[
\sum_{k\in I}\mathcal B_k
\le
(1+\eta)\Delta(H)S_I
-\mathsf{Gain}_I
+\mathsf{Boundary}_I,
\]

且

\[
\mathsf{Boundary}_I/(b^2S_I)\to0,
\]

再用 F-0042/Q-0007 选参数使最终系数严格小于 \(1/4\)。这个参数后端已
条件可用，不是新的结构 gap。

## 8. 哪些方向不再作为主线？

- 动态刷新 descendant blocker capacity；
- 静态 core edge-set Hall 压缩；
- 抽象 Latin/phase/monodromy 自动收费；
- 仅用 finite token-universe exhaustion；
- 把 positive natural core defect 重新要求为独立 root edge entitlement。

## 9. 必读顺序

1. `../HANDOFF_CURRENT.md`
2. `MAIN_PROOF_ROUTE.md`
3. `PROOF_DAG.md`
4. `../knowledge/DECISIONS.md#D-0012`
5. `../knowledge/FACTS.md#F-0068`
6. `../knowledge/QUESTIONS.md#Q-0016`
7. `../knowledge/QUESTIONS.md#Q-0018`
8. `../evidence/proofs/ROOT_ONLY_EXCESS_SWITCH_CUBE_ROUTE.md`
9. `framework/FW-60_CRITICAL_STABILITY_ROUTE.md`

## 10. 当前状态一句话

证明图和实现路线已固定；F-0068--F-0070 是已验证支持事实；switch-cube
core defect、root-excess clean-chart reduction 和 three-cylinder fresh-token
regeneration 仍开放，主定理仍未证明。
