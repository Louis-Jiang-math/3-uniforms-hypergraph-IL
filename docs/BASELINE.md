# Source baseline

本完整重构版以公开仓库 `main` 在 **2026-07-28** 的提交 **`cfadd24`**（完整 SHA `cfadd24b52546d4d5800c4a3c5a75a2add86f928`） 为来源基线。GitHub 提交页显示该提交标题为 `20260728`，当时仓库共有 20 次提交。

由于此交付不是 Git bundle，压缩包不包含原仓库的 `.git/` 对象数据库；`docs/BASELINE_MANIFEST.json` 和根目录 `SHA256SUMS` 固定本交付的文件内容。

## Source-derived active files

已纳入并重构：

- `knowledge/FACTS.md`, `knowledge/FAILURES.md`, `knowledge/QUESTIONS.md`；
- 两份根框架文档；
- Q-0015 计算报告与结构分析；
- requirements 和 workflow；
- 可获取的历史对话；
- 用户补充的最新深度二对话。

## Deliberate code replacement

原公开 Q-0015 审计器被拆成 `src/hypergraph_il/` 库、CLI、tests 与 schema。新实现保留公开回归数值，并新增 projection-sensitive slot 类型、全局真实边 ledger、E-exit schema 与一致性测试。

## Historical note

`sources/raw/conversations/` 是历史材料，不参与 claim status。若某个上游巨型导出不在本快照中，`docs/history/README.md` 与当前账本已保留其规范净结论；研究状态不依赖历史文件的逐字完整性。
