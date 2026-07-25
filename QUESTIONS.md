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

- **Question:** 对每个固定 \(\varepsilon>0\)，能否从任意块极小无 IT 实例构造满足真实执行性、质量守恒、唯一两步单缺陷因子化、投影闭包和投影重数 \(1+\gamma\) 的搜索方案？
- **Status:** open
- **Why it matters:** 由 F-0022，这一方案直接给出 \((1/4-\varepsilon)b^2\) 以下存在 IT。
- **Known so far:** `SINGLE_DEFECT_FRAMEWORK.md` 已给出候选稳定执行记录、压缩稳定状态、活动缺陷状态、root projection、缺陷移动和两类容量账本；条件递推已严格化（F-0005, F-0022, F-0027, F-0028）。
- **Missing:** 证明以下三个接口对实际搜索同时成立：
  1. O1：除受控异常外，每个失败有唯一两步定向；
  2. O2：root projection 属于实际访问的深度 \(k-2\) 稳定层；
  3. O3：每个 \((\widetilde S,e)\) 的投影重数至多 \(1+\gamma\)。
- **Related:** F-0022, F-0027, F-0028, Q-0003, Q-0004, Q-0005, Q-0014
- **Sources:**
  - `handoff_toward_one_quarter.md`，第 827–951 行及第 1103–1121 行，发言者 `unknown`
  - `SINGLE_DEFECT_FRAMEWORK.md`，第 4–12、17、20 节
- **Suggested next action:** 先解决 Q-0014 的零误差两步定向；在此之前不要把任意失败直接送入 terminal defect graph。
- **Answer criterion:** 对所有步 \(k\) 完整验证 SD1–SD8、MC1–MC5，并证明
  \[
  \mathcal B_k\le(1+\gamma)\Delta(H)A_{k-2}
  \]
  且所有异常进入显式误差账本。
- **Last updated:** 2026-07-25

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

## Q-0004 — pivot 相位的全局粘合

- **Question:** 剥离少量异常后，正常交换方块的八相位能否在保留真实 root projection 和 pivot genealogy 的执行图上全局定向，使每个 \((\widetilde S,e)\) 的平均投影重数至多 \(1+O(\delta)\)？
- **Status:** open
- **Why it matters:** 局部 \(\mathcal T_4\) 分类只有在控制真实身份、协变端点运输和投影 genealogy 后才能用于 F-0022。
- **Known so far:** F-0008–F-0013；纯 monodromy 收费和纯相位乘积化均失败（A-0001, A-0002）；原始端点变化不能直接收费（A-0006）。
- **Missing:** 跨图表的真实边身份守恒、闭路 root projection 重数定理，以及“执行记录可合并”的精确判据。
- **Related:** F-0013, F-0022, A-0001, A-0005, A-0006
- **Sources:**
  - `handoff_toward_one_quarter.md`，第 993–1010 行，发言者 `unknown`
  - `SINGLE_DEFECT_FRAMEWORK.md`，第 9–10、13 节
- **Suggested next action:** 对精确执行缺陷图的每条边保存插入顶点、释放顶点、第一真实阻断边、root projection 和正常方块编号；先分类哪些压缩汇合可保持可恢复性。
- **Answer criterion:** 构造全局定向并证明投影重数界；若还需要全局真实边注入，另行证明加权 Hall，不能只给 cocycle 分类。
- **Last updated:** 2026-07-25

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
- **Suggested next action:** 只在 Q-0014 和 Q-0002 的投影闭包完成后研究执行 terminal SCC；失败时输出真实块、顶点、边、pivot、缺失块和每一步阻断边。
- **Answer criterion:** 对每个 terminal 组件证明增广叶、真实 \(1/4\) link 乘积、完整真子核心之一；子核心必须由完整真实块组成。
- **Last updated:** 2026-07-25

## Q-0006 — 零误差 terminal SCC 分类

- **Question:** 在满足下列零误差公理的有限执行缺陷图中，terminal SCC 是否必产生增广叶、完整真实块子核心或精确 \(1/4\) link 乘积？
  - 每个失败具有唯一两步单缺陷因子化；
  - pivot 在缺陷移动中保持；
  - 单端点释放后迹仍独立；
  - 无竞争认证、无边界、无不相容配置；
  - 所有四块交换方块正常；
  - 真实 genealogy 与边身份完整保留；
  - 投影—边重数为一；
  - terminal pivot link 为精确平衡完全二部图。
- **Status:** blocked
- **Why it matters:** 这是误差最少的核心终局，但它只有在零误差两步定向和执行图确实存在后才有定义。
- **Known so far:** 局部模板已完全枚举（F-0009–F-0012）；候选框架给出了 Z1–Z9 和可编程数据格式。
- **Missing:** Q-0014、Q-0002 的零误差存在性，以及不依赖进一步 atlas 细分的全局图论分类。
- **Related:** Q-0002, Q-0005, Q-0007, Q-0014
- **Sources:**
  - `handoff_toward_one_quarter.md`，第 1148–1168 行及第 1253–1290 行，发言者 `unknown`
  - `SINGLE_DEFECT_FRAMEWORK.md`，第 14、18 节
- **Suggested next action:** 在 Q-0014 通过后，对最小真实执行模型进行证明或穷举；枚举器必须检查每条阻断边和每个 root projection 的真实身份。
- **Answer criterion:** 给出严格三出口分类；若为假，给出满足全部零误差公理的真实反模型，而不是仅给相位商图。
- **Last updated:** 2026-07-25

## Q-0007 — 固定 \(\varepsilon\) 的稳定化

- **Question:** 零误差分类成立后，能否把 multi-defect、off-pivot、orientation ambiguity、projection failure、competition、reuse、boundary 和 non-normal square 的总质量控制为 \(\gamma(\varepsilon)\)，并满足
  \[
  (1+\gamma(\varepsilon))(1/4-\varepsilon)<1/4?
  \]
- **Status:** blocked
- **Why it matters:** 它把精确分类升级为实际的 \(1/4-\varepsilon\) 证明。
- **Known so far:** 非正常窗口有九面证书，真实边容量与 link 边数可提供预算（F-0005, F-0011）；候选框架已给出异常类型及其不得混用的账本。
- **Missing:** Q-0006 的零误差定理，以及每一类异常的独立定量稳定性和汇总方式。
- **Related:** Q-0003, Q-0004, Q-0006
- **Sources:**
  - `handoff_toward_one_quarter.md`，第 1170–1194 行，发言者 `unknown`
  - `SINGLE_DEFECT_FRAMEWORK.md`，第 15、17、20 节
- **Suggested next action:** 在 Q-0006 完成后，逐类定义异常质量；禁止把 root failure、transition edge 和全局真实边容量记在同一份未归一化账本中。
- **Answer criterion:** 显式给出 \(\delta(\varepsilon)\)、\(\gamma(\varepsilon)\)、全部异常账本和最终递推。
- **Last updated:** 2026-07-25

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

## Q-0014 — 零误差两步单缺陷定向

- **Question:** 在所有相关四块交换均正常、无竞争认证、无边界的执行组件中，能否预先为每个稳定记录指定唯一真实 pivot，并使每个普通失败唯一写成
  \[
  \widetilde S_0\xrightarrow{\,r\,}\widetilde S_1
  \xrightarrow[\mathrm{fail}]{\,x\,},
  \qquad
  e_0=\{p,r,x\},
  \]
  其中第一步保持 pivot，且释放 \(r\) 后 \(T(\widetilde S_0)\cup\{x\}\) 独立？
- **Status:** open
- **Why it matters:** 这是 terminal defect graph 存在的前置命题；若失败，单缺陷路线在 SCC 分类之前就需要增加 multi-defect 或多 pivot 状态。
- **Known so far:** 当前框架给出精确定义；预置 pivot 对 F-0022 的单个 \(\Delta(H)\) 因子是必要接口（F-0027），释放后独立性不能省略（F-0028）。
- **Missing:** 从正常 \(\mathcal T_4\) 方块与块极小实例中推出全局一致定向，或构造满足局部正常性但无法定向的真实反模型。
- **Related:** F-0027, F-0028, Q-0002, Q-0004, Q-0006
- **Sources:**
  - `SINGLE_DEFECT_FRAMEWORK.md`，第 6、17、20–21 节
- **Suggested next action:** 先搜索最小反模型，检查三种失败签名：不可避免的 multi-defect、正常相位方块不可全局定向、同一真实闭路迫使投影重数大于一。
- **Answer criterion:** 给出对所有普通失败的唯一两步因子化证明；若为假，反模型必须列出完整真实块、顶点、边、执行词、pivot 和每一步第一阻断边。
- **Last updated:** 2026-07-25
