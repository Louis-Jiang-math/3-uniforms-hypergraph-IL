# Research workflow

## 1. Start

从 `HANDOFF_CURRENT.md` 取得唯一 active node，复制其 exact target 到研究日志。

## 2. Formalize

写出：

```text
Claim ID:
Status sought:
Input:
Output:
Dependencies:
Ledger:
Nonclaims:
```

若无法写完整量词，不开始证明。

## 3. Audit

- 搜索 `FAILURES.md`；
- 检查真实边/projection/genealogy；
- 检查三份账本；
- 检查块支持是否完整；
- 检查是逻辑应用顺序还是条件开发顺序。

## 4. Work product

优先顺序：

1. 完整证明；
2. 严格反例；
3. 形式二分/规范化；
4. 精确最小子引理；
5. 计算观察。

不得用第 5 类冒充第 1 类。

## 5. Close or update

只有满足原 answer criterion 才关闭 Question。否则更新：

- Known so far；
- Missing；
- Suggested next action；
- Caveats。

## 6. Handoff discipline

handoff 不保存探索过程。探索过程进入 `old/` 或 lab notes；handoff 只保存净状态。
