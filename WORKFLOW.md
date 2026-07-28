# 对话驱动项目工作流

本文件解释 [`agent.md`](agent.md) 中的强制规则，并提供可复用模板。
`agent.md` 是短协议；本文件是按需读取的操作手册。项目专有规则仍以
[`AGENTS.md`](AGENTS.md) 为准。

## 1. 为什么要分层

长期对话项目最常见的问题不是缺少文字，而是以下内容混在一起：

- 原始输入；
- 当前可信知识；
- 完整证据；
- 临时探索；
- 当前行动；
- 历史修订。

推荐分为五层：

| 层 | 作用 | 默认更新语义 |
|---|---|---|
| 原始来源 | 保存上下文和输入 | 只读 |
| 知识注册 | 说明当前可依赖什么 | 原地更新 |
| 证据与实现 | 说明为什么可信 | 原地整理或新建独立记录 |
| 当前状态 | 指引下一步 | 重写当前快照 |
| 历史 | 保存演化过程 | Git、归档、日志 |

一个条目出现在注册表中，不代表它已经被证明；其状态和证据链接共同决定可信程度。

## 2. 推荐目录

```text
project/
├── README.md
├── AGENTS.md
├── agent.md
├── WORKFLOW.md
├── HANDOFF_CURRENT.md
├── knowledge/
│   ├── FACTS.md
│   ├── REQUIREMENTS.md
│   ├── DECISIONS.md
│   ├── FAILURES.md
│   └── QUESTIONS.md
├── evidence/
│   ├── proofs/
│   ├── analyses/
│   ├── audits/
│   ├── experiments/
│   └── certificates/
├── src/
├── tests/
├── tools/
├── sources/raw/
└── history/
```

小项目可以使用集中式文件；大项目可以每条记录一个文件，并让顶层文件只做索引。

## 3. 一轮工作的生命周期

### 3.1 读取

依次读取项目规则、README、当前 handoff、相关知识与失败、证据和必要来源。
不要把聊天摘要当成仓库状态。

### 3.2 范围锁定

使用：

```text
Task:
Mode:
Base version:
Target:
Inputs:
Outputs:
Allowed paths:
Forbidden paths:
Expected status change:
Acceptance criteria:
Required checks:
Non-goals:
```

范围锁定的目的不是增加仪式，而是防止任务从一个小修复扩张成全仓库重写。

### 3.3 提取变化

从对话和工作结果中提取：

```text
ADD        新增独立内容
UPDATE     修正或扩展已有内容
CONFIRM    增加可靠证据
DOWNGRADE  降低状态
REFUTE     否定陈述或方法
SUPERSEDE  用更准确版本替代
MERGE      合并重复内容
CLOSE      关闭问题
REOPEN     重新打开问题
NO_CHANGE  不应进入仓库
```

变化清单应写明依据、目标文件、状态影响和人工复核需求。

### 3.4 语义查重

检查候选内容是否已经存在、只是换一种措辞、属于特例或推广、与现有记录冲突，
或重复已知失败。重点比较前提、范围、结论和机制，而不是关键词。

### 3.5 建立证据

优先生成能失败的测试、验收用例或反例，再修改实现或正文。
完成后进行敌对审计：

- 是否遗漏前提；
- 是否扩大范围；
- 是否混淆局部和一般结论；
- 是否存在循环依赖；
- 是否忽略边界；
- 是否把超时或工具错误当成对象错误；
- 是否重复旧失败。

### 3.6 写回

先写证据，再写知识，最后写状态和 handoff。
修改当前条目时应原地整理，不要堆叠修正说明。

### 3.7 验证和交付

运行实际存在的检查，审阅完整 diff，确认没有无关修改，再生成完成报告。
默认不提交、不推送。

## 4. 文件更新决策

### 新建文件

适用于：

- 新的独立事实、问题或失败；
- 新的一次审计或实验；
- 新的证明、分析或设计模块；
- 新的历史快照。

### 原地修改

适用于：

- 同一条目的状态变化；
- 范围修正；
- 当前证明或实现的漏洞修复；
- 过时下一步的替换；
- 当前 handoff；
- 重复内容清理。

### 追加

主要适用于：

- changelog；
- 时间序列日志；
- 独立运行索引。

“可审计”不意味着所有文件只能追加；Git 已经保存历史。

## 5. 状态建议

若项目没有自己的体系，可以使用：

| 状态 | 含义 |
|---|---|
| `verified` | 有完整可检查证据 |
| `verified-conditional` | 只在明确附加条件下成立 |
| `implemented` | 已实现并通过规定测试 |
| `observed` | 仅有有限实验或样例 |
| `proposed` | 候选方案 |
| `partially-verified` | 只完成部分范围 |
| `open` | 尚未解决 |
| `blocked` | 缺少依赖、输入或工具 |
| `disputed` | 来源或审计冲突 |
| `refuted` | 有有效否定证据 |
| `superseded` | 被更准确版本替代 |
| `deprecated` | 保留但不应继续使用 |

AI 的肯定回答、少量样例、随机测试、超时和“没有发现问题”均不能单独支持
`verified`。

## 6. 知识条目模板

```markdown
# 标题

- **ID:** K-xxxx
- **Status:** verified
- **Statement:** 精确陈述
- **Scope:** 适用条件和边界
- **Dependencies:** K-xxxx, K-yyyy
- **Evidence:** `evidence/...`
- **Mechanism:** 简短说明为何成立
- **Caveats:** 限制和易误用之处
- **Updated:** YYYY-MM-DD
```

完整证明、实现、分析或实验放在独立证据文件中。

## 7. 开放问题模板

```markdown
# 问题标题

- **ID:** Q-xxxx
- **Status:** open
- **Question:** 可独立回答的问题
- **Why it matters:** 阻塞什么
- **Known:** 已确认内容
- **Missing:** 仍缺什么
- **Answer criterion:** 何时可以关闭
- **Next action:** 一个具体动作
```

问题解决后原地更新并链接证据，不要删除历史 ID。

## 8. 失败记录模板

```markdown
# 方法标题

- **ID:** A-xxxx
- **Goal:** 原目标
- **Approach:** 核心方法
- **Failure type:** logical / counterexample / timeout / unsupported assumption / ...
- **Failure point:** 最具体断点
- **Why it failed:** 已确认原因
- **Failure signature:** 用于识别换名重复
- **Evidence:** 证据位置
- **Retry conditions:** 何时值得重试
- **Do not repeat:** 哪些表面变化仍属同一路线
```

超时、工具报错和暂时未完成不应自动登记为原理失败。

## 9. 机器产物模板

每个生成产物至少记录：

```yaml
generator: tools/example.py
command: python tools/example.py --input ...
inputs:
  - data/input.json
parameters:
  seed: 1234
dependencies:
  python: "3.12"
base_version: "<commit-or-data-version>"
result_type: exhaustive
generated_at: "YYYY-MM-DDTHH:MM:SSZ"
payload_sha256: "<sha256>"
```

应先写临时文件，完成 schema 和哈希验证后再原子替换目标。

## 10. 当前 handoff 模板

```markdown
# Current Handoff

## Objective

当前目标与成功标准。

## Current state

- 当前阶段：
- 最近完成：
- 当前阻塞：
- 当前路线：

## Reliable inputs

下一轮可安全依赖的条目和证据。

## Provisional findings

尚未完全验证的发现及状态。

## Do not repeat

相关失败及重试条件。

## Open questions

按优先级列出少量问题。

## Immediate next actions

最多 3–5 项，每项有明确完成标准。

## Required reading

下一位参与者开始前必须读取的文件。

## Integrity warnings

冲突、未验证步骤、数据缺口和环境限制。
```

更新后应像当前时刻一次写成，不应保留连续的日期更新区块。

## 11. 主结论组装检查

使用多个知识模块构建更大结论时，对每个调用点检查：

- 当前对象是否满足前提；
- 输入输出是否匹配；
- 范围和量词是否兼容；
- 依赖是否已验证；
- 结论是否足够强；
- 模块之间是否缺少连接步骤；
- 是否引用被否定或废弃条目。

最终正式文本应展开逻辑连接，而不是只列内部 ID。

## 12. Git 与冲突处理

默认不提交、不推送、不建 PR。不得强制 reset、清理未知文件或覆盖无关修改。

若当前对话与仓库冲突：

1. 不静默覆盖；
2. 保留双方来源；
3. 标记冲突或创建问题；
4. 只有证据足够时才裁决；
5. handoff 与权威记录冲突时修复 handoff。

## 13. 完整性检查

结束前检查：

1. 是否读取项目规则和当前状态；
2. 是否限制修改范围；
3. 是否完成语义查重；
4. 是否保留稳定 ID；
5. 是否把观察或条件结果写成一般结论；
6. 是否存在开放义务却关闭问题；
7. 是否存在循环依赖；
8. 是否引用不存在或废弃条目；
9. 是否修改原始来源；
10. 是否手改生成结果；
11. 是否运行实际存在的检查；
12. 是否审阅完整 diff；
13. handoff 是否删除过时内容并保持简短；
14. 是否诚实记录环境和工具限制。

## 14. 完成报告模板

```text
Base version:
Mode:
Scope:
Authoritative files read:

Added:
Updated:
Downgraded or refuted:
Closed or reopened:

Changed files:
Generated artifacts:
Checks run:
Results:

Canonical status change:
Unresolved issues:
Non-goals:

Diff stat:
Committed: no
Next action:
```

若无权威状态变化，写：

```text
No canonical status was promoted.
```

## 15. 总结

推荐工作链：

```text
读取权威状态
→ 锁定范围
→ 提取候选变化
→ 语义查重
→ 建立证据或实现
→ 敌对审计
→ 原地整理知识
→ 最后同步状态
→ 生成干净 handoff
→ 审阅 diff
```

强制规则见 [`agent.md`](agent.md)。
