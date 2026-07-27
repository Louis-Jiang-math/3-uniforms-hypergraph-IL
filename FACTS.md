# Facts

## F-0001 — 定义：三一致分块超图与独立横截

- **Status:** confirmed
- **Statement:** 研究对象是顶点集分成等大块 \(B_1,\ldots,B_m\)、每条边交三个不同块的三一致超图；独立横截（IT）是从每个块恰取一个顶点且不完整包含任何超边的集合。
- **Scope:** 仅适用于当前材料中的 stretched、三一致、等块大小模型；块大小记为 \(b\)。
- **Evidence:** 两份自足 handoff 均给出相同定义。
- **Sources:**
  - `handoff_toward_one_quarter.md`，第 78–119 行，发言者 `unknown`
  - `handout(4).md`，第 64–109 行，发言者 `unknown`
- **Dependencies:** none
- **Related:** Q-0013
- **Caveats:** 当前文件未重新审查更一般的非等块或非 stretched 模型。
- **Last updated:** 2026-07-24

## F-0002 — 块极小反例归约

- **Status:** confirmed
- **Statement:** 若存在无 IT 的实例，则存在一个由部分完整块诱导的无 IT 实例，使删除任意一个块后均存在 IT。
- **Scope:** 极小化只能对完整真实块的子系统使用。
- **Evidence:** 通过在所有无 IT 的完整块子系统中取块数最少者得到。
- **Sources:**
  - `handoff_toward_one_quarter.md`，第 122–134 行，发言者 `unknown`
  - `handout(4).md`，第 152–174 行，发言者 `unknown`
- **Dependencies:** F-0001
- **Related:** A-0013, Q-0005
- **Caveats:** 代码簿、相位轨道和部分顶点支持不能据此直接视为真子实例。
- **Last updated:** 2026-07-24

## F-0003 — 中位质量恒等式

- **Status:** confirmed
- **Statement:** 对最大深度独立状态 \(T_\star\)，令 \(i=t(T_\star)\)、\(C=B(T_\star)\setminus D(T_\star)\)、\(j_x=t(T_\star\cup\{x\})\)、\(h=\lfloor b/2\rfloor\)、\(W=i+\sum_{x\in C}j_x\)，则
  \[
  W-\left(b+\left\lfloor\frac{b^2}{4}\right\rfloor\right)
  =
  h(h-i)+\sum_{x\in C}(j_x-(h+1)).
  \]
- **Scope:** 使用固定块顺序与材料中定义的“下一块坏点数”。
- **Evidence:** 自足 handoff 给出逐项代数证明。
- **Sources:**
  - `handoff_toward_one_quarter.md`，第 138–231 行，发言者 `unknown`
  - `handout(4).md`，第 178–346 行，发言者 `unknown`
- **Dependencies:** F-0001
- **Related:** F-0004, F-0007
- **Caveats:** 该恒等式给出义务质量，不自动给出互异真实边或单一顶点次数。
- **Last updated:** 2026-07-24

## F-0004 — 中位源下界

- **Status:** derived
- **Statement:** 在 F-0003 的条件下，
  \[
  W\ge b+\left\lfloor\frac{b^2}{4}\right\rfloor
  =\left(\frac14+o(1)\right)b^2.
  \]
- **Scope:** 同 F-0003。
- **Evidence:** F-0003 右端各项非负，因为 \(i\le h\) 且 \(j_x\ge h+1\)。
- **Sources:**
  - `handoff_toward_one_quarter.md`，第 155–199 行，发言者 `unknown`
  - `handout(4).md`，第 254–345 行，发言者 `unknown`
- **Dependencies:** F-0003
- **Related:** F-0007, Q-0002
- **Caveats:** 这是源义务总量，不是已完成的 \(1/4\) 最大度证明。
- **Last updated:** 2026-07-24

## F-0005 — 真实边单位容量与加权 Hall 接口

- **Status:** partially_proved
- **Statement:** 在统一认证网络中，若每条真实边配置容量至多为一，则义务质量能否注入真实边等价于相应加权 Hall 条件；该接口可防止把不同历史中同一真实边重复计为多条边。确定性的第一阻断边只把失败尝试分成互斥证书类，并不自动给出单位容量。
- **Scope:** 依赖统一测试空间、第一认证分割、真实边身份完整保留，以及义务账本与真实边容量账本的明确分离。
- **Evidence:** 两份 handout 给出最大流/最小割形式的加权 Hall 证明；`SINGLE_DEFECT_FRAMEWORK.md` 进一步区分“投影—边出现重数”与“全局真实边容量”。从任意极小反例抽取满足全部网络公理的全局对象仍开放。
- **Sources:**
  - `handoff_toward_one_quarter.md`，第 233–270 行，发言者 `unknown`
  - `handout(4).md`，第 347–491 行，发言者 `unknown`
  - `chatgpt-export_第一阶段解析骨架.txt`，助手回答轮次 1，第 73–117 行，发言者 `assistant`
  - `SINGLE_DEFECT_FRAMEWORK.md`，第 12 节
- **Dependencies:** F-0001
- **Related:** A-0010, A-0019, Q-0002
- **Caveats:** 第一阻断证书唯一、每个投影—边对出现一次，均不足以推出同一真实边在不同投影间没有被重复兑现；Hall 接口本身也不证明所需网络必能从原超图近无损构造。
- **Last updated:** 2026-07-25

## F-0006 — \(4/27\) 基准充分条件

- **Status:** partially_proved
- **Statement:** 在当前 stretched 三一致分块模型中，材料使用
  \[
  \Delta(H)\le\left(\frac4{27}-o(1)\right)b^2
  \Longrightarrow H\text{ 有 IT}
  \]
  作为基准输入。
- **Scope:** 证明重建依赖 Wanless–Wood 型外部定理；该外部定理未在本轮源文件中独立核验。
- **Evidence:** 对块关联数 \(M_i\) 取参数 \(\beta=2b/3\)，得到阈值 \(M_i\le4b^3/27\)，再由 \(M_i\le b\Delta(H)\) 推出结论。
- **Sources:**
  - `chatgpt-export_基准真实边集合证明.txt`，助手回答轮次 1，第 23–118 行，发言者 `assistant`
  - `handoff_toward_one_quarter.md`，第 272–282 行，发言者 `unknown`（标记为 `[INPUT]`）
- **Dependencies:** F-0001
- **Related:** F-0007, Q-0012
- **Caveats:** 不应把该条标记为完全独立核验的 `confirmed`。
- **Last updated:** 2026-07-24

## F-0007 — 基准后 residual 质量为 \(11/108\)

- **Status:** derived
- **Statement:** 将 F-0004 的 \(1/4\) 规模中位源与 F-0006 的 \(4/27\) 基准预留相减，得到 residual 至少
  \[
  \left(\frac{11}{108}-o(1)\right)b^2.
  \]
- **Scope:** 条件于 F-0006 的基准输入和预留账本合法。
- **Evidence:** 恒等式 \(1/4-4/27=11/108\)。
- **Sources:**
  - `handoff_toward_one_quarter.md`，第 284–315 行，发言者 `unknown`
  - `handout(4).md`，第 492–655 行，发言者 `unknown`
- **Dependencies:** F-0004, F-0006
- **Related:** Q-0001, Q-0002
- **Caveats:** 达到 \(1/4\) 需要近乎无损处理全部 residual；固定比例损失不足。
- **Last updated:** 2026-07-24

## F-0008 — 干净四块窗口匹配化

- **Status:** confirmed
- **Statement:** 在四个活动块各取两个候选，且每个角点有唯一第一认证边并剥离外部锚、竞争认证、配置冲突和边界异常时，16 个角点按遗漏方向配成 \(Q_4\) 的坐标完美匹配。
- **Scope:** 仅对“干净微立方体”成立。
- **Evidence:** 翻转认证边遗漏的坐标不改变该边的三个真实端点，因此方向在对应坐标边两端一致。
- **Sources:**
  - `handoff_toward_one_quarter.md`，第 319–343 行，发言者 `unknown`
  - `handout(4).md`，第 914–979 行，发言者 `unknown`
- **Dependencies:** F-0005
- **Related:** F-0009, F-0010, Q-0004
- **Caveats:** 异常窗口必须先进入真实费用账本，不能直接套用枚举。
- **Last updated:** 2026-07-24

## F-0009 — \(Q_4\) 坐标完美匹配数为 272

- **Status:** confirmed
- **Statement:** \(Q_4\) 的坐标完美匹配总数是 272。
- **Scope:** 带标号四维二进制立方体，匹配边必须沿坐标方向。
- **Evidence:** 两份 handout 附有可复核穷举程序，并将该数标记为 `[M-PROVED]`。
- **Sources:**
  - `handoff_toward_one_quarter.md`，第 345–398 行及附录 A，第 1329–1476 行，发言者 `unknown`
  - `handout(4).md`，第 980–1169 行及附录 A，第 2125–2287 行，发言者 `unknown`
- **Dependencies:** F-0008
- **Related:** F-0010, F-0011, Q-0012
- **Caveats:** 本轮未重新运行附录程序。
- **Last updated:** 2026-07-24

## F-0010 — 正常带标号模板恰有 8 个

- **Status:** confirmed
- **Statement:** 若“正常”定义为每个二维面恰出现三个匹配方向，则 272 个坐标完美匹配中恰有 8 个正常带标号模板。
- **Scope:** 同 F-0009 的带标号模型。
- **Evidence:** 附录枚举程序与显式相位描述相互一致。
- **Sources:**
  - `handoff_toward_one_quarter.md`，第 345–398 行，发言者 `unknown`
  - `chatgpt-export_数学语言描述_mathcal T_4图册(2).txt`，助手回答轮次 1，第 27–176 行，发言者 `assistant`
- **Dependencies:** F-0009
- **Related:** F-0012, Q-0004
- **Caveats:** 这是局部模板分类，不是超图真实支持分类。
- **Last updated:** 2026-07-24

## F-0011 — 非正常匹配至少有 9 个共同锚面

- **Status:** confirmed
- **Statement:** 每个非正常坐标完美匹配至少有 9 个满足共同锚指标的二维面。
- **Scope:** 共同锚指标按 handoff 中的 \(a_F(M)\) 定义。
- **Evidence:** 完整直方图为共同锚面数 \(0,9,15,16,20,24\)，对应匹配数 \(8,32,96,48,84,4\)。
- **Sources:**
  - `handoff_toward_one_quarter.md`，第 359–398 行，发言者 `unknown`
  - `handout(4).md`，第 1038–1169 行，发言者 `unknown`
- **Dependencies:** F-0009, F-0010
- **Related:** Q-0003, Q-0007
- **Caveats:** 该证书只控制局部非正常异常；正常图册仍可能有全局无损循环。
- **Last updated:** 2026-07-24

## F-0012 — 八相位参数化

- **Status:** confirmed
- **Statement:** 8 个正常模板是一个基准匹配 \(M_\ast\) 的平移轨道，并由
  \[
  \mathbf F_2^4/\langle1111\rangle\cong\mathbf F_2^3
  \]
  参数化。
- **Scope:** 保留坐标方向与带标号结构。
- **Evidence:** 显式方向函数及平移稳定子计算。
- **Sources:**
  - `handoff_toward_one_quarter.md`，第 400–436 行，发言者 `unknown`
  - `chatgpt-export_数学语言描述_mathcal T_4图册(2).txt`，助手回答轮次 1，第 81–176 行，发言者 `assistant`
- **Dependencies:** F-0010
- **Related:** F-0013, A-0001
- **Caveats:** 相位名称的一致性不携带真实边身份或真实支持。
- **Last updated:** 2026-07-24

## F-0013 — 刚性交叠图册的 cocycle 分类

- **Status:** partially_proved
- **Statement:** 在固定刚性交叠 nerve 上，抽象 \(\mathcal T_4\) 图册的唯一过渡形成 \(G\)-值 cocycle；连通 nerve 的 gauge 等价类可写为 \(\operatorname{Hom}(\pi_1(|N|),G)/G\)。
- **Scope:** 只分类局部坐标与相位的粘合；不分类真实超图支持。
- **Evidence:** handout 给出唯一过渡、cocycle 与 gauge 论证；对自同构群还报告 \(|G|=48\)。
- **Sources:**
  - `handoff_toward_one_quarter.md`，第 438–452 行，发言者 `unknown`
  - `handout(4).md`，第 1497–1567 行，发言者 `unknown`
  - `chatgpt-export_第一阶段解析骨架.txt`，助手回答轮次 36，第 14075–14449 行，发言者 `assistant`
- **Dependencies:** F-0012
- **Related:** A-0001, A-0002, Q-0004
- **Caveats:** 群同构类型与全部有限计算未在本轮独立复核。
- **Last updated:** 2026-07-24

## F-0014 — 遗传扩张完整时可 lift 到乘积/终局

- **Status:** partially_proved
- **Statement:** 若终端图册分量对完整真实块具有遗传单块扩张完整性并保持真实认证闭合，则其支持可乘积化，并导出 IT 或由完整块组成的真子无 IT 核心。
- **Scope:** 必须是完整真实块上的遗传扩张完整性；仅有全局相位截面或每块投影满射不足。
- **Evidence:** handout 给出乘积化定理和 IT/真子核心终局；后续 S3.5 审计把所需充分条件明确为矩形饱和、真实内部闭合与终端性。
- **Sources:**
  - `handout(4).md`，第 1568–1676 行，发言者 `unknown`
  - `chatgpt-export_第一阶段解析骨架.txt`，助手回答轮次 36–37，第 14794–15146 行及第 15536–15650 行，发言者 `assistant`
- **Dependencies:** F-0002, F-0013
- **Related:** A-0002, A-0013, Q-0009
- **Caveats:** 从一般终端分量推出遗传扩张完整性仍未完成。
- **Last updated:** 2026-07-24

## F-0015 — \(3/20\) 管线的当前唯一 Gap

- **Status:** confirmed
- **Statement:** 在 2026-07-22 的特定 \(3/20\) 证明框架内部，未闭合命题是
  \[
  \operatorname{ExtDef}(\mathscr C)\le C\,\operatorname{Credit}(\mathscr C),
  \]
  即正常图册遗漏合法混合扩张时，遗漏必须产生可计费的真实结构。
- **Scope:** “唯一”只针对该 \(3/20\) 管线，不适用于 \(1/4\) 项目。
- **Evidence:** 旧 handout 的完整状态表与 2026-07-24 handoff 的重新审计一致。
- **Sources:**
  - `handout(4).md`，第 1750–1944 行及第 1989–2012 行，发言者 `unknown`
  - `handoff_toward_one_quarter.md`，第 500–517 行及第 793–825 行，发言者 `unknown`
- **Dependencies:** F-0005, F-0011, F-0014
- **Related:** Q-0001, A-0015
- **Caveats:** 即使该不等式以固定常数成立，也不能直接达到 \(1/4\)。
- **Last updated:** 2026-07-24

## F-0016 — 固定核心的次数下界

- **Status:** partially_proved
- **Statement:** 对含 \(s\) 个块的固定内部核心，若大小为 \(\lambda b\) 的外部顶点集对核心的每个 IT 都由一条含该外部顶点与两个核心顶点的真实边阻断，则归一化最大度 \(q=\Delta/b^2\) 满足
  \[
  q\ge\frac{3}{s+3-2\lambda}.
  \]
- **Scope:** 依赖固定核心、完全阻断和文中定义的 \(E_2,E_3\) 计数。
- **Evidence:** 由内部三边覆盖非 IT、外部二端边覆盖 IT 义务及两次顶点度数求和得到。
- **Sources:**
  - `handoff_toward_one_quarter.md`，第 531–593 行，发言者 `unknown`
- **Dependencies:** F-0001
- **Related:** Q-0001, A-0015
- **Caveats:** 不适用于随外部状态迁移的核心。
- **Last updated:** 2026-07-24

## F-0017 — 低秩事件模型中的支撑分散界

- **Status:** partially_proved
- **Statement:** 若覆盖事件 \(A_y\) 仅依赖坐标集 \(C_y\)、\(\mu(A_y)\le q\)、\(U\subseteq\cap_yA_y\)，且每个内部块最多出现在 \(r\) 个 \(C_y\) 中，则
  \[
  \mu(U)\le q^{b/r}.
  \]
- **Scope:** 低秩乘积概率事件模型；不是任意相关真实支持的结论。
- **Evidence:** 重复应用 Hölder/Finner 不等式。
- **Sources:**
  - `handoff_toward_one_quarter.md`，第 595–629 行，发言者 `unknown`
- **Dependencies:** none
- **Related:** A-0004, Q-0001
- **Caveats:** 高共享不等于存在完全相同的固定核心。
- **Last updated:** 2026-07-24

## F-0018 — 迁移坐标模型的局部可实现性与全局度数代价

- **Status:** confirmed
- **Statement:** 文中构造的状态依赖迁移坐标模型能精确分割目标集合并保持局部刷新不变性，但固定根顶点的次数等于 \(b^2\)，因此它不是低度反例。
- **Scope:** 有限域标号、映射 \(\phi\) 与集合 \(S_a\) 的显式构造。
- **Evidence:** pair 柱面与 triple 柱面分别分割 \(U\) 和 \(U^c\)，根顶点次数为 \(\rho b^2+(1-\rho)b^2=b^2\)。
- **Sources:**
  - `handoff_toward_one_quarter.md`，第 631–676 行，发言者 `unknown`
- **Dependencies:** none
- **Related:** A-0004
- **Caveats:** 它反驳固定坐标圆整，但不反驳可能存在其他全局稳定性定理。
- **Last updated:** 2026-07-24

## F-0019 — 连续松弛的平均值公式及其局限

- **Status:** observed
- **Statement:** 在 handoff 的有限模型中，将超边变量放松到 \([0,1]\) 后，报告的最优平均值为
  \[
  \lambda_{\mathrm{frac}}(n,b)=\frac{1+nD/3}{b^2},
  \]
  且只在 \(nD\le17\) 时满足相应 \(3/20\) 阈值。
- **Scope:** 指定的有限 LP 模型；不是原超图的一般定理。
- **Evidence:** handoff 汇总了计算公式和首次失败参数表。
- **Sources:**
  - `handoff_toward_one_quarter.md`，第 751–789 行，发言者 `unknown`
- **Dependencies:** none
- **Related:** A-0011, Q-0012
- **Caveats:** 本轮未获得原始求解日志，也未重新运行。
- **Last updated:** 2026-07-24

## F-0020 — 当前材料没有无条件改进 \(4/27\) 的证明

- **Status:** confirmed
- **Statement:** 所有上传记录综合后，没有得到适用于全部三一致等块分块超图的无条件首项常数改进；\(3/16\)、\(1/6\)、\(\sqrt6\)、\(3/20\) 和 \(1/4\) 的相关增强均仍依赖未证结构桥梁。
- **Scope:** 仅是对这 8 个源文件所含研究状态的判断，不是外部文献现状声明。
- **Evidence:** 较晚审计明确撤回无条件化，两个 dated handoff 也分别将 \(3/20\) 和 \(1/4\) 标为条件/开放。
- **Sources:**
  - `chatgpt-export_证明主线与障碍.txt`，助手回答轮次 73–74，第 20003–20097 行，发言者 `assistant`
  - `handout(4).md`，第 2084–2121 行，发言者 `unknown`
  - `handoff_toward_one_quarter.md`，第 809–825 行及第 1292–1325 行，发言者 `unknown`
- **Dependencies:** F-0006, F-0015
- **Related:** A-0010, Q-0002
- **Caveats:** 未搜索或核对上传文件之外的最新文献。
- **Last updated:** 2026-07-24

## F-0021 — 条件化保留标签时不产生信息损失

- **Status:** confirmed
- **Statement:** 对重纤维作条件化并保留纤维标签只重组联合分布，不产生真实熵下降；确定性粘合 \(\Gamma_{\rm out}=F(\Gamma_{\rm in})\) 的信息损失恰为
  \[
  H(\Gamma_{\rm in}\mid\Gamma_{\rm out},Q).
  \]
- **Scope:** 信息势函数以源义务标签 \(Q\) 为条件，并完整保留接口代码。
- **Evidence:** 链式法则给出精确恒等式；条件熵为零时旧接口可恢复。
- **Sources:**
  - `chatgpt-export_第一阶段解析骨架.txt`，助手回答轮次 1，第 139–204 行，发言者 `assistant`
  - `handoff_toward_one_quarter.md`，第 1196–1204 行，发言者 `unknown`
- **Dependencies:** none
- **Related:** A-0003, A-0012
- **Caveats:** 信息损失公式不自动把可恢复循环转换为真实边费用。
- **Last updated:** 2026-07-24

## F-0022 — 配置预算下单缺陷递推的条件闭合

- **Status:** partially_proved
- **Statement:** 设深度 \(k\) 的源稳定执行记录总质量为 \(A_k\)，获得合法配置流的根失败质量为 \(\mathcal B_k\)。若：
  1. 每个普通根缺陷来自真实合法两步配置；
  2. 对每个源根投影 \(\widehat S\) 存在 root-pivot 预算
     \[
     \lambda_{\widehat S}(p)\ge0,\qquad
     \sum_p\lambda_{\widehat S}(p)\le1+\eta;
     \]
  3. 对每个 \((\widehat S,p,e)\) 有投影—pivot—根边槽位容量
     \[
     \sum_{\substack{\widetilde D\ {\rm root}\\
     \pi_{\rm exec}(\widetilde D)=\widehat S\\
     p(\widetilde D)=p\\
     e_{\rm root}(\widetilde D)=e}}
     w(\widetilde D)
     \le
     (1+\gamma)\lambda_{\widehat S}(p)w(\widehat S);
     \]
  4. 所有未分配配置质量和其他异常进入显式误差项 \(E_k\)；
  则
  \[
  \mathcal B_k\le(1+\eta)(1+\gamma)\Delta(H)A_{k-2},
  \]
  且
  \[
  A_k\ge
  bA_{k-1}
  -(1+\eta)(1+\gamma)\Delta(H)A_{k-2}
  -E_k.
  \]
  若 \(E_k=0\) 且
  \[
  (1+\eta)(1+\gamma)(1/4-\varepsilon)<1/4,
  \]
  则 \(\Delta(H)\le(1/4-\varepsilon)b^2\) 推出存在 IT。
- **Scope:** 条件于实际搜索的质量守恒、合法配置完备性、root projection 属于实际源稳定层、配置流需求守恒以及异常质量没有被静默丢弃。全局真实边 Hall 容量是第三份账本，不能由槽位容量自动推出。
- **Evidence:** 对固定 \(\widehat S\)，按 pivot 和根边求和：
  \[
  \sum_{\pi_{\rm exec}(\widetilde D)=\widehat S}w(\widetilde D)
  \le
  (1+\gamma)w(\widehat S)
  \sum_p\lambda_{\widehat S}(p)d_H(p)
  \le
  (1+\eta)(1+\gamma)\Delta(H)w(\widehat S).
  \]
  再对全部源根投影求和并应用二阶递推。
- **Sources:**
  - `handoff_toward_one_quarter.md`，第 827–951 行，发言者 `unknown`
  - `SINGLE_DEFECT_FRAMEWORK.md` v0.3，第 6、10–12 节
- **Dependencies:** F-0005
- **Related:** F-0027, F-0028, F-0029, Q-0002, Q-0003, Q-0004, Q-0005, Q-0015
- **Caveats:** 配置搜索方案存在性、投影闭包、槽位重数和全局真实边容量仍开放，故不能据此声称 \(1/4\) 已证。
- **Last updated:** 2026-07-27

## F-0023 — 固定轻锚可局部关闭 residual

- **Status:** partially_proved
- **Statement:** 对一个已给定的固定接口 \((p,q)\)，若存在此前只承担低负载的固定顶点 \(p\)，则材料中的 residual 可用 \((11/54+o(1))b^2\) 条经过 \(p\) 的边局部关闭，严格低于 \(b^2/4\)。
- **Scope:** 单个局部接口；不允许同一轻锚服务线性多个兄弟状态。
- **Evidence:** 对 residual 集 \(R\) 和新块 \(W\) 加入全部 \(\{p,u,w\}\)，边数为 \(|R||W|=(11/54+o(1))b^2\)。
- **Sources:**
  - `chatgpt-export_文章核心问题分析(1).txt`，助手回答轮次 100，第 52282–52405 行，发言者 `assistant`
- **Dependencies:** F-0007
- **Related:** A-0018, Q-0010
- **Caveats:** 该局部事实不能直接组成全局无 IT 低度实例。
- **Last updated:** unknown

## F-0024 — 三端口圆柱连接器的 \(1/4\) 下界

- **Status:** partially_proved
- **Statement:** 在记录所定义的三端口圆柱连接器模型中，若全部残余四元选择由一个固定重枢轴关系与两个可随变量锚改变的二元关系覆盖，则归一化最大度 \(D\) 必满足 \(D\ge1/4\)。
- **Scope:** 仅限该三类二元关系组成的完整覆盖模型。
- **Evidence:** 对固定 residual 顶点平均变量锚度数，结合重枢轴已有 \(4/27\) 负载，得到
  \[
  -\frac{(4D-1)(27D-19)}{54}\ge0,
  \]
  在 \(D<1/2\) 时推出 \(D\ge1/4\)。
- **Sources:**
  - `chatgpt-export_文章核心问题分析(1).txt`，助手回答轮次 100，第 52540–52866 行，发言者 `assistant`
- **Dependencies:** F-0006
- **Related:** Q-0010
- **Caveats:** 不能外推到允许任意跨历史三元边的所有连接器网络。
- **Last updated:** unknown

## F-0025 — 自适应二相位安全核的历史计算报告

- **Status:** observed
- **Statement:** 一份对话记录报告：在 749 个处于循环核心的局部关系状态上，存在自适应安全核，每个状态至少保留两个二位起始状态；该结果允许相位随历史变化。
- **Scope:** 指定的有限关系自动机，不是原超图的直接结论。
- **Evidence:** 记录给出状态计数与安全集合大小分布，但本轮未获得独立检查器输出。
- **Sources:**
  - `chatgpt-export_基准真实边集合证明.txt`，助手回答轮次 35，第 14992–15109 行，发言者 `assistant`
- **Dependencies:** none
- **Related:** Q-0008, Q-0012
- **Caveats:** 从真实高重叠纤维抽取覆盖保持的二点接口仍未证明。
- **Last updated:** unknown

## F-0026 — 小规模整数模型的历史不可行报告

- **Status:** observed
- **Statement:** 最新 handoff 汇总的小规模整数 MILP 在若干 \((n,b,D)\) 参数上报告严格违反或等号违反不可行，并在 \(n=4,b=3\) 的完整见证枚举中报告所有最小无公共 pair 子族的 fractional matching 值为 \(3/2\)。
- **Scope:** 仅限表中有限参数。
- **Evidence:** handoff 保存了参数、变量数、约束数与结果摘要。
- **Sources:**
  - `handoff_toward_one_quarter.md`，第 702–750 行，发言者 `unknown`
- **Dependencies:** none
- **Related:** A-0011, Q-0012
- **Caveats:** handoff 明确说明未重新运行全部求解；不能升级为渐近事实。
- **Last updated:** 2026-07-24

## F-0027 — 单个 \(\Delta\) 因子的正确接口是配置预算

- **Status:** derived
- **Statement:** 若源状态只记录无指针部分横截 \(T\)，并在失败后自由选择收费顶点，则直接估计一般只有
  \[
  \sum_{v\in T}d_H(v)\le |T|\Delta(H).
  \]
  因此要在配置优先的单缺陷递推中保住单个 \(\Delta(H)\) 因子，必须提供总预算
  \[
  \sum_p\lambda_{\widehat S}(p)\le1+\eta
  \]
  和逐 \((\widehat S,p,e)\) 槽位容量；源状态预置共同唯一 pivot 只是 \(\eta=0\) 的特殊情形，并非普遍可行。
- **Scope:** 这是当前配置化二阶递推账本的必要接口；不排除不同势函数或完全不同证明方法。
- **Evidence:** F-0022 的逐源投影求和按配置分支的 pivot 星展开。F-0029 进一步证明，正常、无竞争的真实四块组件也可能不存在共同预置 pivot。
- **Sources:**
  - `SINGLE_DEFECT_FRAMEWORK.md` v0.3，第 3–4、10–11 节
- **Dependencies:** F-0022
- **Related:** A-0021, A-0022, F-0029, Q-0002, Q-0014, Q-0015
- **Caveats:** 配置预算仍需由真实最大流/Hall 证明；不能把源层任意分数 pivot 当作已获得的容量。
- **Last updated:** 2026-07-27

## F-0028 — 单端点释放后必须重新验证独立性

- **Status:** confirmed
- **Statement:** 设 \(T\) 为独立部分横截，尝试加入 \(x\) 时第一阻断边为 \(e_0=\{p,r,x\}\)。删除 \(r\) 后所得
  \[
  (T\setminus\{r\})\cup\{x\}
  \]
  不必自动独立，因为另一条阻断边可能不含 \(r\)。因此普通单缺陷状态必须把释放后独立性列为定义条件；否则该失败属于 multi-defect 或其他异常分支。
- **Scope:** 任意三一致分块超图中的单缺陷交换。
- **Evidence:** 若另有阻断边 \(\{x,u,v\}\) 且 \(r\notin\{u,v\}\)，删除 \(r\) 后该边仍完整存在。
- **Sources:**
  - `SINGLE_DEFECT_FRAMEWORK.md`，第 6.2–6.3 节
- **Dependencies:** F-0001
- **Related:** A-0020, Q-0002, Q-0014
- **Caveats:** 第一阻断边的确定性只选择证书，不排除同时存在其他阻断边。
- **Last updated:** 2026-07-25

## F-0029 — 零误差共同预置 pivot 命题的真实正常四块反例

- **Status:** confirmed
- **Statement:** 存在一个四块、每块两个顶点的三一致分块超图，满足：
  1. 无 IT，且每个完整横截恰含一条边；
  2. 边极小、块极小、无竞争认证；
  3. 对应的 \(Q_4\) 坐标完美匹配正常；
  4. 存在真实可达的两步窗口，其中同一成功后继的两个普通失败分别强制两个不同 pivot，且两次释放旧端点后都恢复独立。
  因而不能为该源稳定记录预先指定一个共同唯一 pivot。
- **Explicit model:** 四个块
  \[
  B_i=\{i_0,i_1\},\qquad i=0,1,2,3,
  \]
  边集
  \[
  \begin{aligned}
  &\{0_0,1_0,2_0\},\{0_0,1_1,3_0\},
    \{0_0,2_1,3_1\},\{0_1,1_0,3_1\},\\
  &\{0_1,1_1,2_1\},\{0_1,2_0,3_0\},
    \{1_0,2_1,3_0\},\{1_1,2_0,3_1\}.
  \end{aligned}
  \]
  对根迹 \(R=\{0_0,1_0\}\) 成功加入 \(r=2_1\) 后：
  \[
  x=3_0\Rightarrow e_0=\{1_0,2_1,3_0\},\ p=1_0,
  \]
  \[
  x=3_1\Rightarrow e_0=\{0_0,2_1,3_1\},\ p=0_0.
  \]
- **Scope:** 否定 Q-0014 的字面零误差共同 pivot 命题，以及把共同 pivot 写入源稳定状态定义的做法。
- **Evidence:** 八条边分别覆盖两个完整横截并恰好分割全部 \(16\) 个横截；两个失败各有唯一阻断边，释放 \(r\) 后的三点迹均不在边集中。方向表逐二维面检查为正常模板。
- **Sources:**
  - `SINGLE_DEFECT_FRAMEWORK.md` v0.3，第 3 节
- **Dependencies:** F-0008, F-0010, F-0028
- **Related:** A-0022, Q-0002, Q-0004, Q-0014, Q-0015
- **Caveats:** 该模型有 \(b=2,\Delta=3\)，不是 \(1/4\) 低度反例；它不否定低度渐近条件下近无损配置流的可能性。
- **Last updated:** 2026-07-27


## F-0030 — Q-0015 首轮真实执行审计基线
- **Status:** confirmed_computational
- **Statement:** 对 F-0029 八边模型的全部 24 个块顺序，审计器生成 144 个带失败义务的实际 root group：48 个零误差 root-pivot 预算可行、48 个正 root-budget 缺口、48 个含 `no-configuration` 义务。指定窗口满足 \(t_{\min}=2,\eta=1\)，固定半预算槽位流为 \(1/2\) 总需求，而独立真实边流为 \(2/2\)。
- **Evidence:** `enumerate/q0015_first_execution_results.json` 与 `enumerate/q0015_first_execution_report.md`。
- **Related:** F-0027–F-0029, Q-0015
- **Caveats:** 这是计算证书，不是一般低度配置定理。
- **Last updated:** 2026-07-27

## F-0031 — \((b,m,\Delta)=(3,14,2)\) 必有 IT
- **Status:** confirmed
- **Statement:** 每块大小 3、块数 14、最大度至多 2 的三一致分块超图必有独立横截。
- **Evidence:** 若随机横截含边数为 \(Z\)，无 IT 给出 \(Z\ge1\)，而总度预算给出 \(|E|\in\{27,28\}\)。\(|E|=27\) 时所有边对必须不相容，但 14 个块至多认证 168 对，而共有 351 对。\(|E|=28\) 时至少 210 对相容，故 \(\mathbb E\binom Z2\ge70/243\)；另一方面 \(Z\le9\) 且 \(\mathbb E(Z-1)=1/27\)，故 \(\mathbb E\binom Z2\le1/6\)，矛盾。
- **Sources:** `enumerate/q0015_hall_cut_structural_analysis.md`
- **Related:** Q-0015
- **Caveats:** 这是单个有限参数点，不给出渐近 \(1/4\) 定理。
- **Last updated:** 2026-07-27

## F-0032 — 组合 pivot-switch 与真实 reroot lift
- **Status:** confirmed
- **Statement:** 若活动独立迹 \(U\) 恰缺块 \(M\)，尝试 \(y\in M\) 的阻断边为 \(f=\{q,z,y\}\)，且 \((U-z)+y\) 独立，则 \(z\leftrightarrow y\) 围绕共同端点 \(q\) 构成组合 pivot-switch 方块。该方块可重新解释为合法 \(q\)-pivot 根配置，当且仅当存在实际访问的 path-lift \(U-z\xrightarrow{+z}U\xrightarrow{y}f\)。
- **Sources:** `PIVOT_SWITCH_ESCAPE_FRAMEWORK.md` §§2–3
- **Related:** F-0028, Q-0002
- **Caveats:** 组合方块本身不提供新的免费 pivot 预算。
- **Last updated:** 2026-07-27

## F-0033 — Escape obligation 的真实边 Hall 二分
- **Status:** confirmed
- **Statement:** `off-pivot` switch 与 `multi-defect` 的第二阻断边均可产生真实 incidence 候选。对任意有限 escape obligation 族，或者全部质量可注入真实边剩余容量，或者存在义务子集的需求严格超过其候选真实边容量，形成可复算 Hall/reuse 证书。
- **Sources:** `PIVOT_SWITCH_ESCAPE_FRAMEWORK.md` §§4–7
- **Dependencies:** F-0005, F-0032
- **Related:** Q-0002, Q-0015
- **Caveats:** 满流只给出总真实费用，不保证费用集中到一个顶点。
- **Last updated:** 2026-07-27

## F-0034 — 条件临界分裂器森林的最佳截断摊还
- **Status:** confirmed_conditional
- **Statement:** 若 genealogy 森林每个节点质量守恒，且子节点总质量至多为父质量的 \(11/27\)，则任意深度截断满足
  \[
  W_h\le\frac{27}{16}(F_h+R_h+A_h)+B_h.
  \]
  临界 \(16/27\)-\(11/27\) 几何链取等，故 \(27/16\) 最佳。
- **Sources:** `PIVOT_SWITCH_ESCAPE_FRAMEWORK.md` §8
- **Related:** Q-0005, Q-0017
- **Caveats:** 未证明一般 persistent blocker 自动满足该局部收缩正常形。
- **Last updated:** 2026-07-27

## F-0035 — 真实 incidence 只能无条件推出集中或增殖
- **Status:** confirmed
- **Statement:** 若总收费质量为 \(M\)，顶点负载为 \(L(v)\)，则
  \[
  \sum_vL(v)=M,\qquad L(v)\le d_H(v)\le\Delta(H),
  \]
  从而 \(|\operatorname{supp}L|\ge M/\Delta(H)\)。
- **Evidence:** 真实边单位容量逐顶点求和。
- **Sources:** `PIVOT_SWITCH_ESCAPE_FRAMEWORK.md` §9
- **Related:** A-0024, Q-0016
- **Caveats:** 对角分散 switch 模型表明，incidence 增殖不自动给出完整子核心或 \(1/4\) link 乘积。
- **Last updated:** 2026-07-27
