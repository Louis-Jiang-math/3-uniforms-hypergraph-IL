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

## Q-0002 — 配置优先的单缺陷搜索方案是否存在

- **Question:** 对每个固定 \(\varepsilon>0\)，能否从任意块极小无 IT 实例构造满足真实执行性、质量守恒、合法根配置完备性、投影闭包、配置流预算和槽位重数 \(1+\gamma\) 的搜索方案？
- **Status:** open
- **Why it matters:** 由修订后的 F-0022，这一方案若满足
  \[
  (1+\eta)(1+\gamma)(1/4-\varepsilon)<1/4
  \]
  并控制全部异常质量，就直接给出 \((1/4-\varepsilon)b^2\) 以下存在 IT。
- **Known so far:** Q-0014 的共同预置 pivot 命题已被 F-0029 的真实正常四块反例否定。`SINGLE_DEFECT_FRAMEWORK.md` v0.5 改用无 pivot 源稳定记录、失败义务、合法根配置和配置流；条件递推已保留（F-0005, F-0022, F-0027–F-0029）。
- **Missing:** 证明以下接口对实际搜索同时成立：
  1. O1：每个失败义务的全部真实两步单缺陷配置被完备枚举；
  2. O2：每个合法配置的 root projection 属于实际访问的深度 \(k-2\) 源稳定层；
  3. O3：除受控异常外，存在近无损配置流并满足 root-pivot 预算及投影—pivot—根边槽位容量；
  4. O4：获得正流的分支在后续缺陷移动中保持真实 pivot、root projection 与一个缺失块。
- **Related:** F-0022, F-0027, F-0028, F-0029, Q-0003, Q-0004, Q-0005, Q-0014, Q-0015
- **Sources:**
  - `handoff_toward_one_quarter.md`，第 827–951 行及第 1103–1121 行，发言者 `unknown`
  - `SINGLE_DEFECT_FRAMEWORK.md` v0.5，第 3–11、17、20–22 节
- **Suggested next action:** 审计器已完成；下一步把它接到低度候选生成器，并加入 escape-charge、跨 root projection 联合预算和可复算最小割分类。
- **Answer criterion:** 对所有步 \(k\) 完整验证修订后的 SD1–SD8、MC1–MC5，并证明
  \[
  \mathcal B_k\le(1+\eta)(1+\gamma)\Delta(H)A_{k-2},
  \]
  且所有未分配配置质量和其他异常进入显式误差账本。
- **Last updated:** 2026-07-27

## Q-0003 — critical link 稳定性

- **Question:** 在 F-0022 的活动缺陷图中，承载正比例失败质量的固定 pivot link \(L_H(p)\) 是否必有增广出口、正比例真实费用，或接近平衡完全二部图？
- **Status:** open
- **Why it matters:** 每次普通缺陷移动
  \[
  U\longmapsto (U\setminus\{z\})\cup\{y\}
  \]
  对应真实 link 边 \(yz\in L_H(p)\)；它是单缺陷方案的局部近等号分类。
- **Known so far:** 非正常四块窗口有九面共同锚证书（F-0011）；普通 defect transition 的真实 link 解释已在候选框架中明确。
- **Missing:** 从失败质量、增广出口缺失和最大度约束推导 graph-link 稳定性的定量论证；还需确保 transition edge 与根收费边的账本不被混用。
- **Related:** F-0011, F-0022, Q-0005, Q-0006
- **Sources:**
  - `handoff_toward_one_quarter.md`，第 955–991 行，发言者 `unknown`
  - `SINGLE_DEFECT_FRAMEWORK.md`，第 8–9、12 节
- **Suggested next action:** 先在零误差执行缺陷图中证明 terminal link 必为精确平衡完全二部图或有出口。
- **Answer criterion:** 对每个 \(\varepsilon\) 给出 \(\delta(\varepsilon)>0\) 和完整三分证明，并逐项说明真实边容量来源。
- **Last updated:** 2026-07-25

## Q-0004 — 配置分支的正常相位全局粘合

- **Question:** 在配置提取之后，正常交换方块产生的带 pivot 分支能否在保留真实 root projection、配置来源和 pivot genealogy 的执行图上全局运输，使每个 \((\widehat S,p,e)\) 槽位的平均重数至多 \(1+O(\delta)\)？
- **Status:** open
- **Why it matters:** F-0029 已否定“先为源状态选择共同 pivot”的局部版本；正常 \(\mathcal T_4\) 分类只有在配置分支层控制真实身份、协变端点运输和 genealogy 后才能用于 F-0022。
- **Known so far:** F-0008–F-0013；纯 monodromy 收费和纯相位乘积化均失败（A-0001, A-0002）；原始端点变化不能直接收费（A-0006）；共同预置 pivot 被 F-0029/A-0022 否定。
- **Missing:** 跨图表的真实边身份守恒、配置分支闭路重数定理，以及高度复用配置何时可按未来等价合法合并的精确判据。
- **Related:** F-0013, F-0022, F-0029, A-0001, A-0005, A-0006, A-0022, Q-0015
- **Sources:**
  - `handoff_toward_one_quarter.md`，第 993–1010 行，发言者 `unknown`
  - `SINGLE_DEFECT_FRAMEWORK.md` v0.5，第 3、9–10、13、20–21 节
- **Suggested next action:** 对 Q-0015 输出的真实 Hall 最小割保存插入顶点、释放顶点、根边、root projection 和配置来源；先分类哪些高重叠分支可以保持未来行为地合并。
- **Answer criterion:** 构造配置分支的全局运输并证明槽位重数界；若还需要全局真实边注入，另行证明加权 Hall，不能只给 cocycle 分类。
- **Last updated:** 2026-07-27

## Q-0005 — 二进制强迫森林终局

- **Question:** 无增广出口、正常交换、无边复用且 links 接近平衡二部的 terminal 执行缺陷组件，是否必产生完整真子无 IT 核心、\((1/4-o(1))b^2\) 的真实 link 乘积，或可继续增广的 genealogy 叶？
- **Status:** open
- **Why it matters:** 这是把局部近等号结构转化为 \(1/4\) 次数或块极小性矛盾的终局。
- **Known so far:** F-0002, F-0022；固定核心和若干连接器类已有下界（F-0016, F-0024）；候选框架已区分执行缺陷图与压缩 defect graph。
- **Missing:** terminal SCC 的精确分类，以及从压缩 SCC 展开到真实 genealogy 后产生完整 link 乘积或完整块子核心的证明。
- **Related:** Q-0003, Q-0004, Q-0006
- **Sources:**
  - `handoff_toward_one_quarter.md`，第 1012–1047 行及第 1257–1290 行，发言者 `unknown`
  - `SINGLE_DEFECT_FRAMEWORK.md`，第 9、14 节
- **Suggested next action:** 只在 Q-0015 的配置流、Q-0002 的投影闭包与配置化 defect closure 完成后研究执行 terminal SCC；失败时输出真实块、顶点、边、配置来源、pivot、缺失块和每一步阻断边。
- **Answer criterion:** 对每个 terminal 组件证明增广叶、真实 \(1/4\) link 乘积、完整真子核心之一；子核心必须由完整真实块组成。
- **Last updated:** 2026-07-25

## Q-0006 — 配置化零误差 terminal SCC 分类

- **Question:** 在满足下列零误差公理的有限执行缺陷图中，terminal SCC 是否必产生增广叶、完整真实块子核心或精确 \(1/4\) link 乘积？
  - 每个普通失败义务被完整分配到合法真实根配置；
  - 每个获得正流的配置分支带唯一 pivot，且 pivot 在缺陷移动中保持；
  - 单端点释放后迹仍独立；
  - 无竞争认证、无边界、无不相容未记账配置；
  - 所有四块交换方块正常；
  - 真实 genealogy、root projection 与边身份完整保留；
  - 配置槽位重数为一；
  - terminal pivot link 为精确平衡完全二部图。
- **Status:** blocked
- **Why it matters:** 这是误差最少的核心终局，但它只有在配置提取、投影闭包和配置化执行图确实存在后才有定义。
- **Known so far:** Q-0014 的共同预置 pivot 版本已被 F-0029 否定；局部模板已完全枚举（F-0009–F-0012）；候选框架 v0.3 给出了配置化 Z1–Z9 和可编程数据格式。
- **Missing:** Q-0015、Q-0002 的零误差配置流与执行闭包，以及不依赖进一步 atlas 细分的全局图论分类。
- **Related:** Q-0002, Q-0005, Q-0007, Q-0014, Q-0015
- **Sources:**
  - `handoff_toward_one_quarter.md`，第 1148–1168 行及第 1253–1290 行，发言者 `unknown`
  - `SINGLE_DEFECT_FRAMEWORK.md` v0.5，第 14、18、20 节
- **Suggested next action:** 在 Q-0015 与配置化 defect closure 通过后，对最小真实执行模型进行证明或穷举；枚举器必须检查每条阻断边、每个 root projection 和每份配置流的真实身份。
- **Answer criterion:** 给出严格三出口分类；若为假，给出满足全部配置化零误差公理的真实反模型，而不是仅给相位商图。
- **Last updated:** 2026-07-27

## Q-0007 — 固定 \(\varepsilon\) 的 faithful stability backend

- **Question:** 若 Q-0018 给出 zero-或 vanishing-loss 的 faithful Round-or-Core，且 Q-0016 给出每个 actual recurrent core 的终局后果，F-0038/F-0051/F-0042 的现有稳定性代数是否以统一参数闭合固定 \(\varepsilon\)？
- **Status:** blocked
- **Backend status:** conditional backend available
- **Why it matters:** 它把精确/近精确的 actual-object 分类翻译为 \(1/4-\varepsilon\) 的二阶递推，但不应再被误写成一个独立的异常分类计划。
- **Known so far:** F-0038 给出精确 critical-profile deficit 恒等式；F-0051 在 clean faithful product chart 中给出互斥 rank/leaf/structural-exit 账本；F-0042 在有效重数与未控余项满足显式 \(<1/4\) 不等式时关闭递推。若 strong Round-or-Core 的损失为零，或随深度一致趋零，则这些工具构成可用的条件 stability backend。
- **Missing:** Q-0018 必须提供与递推量一致的 global Round 质量、三份账本的合法输入及 zero/vanishing loss；Q-0016 必须关闭 positive-mass actual core。不存在独立证据支持再逐类发明一套新的 stability defect taxonomy。
- **Related:** F-0038, F-0042, F-0051, F-0055, Q-0016, Q-0018
- **Suggested next action:** 无独立主线动作。把所有 loss/normalization 义务写入 Q-0018 的 global entrance/Round compatibility；把 core 后果写入 Q-0016。
- **Answer criterion:** 在 Q-0018/Q-0016 的实际输出上验证统一参数使最终二阶系数严格小于 \(1/4\)，或证明 exact zero-loss 情形直接适用 F-0042；不得把条件 chart 结论提升为无条件 stability theorem。
- **Last updated:** 2026-08-01

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

## Q-0014 — 零误差共同预置 pivot 定向

- **Question:** 在所有相关四块交换均正常、无竞争认证、无边界的执行组件中，能否预先为每个稳定记录指定一个共同唯一真实 pivot，并使同一成功后继的每个普通失败都写成
  \[
  \widetilde S_0\xrightarrow{\,r\,}\widetilde S_1
  \xrightarrow[\mathrm{fail}]{\,x\,},
  \qquad
  e_0=\{p,r,x\},
  \]
  其中第一步保持该共同 pivot，且释放 \(r\) 后 \(T(\widetilde S_0)\cup\{x\}\) 独立？
- **Status:** answered — negative
- **Answer:** 否。F-0029 给出四个二元块上的八边真实反例。它无 IT、边极小、块极小、无竞争认证，且对应正常 \(Q_4\) 模板。对真实根迹
  \[
  R=\{0_0,1_0\}
  \]
  成功加入 \(r=2_1\) 后，尝试 \(3_0\) 的唯一阻断边为
  \[
  \{1_0,2_1,3_0\},
  \]
  强制 pivot 为 \(1_0\)；尝试 \(3_1\) 的唯一阻断边为
  \[
  \{0_0,2_1,3_1\},
  \]
  强制 pivot 为 \(0_0\)。两次释放后都恢复独立，但不存在共同预置 pivot。
- **Why it matters:** 共同唯一 pivot 不能继续作为源稳定状态或 terminal defect graph 的前置公理。
- **Known so far:** 该反例否定字面零误差命题，但因 \(b=2,\Delta=3\)，不否定低度渐近条件下“绝大部分义务可由近无损配置流吸收”的稳定化命题。
- **Related:** F-0027, F-0028, F-0029, A-0021, A-0022, Q-0002, Q-0004, Q-0006, Q-0015
- **Sources:**
  - `SINGLE_DEFECT_FRAMEWORK.md` v0.5，第 3 节
  - `knowledge/FACTS.md`，F-0029
- **Suggested next action:** 不再重试共同预置 pivot；继续把该反例作为配置流、genealogy 和 escape-charge 审计的强制回归测试。
- **Answer criterion:** 已满足：真实块、顶点、边、执行根迹、成功旧端点、两个失败、第一阻断边和释放后独立性均已列出。
- **Last updated:** 2026-07-27

## Q-0015 — Route A：近无损配置流、aggregate heavy excess 与收费出口
- **Question:** 对实际搜索产生的失败义务集合，能否通过近无损真实配置流，或通过保质量的 aggregate future-cylinder 归约，保住单个 \(\Delta(H)\) 因子并把全部超额质量送入可复算的 Hall、quotient 或 closure 出口？
- **Status:** suspended as a main route; partially answered as a supporting program
- **Why it matters:** 这是一个合法的充分路线，但不再被视为 \(1/4\) 定理必须采用的机制。
- **Known so far:** F-0037–F-0042 给出 no-configuration 重标、old-anchor Lyapunov、aggregate normalization、pair-flat/heavy-excess 分解、orientation progress 与条件递推关闭。F-0043–F-0044 又给出局部 Hall-deficiency 正交化和 same-load exchange-flow 工具。
- **Missing if reactivated:** 全部 \(\mathfrak H_k\) 的非循环收费权、可定量 orientation budget、sound repetition 到 accepted structure 的提升，以及满足 F-0042 的全局余项界。
- **Related:** F-0005, F-0022, F-0027–F-0044, A-0026–A-0028, A-0031, Q-0002, Q-0018
- **Sources:**
  - `docs/framework/FW-15_AGGREGATE_PAIR_CYLINDER.md`
  - `evidence/proofs/Q0015_AGGREGATE_PAIR_CYLINDER_RESET.md`
  - `evidence/proofs/ROUTE_B_REORIENTATION_AUDIT.md`
- **Suggested next action:** 无。当前只维护审计器、回归和可复用的精确引理；不得以一个新收费子类自动重新激活本问题。
- **Answer criterion:** 原 answer criterion 保留：一般近无损 configuration/escape flow，或统一 \(c_\varepsilon<1/4\) aggregate recurrence，且全部账本和 structural exits 合法。满足全部真实条件的反模型也可回答。
- **Reactivation criterion:** `knowledge/DECISIONS.md` 中新增显式决策，并同步更新全部权威状态文件。
- **Last updated:** 2026-07-30

## Q-0016 — actual-support Core Endgame
- **Question:** 对 Q-0018/F-0055 输出的正质量 actual reversible exact-future core，能否证明其产生增广、真实 near-\(1/4\) single-pivot link、完整真子无 IT 块系统，或一个独立自然正 defect？
- **Status:** open
- **Why it matters:** 在 strong faithful Round-or-Core 之后，这是从 actual recurrent core 到最终结构矛盾的唯一主要 endgame；phase、projection 或 partial support 正常形本身都不够。
- **Known so far:** F-0035 只给 incidence 集中或顶点增殖；A-0024 排除纯 incidence 论证。A-0029 排除“可逆性自动给 common-base diamond”；A-0030 排除“splice 可免费反复”。F-0052/F-0055 提供条件 actual recurrent-core 入口。F-0058 给 fixed-pivot target-follow terminal module；F-0063–F-0066 给 all-release core 的三角形分解、weighted context regularity、共同状态恒等式、forced-off-pivot 质量和 pairwise-incompatible 静态界。F-0067 完成最大复用边的 completion–switch 同步—分散二分。A-0041 证明纯矩阵分散不能产生 capacity slack。
- **Missing:** 从饱和 completion–switch fractional matching 加上实际三端点 incidence、support transport、no-IT 与 block-minimality，推出 augmentation/survivor、real near-\(1/4\) link、complete-block no-IT core、pairwise-incompatible exact cover，或可进入递推的 strict loss。同步不自动给 product support，分散不自动给 spare capacity。
- **Related:** Q-0003, Q-0004, Q-0005, Q-0006, Q-0009, Q-0010, Q-0017, Q-0018, A-0024, A-0025, A-0029, A-0030
- **Suggested next action:** 固定 D-0011 的 saturated actual switch-matching 子问题。先攻击一个忠实的两 slot 交换方块：若两次 switch 可交换，推出遗传 actual coordinate expansion；若不可交换，识别造成差异的具体真实 blocker edges 并证明 strict Hall slack、真实边增长或 accepted terminal structure。停止继续命名同一 context-reuse 障碍。
- **Answer criterion:** 对每个正质量 actual reversible core 给出增广、真实 near-\(1/4\) pivot link、完整真实块子核心或正 defect 之一；phase、projection、holonomy 或 partial support 结论不够。
- **Last updated:** 2026-08-01

## Q-0017 — 零 defect 的 faithful forest/core 正常形
- **Question:** 对 Q-0018 产生的 faithful global execution object，若所有自然 defect 项严格为零，是否必分解为 no-copy transient/Round forest 与 reversible exact-future cores？
- **Status:** open
- **Why it matters:** 它必须把实际未终止历史分成可由现有 stability backend 处理的 transient 部分和交给 Q-0016 的 actual cores，而不是预先要求所有 residual 被收费。
- **Known so far:** F-0038 证明固定 genealogy 内 near-critical profile 近二值且近平衡；F-0041 给出 edge/support/orientation/repetition 的精确进展字典。F-0055 已在 exact execution-tree、pre-owned ledgers 与 finite stable atlas 前提下给出 pathwise Round / named exit / R / actual multi-edge core 分解；F-0052 处理 stable quotient 中的 potential-or-core。F-0061 修复 unique-blocker 的 all-release no-copy 语义，F-0062 在单调 clean epochs 与有限完整转移类型下证明 transient mass 消失。零信息损失仍只推出历史可恢复或 permutation behavior，不自动推出 product support。
- **Missing:** 从原实例获得 F-0055 所需的 global exact tree 与 owner/ledger interface；证明零 defect 与该 pathwise decomposition 的 hypotheses/zero-loss 条件一致；处理 F-0053 的 unbounded overflow。actual core 的终局分类属于 Q-0016，不再重复列入本问题。
- **Related:** F-0034, F-0036–F-0041, F-0052, F-0053, F-0055, Q-0005, Q-0006, Q-0016, Q-0018, A-0001–A-0003, A-0025
- **Suggested next action:** 通过 Q-0018 的 global entrance 与 overflow conversion 把 F-0055 从条件 exact tree 提升到原超图；不要重新发明另一套 finite core taxonomy。
- **Answer criterion:** 给出完整零 defect/no-copy forest-core 分解，保留真实边、块、root projection、pivot、genealogy 和 actual support；或给出满足全部零 defect 公理的真实反模型。
- **Nonclaim:** F-0055 是条件 finite-interface theorem，不构造 global entrance，也不关闭 overflow 或 Q-0016。
- **Last updated:** 2026-08-01

## Q-0018 — Faithful global Round-or-Core entrance 与自然 defect
- **Question:** 能否从任意目标低度、块极小、无 IT 实例构造一个质量守恒、future-complete、genealogy-coherent、保存 actual support 和三份账本历史的全局执行对象，使 F-0055 的 pathwise Round-or-Core-or-Overflow 接口适用，并使 Round loss/自然 defect 为零或一致趋零？
- **Status:** active
- **Why it matters:** 这是 Route B 的合法全局入口。它允许无法路由的正质量成为实际临界 core 或 overflow，而不要求每份 residual 预先获得独立收费权。
- **Known so far:** F-0036–F-0041 提供 faithful lift、无损重标、精确 near-equality identity、aggregate normalization 和 orientation progress；F-0043–F-0044 提供局部正交化工具。F-0048–F-0053 给出 competing-blocker rank-one release、fresh/return、wide-fan/heavy-pair、clean product-chart ledger、actual-edge-history core 与 finite signature overflow。F-0055 进一步闭合 exact execution tree 上的 first-owner、动态 max-flow/min-cut、pathwise no-copy realization，以及 stable-atlas `R`/Core / nonstable Overflow 分解。F-0056 说明完整有限 Markov 标签足以在深度零稳定 future signatures，F-0061 说明 future-complete unique-blocker execution 必须保留两个 release branches；二者均为条件接口，不构造 global entrance。
- **Natural-defect constraints:**
  1. defect 必须来自独立可审计的实际量，例如不可逆信息损失、F-0038 deficit、非正常交换、actual-support splice failure 或真实执行不一致；
  2. 不得把“不是 binary forest”“不是 product support”“没有 terminal exit”或“没有被当前 LP 路由”直接写成 defect；
  3. 对 faithful refinement、genealogy 展开和实际 reroot 必须有明确协变性；
  4. defect 为零时仍须保留 actual edge/support identity，不能只得到 phase quotient。
- **Missing:**
  1. **Global faithful entrance/Round compatibility:** 从任意目标实例构造统一实际样本空间、first-owner stopping line、完整 candidate blocker sets 与不复制的 root/slot budgets，并证明 Round 输出正是 F-0038/F-0051/F-0042 所需的 actual recurrence mass；critical-profile identification 与 heavy-pair aggregation 是该接口的子合同，而不是独立最终 gap。
  2. **Overflow conversion:** 把 F-0053 的 unbounded exact-future interface growth 转化为命名 W/M/A/N/S/reset、实际资源增长或 positive-mass actual core；不得静默商化。
  actual recurrent core 的模板与终局后果由 Q-0016 处理。
- **Related:** F-0036–F-0044, F-0048–F-0055, Q-0003–Q-0007, Q-0016, Q-0017, A-0031, A-0035
- **Sources:**
  - `docs/framework/FW-60_CRITICAL_STABILITY_ROUTE.md`
  - `evidence/proofs/ROUTE_B_ATLAS_LP_LEDGER.md`
  - `evidence/proofs/ROUND_OR_CORE_FINITE_INTERFACE.md`
- **Suggested next action:** 构造原实例上的 exact first-owner execution tree，并逐项验证 F-0055 的 entrance、owner、candidate-set 和 Round-compatibility hypotheses；随后单独证明 overflow conversion。不要再把 critical-profile、heavy-pair 和 core classification 混成一个 generic defect。
- **Answer criterion:** 给出可应用于原超图的 faithful entrance construction、三账本兼容的 pathwise Round-or-Core、自然 defect/zero-loss 接口，以及 overflow conversion；或证明这套入口不可能并提供真实反模型。
- **Last updated:** 2026-08-01
