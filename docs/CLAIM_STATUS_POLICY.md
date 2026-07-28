# Claim status policy

## Allowed statuses

| Status | 含义 |
|---|---|
| `definition` | 定义、类型或规范，不断言目标对象存在 |
| `proved` | 原声明范围内完整证明 |
| `proved-conditional` | 在显式额外假设/接口下证明 |
| `proved-formal` | 规范化、提升、等价或网络二分 |
| `computational-observation` | 有限计算观察 |
| `conjecture` | 精确命题，无证明 |
| `open` | 原问题未解决 |
| `blocked` | 等待上游接口 |
| `disproved` | 有严格反例 |
| `superseded` | 被新框架替代 |

## Scope rule

任何命题必须同时写：

- **Input scope**
- **Output**
- **Dependencies**
- **Nonclaims**
- **DAG role**

例如：

```text
Status: proved-formal
Input: a Q-0015 actual root obstacle with all ledgers
Output: finite named exit or future-complete lift
Nonclaims: no entrance theorem; no 11/27; no Q-0016
```

不得只写“Q-0015 有进展”或“Q-0016 已在 AMCG 中完成”。

## Source hierarchy

1. 当前规范 framework 与 Proof DAG；
2. `knowledge/FACTS.md` / `knowledge/FAILURES.md` / `knowledge/QUESTIONS.md`；
3. 可复算代码与证书；
4. 当前 handoff；
5. 历史 handoff 和对话。

低层来源不能覆盖高层状态。旧对话中的中途结论若在同一对话后续被纠正，只能引用最终净结论。

## Updating ledgers

- 新一般定理：加入 `knowledge/FACTS.md`，状态 `confirmed` 或项目既有等价状态。
- 条件/形式结果：加入 `knowledge/FACTS.md` 并显式 caveat。
- 反例/错误路线：加入 `knowledge/FAILURES.md`。
- 问题范围变化：更新 `knowledge/QUESTIONS.md`，不得无依据改为 closed。
- 主线变化：更新 `PROOF_DAG.md` 和 `HANDOFF_CURRENT.md`。
- 净变化：追加 `ledger/PROGRESS.md`。
