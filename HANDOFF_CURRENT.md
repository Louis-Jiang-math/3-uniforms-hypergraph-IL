# Current Handoff

## 1. Project objective

当前项目研究三一致等块分块超图中的独立横截阈值。目标是在块大小为 \(b\) 时证明：若最大度严格低于 \((1/4-o(1))b^2\)，则存在独立横截。成功标准是得到对当前模型全部实例成立的无条件证明，同时严格保留真实边身份、单位容量、完整块范围、执行 genealogy 和所有低阶误差。当前输入仍没有在同一手稿中完整复核 \(1/4\) 锐性构造（Q-0013）。

## 2. Current state

- 当前阶段：`SINGLE_DEFECT_FRAMEWORK.md` 已修订为 v0.5 的配置优先、switch 可审计框架。
- 已确认的关键变化：Q-0014 的“同一源稳定记录预置共同唯一 pivot”零误差命题为假。
- 真实反例：四个二元块上的八边正常 \(Q_4\) 模型，无 IT、边极小、块极小、无竞争认证；同一成功后继的两个失败分别强制两个不同 pivot，且释放后均独立（F-0029）。
- 因此源稳定记录不再包含 pivot。失败先形成义务，枚举全部合法真实两步配置；只有获得正配置流的分支才生成带 pivot 的缺陷记录。
- 当前主要方向：Q-0015 首轮审计器与结果已归档到 `enumerate/`；形式 defect closure 已细化为 ordinary fixed-pivot 继续或真实 incidence 收费/Hall 割。下一结构任务是 Q-0017 的 persistent-blocker 正常形和 Q-0016 的因果 incidence 再生集中；在此之前不声称 terminal SCC 三出口分类。
- 当前阻塞点：尚未证明一般低度搜索中的近无损配置流；也未证明 persistent blocker 进入 11/27 临界正常形，或大量分散的新 pivot 必然重新集中、形成完整子核心或产生 IT。

## 3. Confirmed knowledge

- F-0002 — 可先取对完整真实块块极小的无 IT 实例。
- F-0003 — 中位源满足精确质量恒等式。
- F-0004 — 中位义务质量至少为 \(b+\lfloor b^2/4\rfloor\)。
- F-0008 — 干净四块窗口产生 \(Q_4\) 坐标完美匹配。
- F-0009 — 坐标完美匹配总数为 272。
- F-0010 — 正常带标号模板恰有 8 个。
- F-0011 — 每个非正常模板至少有 9 个共同锚面。
- F-0012 — 八相位由 \(\mathbf F_2^4/\langle1111\rangle\) 参数化。
- F-0018 — 状态依赖坐标迁移局部可实现，但显式模型付出 \(b^2\) 根次数。
- F-0020 — 当前材料没有完成任何无条件优于 \(4/27\) 的首项常数证明。
- F-0021 — 保留纤维标签的条件化不产生信息损失。
- F-0028 — 单端点释放后必须重新验证独立性。
- F-0029 — 零误差共同预置 pivot 命题已由真实正常四块反例否定。

## 4. Important provisional findings

- F-0005 — status: partially_proved；真实边单位容量与加权 Hall 是正确账本接口，但全局近无损网络抽取仍需审计。
- F-0006 — status: partially_proved；\(4/27\) 基准依赖未在本轮独立核验的外部定理。
- F-0007 — status: derived；基准后 residual 为 \(11/108\)，条件于 F-0006。
- F-0013 — status: partially_proved；抽象刚性图册由 cocycle 分类，但不含真实支持。
- F-0014 — status: partially_proved；遗传扩张完整时可 lift，缺的是从一般终端核心推出该完整性。
- F-0015 — status: confirmed；\(3/20\) 管线唯一 Gap 是 ExtDef–Credit，但它不是 \(1/4\) 的唯一 Gap。
- F-0022 — status: partially_proved；配置预算和槽位容量若成立，则条件递推以系数 \((1+\eta)(1+\gamma)\Delta(H)\) 闭合。
- F-0027 — status: derived；单个 \(\Delta\) 因子的正确入口是总 root-pivot 配置预算和逐槽位容量，不是源状态共同 pivot。
- F-0023 — status: partially_proved；单个固定轻锚可低于 \(1/4\) 局部关闭 residual。
- F-0024 — status: partially_proved；广泛的三端口圆柱连接器仍被 \(1/4\) 下界阻挡。
- F-0025, F-0026 — status: observed；历史机器报告尚需独立复核。

## 5. Do not repeat

- A-0001 — 非平凡 monodromy 可完全可逆；不能自动收费。
- A-0002 — 相位一致不等于真实支持乘积化；对角代码簿是反例。
- A-0003/A-0012 — 条件化或 bounded width 本身不产生熵损失。
- A-0004 — 状态依赖的好坐标不能无条件圆整为固定坐标。
- A-0008/A-0010 — 错误依赖图或未证忠实相位投影不能产生无条件新常数。
- A-0009 — “任意二相位关系可分裂为三相位最大负载 5”已有显式反例。
- A-0011 — 小规模 LP/MILP 不可行不能代替有限见证定理。
- A-0013 — 不得对部分支持、代码簿或相位轨道使用块极小性。
- A-0015 — 十八块是 \(3/20\) sector 阈值，不是 \(1/4\) 的本征结构。
- A-0018 — 单个轻锚服务线性多个兄弟状态会累积 \(\Theta(b^3)\) 次数。
- A-0019 — 第一阻断边的确定性不等于真实边单位容量。
- A-0020 — 删除第一阻断边一个端点后不能跳过独立性复检。
- A-0021 — 无指针稳定状态不能直接给出逐状态单个 \(\Delta\) 因子。
- A-0022 — 正常性不推出同一成功后继的共同预置 pivot；不要通过换序或事后选 pivot 重试。

## 6. Open and answered questions

1. Q-0014 — **answered negative**：共同预置 pivot 的零误差命题为假。
2. Q-0015 — 审计基础设施已完成；一般近无损配置流与 Hall 最小割结构分类仍开放。
3. Q-0002 — 配置优先搜索能否满足投影闭包、槽位容量和配置化 defect closure？
4. Q-0004 — 配置分支的正常相位如何保留真实 root projection 和 genealogy 地全局粘合？
5. Q-0006 — 在配置化执行图存在后，零误差 terminal SCC 是否有增广叶、\(1/4\) link 乘积或完整子核心？
6. Q-0003 — terminal critical link 的平衡二部稳定性。
7. Q-0005 — 无出口 terminal 组件如何迫使 \(1/4\) link 乘积或完整真子核心？
8. Q-0007 — 配置化零误差分类后的固定 \(\varepsilon\) 稳定化。
9. Q-0012 — 机器证书独立复核。
10. Q-0013 — \(1/4\) 锐性构造同稿复核。
11. Q-0001 — 若继续较弱目标，\(3/20\) ExtDef–Credit 仍开放。

## 7. Immediate next actions

1. **把 Q-0015 审计器接到外层候选生成器：** 对每个低度候选输出 IT、无配置、配置预算/槽位最小割或全局真实边 Hall 最小割，并保存边极小、块极小、块顺序和 genealogy 见证。
2. **实现 escape-charge 审计：** 对每个非 ordinary 步骤枚举组合 switch 方向或第二阻断边，把质量路由到真实 incidence；满流失败时输出可复算的真实边 Hall 割。
3. **完成配置入口的搜索存在性（Q-0002）：** 证明正流配置的 root projection 实际可达，配置分裂/汇合质量守恒，且未分配质量进入命名残余账本。
4. **攻击 Q-0017 的深度二正常形：** 展开两个连续 persistent-blocker 模块，搜索或证明 \(11/27\) 收缩失败必产生 fresh、reuse、增广、quotient 或内部闭合。
5. **攻击 Q-0016 的因果 incidence 再生：** 在真实 switch/reroot genealogy 下证明新锚不能长期无损增殖；先做两个连续近临界模块的附加费引理。
6. **terminal SCC 后置：** 只有在配置入口、formal closure-or-charge 和正常形接口完成后，才研究 Q-0006/Q-0003/Q-0005。
7. **复核证书（Q-0012, Q-0013）：** 保留 F-0029、genealogy collision 和 \((3,14,2)\) 精确排除作为回归测试，并补充历史程序与锐性构造。

## 8. Required reading for the next agent

- `SINGLE_DEFECT_FRAMEWORK.md` v0.5：优先读第 3–12、20、23–24 节。
- `PIVOT_SWITCH_ESCAPE_FRAMEWORK.md`：组合 switch、reroot lift、escape Hall、条件森林摊还及其结构边界。
- `QUESTIONS.md`：优先读 Q-0002、Q-0004、Q-0006、Q-0007、Q-0015–Q-0017。
- `enumerate/README.md` 与 `enumerate/manifest.json`：机器文件角色、历史运行状态和后续严格升级。
- `FACTS.md`：优先读 F-0005、F-0022、F-0027–F-0029、F-0030–F-0035。
- `FAILURES.md`：优先读 A-0019–A-0025。
- `old/handoff_toward_one_quarter.md`：优先读第 2–4、6–8、10–14 节。
- 旧导出中的相位、配置和真实容量讨论仍可作历史证据，但抽象相位缺口不能替代真实配置/escape Hall 最小割。

## 9. Recent changes

- `SINGLE_DEFECT_FRAMEWORK.md`：当前为 v0.5；Q-0015 审计状态、组合 pivot-switch、escape charge、条件森林摊还和 incidence 集中边界均已写入。
- `PIVOT_SWITCH_ESCAPE_FRAMEWORK.md`：新增纯组合 switch、真实 reroot lift、可路由容量和 formal closure-or-charge 规范。
- `QUESTIONS.md`：Q-0015 拆分为“审计基础设施已完成、一般近无损/结构分类仍开放”；新增 Q-0016、Q-0017。
- `enumerate/`：统一归档审计脚本、原始 JSON、可读报告和结构分析；根目录不再保存重复机器产物。
- 主线调整：不再把 off-pivot/multi-defect 全部预设为小误差；先做真实 incidence 收费或 Hall 割，再研究因果再生与 persistent-blocker 正常形。

## 10. Integrity warnings

- F-0029 否定的是字面零误差共同 pivot 命题，不是 \(1/4\) 阈值；该模型有 \(b=2,\Delta=3\)。
- 配置流、槽位容量和全局真实边 Hall 是三份不同账本；任何后续证明必须说明当前使用哪一份。
- 局部正常相位或源 Hall 缺口不能直接升级为真实边容量 obstruction。
- terminal SCC 只有在配置提取、投影闭包和配置化 defect closure 完成后才有合法定义。
- F-0006 的外部 \(4/27\) 输入、Q-0013 的锐性构造及部分历史机器报告仍未独立复核。
- 当前框架是候选基础设施，不是 \(1/4\) 证明。


## 11. 2026-07-27 switch/escape 更新

- 新增 `PIVOT_SWITCH_ESCAPE_FRAMEWORK.md`：把 pivot-switch 分成纯组合交换方块、真实 reroot lift 与容量可路由三层。
- 已证明局部交换方向三分法：ordinary move、组合 switch、或释放后暴露第二真实阻断边。
- 已证明 escape obligation 的真实边 Hall 二分：全部逃逸质量可由真实 incidence 支付，或输出真实边 reuse 最小割。
- 已证明条件临界分裂器森林的截断摊还
  \[
  W_h\le\frac{27}{16}(F_h+R_h+A_h)+B_h,
  \]
  但 \(11/27\) 收缩仍是正常形假设。
- 已确认真实 incidence 无条件只给出“集中或顶点增殖”；朴素集中到 \(1/4\)/子核心的命题有对角分散反例。
- 新的主开放问题是 Q-0016（因果 incidence 再生与集中）和 Q-0017（persistent-blocker 临界正常形）。
- 所有枚举脚本、JSON 输出和报告统一放入 `enumerate/`；后续机器结果不得散落根目录。
