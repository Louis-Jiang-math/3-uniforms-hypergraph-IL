# Current Handoff

## 1. Objective and status

研究对象是三一致等块分块超图。目标是在块大小为 \(b\) 时证明
\[
\Delta(H)<\left(\frac14-o(1)\right)b^2\Longrightarrow H\text{ 有独立横截（IT）}.
\]
当前尚无完整的 \(1/4\) 证明。现有成果已经建立配置优先的单缺陷账本、可审计 pivot-switch、escape Hall 收费和条件森林摊还；未解决的是近无损配置入口、persistent-blocker 正常形，以及因果 incidence 再生为何最终集中或闭合。

任何证明必须保留真实块、顶点、边身份，全局单位边容量，实际执行 genealogy，root projection，配置槽位和完整块支持。相位标签、压缩状态或历史出现次数不能替代这些对象。

## 2. Frozen decisions

- **共同预置 pivot 已被否定。** F-0029/Q-0014 的四块八边反例表明，同一成功后继的不同失败可强制不同 pivot；源稳定记录不得预置共同 pivot。
- **配置优先入口已冻结。** 失败先形成 obligation；枚举全部合法真实两步 root configurations；只有获得正配置流的分支才生成带 pivot 的 defect record。
- **释放端点后必须复检独立性。** 结果是 ordinary single-defect、组合 pivot-switch，或仍含第二真实边的 multi-defect。
- **pivot-switch 不是免费换账。** 组合 switch 是静态交换方块；只有真实 reroot lift 才能生成新的可执行根配置，继续质量必须保留旧 genealogy 和统一真实边容量。
- **terminal SCC 后置。** 在配置流、投影闭包、formal closure-or-charge 和正常形接口成立前，不把压缩 SCC 当作合法终局对象。

## 3. Current proof architecture

当前候选管线是
\[
\text{obligations}\to\text{root-configuration LP/Hall}\to
\text{positive-flow defect fibers}\to\text{ordinary or escape charge}\to
\text{critical forest}\to\text{degree / IT / complete-block core}.
\]
三份账本必须分开：
1. obligation–configuration 需求与 root-pivot 总预算；
2. \((\widehat S,p,e)\) 递推槽位容量；
3. 全局真实边剩余容量。
任何一份可行都不能自动推出另外两份可行。

## 4. Established components

- 完整真实块上的块极小化成立；中位源给出 \((1/4+o(1))b^2\) 规模义务（F-0002–F-0004）。
- 真实边单位容量的正确接口是加权 Hall；配置预算与槽位容量若成立，条件递推保留单个 \(\Delta(H)\) 因子（F-0005、F-0022、F-0027）。
- Q-0015 审计器已归档在 `enumerate/`：合法配置枚举、预算原始/对偶 LP、槽位流、真实边 Hall 流和回归证书（F-0030）。
- \((b,m,\Delta)=(3,14,2)\) 的无 IT 候选已被严格排除（F-0031）。
- 组合 pivot-switch、真实 reroot lift 和执行可审计性已证明（F-0032）。
- 非 ordinary 失败可产生 switch incidence 或第二真实边 incidence；有限 escape obligations 要么全部由真实边剩余容量支付，要么输出真实边 Hall/reuse 割（F-0033）。
- 移除已支付 escape 质量后，未支付活动质量严格保持同一 pivot、同一 root projection 和一个缺失块：这是 **formal closure-or-charge**，不是近无损动态 closure。
- 若每个森林节点的继续质量至多为父质量的 \(11/27\)，则
  \[
  W_h\le \frac{27}{16}(F_h+R_h+A_h)+B_h;
  \]
  常数最佳（F-0034）。
- 真实 incidence 无条件只能推出“负载集中或收费顶点增殖”，不能推出 \(1/4\) 或完整子核心（F-0035）。

## 5. Open bottlenecks

### A. Configuration entry — Q-0002 / Q-0015
需要从任意低度、块极小、无 IT 实例构造近无损配置流，并同时证明合法配置完备、root projection 实际可达、质量守恒、root-pivot 预算、槽位容量及全局真实边容量。审计基础设施已完成；一般存在性定理仍开放。

### B. Persistent-blocker normal form — Q-0017
需要证明持续 blocker 要么进入增广、fresh、reuse、Hall、quotient 或内部闭合出口，要么可归约为每层继续质量至多 \((11/27+o(1))\) 的临界 splitter。F-0034 只是在该假设下的摊还定理。

### C. Causal incidence regeneration — Q-0016
即使 escape 费用可注入真实边，费用仍可分散到不断出生的新 pivot。需要证明：在无 reuse、无增广、无 exact-future quotient 的未来闭合区域中，可审计的新 pivot 再生不能长期无损；否则产生正比例 fresh 容量、某点 \((1/4-o(1))b^2\) 度数、完整真子无 IT 核心或未覆盖未来选择。

### D. Terminal structure and stability — Q-0003 / Q-0005–Q-0007
critical-link 稳定性、二进制强迫森林终局、零误差 terminal 分类和固定 \(\varepsilon\) 稳定化均依赖 A–C；当前均未完成。

## 6. Immediate proof target

下一条应证明的是 **深度二临界 splitter–再生引理**：对两个连续近临界 defect 模块，在保留真实边、pivot、root projection 和 genealogy 的条件下，至少出现：
1. 第二层支付使用正比例新鲜真实容量；
2. 第二层质量回到有界旧锚集合，从而可用已有基准负载逼近 \(1/4\)；
3. 两层未来支持对完整真子块集闭合并形成无 IT 子核心；
4. 存在未被 blocker 覆盖的合法未来选择，产生增广或 IT；
5. 或输出槽位/真实边 reuse、exact-future quotient 等已命名证书。

先证明零误差深度二版本，再迭代到 genealogy 森林；不要从总 incidence 质量直接声称集中。计算侧应在 `enumerate/` 中加入两层 ordinary/switch/multi-defect 展开，搜索最小反例和等号结构。

## 7. Computational state

- `enumerate/q0015_configuration_auditor.py` 是当前审计基线。
- `q0015_first_execution_results.json` 保存历史原始运行；当时的 100 轮 MILP 不是穷尽证明。
- `q0015_hall_cut_structural_analysis.md` 随后严格排除 \((3,14,2)\)，并分析预算缺口、no-configuration 和 genealogy collision。
- F-0029、九边预算修复、错误 genealogy 合并和 \((3,14,2)\) 排除必须保留为回归测试。
- 所有新脚本、JSON、日志和报告只能进入 `enumerate/`。

## 8. Do not repeat

- 不用 monodromy、条件化、bounded width 或状态熵自动收费。
- 不从相位一致、满投影、代码簿或部分支持推出笛卡尔乘积；块极小性只适用于完整真实块。
- 不把第一阻断边唯一性当作真实边单位容量；不在删除端点后跳过独立性复检。
- 不合并仅有相同压缩迹、但 genealogy、槽位或未来阻断标签不同的状态。
- 不把 pivot-switch 当作重新获得免费 \(\Delta(H)\) 预算。
- 不从 incidence 增殖直接推出 \(1/4\) 或子核心；对角分散模型是否定该推论的回归反例。
- 不把 persistent-blocker 圆柱化当作已知分类；“闭合后推出子核心”不等于“必须闭合”。
- 不用有限 LP/MILP 超时或小参数不可行代替一般结构定理。

## 9. Integrity checks

任何新的 closure、quotient、收费或终局命题都必须说明：使用哪份容量账本；真实边是否跨 projection/genealogy 重复；root projection 是否实际可达；switch 后质量是否保留原 genealogy 且是否已支付；quotient 是否保持未来义务、槽位、真实边账本和第一阻断标签；子核心是否由完整真实块组成并对每个完整横截都有内部真实阻断边。

当前框架是候选证明基础设施，不是 \(1/4\) 定理。外部 \(4/27\) 基准、历史机器报告和 \(1/4\) 锐性构造仍需独立复核。

## 10. Required reading

1. `SINGLE_DEFECT_FRAMEWORK.md` v0.5：第 3–12、20、23–24 节。
2. `PIVOT_SWITCH_ESCAPE_FRAMEWORK.md`：组合 switch、reroot lift、escape Hall、formal closure-or-charge、条件森林摊还及其局限。
3. `QUESTIONS.md`：Q-0002、Q-0015–Q-0017；随后读 Q-0003、Q-0005–Q-0007。
4. `FACTS.md`：F-0005、F-0022、F-0027–F-0035；`FAILURES.md`：A-0019–A-0025。
5. `enumerate/q0015_first_execution_report.md` 与 `enumerate/q0015_hall_cut_structural_analysis.md`。
6. `old/handoff_toward_one_quarter.md` 仅作历史背景；共同预置 pivot、直接 terminal SCC 和未经配置审计的圆柱化表述已被当前框架替代。
