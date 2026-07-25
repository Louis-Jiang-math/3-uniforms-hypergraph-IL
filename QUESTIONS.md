# Questions

## Q-0001 — \(3/20\) 扩张缺陷如何收费

- **Question:** 对终端正常图册核心 \(\mathscr C\)，能否证明 \(\operatorname{ExtDef}(\mathscr C)\le C\,\operatorname{Credit}(\mathscr C)\)，并达到 \(3/20\) 所需的定量强度？
- **Status:** open
- **Why it matters:** 这是现有 \(3/20\) 管线中唯一未闭合的结构命题。
- **Known so far:** F-0015；零信用定性闭包不足以推出固定正间隙（A-0014）。
- **Missing:** 对许多小正常圆柱 sector 的统一压缩或真实阻断图定理。
- **Related:** F-0015, F-0016, A-0014
- **Sources:**
  - `handout(4).md`，第 1750–1944 行，发言者 `unknown`
  - `handoff_toward_one_quarter.md`，第 500–517 行，发言者 `unknown`
- **Suggested next action:** 在原超图上形式化一维近满 pair-star blocker graph，并证明其不能无费用覆盖全部完整横截。
- **Answer criterion:** 给出统一常数 \(C\) 的完整证明，且所有费用使用真实边身份、单位容量和完整块边界。
- **Last updated:** 2026-07-24

## Q-0002 — 单缺陷搜索方案是否存在

- **Question:** 对每个固定 \(\varepsilon>0\)，能否从任意块极小无 IT 实例构造满足质量守恒、真实边容量一和投影重数 \(1+\gamma\) 的单缺陷搜索方案？
- **Status:** open
- **Why it matters:** 由 F-0022，这一方案直接给出 \((1/4-\varepsilon)b^2\) 以下存在 IT。
- **Known so far:** 中位源、真实边容量和条件递推已完成（F-0004, F-0005, F-0022）。
- **Missing:** 严格定义 \(\mathcal S_k,\mathcal D_k,\pi\) 并控制 defect 投影重数。
- **Related:** F-0022, Q-0003, Q-0004, Q-0005
- **Sources:**
  - `handoff_toward_one_quarter.md`，第 827–951 行及第 1103–1121 行，发言者 `unknown`
- **Suggested next action:** 冻结状态只含真实部分横截、唯一 pivot、唯一缺失块和第一阻断边，证明每个失败扩张恰进入一个 defect 状态。
- **Answer criterion:** 对所有步 \(k\) 证明 \(|\mathcal B_k|\le(1+\gamma)\Delta|\mathcal S_{k-2}|\) 且 \((1+\gamma)(1/4-\varepsilon)<1/4\)。
- **Last updated:** 2026-07-24

## Q-0003 — critical link 稳定性

- **Question:** 低于 \(1/4-\varepsilon\) 的块极小实例中，承载正比例失败质量的 terminal pivot link 是否必有增广出口、正比例真实费用，或接近平衡完全二部图？
- **Status:** open
- **Why it matters:** 它是单缺陷方案的局部近等号分类。
- **Known so far:** 非正常四块窗口有九面共同锚证书（F-0011）。
- **Missing:** 从失败质量与最大度约束推导 graph-link 稳定性的定量论证。
- **Related:** F-0011, F-0022, Q-0005
- **Sources:**
  - `handoff_toward_one_quarter.md`，第 955–991 行，发言者 `unknown`
- **Suggested next action:** 先在零误差模型中证明 terminal link 必为精确平衡完全二部图或有出口。
- **Answer criterion:** 对每个 \(\varepsilon\) 给出 \(\delta(\varepsilon)>0\) 和完整三分证明。
- **Last updated:** 2026-07-24

## Q-0004 — pivot 相位的全局粘合

- **Question:** 剥离少量异常后，正常交换方块的八相位能否全局定向，使真实边不重复、defect 投影平均重数至多 \(1+O(\delta)\)，并保留真实 pivot 谱系？
- **Status:** open
- **Why it matters:** 局部 \(\mathcal T_4\) 分类只有在控制真实身份和投影重数后才能用于单缺陷递推。
- **Known so far:** F-0008–F-0013；纯 monodromy 收费和纯相位乘积化均失败（A-0001, A-0002）。
- **Missing:** 跨图表的真实边身份守恒和闭路 pivot genealogy 定理。
- **Related:** F-0013, A-0001, A-0005
- **Sources:**
  - `handoff_toward_one_quarter.md`，第 993–1010 行，发言者 `unknown`
- **Suggested next action:** 在精确 terminal defect graph 上标记每条过渡使用的第一真实阻断边，并分类所有正常交换方块的可交换性。
- **Answer criterion:** 构造全局定向并证明容量与投影重数界；不能只给 cocycle 分类。
- **Last updated:** 2026-07-24

## Q-0005 — 二进制强迫森林终局

- **Question:** 无增广出口、正常交换、无边复用且 links 接近平衡二部的 terminal defect 组件，是否必产生完整真子无 IT 核心、\((1/4-o(1))b^2\) 的 link 乘积，或可继续增广的叶？
- **Status:** open
- **Why it matters:** 这是把局部近等号结构转化为 \(1/4\) 次数或极小性矛盾的终局。
- **Known so far:** F-0002, F-0022；固定核心和若干连接器类已有下界（F-0016, F-0024）。
- **Missing:** terminal SCC 的精确分类及其 genealogy 到完整 link 乘积的证明。
- **Related:** Q-0003, Q-0004, Q-0006
- **Sources:**
  - `handoff_toward_one_quarter.md`，第 1012–1047 行及第 1257–1290 行，发言者 `unknown`
- **Suggested next action:** 先证明零误差 terminal SCC 定理，失败时输出一个真实边身份完整的反模型。
- **Answer criterion:** 对每个 terminal 组件证明三出口之一，并确保子核心由完整真实块组成。
- **Last updated:** 2026-07-24

## Q-0006 — 零误差 terminal SCC 分类

- **Question:** 在所有交换方块正常、无竞争认证、无边界、无真实边复用且 links 恰为完全二部图的精确模型中，terminal SCC 是否必为二进制强迫森林或完整子核心？
- **Status:** open
- **Why it matters:** 这是当前建议最先解决的、最小化了误差项的核心命题。
- **Known so far:** 局部模板已完全枚举（F-0009–F-0012）。
- **Missing:** 不依赖进一步 atlas 细分的全局图论分类。
- **Related:** Q-0005, Q-0007
- **Sources:**
  - `handoff_toward_one_quarter.md`，第 1148–1168 行及第 1253–1290 行，发言者 `unknown`
- **Suggested next action:** 明确定义 terminal defect graph 的顶点、边、pivot 继承和缺失块移动，然后证明或计算搜索最小反例。
- **Answer criterion:** 给出严格分类定理；若为假，给出满足全部零误差条件的真实反模型。
- **Last updated:** 2026-07-24

## Q-0007 — 固定 \(\varepsilon\) 的稳定化

- **Question:** 零误差分类成立后，能否把所有异常质量控制为 \(\gamma(\varepsilon)\)，并满足 \((1+\gamma(\varepsilon))(1/4-\varepsilon)<1/4\)？
- **Status:** blocked
- **Why it matters:** 它把精确分类升级为实际的 \(1/4-\varepsilon\) 证明。
- **Known so far:** 非正常窗口有九面证书，且真实边容量和 link 边数可提供预算（F-0005, F-0011）。
- **Missing:** Q-0006 的零误差定理以及各异常分支的统一定量稳定性。
- **Related:** Q-0003, Q-0004, Q-0006
- **Sources:**
  - `handoff_toward_one_quarter.md`，第 1170–1194 行，发言者 `unknown`
- **Suggested next action:** 在 Q-0006 完成后，逐类定义异常质量并证明总量 \(O(\delta)\)。
- **Answer criterion:** 显式给出 \(\delta(\varepsilon)\)、\(\gamma(\varepsilon)\) 和所有误差账本。
- **Last updated:** 2026-07-24

## Q-0008 — 重纤维的覆盖保持二点选择

- **Question:** 逐层具有线性大完成集的高重叠循环核心，能否选择每层两个真实顶点，使诱导二相位接口覆盖全部二进制循环词并保留固定比例质量？
- **Status:** partially_answered
- **Why it matters:** 这是旧 \(\sqrt6\)/二相位路线从真实纤维到有限自动机的忠实接口。
- **Known so far:** 自适应二相位安全核被有限计算报告支持（F-0025）；逐层平均捕获不保证全局覆盖。
- **Missing:** 循环相容、覆盖保持的选择定理，或证明障碍产生新鲜度数/survivor/真子核心。
- **Related:** F-0025, A-0009, A-0010, A-0016
- **Sources:**
  - `chatgpt-export__(_sqrt{6}_) 路线评估.txt`，助手回答轮次 12，第 5760–5809 行，发言者 `assistant`
- **Suggested next action:** 建立二点覆盖博弈的对偶；把 one-hot 对偶障碍翻译为真实边费用或完整子核心。
- **Answer criterion:** 给出绝对常数 \(\theta,\rho>0\) 的四出口“重纤维相干—扩张引理”。
- **Last updated:** unknown

## Q-0009 — 遗传相位饱和与块完全 lift

- **Question:** 无损可逆相位覆盖核心为何不能长期只覆盖相关代码簿，而必须产生可收费的未来选择依赖、liftable survivor 或对未来不筛选的圆柱分量？
- **Status:** partially_answered
- **Why it matters:** 这是旧 S3.5 路线从相位代数到完整真实块子实例的缺失桥梁。
- **Known so far:** cocycle/覆盖代数和矩形 lift 的充分条件已部分证明（F-0013, F-0014）；纯相位结论不足（A-0001–A-0003）。
- **Missing:** “终端分量对未来真实选择的可恢复筛选”必须收费或消失的结构定理。
- **Related:** F-0014, A-0002, A-0013
- **Sources:**
  - `chatgpt-export_第一阶段解析骨架.txt`，助手回答轮次 37，第 15683–16094 行，发言者 `assistant`
- **Suggested next action:** 尝试把未来选择依赖归约为端口复用、锚谱系或 single-defect pivot 迁移；否则构造真实代码簿反模型。
- **Answer criterion:** 对全部完整块选择建立精确遗传扩张完整性，不能只覆盖 \(1-o(1)\) 质量。
- **Last updated:** unknown

## Q-0010 — 固定轻锚能否持续生成

- **Question:** 在有限块完全连接器网络中，能否反复产生新的、固定的、此前仅有 \(o(b^2)\) 负载的锚点，同时保持所有顶点次数低于 \((1/4-\varepsilon)b^2\)？
- **Status:** open
- **Why it matters:** 单个固定轻锚可低于 \(1/4\) 局部关闭 residual（F-0023），但已知圆柱型替代结构回到 \(1/4\)（F-0024）。
- **Known so far:** 重复使用同一轻锚会产生 \(\Theta(b^3)\) 次数（A-0018）。
- **Missing:** 对任意跨历史三元边网络的全局锚依赖图论证。
- **Related:** F-0023, F-0024, A-0018, Q-0005
- **Sources:**
  - `chatgpt-export_文章核心问题分析(1).txt`，助手回答轮次 100，第 52902–53005 行，发言者 `assistant`
- **Suggested next action:** 将固定轻锚生成链嵌入 terminal defect SCC，证明有限性迫使返回旧锚或服务线性多个状态。
- **Answer criterion:** 证明每次生成新轻锚必触发变量锚复制、旧锚复用、未完成汇合或递归 residual，且递归终局给出 \(1/4\)。
- **Last updated:** unknown

## Q-0011 — 拓扑 Hall 连通度下界

- **Question:** 对当前 stretched multipartite 类，是否存在足够强的独立复形连通度下界，例如 \(\eta(\operatorname{Ind}(F))\gtrsim |V(F)|/(2\sqrt{\Delta(F)})\)？
- **Status:** open
- **Why it matters:** 若成立，可能直接导出 \(1/4\) 并为 critical link 稳定性提供归纳框架。
- **Known so far:** 标准拓扑 Hall/Rado 准则可把 IT 归约为所有块子集的独立复形连通度。
- **Missing:** 对三一致到 \((2,3)\)-mixed link 的连通度递推或反例。
- **Related:** Q-0003
- **Sources:**
  - `handoff_toward_one_quarter.md`，第 1049–1099 行，发言者 `unknown`
- **Suggested next action:** 先检验该不等式在树型极端例、完整二部 link 圆柱和小参数 mixed links 上是否成立。
- **Answer criterion:** 给出严格定理及常数，或给出当前模型内反例。
- **Last updated:** 2026-07-24

## Q-0012 — 历史机器证书的独立复核

- **Question:** 272/8/9 枚举、749 状态安全核、小规模 MILP 和 fractional matching 报告能否由当前可用代码与日志独立重现？
- **Status:** blocked
- **Why it matters:** 多个结构判断依赖这些有限结果，但部分记录只有摘要，未含本轮运行日志。
- **Known so far:** handout 附有 \(Q_4\) 枚举程序；其他机器结果主要以对话报告形式出现。
- **Missing:** 完整检查器、版本、输入、输出、哈希和独立运行记录。
- **Related:** F-0009, F-0010, F-0011, F-0025, F-0026
- **Sources:**
  - `handoff_toward_one_quarter.md`，第 698–750 行及附录 A，第 1329–1476 行，发言者 `unknown`
  - `chatgpt-export_基准真实边集合证明.txt`，助手回答轮次 35，第 14992–15109 行，发言者 `assistant`
- **Suggested next action:** 先运行两份 handout 自带的 \(Q_4\) 枚举，再索取或重建其余检查器并保存机器可读证书。
- **Answer criterion:** 每个数字均可由固定版本脚本从声明输入重现，并有独立校验。
- **Last updated:** 2026-07-24

## Q-0013 — \(1/4\) 锐性构造的同稿复核

- **Question:** 当前项目接受的 \(1/4\) 目标常数是否有一份在本输入集合内完整、独立可复核的锐性构造与最大度计算？
- **Status:** blocked
- **Why it matters:** 证明 \(1/4\) 下界若要宣称最优，需要同时确认相匹配的无 IT 构造。
- **Known so far:** 对话多次描述树型构造在 \(k=3\) 时最大度为 \(b+\lfloor b^2/4\rfloor\)，但最新 handoff 明确说未在同一手稿中完整复核锐性。
- **Missing:** 原始论文/PDF 或自足构造证明、无 IT 证明和最大度审计。
- **Related:** F-0001, F-0020
- **Sources:**
  - `handoff_toward_one_quarter.md`，第 10–20 行，发言者 `unknown`
  - `chatgpt-export_证明主线与障碍.txt`，助手回答轮次 1，第 44–67 行，发言者 `assistant`
- **Suggested next action:** 提供原始构造文档并逐步核对路径阻断机制与最大度公式。
- **Answer criterion:** 在当前知识库中加入一条带完整证明来源的 `confirmed` 锐性事实。
- **Last updated:** 2026-07-24
