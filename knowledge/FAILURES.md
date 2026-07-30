# Failures

## A-0001 — 用 monodromy 自动收费

- **Goal:** 从非平凡相位闭路直接得到真实边、熵或边界费用。
- **Approach:** 将非平凡 holonomy/monodromy 视为不可逆结构变化。
- **Failure type:** counterexample
- **Failure point:** 闭路可以在相位或 sheet 上作测度保持置换，同时没有信息擦除、边容量消耗或局部 cocycle 缺陷。
- **Why it failed:** 返回同一图表不等于返回同一真实测试或同一 sheet。
- **Failure signature:** `phase permutation without real-identity loss`
- **Evidence:**
  - F-0012, F-0013
  - 明确的“无损 monodromy”反模型。
- **Sources:**
  - `handoff_toward_one_quarter.md`，第 454–474 行，发言者 `unknown`
  - `chatgpt-export_第一阶段解析骨架.txt`，助手回答轮次 36，第 14621–14728 行，发言者 `assistant`
- **Related:** F-0013, Q-0004
- **Retry conditions:** 只有额外证明闭路保持真实 pivot genealogy 且某种真实身份无法可逆恢复时才可重试收费。
- **Do not repeat:** 仅更换群、相位名称、覆盖图或 gauge 表述不构成新方法。
- **Status:** failed
- **Last updated:** 2026-07-24

## A-0002 — 从全局相位一致推出真实支持乘积化

- **Goal:** 把一致相位图册直接 lift 成完整块乘积或真子无 IT 核心。
- **Approach:** 认为相位坐标一致即可消除真实支持相关性。
- **Failure type:** counterexample
- **Failure point:** 对角代码簿 \(\{(i,i):i\in[b]\}\) 具有一致局部坐标，但不是笛卡尔积。
- **Why it failed:** 相位只记录局部匹配类型，不记录哪些真实顶点组合实际存在。
- **Failure signature:** `phase-consistent correlated codebook`
- **Evidence:**
  - F-0014
- **Sources:**
  - `handoff_toward_one_quarter.md`，第 476–496 行，发言者 `unknown`
  - `chatgpt-export_第一阶段解析骨架.txt`，助手回答轮次 36–37，第 14732–14781 行及第 15519–15532 行，发言者 `assistant`
- **Related:** F-0014, Q-0009
- **Retry conditions:** 必须新增遗传单块扩张完整性、矩形饱和和真实内部闭合。
- **Do not repeat:** “每块投影满射”“存在全局相位截面”或“holonomy 平凡”都不是乘积化替代条件。
- **Status:** failed
- **Last updated:** 2026-07-24

## A-0003 — 把重纤维条件化当作势能下降

- **Goal:** 用每次重纤维条件化的熵损失支付 residual。
- **Approach:** 假定条件化本身严格降低信息势。
- **Failure type:** logical
- **Failure point:** 若保留纤维标签，链式法则显示只是重新组织同一联合分布，信息没有被删除。
- **Why it failed:** 真正损失只发生在标签被遗忘或不可逆合并时。
- **Failure signature:** `conditioning-with-label-preservation`
- **Evidence:**
  - F-0021
- **Sources:**
  - `chatgpt-export_第一阶段解析骨架.txt`，助手回答轮次 1，第 139–204 行，发言者 `assistant`
- **Related:** F-0021, Q-0009
- **Retry conditions:** 明确证明接口标签发生不可恢复擦除，并用条件熵量化。
- **Do not repeat:** 改名为“纯化”“切片”“选重纤维”而仍保留标签，不是新机制。
- **Status:** failed
- **Last updated:** 2026-07-24

## A-0004 — 从状态依赖好坐标圆整到固定坐标

- **Goal:** 把每个状态存在的两个遮蔽坐标统一成全局固定坐标。
- **Approach:** 从小平均边界或高支撑重叠推断固定 footprint。
- **Failure type:** counterexample
- **Failure point:** 显式迁移构造让活动坐标对随状态改变，同时局部刷新保持目标集合不变。
- **Why it failed:** Efron–Stein/影响量只控制平均变化，不控制方向的全局一致性。
- **Failure signature:** `state-dependent coordinate migration`
- **Evidence:**
  - F-0018
- **Sources:**
  - `handoff_toward_one_quarter.md`，第 631–696 行，发言者 `unknown`
- **Related:** F-0017, F-0018
- **Retry conditions:** 需加入真实度数、连通率或 pivot genealogy 约束，排除迁移所需的全局负载。
- **Do not repeat:** 仅把“两个坐标”替换为“少数坐标”或“高概率坐标”仍属同一错误。
- **Status:** failed
- **Last updated:** 2026-07-24

## A-0005 — 从局部兄弟碰撞推出全局 carrier 集中

- **Goal:** 由正常 \(\mathcal T_4\) 内的高端点碰撞直接得到全局高次数顶点。
- **Approach:** 将条件碰撞率平均后视为全局碰撞率。
- **Failure type:** counterexample
- **Failure point:** 四个或更多使用不交真实顶点集的正常上下文可保持局部碰撞高而使全局碰撞低于目标阈值。
- **Why it failed:** 忽略了上下文间色散项。
- **Failure signature:** `high conditional collision with disjoint contexts`
- **Evidence:**
  - 同一上下文兄弟碰撞至少 \(2/9\)，但 \(N\) 个不交上下文混合后全局碰撞降为 \(1/(8N)\)。
- **Sources:**
  - `chatgpt-export_数学语言描述_mathcal T_4图册(2).txt`，助手回答轮次 33，第 21850–22068 行，发言者 `assistant`
- **Related:** Q-0004
- **Retry conditions:** 必须控制上下文图的导通率、共享真实端点或跨上下文传输。
- **Do not repeat:** 仅提高局部碰撞常数不能消除上下文色散。
- **Status:** failed
- **Last updated:** unknown

## A-0006 — 用原始端点分布变化直接收费

- **Goal:** 把相邻上下文端点分布的 \(\ell_2\) 变化计入真实异常费用。
- **Approach:** 认为端点名称变化大即表示结构不忠实。
- **Failure type:** counterexample
- **Failure point:** 合法兄弟刷新 \(\{a,b,y\}\to\{a,b,y'\}\) 无任何异常，但端点分布平方距离为 \(2/9\)。
- **Why it failed:** 未将规范允许的协变刷新从真正的非协变变化中扣除。
- **Failure signature:** `raw endpoint energy without covariant transport`
- **Evidence:**
  - 显式两边刷新反例。
- **Sources:**
  - `chatgpt-export_数学语言描述_mathcal T_4图册(2).txt`，助手回答轮次 34，第 22398–22479 行，发言者 `assistant`
- **Related:** A-0005
- **Retry conditions:** 先定义规范运输，再只对运输后的协变残差收费。
- **Do not repeat:** 更换端点距离、散度或能量范数而不扣除合法刷新仍是同一失败。
- **Status:** failed
- **Last updated:** unknown

## A-0007 — 从原 \(4/27\) 证明中提取非平凡“新鲜边”集合

- **Goal:** 冻结基准边集 \(E_0\)，把其余边自动视为相对基准的新鲜费用。
- **Approach:** 认为 Wanless–Wood 基准证明天然只使用一部分真实边。
- **Failure type:** unsupported-assumption
- **Failure point:** 该证明的自然计费对象覆盖全部 stretched 真实边，投影后 \(E_0^{WW}=E^\times(H)\)。
- **Why it failed:** 每条 stretched 边在某个加入块的状态都可能成为首次阻断边。
- **Failure signature:** `baseline proof already ranges over all real edges`
- **Evidence:**
  - F-0006
- **Sources:**
  - `chatgpt-export_基准真实边集合证明.txt`，助手回答轮次 1，第 120–149 行，发言者 `assistant`
- **Related:** F-0006, F-0007
- **Retry conditions:** 必须人为定义带收费端点和容量的基准预留，并证明其与 residual 同处一个账本。
- **Do not repeat:** 从“原证明使用总度数上界”推断“存在未使用边子集”不成立。
- **Status:** failed
- **Last updated:** unknown

## A-0008 — 错误的 lopsided-LLL 邻域删减

- **Goal:** 把二相位枚举无条件提升到原超图并获得更好常数。
- **Approach:** 只将共享同一有符号相位的坏事件视为相依，删除共享变量但要求相反值的事件。
- **Failure type:** logical
- **Failure point:** 若 \(A\) 要求 \(X=0\)、\(B\) 要求 \(X=1\)，则 \(\Pr(A\mid\overline B)>\Pr(A)\)，二者不能从负依赖邻域删除。
- **Why it failed:** lopsided 依赖判定使用错误。
- **Failure signature:** `omitted opposite-value shared-variable dependency`
- **Evidence:**
  - 条件概率反例及错误不等式 \(\Psi_A(\mu)\le(1+\mu)^3\) 被撤回。
- **Sources:**
  - `chatgpt-export_证明主线与障碍.txt`，助手回答轮次 73，第 20005–20027 行，发言者 `assistant`
- **Related:** A-0010
- **Retry conditions:** 使用正确依赖图并重新核算阈值，或证明忠实相位商后在其精确事件系统上应用。
- **Do not repeat:** 仅改称 cluster expansion、CPE 或负依赖而沿用同一删边规则不构成新证明。
- **Status:** failed
- **Last updated:** unknown

## A-0009 — “三相位分裂负载至多 5”引理

- **Goal:** 将任意低负载二相位关系精确细化成最大边际至多 5 的三相位关系。
- **Approach:** 对每坐标选择 \(2+1\) 分裂并希望统一控制最大边际。
- **Failure type:** counterexample
- **Failure point:** 六个二坐标圆柱关系在任意分裂下最大边际至少为 6；极简反例是 \(F=\{(a,b,c):a\ne b\}\)。
- **Why it failed:** 大纤维在另一坐标的相反值上形成 \(2\times3\) 完整切片。
- **Failure signature:** `2+1 split creates six-point cylinder marginal`
- **Evidence:**
  - 77 个二相位关系的完整穷举及显式反例。
- **Sources:**
  - `chatgpt-export_基准真实边集合证明.txt`，助手回答轮次 35，第 15635–15780 行，发言者 `assistant`
- **Related:** F-0025, Q-0008
- **Retry conditions:** 只研究精确例外模板的有限状态自动机，或允许可计费混格缺陷。
- **Do not repeat:** 更换坐标名称或循环长度不改变该单层反例。
- **Status:** failed
- **Last updated:** unknown

## A-0010 — 将受限相位模型常数冒充无条件常数

- **Goal:** 宣布 \(3/16\)、\(1/6\)、\(\sqrt6\) 或其他严格优于 \(4/27\) 的无条件结果。
- **Approach:** 把忠实二相位 handoff 模型或其他有限相位模型中的覆盖结果直接投影回一般超图。
- **Failure type:** unsupported-assumption
- **Failure point:** 一般近临界超图未被证明能以主阶精度投影到该模型；粗相位格可能只有极少真实禁边。
- **Why it failed:** 缺少真实端点、边身份、质量与 survivor 的忠实 lift。
- **Failure signature:** `finite phase theorem without faithful real-hypergraph projection`
- **Evidence:**
  - F-0020
- **Sources:**
  - `chatgpt-export_证明主线与障碍.txt`，助手回答轮次 73–74，第 20005–20097 行，发言者 `assistant`
  - `chatgpt-export__(_sqrt{6}_) 路线评估.txt`，助手回答轮次 12，第 5760–5809 行，发言者 `assistant`
- **Related:** F-0020, Q-0008
- **Retry conditions:** 证明覆盖保持的真实二点选择或定量投影缺陷界。
- **Do not repeat:** 只增加有限枚举长度或相位数而不解决忠实投影，不会变成无条件证明。
- **Status:** failed
- **Last updated:** unknown

## A-0011 — 用有限 LP/MILP 直接替代全局结构定理

- **Goal:** 通过扩大有限优化模型证明渐近 \(3/20\) 或 \(1/4\)。
- **Approach:** 把小参数不可行和 fractional 最优值外推到任意块数与块大小。
- **Failure type:** insufficient-evidence
- **Failure point:** fractional 模型允许无结构多块扩散；整数模型尚无“失败具有有界整数见证”的定理。
- **Why it failed:** 有限不可行不蕴含统一有限见证，也不控制真实边身份的跨窗口复用。
- **Failure signature:** `small-instance infeasibility without finite-witness theorem`
- **Evidence:**
  - F-0019, F-0026
- **Sources:**
  - `handoff_toward_one_quarter.md`，第 698–789 行及第 1196–1206 行，发言者 `unknown`
- **Related:** F-0019, F-0026, Q-0012
- **Retry conditions:** 先证明有界整数见证、半群闭包或可审计归约，再运行完整证书。
- **Do not repeat:** 仅扩大 \(n,b,L\) 或延长求解时间不是结构进展。
- **Status:** inconclusive
- **Last updated:** 2026-07-24

## A-0012 — 从 bounded width 推出熵损失

- **Goal:** 用接口宽度有限迫使每圈产生固定信息损失。
- **Approach:** 将宽度小与不可逆合并等同。
- **Failure type:** counterexample
- **Failure point:** 宽度 2 的固定轻锚代码簿可形成零熵、可逆闭环。
- **Why it failed:** 有限状态可作置换，宽度不限制可恢复性。
- **Failure signature:** `finite-width reversible codebook`
- **Evidence:**
  - F-0021
- **Sources:**
  - `handoff_toward_one_quarter.md`，第 1198–1204 行，发言者 `unknown`
  - `chatgpt-export_第一阶段解析骨架.txt`，助手回答轮次 1，第 200–204 行，发言者 `assistant`
- **Related:** A-0003, A-0001
- **Retry conditions:** 证明状态转移非单射或真实边身份发生不可恢复合并。
- **Do not repeat:** 将 width 改称状态数、接口复杂度或有限记忆仍不足。
- **Status:** failed
- **Last updated:** 2026-07-24

## A-0013 — 对部分支持错误使用块极小性

- **Goal:** 直接用块极小反例排除相位代码簿或部分顶点核心。
- **Approach:** 把非空相关支持、相位轨道或每块投影满射视为完整真子实例。
- **Failure type:** logical
- **Failure point:** 块极小性只适用于由完整真实块诱导的子系统。
- **Why it failed:** 部分支持可能遗漏唯一 survivor，且不对所有块选择封闭。
- **Failure signature:** `partial-support core treated as full block subsystem`
- **Evidence:**
  - F-0002, F-0014
- **Sources:**
  - `handoff_toward_one_quarter.md`，第 122–134 行及第 1196–1206 行，发言者 `unknown`
  - `chatgpt-export_第一阶段解析骨架.txt`，助手回答轮次 37，第 16080–16094 行，发言者 `assistant`
- **Related:** F-0002, F-0014, Q-0009
- **Retry conditions:** 先证明遗传扩张完整性和真实内部闭合，得到完整块子系统。
- **Do not repeat:** “密度 \(1-o(1)\)”或“每块都有顶点”仍不满足精确块极小性。
- **Status:** failed
- **Last updated:** 2026-07-24

## A-0014 — 从零信用定性闭包跳到 \(1/55\) 定量闭包

- **Goal:** 由“零费用核心可分类”直接得到 \(3/20\) 所需固定比例 residual 捕获。
- **Approach:** 认为定性排除零缺陷自动给出统一正间隙。
- **Failure type:** insufficient-evidence
- **Failure point:** residual 可分散在许多小而正常的圆柱 sector 中，每个分量费用趋于零但总质量为主阶。
- **Why it failed:** 缺少圆柱压缩、递归或统一定量紧性。
- **Failure signature:** `qualitative zero-defect closure without uniform quantitative gap`
- **Evidence:**
  - 旧对话明确说明零信用版本闭合仍不能给 \(1/55\)。
- **Sources:**
  - `chatgpt-export_数学语言描述_mathcal T_4图册(2).txt`，助手回答轮次 35，第 22868–23333 行，发言者 `assistant`
- **Related:** F-0015, Q-0001
- **Retry conditions:** 证明 ExtDef–Credit 的统一常数或原超图上的圆柱/阻断图压缩定理。
- **Do not repeat:** 把“没有完全零费用反例”表述为“存在固定正费用”是同一跳跃。
- **Status:** inconclusive
- **Last updated:** unknown

## A-0015 — 把十八块迁移视为 \(1/4\) 的唯一 Gap

- **Goal:** 通过解决十八块核心迁移直接完成 \(1/4\)。
- **Approach:** 将 \(3/20\) sector 分析的首个逃逸规模当作最优常数的本征结构。
- **Failure type:** logical
- **Failure point:** 十八来自 \(nD\le17\) 的 \(3/20\) 预算；\(1/4\) 还需要单缺陷降秩、全局 pivot 相容和无出口终局。
- **Why it failed:** 混淆两个目标常数和两套递推。
- **Failure signature:** `3/20 sector threshold misidentified as 1/4 structure`
- **Evidence:**
  - F-0015, F-0022
- **Sources:**
  - `handoff_toward_one_quarter.md`，第 519–529 行、第 809–825 行及第 1196–1206 行，发言者 `unknown`
- **Related:** Q-0001, Q-0002
- **Retry conditions:** 仅在研究 \(3/20\) ExtDef 路线时继续使用十八块对象。
- **Do not repeat:** 将十八换成另一固定块数仍不能替代单缺陷递推。
- **Status:** superseded
- **Last updated:** 2026-07-24

## A-0016 — 将任意二值限制塞入连续三窗环

- **Goal:** 用连续三窗有限自动机处理所有二值限制后的不可满足关系。
- **Approach:** 假设所有低出现度最小核心都呈环状。
- **Failure type:** unsupported-assumption
- **Failure point:** 一般二值限制的变量—约束关联图可能分叉，不必是连续三窗环。
- **Why it failed:** 自动机模型丢失了分叉结构和真实窗口所属关系。
- **Failure signature:** `arbitrary binary CSP forced into cyclic window model`
- **Evidence:**
  - 后续打表将目标改为区分“环核心”和“分叉核心”。
- **Sources:**
  - `chatgpt-export_基准真实边集合证明.txt`，助手回答轮次 35，第 15622–15632 行，发言者 `assistant`
- **Related:** F-0025, Q-0008
- **Retry conditions:** 先分类最小不可满足公式的关联图；环用自动机，分叉应产生可计费负载。
- **Do not repeat:** 只增加环长 \(L\) 不覆盖非环核心。
- **Status:** failed
- **Last updated:** unknown

## A-0017 — 把求解器超时解释为数学否定

- **Goal:** 用 SAT/ILP 对长度 \(L=8\) 或更大窗口给出统一结论。
- **Approach:** 直接精确求解大状态空间。
- **Failure type:** timeout
- **Failure point:** \(L=8\) 的求解在记录时间内未判定。
- **Why it failed:** 状态空间和对称性未经压缩；超时不说明命题真假。
- **Failure signature:** `uncompressed exact search timeout`
- **Evidence:**
  - 对话明确把超时与数学状态分开，并改用位集/反链压缩。
- **Sources:**
  - `chatgpt-export_基准真实边集合证明.txt`，助手回答轮次 35，第 15628–15632 行，发言者 `assistant`
- **Related:** Q-0012
- **Retry conditions:** 使用 BDD/ZDD、反链半群、对称约化，并输出可验证证书。
- **Do not repeat:** 仅增加运行时间或机器资源而不压缩状态不构成新数学路线。
- **Status:** blocked
- **Last updated:** unknown

## A-0018 — 将单个轻锚局部连接器重复用于全局

- **Goal:** 通过不断调用低于 \(1/4\) 的局部 residual 连接器构造全局低度无 IT 系统。
- **Approach:** 让同一固定轻锚服务线性数量的兄弟状态。
- **Failure type:** computational
- **Failure point:** 不同兄弟状态产生不同真实边，固定锚次数累积为 \(\Theta(b^3)\)。
- **Why it failed:** “逻辑上只激活一个状态”不会降低静态超图中所有已加入边的度数。
- **Failure signature:** `light anchor reused across linearly many sibling states`
- **Evidence:**
  - F-0023
- **Sources:**
  - `chatgpt-export_文章核心问题分析(1).txt`，助手回答轮次 100，第 52409–52466 行，发言者 `assistant`
- **Related:** F-0023, F-0024, Q-0010
- **Retry conditions:** 必须证明可持续产生新的固定低负载锚，或将负载分配到不形成变量锚复制的全局结构。
- **Do not repeat:** 更换每个兄弟状态的新后继块仍会产生不同真实边并累加到旧锚。
- **Status:** failed
- **Last updated:** unknown

## A-0019 — 将第一阻断边唯一性当作真实边单位容量

- **Goal:** 用确定性的第一阻断规则直接完成真实边不复用账本。
- **Approach:** 对每次失败选择字典序最小阻断边，并认为不同失败因此自动对应不同真实边。
- **Failure type:** logical
- **Failure point:** 确定规则只保证每次失败有唯一证书；同一真实边仍可能是许多不同执行记录或投影状态的第一阻断边。
- **Why it failed:** “失败尝试的分割”与“义务注入真实边的容量分配”是不同问题；后者仍需显式注入或加权 Hall。
- **Failure signature:** `deterministic first blocker mistaken for unit real-edge capacity`
- **Evidence:**
  - F-0005
  - `SINGLE_DEFECT_FRAMEWORK.md`，第 5、12 节
- **Related:** F-0005, F-0022, Q-0002
- **Retry conditions:** 明确区分投影—边出现重数与全局真实边容量；为后者给出注入或 Hall 证明。
- **Do not repeat:** 把字典序、最早时间或最小相位换成另一确定规则不会解决跨状态复用。
- **Status:** failed
- **Last updated:** 2026-07-25

## A-0020 — 删除第一阻断边一个端点后自动宣称单缺陷

- **Goal:** 把每次失败直接降秩为一个缺失块的活动缺陷。
- **Approach:** 若第一阻断边为 \(\{p,r,x\}\)，删除旧端点 \(r\)，不再检查剩余迹是否独立。
- **Failure type:** logical
- **Failure point:** 另一条阻断边 \(\{x,u,v\}\) 可能不含 \(r\)，删除 \(r\) 后仍完整存在。
- **Why it failed:** 一次加入可同时产生多条超边；第一阻断边只是证书选择，不是唯一阻断边断言。
- **Failure signature:** `single endpoint release without rechecking independence`
- **Evidence:**
  - F-0028
  - `SINGLE_DEFECT_FRAMEWORK.md`，第 6.2–6.3 节
- **Related:** F-0028, Q-0002, Q-0014
- **Retry conditions:** 把释放后独立性写入普通 defect 的定义；失败时进入 multi-defect 或显式异常账本。
- **Do not repeat:** 改为删除另一旧端点也必须重新验证全部真实边。
- **Status:** failed
- **Last updated:** 2026-07-25

## A-0021 — 用无指针稳定状态直接得到单个 \(\Delta\) 因子

- **Goal:** 从深度 \(k-2\) 的部分横截状态直接估计根失败数。
- **Approach:** 状态只保存 \(T\)，失败发生后任选 \(p\in T\) 收费，并把总量估为 \(\Delta(H)|\mathcal S_{k-2}|\)。
- **Failure type:** computational
- **Failure point:** 对同一状态的所有可能 pivot 求和一般只有
  \[
  \sum_{p\in T}d_H(p)\le |T|\Delta(H).
  \]
- **Why it failed:** 无指针状态本身没有逐 pivot 容量。进一步把修复定义为“预先固定一个共同 pivot”也不成立；F-0029/A-0022 给出正常四块反例。
- **Failure signature:** `unpointed stable state loses a factor equal to state depth`
- **Evidence:**
  - F-0027
  - `SINGLE_DEFECT_FRAMEWORK.md`，第 3–4、10–11 节
- **Related:** F-0022, F-0027, Q-0002, Q-0014
- **Retry conditions:** 不再要求源状态预置共同 pivot。先枚举全部真实两步配置，再证明义务—配置流、root-pivot 总预算及投影—pivot—根边槽位容量；任何未分配质量必须进入显式异常或 Hall 最小割。
- **Do not repeat:** 事后选择度数最大的、最小的或最早出现的顶点仍不能自动恢复逐状态单位预算。
- **Status:** failed
- **Last updated:** 2026-07-25

## A-0022 — 用正常性推出同一成功后继的共同预置 pivot

- **Goal:** 在零误差正常执行组件中，为每个源稳定记录预先指定一个 pivot，使该记录的全部后续普通失败均由同一 pivot 解释。
- **Approach:** 假设正常 \(\mathcal T_4\) 方块、无竞争认证、无边界和单端点释放独立性足以全局粘合 pivot。
- **Failure type:** structural
- **Failure point:** 四个二元块上的八边超图
  \[
  \begin{aligned}
  &\{0_0,1_0,2_0\},\{0_0,1_1,3_0\},
    \{0_0,2_1,3_1\},\{0_1,1_0,3_1\},\\
  &\{0_1,1_1,2_1\},\{0_1,2_0,3_0\},
    \{1_0,2_1,3_0\},\{1_1,2_0,3_1\}
  \end{aligned}
  \]
  是正常、无竞争、边极小和块极小的无 IT 实例。在根迹
  \[
  R=\{0_0,1_0\}
  \]
  成功加入 \(r=2_1\) 后，失败 \(x=3_0\) 只接受 pivot \(1_0\)，失败 \(x=3_1\) 只接受 pivot \(0_0\)；两次释放后均独立。
- **Why it failed:** 正常性保证的是有限四块相位结构，不保证同一成功后继的全部第一阻断边共享一个旧端点。
- **Failure signature:** `normal Q4 square with individually orientable failures but no common preassigned pivot`
- **Evidence:**
  - F-0029
  - `SINGLE_DEFECT_FRAMEWORK.md` v0.3，第 3 节
- **Related:** F-0027, F-0028, F-0029, Q-0002, Q-0004, Q-0014, Q-0015
- **Retry conditions:** 只有加入额外的低度渐近稳定性并证明坏窗口总质量可控，或改用配置优先入口，才可继续；不能把正常性本身当作共同 pivot 定理。
- **Do not repeat:** 不要通过更换字典序、块顺序或事后选择 pivot 来声称解决；同一执行组件必须同时处理两个失败。
- **Status:** failed
- **Last updated:** 2026-07-27


## A-0023 — 把 pivot-switch 当作免费重新开账
- **Goal:** 在遇到 off-pivot 阻断边后直接改用新 pivot，并重新获得一份完整 \(\Delta(H)\) 预算。
- **Approach:** 只依据阻断边中出现了另一个旧端点，就把当前义务迁移到新 fixed-pivot fiber。
- **Failure type:** logical
- **Failure point:** 同一质量可沿 \(p_0\to p_1\to\cdots\) 反复重置预算；同一真实 switch 边也可能被不同 genealogy 重复当作新度数证书。
- **Why it failed:** pivot 是真实 link 的共同端点，不是免费状态标签；切换必须作为已支付出口，或通过真实 reroot lift 与统一容量 LP 路由。
- **Retry conditions:** 使用 `PIVOT_SWITCH_ESCAPE_FRAMEWORK.md` 的组合 switch、真实 reroot lift 和全局真实边容量。
- **Do not repeat:** 仅保留新 pivot 名称而删除旧 genealogy 不能修复账本。
- **Status:** failed
- **Last updated:** 2026-07-27

## A-0024 — 从大量分散 incidence 自动推出 \(1/4\) 或子核心
- **Goal:** 用真实 incidence 总量直接证明某个顶点高度集中，或完整块支持闭合。
- **Approach:** 由 \(\sum_vL(v)=M\) 和低度假设断言分散收费不可持续。
- **Failure type:** counterexample
- **Failure point:** 对角分散模型 \(f_i=\{q_i,z_i,y_i\}\) 可让每个 switch 使用不同顶点和不同真实边，最大度为 1、无 reuse，但仍有 IT 且没有完整块无 IT 子核心。
- **Why it failed:** Hall/度数账本只给出“集中或顶点增殖”，不编码新 pivot 的因果产生、未来闭合或全局无 IT。
- **Retry conditions:** 加入块极小无 IT、未来闭合、因果再生见证和 exact-future quotient 排除。
- **Do not repeat:** 仅用鸽巢原理或总顶点数不能控制块数增长。
- **Status:** failed
- **Last updated:** 2026-07-27

## A-0025 — 把 persistent-blocker 圆柱化当作已知分类
- **Goal:** 由无 fresh、无 quotient 直接推出完整笛卡尔覆盖或 \(1/4\) link 圆柱。
- **Approach:** 将所有尚未解释的选择性未来筛选统一命名为 persistent blocker，并假设其最终圆柱化。
- **Failure type:** unsupported-assumption
- **Failure point:** 旧阻断边可跨 genealogy 持续存在，且不同前驱在更远未来才被区分；尚无单调量或因果再生定理迫使坐标饱和。
- **Why it failed:** “闭合后推出子核心”已证明，但“为什么必须闭合”正是开放结构命题。
- **Retry conditions:** 先证明 persistent-blocker 正常形或因果 incidence 再生/集中定理。
- **Do not repeat:** 不得把该开放命题改名为 terminal classification 后当作引理使用。
- **Status:** open-obstruction
- **Last updated:** 2026-07-27

## A-0026 — 用 ordinary transition 截帽自动制造 \(11/27\) 正常形
- **Goal:** 将每个节点超过 \(11/27\) 的 ordinary continuation 拆成 transition-charge，并用实际 transition edge 的 Hall 网络支付，从而直接关闭 Q-0017/Q-0016。
- **Approach:** 在 AMCG 质量接口中人为保留至多 \(11/27\) 的 ordinary child mass，把其余质量绑定到该 move 的 transition edge。
- **Failure type:** circular-capacity-assumption
- **Failure point:** AMCG 的可分数细化只保证质量不复制；它不证明每份超额 ordinary mass 天然拥有一份独立、未消费且允许支付的全局真实边容量权。若把这项权利放进 obligation 定义，再由 Hall 二分支付或输出 cut，就已把待证出口写入接口。
- **Why it failed:** transition edge 属于执行因果链不等于可作为额外收费资源；还必须排除它已被 root、slot、此前 transition 或 escape 账本使用，并证明收费不循环。
- **Failure signature:** `desired contraction enforced by defining excess continuation as an already-entitled edge charge`
- **Evidence:** `sources/raw/conversations/chatgpt-export_深度二分析执行.txt` 的最终逻辑顺序审计；`docs/framework/FW-50_PERSISTENT_BLOCKER.md`。
- **Related:** F-0034, F-0036, Q-0015, Q-0016, Q-0017
- **Retry conditions:** 先从目标超图和 Q-0015 真实入口证明 ordinary transition 的非循环收费权、剩余容量和三账本兼容；或改用不创造容量的单调量/结构割。
- **Do not repeat:** 不得把 AMCG 定义、统一标度或无原子细化当作收费合法性证明。
- **Status:** failed
- **Last updated:** 2026-07-28

## A-0027 — 用单个 named E 子类替代 Q-0015 的全部质量控制
- **Goal:** 选择一个 named E-exit 子类，证明其可控或结构化后直接关闭 Q-0015。
- **Approach:** 把 handoff 的即时行动“choose one E-exit class”误读为完整 answer criterion。
- **Failure type:** scope / acceptance-criterion error
- **Failure point:** 一个子类定理既不控制全部二步失败，也不产生统一的 \(c<1/4\) 递推；未处理质量不能静默移到下游。
- **Why it failed:** 选择一个子类是获得可审计进展的工作顺序，不是最终证明的质量覆盖定理。
- **Failure signature:** `one named-exit subcase promoted to full Q-0015 closure`
- **Evidence:** F-0037–F-0042；`knowledge/QUESTIONS.md#Q-0015`。
- **Related:** Q-0015
- **Retry conditions:** 证明原近无损 configuration/escape flow，或证明 F-0042 的 aggregate heavy-excess 判据。
- **Do not repeat:** 不得只命名一个 heavy pair 而不控制其正部总质量。
- **Status:** failed
- **Last updated:** 2026-07-29

## A-0028 — 无新边、无新支持的第一次 reset 必立即闭合
- **Goal:** 把每次不增加 blocker edge 与 carrier support 的 carrier reset 立即识别为 quotient repetition。
- **Approach:** 只使用 \((|\mathcal E_t|,|\mathcal A_t|,Q_t)\) 势，忽略同一资源下不同 hole orientations。
- **Failure type:** exact bounded counterexample
- **Failure point:** 三个二元块与单边 \(\{0_0,1_0,2_0\}\) 有三个不同 hole orientations。第二次 reset 不增加边或支持，却进入新的完整带标签状态；再一步才重复。
- **Why it failed:** 固定资源仍可支持多个 continuation-distinct orientation tokens。
- **Failure signature:** `free reset enters a new orientation of an old edge`
- **Evidence:** `enumerate/q0015_reset_compensation.py`；`tests/test_q0015_reset_compensation.py`；`evidence/experiments/q0015/reports/q0015_reset_compensation_attack.md`。
- **Related:** F-0041, Q-0015
- **Retry conditions:** 使用 future-compatible orientation budget；只有 token 也不被消费时才推出 quotient。
- **Do not repeat:** 不得按当前 trace、edge set 或 anchor support 单独合并 genealogy states。
- **Status:** failed
- **Last updated:** 2026-07-29

## A-0029 — 可逆普通单缺陷轨迹自动补出 common-base diamond
- **Goal:** 从零信息损失、正常局部交换、普通单缺陷和完整 genealogy 可恢复性推出两条轨迹可拉回同一个 actual base 并补出第四角点。
- **Approach:** 把历史可恢复性解释成 actual-support 矩形闭包。
- **Failure type:** bounded exhaustive counterexample
- **Failure point:** 在全部正常 \(Q_4\) 模型的对应窗口中，缺失角点可在加入第二个 future coordinate 前被一条 internal old-anchor edge 阻断；F-0029 的八边模型给出最小显式实例。
- **Why it failed:** reversibility 防止历史丢失，但不创造一个本来不独立的共同 base，也不保证 actual support 对坐标拼接闭合。
- **Failure signature:** `invertible genealogy mistaken for common-base product closure`
- **Evidence:** `enumerate/q4_splice_pay_cylinder_validation.py`；
  `evidence/experiments/route_b/reports/q4_splice_pay_cylinder_validation.md`。
- **Related:** F-0029, F-0045, Q-0016
- **Retry conditions:** 把 internal old-anchor、unavoidable reuse 和 local same-pivot 作为实际分支，并在 actual support 上证明饱和或终局。
- **Do not repeat:** 不得从 entropy zero、phase consistency 或完整接口可恢复直接推出 diamond。
- **Status:** failed
- **Last updated:** 2026-07-30

## A-0030 — 反复免费 splice 后必剩正质量 single-pivot cylinder
- **Goal:** 把 common-base/genealogy splice 当作无费用闭包操作，反复执行，直到正质量进入 same-pivot future-complete cylinder。
- **Approach:** 只区分“可 splice”与“必须 reuse”，未记录一次 splice 实际使用的全部真实边。
- **Failure type:** bounded exhaustive counterexample / missing budget
- **Failure point:** 在正常 \(Q_4\) 的全部 384 个 edge-disjoint splice candidates 中，最小 splice 都使用全部 8 条真实边。一次 splice 后已无未使用的局部真实边可支持下一次免费操作。
- **Why it failed:** splice 是实际重新布线，不是纯逻辑闭包；其资源消耗可能吸收全部质量，而不是留下正 cylinder mass。
- **Failure signature:** `splice treated as a free idempotent closure`
- **Evidence:** F-0046。
- **Related:** Q-0016, F-0045, F-0046
- **Retry conditions:** 证明一个独立的全局预算不足定理，或在 Route B 中把 splice 作为 exact-core 结构而非收费操作研究。
- **Do not repeat:** 不得在不记录 actual edge set 的情况下迭代 splice。
- **Status:** failed
- **Last updated:** 2026-07-30

## A-0031 — 把 \(1/4\) 稳定性等同于 \(100\%\) residual charging
- **Goal:** 通过给每份 heavy/residual mass 分配独立 root、slot、edge、token 或 quotient 容量来解释整个 \(1/4\) 阈值。
- **Approach:** 将当前二阶递推需要 \(o(1)\) 余项的充分条件误认为主定理的必要机制，并不断细分未收费余项。
- **Failure type:** strategy mismatch / route drift
- **Failure point:** 大 residual 可能是临界结构证据，而不是必须逐单位支付的债务。当前切割只产生更精确 obstruction，没有产生统一下降量或 terminal theorem。
- **Why it failed:** charging theorem 的量词和容量唯一性极强；临界稳定性可以通过“远离极值有耗散、近极值有刚性”完成，而无需为临界部分逐单位收费。
- **Failure signature:** `sufficient recurrence mechanism promoted to necessary one-quarter mechanism`
- **Evidence:** `evidence/proofs/ROUTE_B_REORIENTATION_AUDIT.md`。
- **Related:** D-0006, Q-0015, Q-0018
- **Retry conditions:** 只有显式重新激活 Route A 时才恢复全部余项收费目标。
- **Do not repeat:** 在 Route B 中不得把“全部 \(\mathfrak H_k\) 小”或“全部 residual 有收费权”写入 active-node acceptance criterion。
- **Status:** suspended-strategy
- **Last updated:** 2026-07-30

## A-0032 — 由三一致性自动推出 3-local realizability
- **Goal:** 用只含二元和三元坏原子的 LLL/工具语言刻画全部返回工具不可组合性。
- **Approach:** 假设三一致性保证任何全局不可实现工具族都有大小至多 3 的不可实现子族。
- **Failure type:** bounded actual-execution counterexample / unsupported locality
- **Failure point:** faithful blocker-release 动力学可以出现四个单目标工具，使每个至多三工具子族都可由实际返回路径共同实现，但四个目标共同到达一个 multi-blocker、无单释放的动态死锁。
- **Why it failed:** 一条三边只含三个端点，不代表“所有释放均失败”的动态条件只有三阶 witness；释放合法性依赖完整 blocker family 和当前 support。
- **Failure signature:** `3-uniform edge rank mistaken for rank-3 dynamic realizability`
- **Evidence:** `evidence/proofs/ROUTE_B_ATLAS_LP_LEDGER.md` §9；`tests/test_route_b_atlas.py::test_four_tool_dynamic_deadlock_counterexample`.
- **Related:** Q-0018, A-0011, A-0025
- **Retry conditions:** 先剥离 multi-defect/deadlock，或使用完整 finite future signatures 与 overflow，而不是固定 rank-3 bad-atom language。
- **Do not repeat:** 不得仅因原超图三一致就声称所有执行不相容性有三元局部见证。
- **Status:** failed-bounded
- **Last updated:** 2026-07-30

## A-0033 — 把抽象四标签 LP 的正余量解释成机制转换
- **Goal:** 从 \(W/S/M/A\) 布尔标签上的共同线性权重推出执行轨迹以正密度在四类间转换。
- **Approach:** 最大化所有 recurrent cycles 的最小平均标签权重，并把最优对偶 circulation 称为混合核心。
- **Failure type:** LP interpretation error
- **Failure point:** 对偶允许把彼此不相交的纯 \(W\) 循环与纯 \(M\) 循环作凸组合。正共同余量只说明多个标签共同击中全部循环，不说明任何一条循环发生机制切换。
- **Why it failed:** 状态标签不是实际不可复制资源；不同纯循环的凸组合被误读为同一执行中的联动摊还。
- **Failure signature:** `fractional cycle hitting mistaken for positive-density mechanism conversion`
- **Evidence:** `evidence/proofs/ROUTE_B_ATLAS_LP_LEDGER.md` §7；F-0052 的 actual-edge-history replacement；bounded artifact `route_b_lp_atlas_validation.json`.
- **Related:** F-0052, Q-0018
- **Retry conditions:** 使用实际循环模块与 blocker-edge history；只有暴露全部 certified modules 后仍存在 residual circulation 才称为 mixed core。
- **Do not repeat:** 不得用四个类别的 simplex 权重代替实际 witness/module variables。
- **Status:** failed
- **Last updated:** 2026-07-30

## A-0034 — 将单个 heavy pair 直接提升为 \(1/4\) 出口
- **Goal:** 从 \(d_H(x,r)\ge\alpha b\) 直接推出 \(\Delta(H)\ge(1/4-o(1))b^2\)。
- **Approach:** 把 wide-fan 的 heavy real-pair 后果视为已经完成的最大度出口。
- **Failure type:** scale mismatch / unsupported implication
- **Failure point:** pair codegree 只有线性 \(b\) 量级。F-0050 证明的是 fan 质量到 heavy pair 的转换；它没有把许多 heavy pairs 集中到同一顶点，也没有排除 pair 身份沿 genealogy 轮换形成 codebook/core。
- **Why it failed:** \(d_H(x,r)\le\deg_H(x)\) 的线性下界远弱于所需二次下界；还缺全局 load concentration 或 actual-edge growth。
- **Failure signature:** `linear pair fiber promoted directly to quadratic vertex degree`
- **Evidence:** F-0050；`evidence/proofs/ROUTE_B_ATLAS_LP_LEDGER.md` §4 and §10.
- **Related:** Q-0008, Q-0016, Q-0018
- **Retry conditions:** 证明 positive heavy-pair load 要么集中在共同实际顶点、产生大量不同真实边，要么形成 `S/A` pair-codebook/recurrent core。
- **Do not repeat:** 不得把“存在一个 heavy pair”单独列为已接受的 \(1/4\) 终局。
- **Status:** failed-as-direct-exit
- **Last updated:** 2026-07-30
