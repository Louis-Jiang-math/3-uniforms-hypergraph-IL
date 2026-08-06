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
- **Evidence:** `evidence/experiments/q0015/historical/q0015_first_execution_results.json` 与 `evidence/experiments/q0015/reports/q0015_first_execution_report.md`。
- **Related:** F-0027–F-0029, Q-0015
- **Caveats:** 这是计算证书，不是一般低度配置定理。
- **Last updated:** 2026-07-27

## F-0031 — \((b,m,\Delta)=(3,14,2)\) 必有 IT
- **Status:** confirmed
- **Statement:** 每块大小 3、块数 14、最大度至多 2 的三一致分块超图必有独立横截。
- **Evidence:** 若随机横截含边数为 \(Z\)，无 IT 给出 \(Z\ge1\)，而总度预算给出 \(|E|\in\{27,28\}\)。\(|E|=27\) 时所有边对必须不相容，但 14 个块至多认证 168 对，而共有 351 对。\(|E|=28\) 时至少 210 对相容，故 \(\mathbb E\binom Z2\ge70/243\)；另一方面 \(Z\le9\) 且 \(\mathbb E(Z-1)=1/27\)，故 \(\mathbb E\binom Z2\le1/6\)，矛盾。
- **Sources:** `evidence/experiments/q0015/reports/q0015_hall_cut_structural_analysis.md`
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

## F-0036 — Q-0015 实根障碍的未来完备提升二分
- **Status:** confirmed_formal
- **Kind:** formal lift / specification theorem
- **Statement:** 对已经给定两两不交实际根 cylinder、真实 root projection、完整 genealogy 与三份容量账本的 Q-0015 实根障碍，逐未来 tuple 作忠实展开并按最短前缀分类，则要么某个正质量分支进入有限命名 E 出口，要么得到质量与账本无损、对忠实 continuation 闭合的 future-complete 执行森林；在块极小无 IT 且无 E 时，至少存在一个真实 persistent-blocker 分支。
- **Scope:** 输入已经是 Q-0015 实根障碍；本条不构造该入口，也不控制 E 出口质量。
- **Evidence:** `docs/framework/FW-40_FUTURE_COMPLETE_LIFT.md`；`sources/raw/conversations/chatgpt-export_深度二分析执行.txt` 的最终纠错后论证。
- **Dependencies:** F-0030, F-0032, F-0033
- **Related:** Q-0015, Q-0016, Q-0017, A-0025, A-0026
- **Caveats:** 不推出 \(11/27\) 正常形、因果 incidence 集中、完整子核心必然出现或 \(1/4\) 定理。
- **DAG role:** G1b supporting input to active G1c
- **Last updated:** 2026-07-28

## F-0037 — no-configuration 无损重标为 surviving old-anchor
- **Status:** confirmed_formal
- **Kind:** exact execution reduction
- **Statement:** 在当前实际执行契约中，若释放成功插入顶点后某失败义务没有合法 configuration，则释放后的根加 attempted vertex 中存在一条真实 blocker；该边包含 attempted vertex、排除已释放顶点，故可将义务以原质量重标为 `external-old-anchor-blocker`。
- **Ledger:** 重标本身不使用 root-budget、slot 或 global-real-edge capacity。
- **Evidence:** `src/hypergraph_il/q0015.py::no_configuration_exit_certificate`；`tests/test_q0015_old_anchor.py`；`evidence/experiments/q0015/reports/q0015_external_old_anchor_temporal_stability.md`。
- **Dependencies:** F-0028, F-0030
- **Related:** Q-0015
- **Caveats:** 只完成 exit 类型重标，不控制该类的总质量。
- **Last updated:** 2026-07-29

## F-0038 — old-anchor profile 的精确稳定恒等式与时间势
- **Status:** confirmed_formal
- **Kind:** exact stability / Lyapunov theorem
- **Statement:** 对 \(a=(a_1,\ldots,a_n)\in[0,1]^n\)，令
  \[
  F(a)=\frac1{n(n-1)}\sum_{i\ne j}a_i(1-a_j),\quad
  Q=n-2\sum_i a_i,\quad
  P=\sum_i a_i(1-a_i).
  \]
  则
  \[
  \frac{n}{4(n-1)}-F(a)
  =
  \frac{Q^2}{4n(n-1)}+\frac{P}{n(n-1)}.
  \]
  对坐标单调不增、每步删除一块的轨道，
  \[
  Q_{t+1}-Q_t=2\alpha_t-1+2D_t,
  \]
  从而首尾 near-critical deficit 控制中间 near-good 删除步数；额外 drift 只加速耗散。
- **Evidence:** `src/hypergraph_il/q0015.py::old_anchor_profile_summary` 与 `old_anchor_temporal_certificate`；`tests/test_q0015_old_anchor.py`；`evidence/experiments/q0015/reports/q0015_external_old_anchor_temporal_stability.md`。
- **Dependencies:** F-0001
- **Related:** Q-0015, F-0041
- **Caveats:** 这是单 genealogy 内的 profile 势；reroot/reset 可重新置中 profile。
- **Last updated:** 2026-07-29

## F-0039 — 实际二步失败的规范 aggregate-cylinder 恒等式
- **Status:** confirmed_formal
- **Kind:** exact mass identity
- **Statement:** 对实际根 \(R\) 的成功第一坐标 \(r\)，给扩展源 \(R+r\) 权重 \(w_R/b\)，并按实际第二块 \(N(R,r)\) 分组。若 \(W_N\) 是 cylinder 根质量、\(E_N\) 是再除以 \(b\) 的规范失败质量、\(\mathcal B\) 是未规范化全部二步失败质量，则
  \[
  \mathcal B=b^2\sum_NE_N,
  \qquad
  \sum_NW_N=\frac1b\sum_Rw_R|G_R|\le\sum_Rw_R.
  \]
- **Mechanism:** 成功 \(r\)-genealogy 是一个规范 future 坐标的不同取值，不复制源质量。
- **Evidence:** `evidence/proofs/Q0015_AGGREGATE_PAIR_CYLINDER_RESET.md`，Theorem 1。
- **Dependencies:** F-0001
- **Related:** Q-0015, F-0040
- **Caveats:** 不控制 heavy-pair excess。
- **Last updated:** 2026-07-29

## F-0040 — 统一 old/fresh pair-cylinder 界与精确 heavy excess
- **Status:** confirmed_formal
- **Kind:** quantitative supporting theorem
- **Statement:** 在每个规范 future cylinder \(N\) 上，以
  \[
  \Gamma_N(p)=\sum_{S:p\subseteq S}a_S
  \]
  同时归因 old-anchor pair 和 fresh/configurable pair。对任意 \(\eta\ge0\)，或者
  \[
  E_N\le(1+\eta)\frac{\Delta(H)}{b^2}W_N,
  \]
  或者存在真实边 \(p+x\) 及 coherent heavy root cylinder
  \[
  \Gamma_N(p)>(1+\eta)\frac{W_N}{b^2}.
  \]
  全部未控质量精确隔离为
  \[
  \mathfrak H=
  b\sum_N\sum_{\substack{x\in N\\p+x\in E(H)}}
  \left(\Gamma_N(p)-(1+\eta)\frac{W_N}{b^2}\right)_+,
  \]
  且
  \[
  \mathcal B\le(1+\eta)\Delta(H)W+\mathfrak H.
  \]
- **Evidence:** `evidence/proofs/Q0015_AGGREGATE_PAIR_CYLINDER_RESET.md`，Theorem 2 与式 (10)–(11)。
- **Dependencies:** F-0001, F-0039
- **Related:** Q-0015, F-0042
- **Caveats:** 单个 heavy pair 的存在不控制正部总量 \(\mathfrak H\)。
- **Last updated:** 2026-07-29

## F-0041 — future-compatible orientation budget 的 reset compensation
- **Status:** confirmed_formal
- **Kind:** finite-state Lyapunov theorem
- **Statement:** 设 orientation token 等价保存当前输出、合法后继和资源增量，即为 transition congruence。沿执行轨道记录已见 blocker edges \(\mathcal E_t\)、carrier support \(\mathcal A_t\) 与尚未访问的兼容 token 数 \(U_t\)。则每一步要么产生新边，要么产生新支持，要么使 \(U_t\) 减一，要么重复一个 sound quotient token。因此在 quotient 前
  \[
  (|\mathcal E_t|,|\mathcal A_t|,-U_t)
  \]
  严格字典序增加。
- **Evidence:** `evidence/proofs/Q0015_AGGREGATE_PAIR_CYLINDER_RESET.md`，Theorem 3；`tests/test_q0015_reset_compensation.py`。
- **Dependencies:** F-0032
- **Related:** Q-0015, F-0038, A-0028
- **Caveats:** exact token space 可能指数大；有限性本身不足以支付 heavy excess。
- **Last updated:** 2026-07-29

## F-0042 — Q-0015 aggregate 路线的充分关闭判据
- **Status:** confirmed_conditional
- **Kind:** exact reduction / sufficient criterion
- **Statement:** 若
  \[
  \Delta(H)\le(1/4-\varepsilon)b^2
  \]
  且存在 \(\eta,\rho\ge0\) 满足
  \[
  (1+\eta)(1/4-\varepsilon)+\rho<1/4,
  \]
  并能在每层或合法 telescoping 区间证明
  \[
  \mathfrak H_k\le\rho b^2A_{k-2}
  \]
  除非出现 accepted structural exit，则 F-0005 的二阶递推系数严格小于 \(1/4\)，从而产生 IT。
- **Evidence:** `evidence/proofs/Q0015_AGGREGATE_PAIR_CYLINDER_RESET.md`，§4。
- **Dependencies:** F-0005, F-0039, F-0040
- **Related:** Q-0015
- **Caveats:** 尚未证明 heavy-excess 界；本条不关闭 Q-0015。
- **Last updated:** 2026-07-29

## F-0043 — 局部 Hall-deficiency 正交化
- **Status:** confirmed_formal
- **Kind:** exact max-flow/min-cut identity
- **Statement:** 对一个 cylinder 的失败 atoms \(y\)，令质量为 \(\mu_y\)，实际候选 blocker 集为 \(C(y)\)，每个 blocker 节点容量为 \(\tau\)。若局部最大流亏量为
  \[
  \delta=\sum_y\mu_y-\operatorname{maxflow},
  \]
  则
  \[
  \delta=
  \max_{U}
  \left(\sum_{y\in U}\mu_y-\tau|C(U)|\right)_+.
  \]
  若 \(L_e=\sum_{y:e\in C(y)}\mu_y\)，则
  \[
  \delta\le\sum_e(L_e-\tau)_+.
  \]
  因此逐 cylinder 求和后的 Hall deficiency 不超过 F-0040 的 heavy positive excess。
- **Evidence:** `evidence/proofs/ROUTE_B_REORIENTATION_AUDIT.md`，§2。
- **Dependencies:** max-flow/min-cut, F-0040
- **Related:** Q-0015, Q-0018
- **Caveats:** 这是局部正交化，不赋予后续 trajectory 全局真实边收费权。
- **Last updated:** 2026-07-30

## F-0044 — same-load alternating exchange flow
- **Status:** confirmed_formal
- **Kind:** exact residual-network equivalence
- **Statement:** 固定一个局部最大 blocker assignment \(q\)，令 \(r_a\) 为 residual。构造交替网络
  \[
  s\to a,\qquad a\to\ell,\qquad \ell\to a,
  \]
  容量分别为 \(r_a,\infty,q_{a\ell}\)，并把 \(a\) 接到其实际可达的独立全局资源网络。则一条交换流精确对应另一个局部可行最大 assignment \(q'\)，且每个 blocker 的总负载与 \(q\) 相同；被送入资源网络的量恰为 \(q'\) 的相应 residual。
- **Evidence:** `evidence/proofs/ROUTE_B_REORIENTATION_AUDIT.md`，§3。
- **Dependencies:** F-0043
- **Related:** Q-0015
- **Caveats:** 本条只证明 same-load 重排；不证明任意最大 assignment 间的全局等价，也不证明资源容量足够。
- **Last updated:** 2026-07-30

## F-0045 — 正常 \(Q_4\) 的 splice/reuse/local-cylinder 完整分类
- **Status:** observed
- **Kind:** bounded exhaustive computation
- **Statement:** 穷举 \(Q_4\) 的 272 个坐标完美匹配、其中 8 个正常匹配、192 个正常独立 one-hole states 与 768 个 future-complete release policies，得到：
  \[
  384\ \text{edge-disjoint splice candidates},\quad
  192\ \text{unavoidable real-edge reuse},\quad
  192\ \text{local same-pivot policies}.
  \]
  每个正常 state 的四个 policies 都具有 \(2+1+1\) 的相同模式。
- **Evidence:** `enumerate/q4_splice_pay_cylinder_validation.py`；
  `evidence/experiments/route_b/reports/q4_splice_pay_cylinder_validation.md`。
- **Related:** Q-0016, Q-0017, A-0029, A-0030
- **Caveats:** 仅是 \(b=2\) 正常模型的 bounded exhaustive observation；不证明一般分类或全局 cylinder。
- **Last updated:** 2026-07-30

## F-0046 — 正常 \(Q_4\) 中 edge-disjoint splice 使用全部八条真实边
- **Status:** observed
- **Kind:** bounded exhaustive computation
- **Statement:** 在 F-0045 的全部 384 个 edge-disjoint splice candidates 中，最小两支 reconvergence certificate 的不同真实边总数均为 8，即耗尽该正常 \(Q_4\) 模型的全部真实边。
- **Evidence:** 与 F-0045 相同。
- **Related:** Q-0016, A-0030
- **Caveats:** 不能由此给一般超图中的 splice 赋单位收费；它只排除“splice 在最小正常模型中免费反复”的解释。
- **Last updated:** 2026-07-30

## F-0047 — 均匀四块二元窗口的 splice-density 条件预算
- **Status:** confirmed_conditional
- **Kind:** double-counting bound
- **Statement:** 固定四个大小为 \(b\) 的真实块，并在全部二元窗口及 \(q\) 个 policies 上均匀取样。若每个被标记的 splice policy 都有至少 \(s\) 条互异 actual certificate edges，且每条 certificate edge 的三个端点都属于该窗口，则被标记 policies 的质量比例至多
  \[
  \frac{32}{3s}\frac{\Delta(H)}{b^2}.
  \]
  对 \(s=8\) 得
  \[
  \frac43\frac{\Delta(H)}{b^2}.
  \]
- **Evidence:** `evidence/proofs/ROUTE_B_REORIENTATION_AUDIT.md`，§4。
- **Dependencies:** uniform two-point window sampling
- **Related:** Q-0015, Q-0016
- **Caveats:** 这是窗口密度计数，不是全局 charging theorem；一般 trajectory 是否提供这样的 \(s\)-edge certificate 仍需证明。
- **Last updated:** 2026-07-30

## F-0048 — competing blockers 的公共释放判据与 rank-one 性
- **Status:** confirmed_formal
- **Kind:** exact local execution theorem
- **Statement:** 设独立 one-hole 状态为 \(T\)，向缺失块加入 \(x\)，并令
  \[
  \mathcal K(T,x)=\{e\in E(H):e\subseteq T\cup\{x\}\}.
  \]
  对旧顶点 \(r\in T\)，释放 \(r\) 后独立当且仅当
  \[
  r\in\bigcap_{e\in\mathcal K(T,x)}(e\setminus\{x\}).
  \]
  因而若 \(|\mathcal K(T,x)|\ge2\)，合法单释放至多一个。live multi-blocker 事件的全部真实 blockers 具有共同 pair \((x,r)\) 并写成 \(\{x,r,p\}\)；若交为空则是 release deadlock。
- **Evidence:** `evidence/proofs/ROUTE_B_ATLAS_LP_LEDGER.md` §2；`src/hypergraph_il/route_b_atlas.py::legal_release_vertices`；`tests/test_route_b_atlas.py`。
- **Dependencies:** F-0028
- **Related:** Q-0018, Q-0016
- **Caveats:** 本条只控制单个实际尝试的释放结构；不控制同一 pair 在不同 support/genealogy 中出现多少次。
- **DAG role:** S1 supporting local structure
- **Last updated:** 2026-07-30

## F-0049 — live \(M\) occurrence 的 fresh/return 精确分解
- **Status:** confirmed_formal
- **Kind:** genealogy bookkeeping theorem
- **Statement:** 固定足以决定完整 blocker family、合法释放、successor 和保留标签的 faithful support-interface token \(\sigma\)，以及实际 incidence \((x,e)\)。由 F-0048，固定 \((\sigma,x,e)\) 后至多有一个 live transition。任意有限 genealogy 中，\((x,e)\) 的 occurrence 数精确分解为不同 \(\sigma\) 的首次 occurrence 数与重复 token 的 return/merge occurrence 数：
  \[
  |\mathcal O_\Gamma(x,e)|=G_\Gamma(x,e)+R_\Gamma(x,e).
  \]
  因而 bare incidence \((x,e)\) 没有统一单位容量；精确资源是 \((\sigma,x,e)\)，重复项必须进入 return/information-loss/core 分支。
- **Evidence:** `evidence/proofs/ROUTE_B_ATLAS_LP_LEDGER.md` §3。
- **Dependencies:** F-0048, F-0041
- **Related:** Q-0018, Q-0017
- **Caveats:** 这是精确分割，不证明 fresh tokens 对不同真实边或不同度数资源有有界重数。
- **DAG role:** S1 supporting genealogy interface
- **Last updated:** 2026-07-30

## F-0050 — wide-fan 的 product-tail 与 heavy real-pair 界
- **Status:** confirmed_conditional
- **Kind:** exact counting theorem under rectangular support
- **Statement:** 固定 live common pair \((x,r)\)，对剩余块 \(C\) 令
  \[
  N_C(x,r)=\{p\in C:\{x,r,p\}\in E(H)\}.
  \]
  若固定 kernel 的 actual fresh external support \(\Sigma\) 不是坐标投影的笛卡尔积，则得到有限 `S`-correlation witness；若 \(\Sigma=\prod_C S_C\)，wide-fan 数至多为对应 Poisson-binomial 的至少三次成功尾概率。五块均匀计数中，若三个剩余块 fiber 大小为 \(d_1,d_2,d_3\)，则
  \[
  F_{x,r}\le d_1d_2d_3\le\left(\frac{d(x,r)}3\right)^3.
  \]
  进一步
  \[
  F_x\le\frac{2}{27}D_x^2\deg_H(x),
  \qquad D_x=\max_r d(x,r).
  \]
- **Evidence:** `evidence/proofs/ROUTE_B_ATLAS_LP_LEDGER.md` §4；bounded audit in `evidence/experiments/route_b/baselines/route_b_lp_atlas_validation.json`.
- **Dependencies:** F-0048
- **Related:** Q-0008, Q-0018, Q-0016
- **Caveats:** rectangular support 是显式前提；非矩形时结论是 `S` witness，不是同一乘积上界。heavy pair 本身不推出 \(b^2/4\) 最大度。
- **DAG role:** S1 supporting quantitative exit
- **Last updated:** 2026-07-30

## F-0051 — clean product chart 的 critical-deficit 全局账本
- **Status:** confirmed_conditional
- **Kind:** exact chart ledger theorem
- **Statement:** 在有限 faithful product chart 中，假设 chart 内无 reroot、无未认证 support correlation、无 cross-anchor，且同一外部 SCC 内的 successor 被送入 recurrent-module 账本。对 faithful genealogy 节点 \(u\) 的 continuation profile \(a(u)\)，有
  \[
  \sum_u m(u)D(a(u))
  \le
  G_{\rm rank}+G_{\rm leaf}+G_S+G_A+G_C+G_{\rm reset},
  \]
  其中 \(D\) 是 F-0038 的精确 deficit，\(G_{\rm rank}\) 是外部 SCC condensation 的实际 rank 增量，其余项是互斥的首次终止或结构出口质量。首次退出圆柱两两不交；fresh support 要么进入新 SCC rank，要么属于 recurrent module。
- **Evidence:** `evidence/proofs/ROUTE_B_ATLAS_LP_LEDGER.md` §5–§6。
- **Dependencies:** F-0038, F-0049
- **Related:** Q-0017, Q-0018
- **Caveats:** 本条控制执行质量，不把 rank/leaf 质量自动注入不同原超图边；跨 chart 的全局 atlas completion 与实际资源重数仍开放。
- **DAG role:** S1/S2 supporting stability interface
- **Last updated:** 2026-07-30

## F-0052 — 实际边历史 LP 的 residual-core 等价
- **Status:** confirmed_formal
- **Kind:** finite potential-or-core theorem
- **Statement:** 对有限 faithful quotient，删除具有实际 `W/M/A/N` 证书的 transitions，并以剩余实际 transitions 为顶点；当两个 transitions 可连续执行且 blocker-edge identity 不同时连边。则以下等价：历史图无有向环；存在每条历史边严格增加的有限势；不存在未认证的 multi-real-edge residual circulation。同一实际 blocker edge 内的 release oscillation 不形成 residual 历史环。
- **Evidence:** `evidence/proofs/ROUTE_B_ATLAS_LP_LEDGER.md` §7；`src/hypergraph_il/route_b_atlas.py::reduced_history_graph`；`tests/test_route_b_atlas.py`。
- **Dependencies:** F-0045, F-0046
- **Related:** Q-0016, Q-0017, Q-0018
- **Caveats:** 这是给定 finite faithful quotient 与完整证书字典后的等价；不证明一般 quotient 存在，也不分类 residual core。
- **DAG role:** S1/S2 finite core interface
- **Last updated:** 2026-07-30

## F-0053 — finite future-signature atlas 的稳定化或 overflow
- **Status:** confirmed_formal
- **Kind:** finite-interface completion theorem
- **Statement:** 对有限分支、有限单步标签字母表的 faithful execution，深度 \(k\) future signatures 形成有限逐层细化。若某层 \(K\) 的 signature equality 已决定 \(K+1\) 层 equality，则该划分永久稳定，并给出保存当前实际数据、同标签全部合法 successors 与 ledger increments 的 finite future-compatible congruence。若无层稳定，则 interface complexity 在无穷多层严格增长；兼容 overflow signatures 具有 inverse-limit exact-future object，重复 exact type 给出 return/recurrent object。
- **Evidence:** `evidence/proofs/ROUTE_B_ATLAS_LP_LEDGER.md` §8；`src/hypergraph_il/route_b_atlas.py::stable_partition`；`tests/test_route_b_atlas.py`。
- **Dependencies:** F-0041
- **Related:** Q-0018, Q-0017
- **Caveats:** unbounded interface growth 不自动推出具体 `W/S/A` 结构；这仍需 overflow-structure theorem。
- **DAG role:** R2/S1 supporting compactness-interface alternative
- **Last updated:** 2026-07-30

## F-0054 — Route-B LP/atlas 的 bounded Q4 与 \(b=3\) 审计
- **Status:** observed
- **Kind:** exhaustive-bounded plus fixed-seed bounded computation
- **Statement:** committed generator exhausts 50,528 edge-minimal four-block binary star-forest covers: 50,524 are block-minimal and split into 50,256 multi-blocker `M`, 260 unique-blocker nonnormal `N`, and 8 normal \(Q_4\) models. It also reproduces F-0045/F-0046. In the committed fixed-seed \(b=3\) samples, raw same-edge release kernels are removed by actual-edge-history `R` reduction and no new reduced residual core is observed.
- **Evidence:** `enumerate/route_b_lp_atlas_validation.py`; `enumerate/route_b_b3_reduced_core_search.py`; `evidence/experiments/route_b/baselines/route_b_lp_atlas_validation.json`; `evidence/experiments/route_b/reports/route_b_lp_atlas_validation.md`.
- **Related:** F-0045, F-0046, F-0052, Q-0016, Q-0017
- **Caveats:** Q4 counts are exhaustive in the stated finite space; \(b=3\) results are fixed-seed bounded observations. No general core classification or nonexistence theorem follows.
- **DAG role:** bounded regression evidence only
- **Last updated:** 2026-07-30

## F-0055 — exact execution tree 的 pathwise Round-or-Core-or-Overflow 接口
- **Status:** confirmed_conditional
- **Kind:** finite dynamic max-flow / actual-history theorem
- **Statement:** 给定一个有限分支 exact actual execution tree，假设入口由 first-owner stopping line 互斥分割；每个节点保存完整 actual blocker-edge candidate set；continuation 与 named-exit cylinders 是实际可测互斥分割；root/configuration 与 projection-sensitive slot 预算已另行验证；每条真实边给定全局容量。则对每个有限深度，动态 obligation network 满足精确 max-flow/min-cut 公式，且任意可行流可在 atomless refinement 上实现为互不复制的实际样本路径。若深度流值趋于全部入口质量，则得到任意精度的 faithful Round；若不趋于全部质量，则正质量实际历史永不进入命名出口。future signatures 稳定时，这些历史要么形成正质量 same-edge `R`，要么在收缩 `R` 后产生正质量 actual multi-real-edge recurrent core；不稳定时必须保留 F-0053 的 exact-future overflow。
- **Evidence:** `evidence/proofs/ROUND_OR_CORE_FINITE_INTERFACE.md`。
- **Dependencies:** F-0005, F-0048, F-0049, F-0052, F-0053
- **Related:** Q-0016, Q-0017, Q-0018, A-0035, D-0009
- **Caveats:** 本条不从任意目标超图构造 exact execution tree，不证明 root/slot 预算，不把 Round 流自动识别为 F-0042 所需的全局递推量，不转换 overflow，也不分类 actual recurrent core。它没有重新激活 Route A。
- **DAG role:** R1/S1 finite faithful Round-or-Core interface
- **Last updated:** 2026-08-01

## F-0056 — 完备有限 Markov 标签使 future signature 在深度零稳定

- **Status:** verified-conditional
- **Statement:** 若一个 unfolded actual execution 的有限状态标签完整决定一步的实际 support、完整 blocker family、全部合法 releases、successor、owner 与 ledger increments，则 F-0053 的 future-signature 划分在 \(K=0\) 稳定。
- **Scope:** 条件于该完整有限标签已经从目标执行中构造；不反向证明全局 E1/E2。
- **Evidence:** `evidence/proofs/CHAT_DERIVED_SUPPORTING_LEMMAS.md` §1。
- **Dependencies:** F-0053
- **Related:** Q-0017, Q-0018, A-0036
- **Caveats:** 有限底层超图不自动意味着一个压缩状态保存全部 future-compatible 数据。
- **Last updated:** 2026-08-03

## F-0057 — 均匀 hole-vertex sampling 下 eventually-same-edge 尾事件为零测

- **Status:** verified-conditional
- **Statement:** 若每一步在大小 \(b\) 的缺块中均匀选择尝试顶点，则从任意时刻起永远使用同一真实边 \(e\) 的概率为零；对有限边集和可数起始时刻取并后仍为零测。
- **Scope:** 依赖均匀正概率 sampling；不适用于任意 faithful policy。
- **Evidence:** `evidence/proofs/CHAT_DERIVED_SUPPORTING_LEMMAS.md` §3。
- **Dependencies:** none
- **Related:** F-0052, F-0055, Q-0017
- **Caveats:** 这是测度结论，不是对 history graph 中同边振荡的组合不存在性。
- **Last updated:** 2026-08-03

## F-0058 — fixed-pivot target-following 与 \(b^2\) link 下界

- **Status:** verified
- **Statement:** 固定实际 pivot \(p\)，沿目标横截追踪当前 hole；每个 ordinary blocker \(\{p,x_M,z\}\) 要么产生目标中的 \(p\)-link edge，要么严格增加已匹配目标坐标。故一个 future-complete、无 augmentation/multi-blocker/forced-off-pivot 的 fixed-pivot class 满足
  \[
  d_H(p)=|E(L_H(p))|\ge b^2.
  \]
  对均匀目标，停止于 forced off-pivot 或其他实际出口的概率至少为
  \[
  1-\frac{d_H(p)}{b^2}.
  \]
- **Scope:** actual one-hole states；目标坐标作为 no-copy refinement。
- **Evidence:** `evidence/proofs/CHAT_DERIVED_SUPPORTING_LEMMAS.md` §4。
- **Dependencies:** F-0048
- **Related:** Q-0016, F-0065, A-0040
- **Caveats:** target-follow 是 core 的第二阶段 postprocessing，不字面等同于 F-0051 clean chart 内的 \(G_A\)。
- **Last updated:** 2026-08-03

## F-0059 — literal specified one-coordinate splice closure 的零集是 Cartesian product

- **Status:** verified
- **Statement:** 若非空 \(X\subseteq\prod_iA_i\) 对任意 \(x,y\in X\) 和坐标 \(i\) 都包含把 \(x_i\) 替换为 \(y_i\) 的 tuple，则
  \[
  X=\prod_i\operatorname{proj}_i(X).
  \]
- **Scope:** literal actual-support closure。
- **Evidence:** `evidence/proofs/CHAT_DERIVED_SUPPORTING_LEMMAS.md` §5。
- **Dependencies:** none
- **Related:** Q-0016, A-0002, A-0029
- **Caveats:** phase consistency、reversibility、monodromy 或 projected surjectivity 不蕴含该假设。
- **Last updated:** 2026-08-03

## F-0060 — harmonic failure 的 degree-budget 精确局部压缩

- **Status:** verified
- **Statement:** 对固定 \((S,B)\) 及每个失败顶点选定的最小 harmonic blocker，存在实际生成系数 \(c_{S,B}(y)\) 使 failure term 等于
  \[
  \sum_{y\in S}c_{S,B}(y)\gamma_{S-y},
  \]
  且
  \[
  0\le c_{S,B}(y)\le1,\qquad
  \sum_{y\in S}d_H(y)c_{S,B}(y)=|F(S,B)|.
  \]
- **Scope:** 只对实际 blocker 配对产生的系数成立。
- **Evidence:** `evidence/proofs/HARMONIC_SHADOW_COUNTEREXAMPLE.md` §1。
- **Dependencies:** none
- **Related:** A-0038, Q-0015
- **Caveats:** 任意满足同样线性预算的系数不一定可实现；该投影不足以证明 harmonic feasibility。
- **Last updated:** 2026-08-03

## F-0061 — unique blocker 的 release-complete no-copy 分裂

- **Status:** verified
- **Statement:** 若完整 blocker family 为 \(\{\{x,a,b\}\}\)，则释放 \(a\) 与释放 \(b\) 都合法；父 cylinder 可由独立二元坐标分成两个互不相交的实际后继，质量守恒且不复制。
- **Scope:** unique-blocker actual one-hole transition。
- **Evidence:** `evidence/proofs/CHAT_DERIVED_SUPPORTING_LEMMAS.md` §2。
- **Dependencies:** F-0048
- **Related:** Q-0018, A-0037
- **Caveats:** 只保留其中一个 release 是执行 policy，不是 future completeness。
- **Last updated:** 2026-08-03

## F-0062 — clean epoch 的端点控制收缩与有限类型 transient 消失

- **Status:** verified-conditional
- **Statement:** 在无 reroot/reset 的单调 profile 区间，
  \[
  Q_{t+1}-Q_t=2\alpha_t-1+2D_t,\qquad D_t\ge0,
  \]
  因而 continuation mass 由两个端点的 critical deficit 控制并指数收缩。若实际执行只有有限完整转移类型，则避免终止与有限 recurrent class、且不重复完整转移类型的 surviving mass 随深度趋零。
- **Scope:** 依赖 profile 单调性、F-0038 端点界和有限完整转移类型。
- **Evidence:** `evidence/proofs/CHAT_DERIVED_SUPPORTING_LEMMAS.md` §6。
- **Dependencies:** F-0038, F-0041
- **Related:** Q-0017, Q-0018
- **Caveats:** 不分类 recurrent 部分，也不自动构造全局 faithful execution。
- **Last updated:** 2026-08-03

## F-0063 — all-release unique-blocker core 的三角形分解与 weighted context regularity

- **Status:** verified
- **Statement:** 在有限强连通、无 augmentation、unique-blocker、all-release actual core 中，state graph 是 \(2b\)-正则并按 full completions 分解为三角形；若 \(c_e\) 是真实边 \(e\) 的 completion multiplicity，则
  \[
  b|K|=3|\Omega_K|,
  \qquad
  \sum_{e\ni v}c_e=|K_{B(v)}|.
  \]
- **Scope:** 保留完整实际 support 和全部 release branches 的 finite core。
- **Evidence:** `evidence/proofs/CORE_CONTEXT_REUSE_AND_SWITCH_MATCHING.md` §§1–3。
- **Dependencies:** F-0048, F-0061
- **Related:** Q-0016
- **Caveats:** 低度只迫使高 context reuse，不直接排除 blocker。
- **Last updated:** 2026-08-03

## F-0064 — core common-state multiplicity 恒等式

- **Status:** verified
- **Statement:** 对 F-0063 的 core，若 \(m_{ef}\) 统计同一 one-hole state 中真实边 \(e,f\) 作为不同尝试 blockers 的次数，则
  \[
  \sum_{f\ne e}m_{ef}=3(b-1)c_e,
  \qquad
  m_{ef}\le\min(c_e,c_f).
  \]
  相应不相容图满足
  \[
  \rho(A_K)\ge3(b-1),
  \qquad
  d_{A_K}(e)\le3(b-1)\Delta(H).
  \]
- **Scope:** 同 F-0063。
- **Evidence:** `evidence/proofs/CORE_CONTEXT_REUSE_AND_SWITCH_MATCHING.md` §4。
- **Dependencies:** F-0063
- **Related:** Q-0016, F-0067
- **Caveats:** 谱半径与最大度粗界本身远弱于 \(1/4\) 终局。
- **Last updated:** 2026-08-03

## F-0065 — recurrent core 的 target-follow forced-off-pivot 质量

- **Status:** verified
- **Statement:** 对 F-0063 的 core 中任意当前实际顶点 \(p\)，均匀目标 target-follow 满足
  \[
  \Pr(\text{first forced off-pivot})
  \ge1-\frac{d_H(p)}{b^2}.
  \]
  对互不相交的 core 入口 cylinders，总质量 \(M_K\) 与第二阶段 forced-off-pivot 质量 \(G_A^{\rm core}\) 满足
  \[
  G_A^{\rm core}\ge
  \left(1-\frac{\Delta(H)}{b^2}\right)M_K.
  \]
- **Scope:** unique-blocker all-release core 的第二阶段 no-copy target refinement。
- **Evidence:** `evidence/proofs/CORE_CONTEXT_REUSE_AND_SWITCH_MATCHING.md` §5。
- **Dependencies:** F-0058, F-0063
- **Related:** Q-0016, A-0040
- **Caveats:** \(G_A^{\rm core}\) 与 F-0051 的 clean-chart \(G_A\) 是互斥阶段的同单位质量，不是同一变量。
- **Last updated:** 2026-08-03

## F-0066 — pairwise incompatible 真实边族的静态上界

- **Status:** verified
- **Statement:** 若 \(\mathcal F\subseteq E(H)\) 中任意两边不相容，则
  \[
  |\mathcal F|\le3(b-1)\Delta(H)+1.
  \]
  若其还恰好覆盖每个完整横截一次，则
  \[
  |\mathcal F|=b^3,\qquad
  \Delta(H)\ge\frac{b^2+b+1}{3}.
  \]
- **Scope:** 等块三一致 stretched 模型。
- **Evidence:** `evidence/proofs/CORE_CONTEXT_REUSE_AND_SWITCH_MATCHING.md` §6。
- **Dependencies:** none
- **Related:** Q-0016
- **Caveats:** 仍需从 recurrent core 推出这种精确覆盖。
- **Last updated:** 2026-08-03

## F-0067 — 最大复用边的 completion–switch 同步—分散二分

- **Status:** verified
- **Statement:** 对最大 context multiplicity 边 \(e\)，每个 \(e\)-completion 给出一个 injective switch map \(\pi_W:S(e)\to E(H)\)，其平均矩阵是 slot-side saturated fractional matching。对任意 \(\delta>0\)，要么绝大多数 context–slot pairs 接近某个实际 switch matching，并产生 \(3(b-1)\) 个近最大 multiplicity 邻边；要么
  \[
  \sum_s\left(1-\sum_fp_s(f)^2\right)>\delta\,3(b-1),
  \]
  且正比例 context–slot pairs 偏离各 slot 的 modal output。精确同步时，相邻最大复用 context 族之间存在双射。
- **Scope:** F-0063 的 finite actual core。
- **Evidence:** `evidence/proofs/CORE_CONTEXT_REUSE_AND_SWITCH_MATCHING.md` §§7–9。
- **Dependencies:** F-0063, F-0064
- **Related:** Q-0016, A-0041, D-0011
- **Caveats:** 分散不自动给 actual-edge capacity slack；同步不自动给 product support。
- **Last updated:** 2026-08-03

## F-0068 — actual switch output 的全局 slot 唯一性

- **Status:** verified
- **Statement:** 在 F-0063 的 finite unique-blocker all-release core 中，固定真实边 \(e,f\)。若 completion–switch 输出 \(f\)，则产生该输出的 slot \(s=(u,x)\in S(e)\) 与 completion context 无关且至多一个。因而 F-0067 的
  \[
  m_{ef}=\sum_{s\in S(e)}n_s(f)
  \]
  加强为
  \[
  m_{ef}=n_{s(e,f)}(f)
  \]
  whenever \(m_{ef}>0\).
- **Scope:** F-0063 的 actual completion–switch map；结论依赖 stretched block incidence 与每个 switched completion 的唯一 blocker。
- **Evidence:** `evidence/proofs/ROOT_ONLY_EXCESS_SWITCH_CUBE_ROUTE.md` §2。
- **Dependencies:** F-0063, F-0067
- **Related:** Q-0016, A-0041, D-0011, D-0012
- **Caveats:** 该结论排除单步 actual switch map 的跨 slot Latin-column migration，但不自动产生容量 slack、product support 或终局。
- **Last updated:** 2026-08-04

## F-0069 — 完美 switch transition 的 monodromy 恒等与 sheet 分解

- **Status:** verified
- **Statement:** 在 F-0063 的 core 中，若 \(c_e=c_f=m_{ef}=C>0\)，则 F-0068 给出一个固定 slot \(s(e,f)=(u,x)\)，且
  \[
  \theta_{ef}:\Omega_e\to\Omega_f,\qquad W\mapsto W-u+x
  \]
  是双射。沿任意完美 transition 闭路的复合是恒等；因此等 multiplicity 的完美 transition component 的 lifted completion graph 分解为 \(C\) 个互不相交 sheets。若该 lifted graph 连通，则 \(C=1\)。
- **Scope:** 所有转移均满足 \(c_e=c_f=m_{ef}\) 的 actual perfect-transition component。
- **Evidence:** `evidence/proofs/ROOT_ONLY_EXCESS_SWITCH_CUBE_ROUTE.md` §3。
- **Dependencies:** F-0068
- **Related:** Q-0016, D-0011, D-0012
- **Caveats:** first nonperfect boundary 可以是近满 partial matching；sheet 分解本身不提供 \(1/4\) 级 Hall slack。
- **Last updated:** 2026-08-04

## F-0070 — root-only canonical global excess normalization

- **Status:** verified
- **Statement:** 对有限合法区间 \(I\)，令 \(S_I=\sum_{k\in I}A_{k-2}\)，并在 F-0039 的 actual two-step failure Palm space 中为每个 root failure atom 从完整 blocker family 选一个 canonical actual edge。若 \(L_I(e)\) 是 canonical root load，且
  \[
  c_I(e)=\frac{1+\eta}{S_Ib^3}
  \sum_{\substack{k\in I,N\\e\cap N\ne\varnothing}}W_{k,N},
  \qquad
  \Xi_I=\sum_e(L_I(e)-c_I(e))_+,
  \]
  则
  \[
  \frac{\sum_{k\in I}\mathcal B_k}{b^2S_I}
  \le
  (1+\eta)\frac{\Delta(H)}{b^2}+\Xi_I.
  \]
  同时 \(\sum_ec_I(e)\le(1+\eta)\Delta(H)/b^2\)。
- **Scope:** 只支付原始二步 root failure atoms；不授予 release descendants 新的 root capacity entitlement。
- **Evidence:** `evidence/proofs/ROOT_ONLY_EXCESS_SWITCH_CUBE_ROUTE.md` §4。
- **Dependencies:** F-0039
- **Related:** F-0040, Q-0018, D-0002, D-0012
- **Caveats:** 该恒等式不证明 \(\Xi_I\) 小，也不证明 clean-chart reduction、fresh-token conversion 或 overflow closure。
- **Last updated:** 2026-08-04

## F-0071 — finite all-release core 的 actual switch-cube defect

- **Status:** verified
- **Kind:** exact finite-core natural-defect theorem
- **Statement:** 设 \(K\) 是 F-0063 的 finite unique-blocker all-release actual core，\(\beta_K\) 是 nonliteral context-slot 密度。则
  \[
  \Delta(H)\ge(1-3\beta_K)_+\frac{(b-1)^3}{b}.
  \]
  若 \(\delta_\square(K)\) 是每次 switch 遗失旧 blocker endpoints 的归一化 actual-support defect，则
  \[
  \frac{\beta_K}{2}\le\delta_\square(K)\le\beta_K.
  \]
  因而在 \(\Delta(H)\le(1/4-\varepsilon)b^2\) 下，
  \[
  \delta_\square(K)\ge
  \frac16\left[1-(1/4-\varepsilon)\left(\frac b{b-1}\right)^3\right]
  =\frac18+\frac\varepsilon6-O_\varepsilon(b^{-1}).
  \]
  对互不相交 core 入口 cylinders 加权后，同一常数乘以总 core 入口质量给出全局 defect 下界。
- **Proof mechanism:** 每个 completion 有 \(6(b-1)^3\) 个 ordered three-switch instructions；all-literal instructions 的 intermediate states 均合法并最终产生实际边 \(\{x_1,x_2,x_3\}\)。每个坏 instruction 赋给第一处 nonliteral current context-slot；固定 context-slot 在三个位置的原像分别至多 \(2(b-1)^2\)，总计至多 \(6(b-1)^2\)。
- **Scope:** finite unique-blocker all-release actual cores；带权版本要求入口 cylinders no-copy 且先进入该 normal form。
- **Evidence:** `evidence/proofs/SWITCH_CUBE_AND_ROOT_EXCESS_CLOSURE.md` §§1–4；regression helpers in `src/hypergraph_il/route_b_closure.py` and `tests/test_route_b_closure.py`.
- **Dependencies:** F-0063, F-0061
- **Related:** Q-0016, Q-0017, Q-0018, FW-60
- **Caveats:** 本条关闭 finite normal-form core 的 natural-defect endgame；不构造 global core entrance，也不处理 overflow 或非 finite/all-release core。
- **Last updated:** 2026-08-04

## F-0072 — canonical root excess 的 exact clean-cross reduction

- **Status:** confirmed_conditional
- **Kind:** exact no-copy chart-interface theorem
- **Statement:** 在 F-0070 的 interval Palm normalization 中，以 canonical excess submeasure \(\nu_I\) 表示 \(\Xi_I\)。给定一个 F-0051 scope 的 faithful clean-chart atlas，把 excess atoms 仅在 owner、root projection、actual blocker、support interface、ordered directions 和 genealogy 一致时送入 ordered cross cells；令 \(\operatorname{ChartMis}_I\) 为该有限 no-copy max-flow 的 exact Hall deficiency。定义
  \[
  \mathcal D_I^\sharp=\sum_um(u)(n(u)-1)D_{n(u)}(a(u)),
  \]
  并在 rounded-compatible cells 上按 F-0049/F-0041 分成首次 token 质量 \(\Phi_I\) 与 return/merge/cycle/core 质量 \(\mathcal R_I\)。则
  \[
  \Xi_I\le
  \operatorname{ChartMis}_I+2\mathcal D_I^\sharp+\Phi_I+\mathcal R_I.
  \]
  因此
  \[
  \frac{\sum_{k\in I}\mathcal B_k}{b^2S_I}
  \le
  (1+\eta)\frac{\Delta(H)}{b^2}
  +\operatorname{ChartMis}_I+2\mathcal D_I^\sharp+\Phi_I+\mathcal R_I.
  \]
- **Proof mechanism:** incompatible ordered-cross capacity satisfies
  \[
  \Lambda_{\rm cross}(u)
  \le\frac{m(u)}{n(u)}\sum_i|a_i-\mathbf1_{a_i\ge1/2}|
  \le2m(u)(n(u)-1)D_{n(u)}(a(u)).
  \]
  unassigned mass is exactly the chart Hall deficiency；compatible assigned mass由 first/return token partition 精确分割。
- **Scope:** 需要一个 supplied faithful clean-chart atlas；atlas 可以不覆盖全部 excess，未覆盖部分精确保留为 \(\operatorname{ChartMis}_I\)。root capacity 只属于原始二步 failure atoms。
- **Evidence:** `evidence/proofs/SWITCH_CUBE_AND_ROOT_EXCESS_CLOSURE.md` §§5–7；regression helpers in `src/hypergraph_il/route_b_closure.py` and `tests/test_route_b_closure.py`.
- **Dependencies:** F-0038, F-0049, F-0051, F-0070
- **Related:** Q-0018, Q-0017, F-0041, F-0042
- **Caveats:** 本条不证明 global faithful atlas 存在，不证明 \(\operatorname{ChartMis}_I\)、\(\Phi_I\) 或 \(\mathcal R_I\) 小，也不允许把 chart deficiency 定义为 terminal。F-0038 的负 margin 仍需在最终 master ledger 中保留。
- **Last updated:** 2026-08-04

## F-0073 — fresh compatible mass 的 exact priority split

- **Status:** verified
- **Kind:** exact no-copy genealogy partition
- **Statement:** 在 F-0072 的 rounded-compatible first-token submeasure \(\Phi_I\) 上，先移出由完整实际标签认证的 \(M/A/N/S/\mathrm{reset}\) exits；其余 unique-blocker clean atoms 按优先级精确分为：当前 actual blocker edge 首次出现、edge 已见但 carrier support 新增顶点、以及 edge/support 均已见而 faithful token 首次出现。因 \(\Phi_I\) 本身已是 first-token 质量，入口分解中不存在独立的 repeat 项：
  \[
  \Phi_I=\Phi_I^{\rm exit}+\Phi_I^{\rm edge}
  +\Phi_I^{\rm support}+\Phi_I^{\rm token}.
  \]
  该分解可测、互斥、穷尽、no-copy，并在 faithful refinement 下协变。
- **Evidence:** `evidence/proofs/FRESH_LEAF_THREE_CYLINDER_CLOSURE.md` §§1–2；helpers in `src/hypergraph_il/route_b_closure.py`；`tests/test_fresh_leaf_three_cylinder.py`。
- **Dependencies:** F-0041, F-0049, F-0072
- **Related:** Q-0018, D-0012
- **Caveats:** 本条只分类 first-token mass；edge/support/exit 的全局 terminal 或 recurrence 后果仍需证明。重复 token 仍在 \(\mathcal R_I\) 或 F-0074 的 return stopping output 中。
- **Last updated:** 2026-08-04

## F-0074 — pure fresh-token 的 actual three-cylinder stopping line

- **Status:** verified-conditional
- **Kind:** release-complete no-copy stopping theorem
- **Statement:** 给定 F-0073 的 pure-token atoms 的 faithful release-complete actual execution lift，对当前 unique blocker \(e(W)=\{u_1,u_2,u_3\}\) 在三个端点块独立均匀选择 replacements。沿六种 orders 保存完整 blocker family，并在首次出现 named exit、new actual edge、new carrier support 或 sound token return 时停止；若无这些输出且某 terminal coordinate 不可由 pure prefixes 到达，则输出指定的 actual-support three-cylinder splice defect；仅当三个 terminals 均可达且最终状态仍为 pure fresh token 时继续。若 \(R_L\) 是深度 \(L\) 后的 surviving pure-token mass，则
  \[
  R_L\le q_b^L\Phi_I^{\rm token},
  \qquad q_b=\frac{b\Delta(H)}{(b-1)^3}.
  \]
  对 \(q_b<1\)，全部 pure-token mass 被 no-copy first-stopping cylinders 穷尽为 exit/edge/support/return/splice-defect；没有 token-universe remainder。
- **Proof mechanism:** 若一个 target triple 继续，则每个 terminal coordinate 有一条 pure-prefix order；同一最终 completion 的唯一 blocker必须同时包含三个 replacement vertices，故为 \(\{x_1,x_2,x_3\}\)。逐 root 可继续 triples 至多是三个端点块之间的实际边数，因而不超过 \(b\Delta(H)\)。逐代点态收缩给出几何 remainder。
- **Scope:** 需要保留 actual owner、root projection、complete blocker family、carrier support、faithful token、完整 genealogy，并使用 F-0061 release-complete no-copy branching。六种 order 只用于有限实际路径查询；输出时选择全局次序下最早的 actual certificate，child 选择最早的 pure order 作为 canonical genealogy，因此不复制质量或资源账本。离开 pure-token scope 的质量必须保留为其实际 first output，不能丢弃。
- **Evidence:** `evidence/proofs/FRESH_LEAF_THREE_CYLINDER_CLOSURE.md` §§3–7；helpers in `src/hypergraph_il/route_b_closure.py`；`tests/test_fresh_leaf_three_cylinder.py`。
- **Dependencies:** F-0041, F-0048, F-0049, F-0061, F-0073
- **Related:** Q-0018, Q-0017, FW-60
- **Caveats:** 本条消除 persistent pure-token 分支，但不支付 first-certifying edge mass，不把 Cartesian support 自动当作 terminal，也不构造 global atlas 或转换 overflow。
- **Last updated:** 2026-08-04


## F-0075 — finite-resource restart exhausts edge/support/pure-token persistence

- **Status:** verified-conditional
- **Kind:** no-copy fixed-instance stopping theorem
- **Statement:** 在 F-0072/F-0073/F-0074 的 supplied faithful release-complete actual lift 中，不把 first-certifying edge 或 new carrier support 当作终局，而是在 genealogy 上登记新实际资源并从其实际输出状态重启。令
  \[
  N_H=|E(H)|+|V(H)|,
  \qquad q_b=\frac{b\Delta(H)}{(b-1)^3}.
  \]
  若 \(U_L\) 是经过 \(L\) 次 restart/query transitions 后仍未到达 exit、atlas-boundary、sound return 或 specified splice defect 的质量，则
  \[
  U_L\le
  \Phi_I\sum_{r=0}^{\min\{N_H,L\}}\binom Lr q_b^{L-r}.
  \]
  因而对每个固定有限 \(H\) 和 \(q_b<1\)，\(U_L\to0\)。不存在 persistent new-edge、new-support 或 pure-token remainder；unbounded token-universe size 不再是该 lift 内的 obstruction。
- **Proof mechanism:** 每个 edge/support restart 严格增加已见实际边或 support-vertex 集，故一条 genealogy 至多有 \(N_H\) 个 resource transitions；其余 surviving transitions 都是 F-0074 pure children，逐步总条件质量至多 \(q_b\)。按 resource positions 求和得到 polynomial-geometric bound。
- **Scope:** 需要 faithful atlas、actual owner/root/blocker/support/genealogy 与 release-complete F-0074 lift。离开 clean/compatible scope 的第一时刻必须记录为 actual atlas-boundary output。该结论逐固定实例 exact，但不提供对所有实例统一的有限深度速率。
- **Evidence:** `evidence/proofs/FINITE_RESOURCE_RESTART_EXHAUSTION.md` §§1–4；helpers in `src/hypergraph_il/route_b_closure.py`；`tests/test_finite_resource_restart.py`。
- **Dependencies:** F-0072, F-0073, F-0074
- **Related:** Q-0017, Q-0018, F-0052, F-0057
- **Caveats:** 本条不证明 exit、atlas-boundary、splice 或 return/core 已产生最终 master gain/terminal；不构造 global faithful atlas。
- **Last updated:** 2026-08-04

## F-0076 — supplied-atlas exact zero-defect root closure

- **Status:** confirmed_conditional
- **Kind:** exact common-zero-set closure
- **Statement:** 在 F-0072 faithful atlas、F-0075 restart lift 及 F-0052/F-0057 finite residual normal form均给定时，若
  \[
  \operatorname{ChartMis}_I=\mathcal D_I^\sharp=0,
  \]
  且 restart stopping outputs中的 named exit、atlas-boundary、three-cylinder splice defect及 F-0071 switch-square defect均为零，则
  \[
  \Xi_I=0
  \]
  并且
  \[
  \frac{\sum_{k\in I}\mathcal B_k}{b^2S_I}
  \le(1+\eta)\frac{\Delta(H)}{b^2}.
  \]
- **Proof mechanism:** F-0075 把全部 fresh compatible mass exact 地穷尽为有限 stopping categories；sound return 在 supplied residual normal form 中进入 F-0071 core。共同零集使 F-0072 右端全部消失，再调用 F-0070。
- **Scope:** exact zero-defect branch only；需要 supplied global atlas 与 residual normal form。
- **Evidence:** `evidence/proofs/FINITE_RESOURCE_RESTART_EXHAUSTION.md` §§5–7。
- **Dependencies:** F-0070, F-0071, F-0072, F-0075, F-0052, F-0057
- **Related:** Q-0017, Q-0018, S4, F-0042
- **Caveats:** 不证明任意低度反例的这些 defect 为零或小；positive-density terminal/gain consequence仍是主定理义务。
- **Last updated:** 2026-08-04


## F-0077 — rounding-free actual-cross root-excess reduction

- **Status:** verified-conditional
- **Kind:** exact no-copy chart-interface theorem
- **Statement:** 在 F-0070 的 canonical excess submeasure 和 supplied faithful actual-cross atlas 中，不对 continuation profile 做确定性阈值舍入。每个已分配 cell 本身已经保存实际 continuation direction 与 actual first-stop direction；在全部 assigned cross atoms 上按完整 faithful token 直接作 F-0049 first/return 分割。若 `ChartMis_I` 是同一 no-copy chart max-flow 的 exact Hall deficiency，`Phi_I^x` 与 `R_I^x` 分别为 assigned mass 的 first-token 与 return/merge/cycle/core 部分，则
  \[
  \Xi_I=\operatorname{ChartMis}_I+\Phi_I^\times+\mathcal R_I^\times.
  \]
  因而
  \[
  \frac{\sum_{k\in I}\mathcal B_k}{b^2S_I}
  \le(1+\eta)\frac{\Delta(H)}{b^2}
  +\operatorname{ChartMis}_I+\Phi_I^\times+\mathcal R_I^\times.
  \]
  F-0073--F-0075 的 edge/support/token restart 与 three-cylinder stopping 只使用 actual labels，不使用 threshold bits，故对 `Phi_I^x` 原样适用。
- **Why rounding is removed:** 对 `a_i=1/2` 的 profile，确定性舍入产生 `1/4` incompatible mass，而 F-0038 deficit 只有 `1/(4(n-1))`；二者比值为 `n-1`，所以该误差不可能由 dimension-free deficit margin 支付。
- **Evidence:** `evidence/proofs/ROUNDING_FREE_ACTUAL_CROSS_REDUCTION.md`; helpers in `src/hypergraph_il/route_b_closure.py`; `tests/test_rounding_free_cross.py`.
- **Dependencies:** F-0049, F-0070, F-0072
- **Related:** F-0073, F-0074, F-0075, F-0076, Q-0018
- **Caveats:** 仍需 supplied faithful actual-cross atlas；本条不证明 `ChartMis_I` 的后果或 global atlas 存在。F-0038/F-0051 可用于其他 temporal stability 论证，但不得再作为正 rounding cost 加入 master inequality。
- **Last updated:** 2026-08-04

## F-0078 — history-unfolded physical stopping of canonical root excess

- **Status:** downgraded / verified only in restricted scope
- **Kind:** exact fixed-instance stopping identity
- **Retained statement:** On the fully unfolded actual history tree, the local
  F-0074 kernel and finite edge/support restarts give a fixed-instance terminal
  decomposition
  \[
  \Xi_I=G_\infty^W+G_\infty^M+G_\infty^{\mathrm{return}}
  +G_\infty^{\mathrm{splice}}
  \]
  when the corresponding tail tends to zero.
- **Withdrawn promotions:**
  1. global no-IT does not imply \(G_\infty^W=0\), because \(W\) is only a
     completion on the exposed proper block set;
  2. the physical token without visited-history data is not a transition
     congruence;
  3. return under one canonical policy does not imply an all-release F-0071
     core;
  4. fixed-instance convergence depending on \(|E(H)|+|V(H)|\) is not a
     uniform asymptotic stopping estimate.
- **Evidence:** `evidence/audits/F0078_SCOPE_CORRECTION.md`.
- **Dependencies:** F-0074, F-0075
- **Related:** F-0052, F-0071, Q-0017, Q-0018, Q-0019
- **Last updated:** 2026-08-06

## F-0090 — canonical full-target repair

- **Status:** verified
- **Statement:** Let \(S\) be an independent partial transversal and \(Q\) a
  full target transversal. Repeatedly install the first unmatched target
  coordinate. If a blocker lies inside \(Q\), stop at that actual edge;
  otherwise delete an inclusion-minimal set of currently selected non-target
  vertices hitting the complete blocker family. Each step preserves
  independence and permanently increases agreement with \(Q\). Hence the
  process reaches the independent target \(Q\) or an actual edge \(e\subseteq
  Q\). In a no-IT instance every target yields such an edge.
- **Caveat:** This is a pointwise actual repair map. It gives neither an
  inverse-multiplicity bound nor a negative term.
- **Related:** F-0091, Q-0019
- **Evidence:** `evidence/proofs/FORK_INVERSE_FIBER_ANCHOR_ROUTE.md`.
- **Last updated:** 2026-08-06

## F-0091 — canonical rank-two repair and fork dichotomy

- **Status:** verified under faithful execution-log reconstruction
- **Statement:** For an independent partial transversal \(S\) and attempted
  vertex \(x\), choose a canonical maximal matching in the blocker-link graph
  \(G_x(S)\), and delete all matching endpoints after adding \(x\). The result
  is independent. Matching number one remains a rank-two repair even when the
  blocker family contains many edges. The obstruction is matching number at
  least two, which yields two actual blocker edges disjoint away from \(x\).
- **Entropy consequence:** In the fork-free branch the record polynomial is
  \(1+\Delta z^2\), with minimum growth \(2\sqrt\Delta\), giving the exact
  threshold \(\Delta<b^2/4\). For every fixed \(\varepsilon>0\), under
  \(\Delta\le(1/4-\varepsilon)b^2\), a no-IT faithful long execution has a
  positive linear density of matching excess and hence of disjoint-blocker
  forks.
- **Caveat:** The theorem forces fork occurrences but does not control repeated
  use of the same actual edge.
- **Related:** F-0092, Q-0019
- **Evidence:** `evidence/proofs/FORK_INVERSE_FIBER_ANCHOR_ROUTE.md`; executable
  helpers in `src/hypergraph_il/fork_route.py`.
- **Last updated:** 2026-08-06

## F-0092 — two-coordinate replacement-box codimension

- **Status:** verified
- **Statement:** In an edge-minimal no-IT instance, choose for
  \(e=\{x,a,b\}\) a full transversal \(W_e\) containing no edge other than
  \(e\). Replace \(a,b\) by \((u,v)\) in their blocks and choose an actual edge
  in the resulting target. Every chosen edge contains at least one of \(u,v\).
  A fixed output edge has at most one preimage if it contains both replacement
  coordinates and at most \(b\) preimages if it contains exactly one. The same
  bounds hold for weighted occurrences when the parent history is retained.
- **Consequence:** The two-coordinate part has a genuine \(b^{-2}\) inverse
  multiplicity; the one-coordinate part has only \(b^{-1}\) and carries a
  potentially migrating heavy vertex or pair.
- **Caveat:** Local one-coordinate concentration does not imply future-complete
  persistence of one anchor.
- **Related:** F-0058, F-0091, Q-0019
- **Evidence:** `evidence/proofs/FORK_INVERSE_FIBER_ANCHOR_ROUTE.md`.
- **Last updated:** 2026-08-06

## F-0093 — fork-rooted refill-box codimension

- **Status:** verified
- **Statement:** Fix an actual parent occurrence
  \((h,\operatorname{owner},\operatorname{root},S,x,M)\), where \(S\) is an
  independent partial transversal, \(x\) lies in a block missed by \(S\), and
  \(M\) is the canonical maximal blocker matching. Starting from
  \(R_0=(S\cup\{x\})\setminus V(M)\), refine independently by one uniform
  target coordinate in every parent block and canonically refill holes. Every
  target atom yields either an independent augmentation of size \(|S|+1\) or
  an actual blocker containing the current and an earlier installed target
  coordinate. Recording the actual edge and an unordered two-block witness
  gives inverse mass at most \(W/b^2\) per certificate and at most \(3W/b^2\)
  per actual output edge for parent mass \(W\).
- **Scope:** Uniform in the matching rank, number of blocks, number of actual
  histories and finite-history size; the complete parent history, owner, root,
  actual blocker family and matching-edge identities remain attached to every
  refined atom.
- **Caveat:** The bounded load is on the later output edge, which need not
  contain \(x\). It does not bound the original source-fork load \(\ell_x\).
- **Evidence:** `evidence/proofs/FORK_ROOTED_REFILL_BOX.md` §§1--4.
- **Related:** F-0091, F-0092, F-0094, Q-0019, A-0048--A-0050
- **Last updated:** 2026-08-06

## F-0094 — pivot-protected refill trichotomy

- **Status:** verified
- **Statement:** Under the hypotheses of F-0093, protect the original pivot
  \(x\) and every installed target coordinate. If a blocker pair lies inside
  the protected set, stop; otherwise delete a canonical inherited hitting set
  for the complete blocker family and continue. The process terminates with
  exactly one of: (i) an independent augmentation of size \(|S|+1\) retaining
  \(x\); (ii) an actual edge \(\{x,q_B,q_C\}\); or (iii) an actual off-pivot
  edge \(\{q_B,q_C,q_D\}\) consisting of three target coordinates. For parent
  mass \(W\), a fixed output in (ii) receives at most \(W/b^2\), the total mass
  of (ii) is at most \(d_H(x)W/b^2\), and a fixed output in (iii) receives at
  most \(W/b^3\).
- **Scope:** Actual-history-preserving and uniform in the same parameters as
  F-0093; the hitting set is taken only from selected inherited vertices.
- **Caveat:** Outcome (i) is a larger partial transversal, not a global
  independent transversal. One outcome-(iii) edge, or even a proper subset of
  target atoms with such edges, is not a complete proper-block no-IT subsystem
  and is not a paid pivot-switch exit.
- **Evidence:** `evidence/proofs/FORK_ROOTED_REFILL_BOX.md` §5.
- **Related:** F-0058, F-0090, F-0093, Q-0019, A-0044, A-0048--A-0050
- **Last updated:** 2026-08-06

## F-0095 — direct macro-record arity barrier

- **Status:** verified
- **Statement:** If every matching-excess unit is assigned an independent
  multiplicative mark \(y\), the exact infimum in the corresponding
  simply-generated-tree envelope is
  \[
  G(y)=\inf_{0<u<1/y}
  \frac{1+(1-y)u}{\sqrt u(1-yu)},
  \]
  so a contradiction at \(c=\Delta/b^2\) requires
  \(\sqrt c\,G(y)<1\). As \(c\to1/4\), this forces \(y\to0\). A directly
  recorded new three-edge output has, at best, normalized cost
  \(y=\Delta/b^2=c\): one target coordinate is needed to localize an endpoint
  before the actual edge has at most \(\Delta\) choices, leaving only two net
  target coordinates. Even granting this factor independently to every excess
  unit, the self-consistent threshold is
  \[
  c_0=0.211390706210804\ldots<1/4,
  \]
  the unique root in \((0,1/4)\) of
  \(4c^4-12c^3+4c^2-24c+5=0\).
- **Scope:** The direct independent-mark substitution for source-owned macro
  codes that record each later actual output by a newly degree-indexed edge
  label and use no additional source-determined identity, irreversible
  coordinate or cross-output dependence.
- **Caveat:** Failure of this tree-envelope bound is not a lower bound on the
  actual record language. A smaller language would need a genuinely new
  dependence or source invariant. Independent repetition of the same refill
  boxes does not create one because the dispersed off-pivot certificate family
  still exhausts the complementary target mass.
- **Evidence:** `evidence/analyses/FORK_MACRO_RECORD_ARITY_BARRIER.md`.
- **Related:** F-0093, F-0094, Q-0019, A-0051
- **Last updated:** 2026-08-06
