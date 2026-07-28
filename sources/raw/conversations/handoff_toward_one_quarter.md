---
title: "Handout：迈向 1/4 的下一步"
subtitle: "单缺陷修复、link 稳定性与二进制强迫森林"
date: "2026-07-24"
lang: zh-CN
---

# 使用说明

本文是一份自足研究交接稿。只阅读本文，读者应能够：

1. 理解三一致分块超图独立横截问题及目标常数 \(1/4\)；
2. 复核当前已经完成的解析归约与有限枚举；
3. 明确区分：
   - \(3/20\) 路线内部的唯一 Gap；
   - 通往 \(1/4\) 尚需建立的全新结构定理；
4. 理解为什么继续细分 atlas、相位、锚谱系或十八块核心不会自动推进 \(1/4\)；
5. 直接开始下一项工作：建立**单缺陷可逆修复定理**，并以 link 稳定性和二进制强迫森林作为其结构证明。

本文接受研究项目中的目标常数 \(1/4\)。现有材料没有在同一份手稿中完整复核锐性构造，因此本文集中讨论下界证明，不把“锐性已在本文证明”列为结论。

## 状态标签

- **[A-PROVED]**：正文给出解析证明。
- **[M-PROVED]**：有限命题由精确枚举核验；复核程序收入附录。
- **[INPUT]**：作为已知定理输入，本文不重新证明。
- **[FALSE]**：已有反模型否定。
- **[OPEN-3/20]**：只属于 \(3/20\) 证明路线的开放命题。
- **[OPEN-1/4]**：通往 \(1/4\) 的真正开放任务。
- **[PROPOSED]**：建议采用的下一步定理或研究框架。

# 0. 执行摘要：下一步究竟是什么

核心判断是：

\[
\boxed{
\text{通往 }1/4\text{ 的下一步，不是继续细分 }3/20\text{ 的 atlas Gap。}
}
\]

应当转而证明一个全局的、近乎无损的**单缺陷可逆修复定理**：

> 每个失败扩张 \(\{x,u,v\}\) 中，只释放 \(u,v\) 的一个端点，保留另一个端点为唯一活动 pivot；所有历史在真实边容量下可逆粘合，使阻断尝试总数按
> \[
> \Delta\,A_{k-2}
> \]
> 而不是
> \[
> b\Delta\,A_{k-3}
> \]
> 计数。

若这一点成立，就得到理想递推

\[
A_k\ge bA_{k-1}-(1+o(1))\Delta A_{k-2},
\]

其临界常数正是 \(1/4\)。

现有四块 \(\mathcal T_4\) 枚举的正确用途是：

\[
\boxed{
\text{检验单缺陷 pivot 在交换方块上的局部相容性，}
}
\]

而不是继续为 residual 增加更多收费类型。

整个 \(1/4\) 项目应压缩为三项结构任务：

1. **link 稳定性**：极小失败中的 blocker link 必须接近平衡完全二部图；
2. **全局粘合**：局部二分和 pivot 方向在重叠窗口上能够一致定向；
3. **二进制强迫森林终局**：一致的 link 圆柱若无增广出口，就迫使某个 pivot 的次数达到 \((1/4-o(1))b^2\)，或产生完整真子无 IT 核心。

# 1. 问题、记号与目标

设 \(H\) 是三一致分块超图：

\[
V(H)=B_1\sqcup\cdots\sqcup B_m,
\qquad |B_i|=b.
\]

每条边交三个不同块。完整横截是集合

\[
T=\{x_1,\ldots,x_m\},
\qquad x_i\in B_i.
\]

若 \(T\) 不含 \(H\) 的边，则称 \(T\) 为独立横截，记作 IT。

定义

\[
d_H(v)=|\{e\in E(H):v\in e\}|,
\qquad
\Delta(H)=\max_v d_H(v).
\]

目标为证明渐近界

\[
\boxed{
H\text{ 无 IT}
\Longrightarrow
\Delta(H)\ge
\left(\frac14-o(1)\right)b^2.
}
\tag{1.1}
\]

为便于记号，写

\[
q=\frac{\Delta(H)}{b^2}.
\]

## 1.1 块极小化

### 引理 1.1　块极小反例

若存在无 IT 的实例，则存在一个由部分完整块诱导的无 IT 实例 \(H'\)，删除任意一个块后均有 IT。

### 证明

在所有无 IT 的完整块子系统中取块数最少者。若删除某块后仍无 IT，则得到块数更少的无 IT 完整块子系统，矛盾。 \(\square\)

**状态：[A-PROVED]**

块极小性只能用于由完整真实块构成的子实例；代码簿、相位轨道和部分顶点支持不能直接称为真子实例。

# 2. 已完成的解析骨架

## 2.1 中位 Ferrers 源

固定确定性块顺序。对独立部分横截 \(T\)，令 \(B(T)\) 是下一块，并定义坏点集

\[
D(T)=
\{x\in B(T):T\cup\{x\}\text{ 不独立}\},
\qquad
t(T)=|D(T)|.
\]

令

\[
h=\left\lfloor\frac b2\right\rfloor.
\]

取深度最大的独立状态 \(T_\star\)，满足 \(t(T_\star)\le h\)。写

\[
i=t(T_\star),
\qquad
C=B(T_\star)\setminus D(T_\star).
\]

对 \(x\in C\)，最大深度性给出

\[
j_x=t(T_\star\cup\{x\})\ge h+1.
\]

定义真实阻塞义务总质量

\[
W=i+\sum_{x\in C}j_x.
\]

令

\[
D_b=b+\left\lfloor\frac{b^2}{4}\right\rfloor.
\]

### 定理 2.1　中位质量恒等式

\[
\boxed{
W-D_b
=
h(h-i)+
\sum_{x\in C}\bigl(j_x-(h+1)\bigr).
}
\tag{2.1}
\]

特别地，

\[
W\ge D_b
=
\left(\frac14+o(1)\right)b^2.
\tag{2.2}
\]

### 证明

由 \(|C|=b-i\)，

\[
W=i+(b-i)(h+1)
+\sum_{x\in C}(j_x-(h+1)).
\]

只需验证

\[
i+(b-i)(h+1)-D_b=h(h-i).
\]

若 \(b=2h\)，左端为

\[
i+(2h-i)(h+1)-(2h+h^2)=h(h-i).
\]

若 \(b=2h+1\)，左端为

\[
i+(2h+1-i)(h+1)-(h^2+3h+1)=h(h-i).
\]

故结论成立。 \(\square\)

**状态：[A-PROVED]**

## 2.2 真实边单位容量与加权 Hall

每条真实边 \(e\) 只有一份单位容量。历史分裂、条件化、图表抽取和状态复制不得增加容量。

设义务集合为 \(A\)，义务 \(a\) 的质量为 \(w(a)\)，可认证它的真实边集合为 \(\mathcal E(a)\)，边 \(e\) 的剩余容量为 \(c(e)\in[0,1]\)。认证流 \(x(a,e)\) 满足

\[
\sum_e x(a,e)=w(a),
\qquad
\sum_a x(a,e)\le c(e).
\]

### 定理 2.2　加权 Hall–最大流判据

满流存在，当且仅当对每个 \(U\subseteq A\)，

\[
\boxed{
\sum_{a\in U}w(a)
\le
\sum_{e\in N(U)}c(e),
}
\tag{2.3}
\]

其中 \(N(U)=\bigcup_{a\in U}\mathcal E(a)\)。

### 证明

建立网络：

- 源点到义务 \(a\) 的容量为 \(w(a)\)；
- \(a\to e\) 为无限容量，当 \(e\in\mathcal E(a)\)；
- \(e\) 到汇点容量为 \(c(e)\)。

最大流最小割定理给出的割约束正是 (2.3)。 \(\square\)

**状态：[A-PROVED]**

## 2.3 \(4/27\) 基准与完整 residual

已知基准定理给出

\[
\Delta(H)\ge
\left(\frac4{27}-o(1)\right)b^2.
\tag{2.4}
\]

**状态：[INPUT]**

从一个基准顶点的真实星中预留

\[
K_b=
\left(\frac4{27}-o(1)\right)b^2
\]

条不同真实边后，中位源留下的 residual 至少为

\[
G_b
\ge
D_b-K_b
=
\left(\frac{11}{108}-o(1)\right)b^2.
\tag{2.5}
\]

关键恒等式为

\[
\boxed{
\frac14-\frac4{27}
=
\frac{11}{108}.
}
\tag{2.6}
\]

所以在“基准星 + residual 收费”的框架中，达到 \(1/4\) 需要以 \(1-o(1)\) 的效率处理全部 residual。任何固定比例的 repair、边界、sector、非刚性或重复计数损失都会留下严格低于 \(1/4\) 的常数。

这解释了为什么 \(1/4\) 不是把 \(3/20\) 的捕获比例 \(1/55\) 略微提高，而是需要新的等号结构定理。

# 3. 四块局部结构与精确枚举

## 3.1 干净微立方体产生坐标完美匹配

在四个活动块中各抽取两个候选，得到

\[
Q_4=\{0,1\}^4.
\]

若每个角点有唯一第一认证边，并剥离外部锚、竞争认证、配置冲突和真实边界等异常，则每个角点 \(\varepsilon\) 有唯一遗漏方向

\[
d(\varepsilon)\in\{0,1,2,3\}.
\]

若 \(d(\varepsilon)=r\)，翻转第 \(r\) 位不改变该认证边的三个真实端点。因此

\[
d(\varepsilon)
=
d(\varepsilon\oplus e_r),
\]

十六个角点被配成八条坐标边。这是 \(Q_4\) 的坐标完美匹配。

**状态：[A-PROVED]**

## 3.2 枚举结果

坐标完美匹配总数为

\[
\boxed{272}.
\]

一个匹配称为正常，当每个二维面恰好出现三个匹配方向。正常带标号匹配总数为

\[
\boxed{8}.
\]

对二维面 \(F\)，定义共同锚指标

\[
a_F(M)
=
\mathbf1\{
|d_M(F)|\le2,\ 
J(F)\nsubseteq d_M(F)
\}.
\]

若 \(a_F(M)=1\)，则面上四个角点的全部认证边含有同一个固定真实顶点。

枚举直方图为：

| 共同锚面数 \(\sum_Fa_F(M)\) | 0 | 9 | 15 | 16 | 20 | 24 |
|---:|---:|---:|---:|---:|---:|---:|
| 匹配数 | 8 | 32 | 96 | 48 | 84 | 4 |

因此：

\[
\boxed{
M\text{ 非正常}
\Longrightarrow
\sum_Fa_F(M)\ge9.
}
\tag{3.1}
\]

这给出逐点证书

\[
\mathbf1_{\{M\text{ 非正常}\}}
\le
\frac19\sum_Fa_F(M).
\tag{3.2}
\]

**状态：[M-PROVED]**

## 3.3 八个相位的显式形式

令 \(x=(x_0,x_1,x_2,x_3)\in\mathbf F_2^4\)，定义

\[
\delta_\ast(x)=
\begin{cases}
0,&x_1=x_2=x_3,\\
1,&x_0=x_2\ne x_3,\\
2,&x_0=x_3\ne x_1,\\
3,&x_0=x_1\ne x_2.
\end{cases}
\tag{3.3}
\]

由条件不依赖 \(x_{\delta_\ast(x)}\)，它定义一个坐标完美匹配 \(M_\ast\)。

对 \(a\in\mathbf F_2^4\)，令

\[
M_a=a+M_\ast.
\]

同时翻转四位不改变等式和不等式，因此

\[
M_{a+1111}=M_a.
\]

平移稳定子恰为 \(\langle1111\rangle\)，故八个相位由

\[
P=\mathbf F_2^4/\langle1111\rangle
\cong\mathbf F_2^3
\]

参数化。

## 3.4 图册层的已知结论

把 \(\mathcal T_4\) 看作带坐标方向、二维面和匹配结构的对象，其坐标仿射自同构群稳定子 \(G\) 满足

\[
|G|=48.
\]

在固定刚性交叠 nerve \(N\) 上，抽象图册由 \(G\)-值 cocycle 按 gauge 等价分类；若 \(N\) 连通，则可写成

\[
\operatorname{Hom}(\pi_1(|N|),G)/G.
\]

这些结论只分类局部坐标怎样粘合，不分类真实支持。

## 3.5 两个决定性反模型

### 无损 monodromy

沿闭环使用相位集上的测度保持置换，可以产生非平凡 holonomy，同时：

- 无信息擦除；
- 无边容量消耗；
- 无局部 cocycle 缺陷。

因此

\[
\boxed{
\text{非平凡 monodromy}
\not\Rightarrow
\text{真实费用}.
}
\]

**状态：[FALSE]**

### 对角代码簿

在两个块 \(B=C=[b]\) 上取支持

\[
\mathscr S=\{(i,i):i\in[b]\}.
\]

局部相位坐标可以完全一致，但支持不是笛卡尔积。因此

\[
\boxed{
\text{全局一致相位}
\not\Rightarrow
\text{真实支持乘积化}.
}
\]

**状态：[FALSE]**

结论：\(\mathcal T_4\) 枚举是必要的局部相容性工具，但不能单独给出 \(1/4\) 的全局定理。

# 4. \(3/20\) 路线的真实状态，以及它与 \(1/4\) 的区别

## 4.1 \(3/20\) 路线内部的唯一 Gap

在已有 handout 的记账体系内部，唯一开放命题是：

\[
\operatorname{ExtDef}(\mathscr C)
\le
C\,\operatorname{Credit}(\mathscr C),
\tag{4.1}
\]

即正常图册若遗漏合法混合扩张，该遗漏必须产生真实边、复用、锚、擦除、宽度、配置或边界费用。

这确实是该 **\(3/20\) 管线内部**的唯一 Gap。

**状态：[OPEN-3/20]**

但它不是 \(1/4\) 的唯一 Gap。即使 (4.1) 以某个固定常数成立，也只保证捕获固定比例 residual；达到 \(1/4\) 需要近乎无损的结构化递归。

## 4.2 十八块来自哪里

有限整数覆盖分析给出：在度数严格低于 \(3b^2/20\) 时，至多十七个内部块的 sector 可由随机横截平均直接控制。第一个可能逃逸的规模是十八块。

因此“十八块核心迁移”是 \(3/20\) 路线特有的临界对象；\(1/4\) 的本质结构不是数字十八，而是：

\[
\boxed{
\text{一条三边中的两个旧端点，能否被压缩成一个活动缺陷。}
}
\]

## 4.3 固定核心的全局次数定理

设固定内部核心 \(C\) 有 \(s\) 个块，\(Y\) 是外部块中的顶点集合，

\[
|Y|=\lambda b.
\]

令 \(F=H[C]\)，其独立横截集密度为 \(u\)。假设每个 \(y\in Y\) 和每个 \(T\in\operatorname{IT}(F)\) 都由一条真实边 \(\{y,v,w\}\) 阻断，其中 \(v,w\in T\)。

记：

- \(E_3\)：\(C\) 内部三边；
- \(E_2\)：一个端点在 \(Y\)、两个端点在 \(C\) 的边。

内部三边覆盖非独立横截，所以

\[
|E_3|\ge(1-u)b^3.
\tag{4.2}
\]

外部义务对数量为 \(\lambda u b^{s+1}\)，每条 \(E_2\) 边覆盖 \(b^{s-2}\) 个义务，故

\[
|E_2|\ge\lambda u b^3.
\tag{4.3}
\]

对核心中的顶点求次数和：

\[
3|E_3|+2|E_2|
\le sqb^3,
\]

从而

\[
3(1-u)+2\lambda u\le sq.
\tag{4.4}
\]

对 \(Y\) 中顶点求次数和，得到 \(u\le q\)。代入 (4.4)：

\[
\boxed{
q\ge\frac3{s+3-2\lambda}.
}
\tag{4.5}
\]

特别地：

| \(s\) | \(\lambda\) | 结论 |
|---:|---:|---:|
| 18 | \(0\) | \(q\ge1/7\) |
| 18 | \(1/2\) | \(q\ge3/20\) |
| 18 | \(1\) | \(q\ge3/19\) |

所以固定十八块核心若服务至少半个外部块，不可能成为 \(3/20\) 反例。

**状态：[A-PROVED]**

## 4.4 支撑完全分散也不可能

若对每个外部顶点 \(y\)，覆盖事件 \(A_y\) 只依赖坐标集 \(C_y\)，且

\[
\mu(A_y)\le q,
\qquad
U\subseteq\bigcap_yA_y,
\]

设任一内部块最多出现在 \(r\) 个 \(C_y\) 中。重复应用 Hölder/Finner 不等式得

\[
\mu(U)
\le
q^{b/r}.
\tag{4.6}
\]

因此

\[
\frac rb
\ge
\frac{\log(1/q)}{\log(1/\mu(U))}.
\tag{4.7}
\]

在 \(q=3/20\)、\(\mu(U)\approx1/10\) 时，

\[
\frac rb\gtrsim0.824.
\]

所以可能的十八块反例必须高度共享坐标，而不能完全分散。

## 4.5 迁移坐标的精确构造及其失败

令 \(b\) 为素数幂，所有内部块标号为 \(\mathbf F_b\)。取映射

\[
\phi:\mathbf F_b\to\{1,\ldots,17\},
\]

以及集合 \(S_a\subseteq\mathbf F_b\)，\(|S_a|=\rho b\)。定义

\[
U=
\{x:x_{\phi(x_0)}\in S_{x_0}\}.
\tag{4.8}
\]

对每个外部顶点 \(y\)，加入 pair 边

\[
\{y,(0,a),(\phi(a),s)\},
\qquad s\in S_a.
\]

对 \(s\notin S_a\)，选 \(\psi(a,s)\ne\phi(a)\)，加入内部三边

\[
\{(0,a),(\phi(a),s),(\psi(a,s),t)\},
\qquad t\in\mathbf F_b.
\]

则 pair 柱面精确分割 \(U\)，triple 柱面精确分割 \(U^c\)，活动坐标对

\[
\{0,\phi(x_0)\}
\]

随状态迁移，且刷新其他坐标不改变 \(U\)。

但固定根顶点 \((0,a)\) 的次数为

\[
\rho b^2+(1-\rho)b^2=b^2.
\tag{4.9}
\]

所以局部迁移完全可实现；失败来自全局真实次数，而不是组合定义矛盾。

## 4.6 一个必须保留的逻辑警告

由“小覆盖浪费”可以得到：

> 每个状态的刷新边界大多被某两个状态依赖坐标遮蔽。

不能推出：

> 存在固定两个坐标遮蔽大多数状态。

迁移构造 (4.8) 是明确反例。Efron–Stein 控制总影响，却不会把状态依赖方向自动圆整成固定坐标。

同样，高支撑重叠不能推出完全相同的十八块核心；例如

\[
C_y=\{1,\ldots,17\}\cup\{17+y\}
\]

有十七个公共块，却没有两个核心相同。

# 5. 有限计算与枚举的诊断信息

本节结果用于识别结构，不构成一般渐近证明。

## 5.1 小规模整数 MILP

有限模型同时选择真实超边变量 \(h_e\in\{0,1\}\) 和 pair 权重，检验在给定最大度下是否能违反 \(3/20\) 对偶阈值。

已报告的完整不可行实例：

| 其余块数 \(n\) | 块大小 \(b\) | 整数度数上界 \(D\) | 超边变量数 | 横截约束数 | 结论 |
|---:|---:|---:|---:|---:|---|
| 4 | 4 | 2 | 256 | 256 | 严格违反不可行 |
| 5 | 4 | 2 | 640 | 1024 | 严格违反不可行 |
| 4 | 5 | 3 | 500 | 625 | 严格违反不可行 |
| 4 | 6 | 5 | 864 | 1296 | 严格违反不可行 |
| 5 | 5 | 3 | 1250 | 3125 | 等号也不可行 |
| 5 | 6 | 5 | 2160 | 7776 | 等号也不可行 |

较小规模的精确最优值：

| \(n\) | \(b\) | \(D\) | 最坏对偶值 |
|---:|---:|---:|---:|
| 3 | 3 | 1 | \(1/9\) |
| 4 | 3 | 1 | \(1/9\) |
| 5 | 3 | 1 | \(1/9\) |
| 3 | 4 | 2 | \(1/16\) |

这些值等于均匀二块 pair 权重 \(1/b^2\)。

**状态：历史完整 MILP 报告；本文未重新运行全部求解。**

## 5.2 \(n=4,b=3\) 的完整见证枚举

| 项目 | 数量 |
|---|---:|
| 横截数 | 81 |
| maximal clique | 783 |
| 大小为 4 的 maximal clique | 648 |
| 大小为 9 的 maximal clique | 135 |
| 检查的候选子族 | 57,510 |
| inclusion-minimal 无公共 pair 子族 | 2,592 |
| 每个最小子族的横截数 | 3 |
| fractional matching 值 | \(3/2\) |

而 \(3/20\) 违反需要

\[
\nu^\ast<\frac{27}{20}=1.35.
\]

由于 \(3/2>27/20\)，该有限规模中的失败证书必须有公共 pair。

## 5.3 连续松弛为何不够

把 \(h_e\) 放松到 \([0,1]\) 后，平均计算给出精确值

\[
\lambda_{\mathrm{frac}}(n,b)
=
\frac{1+nD/3}{b^2}.
\tag{5.1}
\]

它满足目标仅当

\[
nD\le17.
\]

首次可能失败的位置：

| \(b\) | \(D\) | 首次失败的 \(n\) |
|---:|---:|---:|
| 3 | 1 | 18 |
| 4 | 2 | 9 |
| 5 | 3 | 6 |
| 6 | 5 | 4 |
| 7 | 7 | 3 |
| 8 | 9 | 2 |

结论是：

\[
\boxed{
\text{真实超边的整数性和单位容量是结构核心，}
}
\]

普通 fractional LP 会允许无结构的多块扩散。

对 \(1/4\) 项目而言，这意味着：继续扩大有限 LP，除非先证明“失败具有有界整数见证”，否则不能取代全局结构定理。

# 6. 对 Gap 的最终审计

## 6.1 对 \(3/20\)

在既定 handout 管线中，以下链条已闭合：

- 中位源；
- 真实边容量；
- 四块二元化；
- \(Q_4\) 枚举；
- 带权修复；
- 刚性 atlas；
- 遗传扩张完整时的 IT/真子核心终局。

只剩图册扩张缺陷收费 (4.1)。

因此“唯一 Gap”这一说法对 **该特定 \(3/20\) 证明框架**成立。

## 6.2 对 \(1/4\)

对 \(1/4\)，至少有三个尚未建立的桥梁：

1. **单缺陷降秩**：把三边阻断的两个旧端点压缩为一个活动 pivot；
2. **全局 pivot 相容性**：局部交换方块的八相位能够粘成不重复消耗真实边的全局修复；
3. **无出口终局**：终端可逆组件必须成为平衡二部 link 圆柱/二进制强迫森林，并迫使次数 \(1/4\)，或给出真子核心。

所以：

\[
\boxed{
\text{“十八块核心能否迁移”不是 }1/4\text{ 的唯一 Gap。}
}
\]

它只是 \(3/20\) sector 路线在末端出现的一种具体障碍。

# 7. 建议的主定理：单缺陷可逆修复

## 7.1 单缺陷搜索方案

固定块顺序。一个单缺陷搜索方案包含：

- \(\mathcal S_k\)：已稳定的独立部分横截状态，每个状态选择前 \(k\) 个块；
- \(\mathcal D_k\)：活动缺陷状态；
- 每个 \(D\in\mathcal D_k\) 有：
  - 唯一 pivot \(p(D)\)；
  - 唯一缺失块；
  - 一个投影 \(\pi(D)\in\mathcal S_{k-2}\)；
- 每个从 \(\mathcal S_{k-1}\) 出发的失败扩张，被分配给一个 \(D\) 和一条含 \(p(D)\) 的真实阻断边；
- 同一真实边容量只使用一次；
- 投影 \(\pi\) 的总重数接近 \(1\)。

理想计数为

\[
|\mathcal B_k|
\le
\Delta(H)\,|\mathcal S_{k-2}|,
\tag{7.1}
\]

其中 \(\mathcal B_k\) 是第 \(k\) 步失败扩张集。

允许固定 \(\varepsilon>0\) 的稳定误差时，目标是

\[
|\mathcal B_k|
\le
(1+\gamma)\Delta(H)\,|\mathcal S_{k-2}|,
\tag{7.2}
\]

并要求

\[
(1+\gamma)\left(\frac14-\varepsilon\right)<\frac14.
\tag{7.3}
\]

## 7.2 为什么它直接推出 \(1/4-\varepsilon\)

令

\[
A_k=|\mathcal S_k|.
\]

每个稳定状态有 \(b\) 个下一块尝试，故

\[
A_k
\ge
bA_{k-1}-|\mathcal B_k|.
\]

由 (7.2)：

\[
A_k
\ge
bA_{k-1}-(1+\gamma)\Delta A_{k-2}.
\tag{7.4}
\]

令

\[
c=\frac{(1+\gamma)\Delta}{b^2}<\frac14,
\qquad
r_k=\frac{A_k}{bA_{k-1}}.
\]

只要 \(A_{k-1}>0\)，式 (7.4) 给出

\[
r_k
\ge
1-\frac{c}{r_{k-1}}.
\tag{7.5}
\]

方程

\[
r=1-\frac cr
\]

的较大根为

\[
r_+
=
\frac{1+\sqrt{1-4c}}2>0.
\]

初值 \(r_1=1\ge r_+\)。函数 \(f(r)=1-c/r\) 在正数上递增，故归纳得到

\[
r_k\ge r_+
\quad\text{对所有 }k.
\]

于是 \(A_k>0\)，最终 \(A_m>0\)，即存在 IT。

因此：

### 定理 7.1　条件闭合

若对每个固定 \(\varepsilon>0\) 能构造满足 (7.2)–(7.3) 的单缺陷搜索方案，则

\[
\Delta(H)
\le
\left(\frac14-\varepsilon\right)b^2
\Longrightarrow
H\text{ 有 IT}.
\]

**状态：[A-PROVED，条件于搜索方案存在]**

这给出了一个明确的验收接口：下一步工作不需要直接证明整个 \(1/4\)，只需证明搜索方案的存在。

# 8. 如何证明单缺陷定理：三项结构引理

## 8.1 引理 A：critical link 稳定性

对 pivot \(p\)，link 图为

\[
L_H(p):
\quad
uv\in E(L_H(p))
\iff
\{p,u,v\}\in E(H).
\]

活动缺陷在 pivot 固定期间，只在 \(L_H(p)\) 中移动。

### 待证命题 A

对每个 \(\varepsilon>0\)，存在 \(\delta>0\)，使块极小无 IT 实例若满足

\[
\Delta(H)\le
\left(\frac14-\varepsilon\right)b^2,
\]

则每个承载正比例失败质量的 terminal link 组件至少满足一项：

1. 有增广出口；
2. 产生 \(\delta b^2\) 个可区分的真实边/复用费用；
3. link 在两个相关块上 \(\delta\)-接近平衡完全二部图
   \[
   K_{A,C},
   \qquad
   |A|,|C|=\left(\frac12+O(\delta)\right)b.
   \]

第三种是近等号结构；前两种提供修复或严格余量。

**状态：[OPEN-1/4]**

## 8.2 引理 B：四块相位的全局粘合

在两个连续缺陷移动可交换的四块窗口中，局部 pivot 方向形成 \(Q_4\) 坐标完美匹配。

- 非正常匹配至少有九个共同锚面，可通过真实 pivot/边容量产生正比例异常；
- 正常匹配只有八个相位。

### 待证命题 B

在剥离 \(O(\delta)\) 异常后，正常交换方块的 pivot 选择可以全局定向，使：

1. 同一真实边不因不同图表重复使用；
2. defect 投影 \(\pi:\mathcal D_k\to\mathcal S_{k-2}\) 的平均重数至多 \(1+O(\delta)\)；
3. 任意闭路若产生非平凡 phase monodromy，仍保留真实 pivot genealogy，而不是只记录相位名称。

**状态：[OPEN-1/4]**

这里必须使用真实边身份和 pivot 谱系；纯 cocycle 不够。

## 8.3 引理 C：二进制强迫森林终局

假设 terminal defect 组件：

- 无增广出口；
- 所有局部交换方块正常；
- 真实边容量无重复；
- links 都接近平衡二部图。

### 待证命题 C

该组件至少满足一项：

1. 存在完整真子块系统仍无 IT；
2. 存在顶点 \(p\) 及两个活动块中的集合 \(A,C\)，使
   \[
   A\times C\subseteq L_H(p),
   \]
   且
   \[
   |A||C|
   \ge
   \left(\frac14-o(1)\right)b^2;
   \]
3. 存在可继续增广的叶状态。

第二项立即给出

\[
d_H(p)\ge
\left(\frac14-o(1)\right)b^2.
\]

结构上，这个 terminal 组件应当是一棵或森林状的二进制 genealogy：每次阻断把一个活动缺陷分成两个近半集分支；若没有叶出口，根 pivot 必须看见两个半集的完整乘积。

**状态：[OPEN-1/4]**

# 9. 拓扑 Hall 的辅助版本

令 \(\operatorname{Ind}(F)\) 为超图 \(F\) 的独立复形。对单纯复形 \(K\)，写

\[
\eta(K)=\operatorname{conn}(K)+2,
\]

其中 \(\operatorname{conn}(K)\) 是最大整数 \(t\)，使 \(K\) 为 \(t\)-连通。

标准拓扑 Hall/Rado 准则的形式是：

> 若对每个块指标集合 \(J\)，
> \[
> \eta\!\left(
> \operatorname{Ind}\left(H\left[\bigcup_{j\in J}B_j\right]\right)
> \right)
> \ge |J|,
> \]
> 则存在独立横截。

该工具可用于证明引理 A：选择一个最小违反拓扑 Hall 的块子系统，分析顶点 link。对 \(v\in V(H)\)，

\[
\operatorname{lk}_{\operatorname{Ind}(H)}(v)
\]

对应一个混合秩 \(2/3\) 的约束系统：

- 含 \(v\) 的三边变为 link 图边；
- 不含 \(v\) 的三边仍为三边。

因此自然的归纳链是

\[
3\text{-uniform}
\longrightarrow
(2,3)\text{-mixed links}
\longrightarrow
\text{graph link stability}.
\]

一个高风险但概念清晰的目标是证明某种连通度下界

\[
\eta(\operatorname{Ind}(F))
\gtrsim
\frac{|V(F)|}{2\sqrt{\Delta(F)}}.
\]

若对当前 stretched multipartite 类成立，它会直接导出 \(1/4\)。本文不把这一不等式列为已知事实；它是拓扑路线的研究猜想。

# 10. 立即执行的工作包

## 工作包 1：冻结单缺陷状态空间

只允许以下数据进入状态：

\[
(\text{真实部分横截},\ \text{唯一 pivot},\ \text{唯一缺失块},\ \text{第一真实阻断边}).
\]

不得再引入抽象 footprint、额外 sheet 或不可审计的历史标签，除非能够证明它们对投影重数 (7.2) 必不可少。

**交付标准：**

1. 给出 \(\mathcal S_k,\mathcal D_k,\pi\) 的严格定义；
2. 证明所有失败扩张质量守恒；
3. 证明真实边容量至多一；
4. 把唯一未证目标写成投影重数
   \[
   \operatorname{mult}(\pi)\le1+\gamma.
   \]

## 工作包 2：建立 terminal defect graph

顶点是活动缺陷状态，边是一次“保留 pivot、释放另一个旧端点”的修复。

需要记录：

- pivot 是否继承；
- 缺失块怎样移动；
- 使用的真实阻断边；
- 四块交换方块的相位。

**交付标准：**

证明每个有限 terminal 强连通分量满足：

\[
\text{增广出口}
\quad\text{或}\quad
\text{link 圆柱}
\quad\text{或}\quad
\text{真子核心}.
\]

这就是引理 A–C 的统一图论形式。

## 工作包 3：先做零误差分类

先假设：

- 每个交换方块都正常；
- 无竞争认证；
- 无边界；
- 无真实边复用；
- 所有 link 恰为完全二部图。

在该精确模型中分类 terminal SCC。

目标不是继续枚举相位，而是证明：

\[
\boxed{
\text{精确 terminal SCC 是二进制强迫森林或完整子核心。}
}
\]

若零误差版本不能证明，应立即寻找真实反模型；不要进入定量稳定性。

## 工作包 4：固定 \(\varepsilon\) 的稳定化

零误差分类完成后，再使用：

- 非正常匹配的九面共同锚证书；
- 最大度与 link 边数预算；
- 真实边单位容量；
- 三向刷新守恒；
- 图稳定性；

把异常质量控制为 \(\gamma(\varepsilon)\)，并确保

\[
(1+\gamma(\varepsilon))
\left(\frac14-\varepsilon\right)
<
\frac14.
\]

## 工作包 5：最后处理 \(\varepsilon\to0\)

证明近等号实例距离二进制强迫森林只有 \(o(b^2)\) 的局部误差；然后：

- 严格低于 \(1/4\) 时出现增广出口；
- 接近 \(1/4\) 时分类近极端结构。

# 11. 明确停止的方向

除非出现新的全局不变量，不建议继续以下工作：

1. **继续细分 atlas 类型。** 八相位和刚性 cocycle 已经足够描述局部交换。
2. **仅凭 bounded width 推熵损失。** 宽度 \(2\) 的固定轻锚代码簿可以零熵闭环。
3. **把条件化当作势能下降。** 保留纤维标签时，链式法则给出零真实信息损失。
4. **用 monodromy 自动收费。** 非平凡置换可以完全可逆。
5. **从状态依赖的两个好坐标推出固定坐标。** 迁移构造否定这一推理。
6. **继续扩大有限 LP 而没有有限见证定理。** fractional 模型会无结构扩散；整数 MILP 的小规模不可行不能自动推广。
7. **把十八块核心迁移称为 \(1/4\) 的唯一 Gap。** 十八是 \(3/20\) 的 sector 阈值，不是 \(1/4\) 的本征常数。

# 12. 完整状态表

| 结论 | 状态 | 对 \(1/4\) 的作用 |
|---|---|---|
| 块极小化 | [A-PROVED] | 允许终局递归 |
| 中位源 \(W\ge b+\lfloor b^2/4\rfloor\) | [A-PROVED] | 解释目标尺度 |
| 真实边容量与加权 Hall | [A-PROVED] | 防止历史重复计数 |
| \(4/27\) 基准 | [INPUT] | 给出全部 residual \(11/108\) |
| \(Q_4\) 坐标匹配化 | [A-PROVED] | 局部 pivot 交换 |
| 坐标匹配数 272 | [M-PROVED] | 完整局部样本空间 |
| 正常模板数 8 | [M-PROVED] | 局部相位有限 |
| 非正常至少九个共同锚面 | [M-PROVED] | 定量异常证书 |
| 刚性 atlas/cocycle | [A-PROVED] | 局部粘合语言 |
| monodromy 自动收费 | [FALSE] | 必须记录真实 pivot |
| 相位一致自动乘积化 | [FALSE] | 必须使用真实支持 |
| \(3/20\) ExtDef–Credit | [OPEN-3/20] | 不足以直接到 \(1/4\) |
| 固定十八块核心次数界 | [A-PROVED] | 排除窄 sector |
| 支撑完全分散 | [A-PROVED，在低秩事件模型] | Finner 强迫高共享 |
| 状态依赖坐标可固定化 | [FALSE] | 迁移构造反例 |
| 单缺陷可逆修复 | [OPEN-1/4] | 主计数接口 |
| critical link 稳定性 | [OPEN-1/4] | 产生平衡二部结构 |
| pivot 全局粘合 | [OPEN-1/4] | 控制投影重数 |
| 二进制强迫森林终局 | [OPEN-1/4] | 达到 \(1/4\) 次数 |

# 13. 下一位研究者的检查清单

开始新工作前，应逐项确认：

1. 所有状态是否来自原超图真实部分横截？
2. 每个失败扩张是否保留第一真实阻断边？
3. 同一真实边是否只消耗一次容量？
4. 活动缺陷是否始终只有一个 pivot 和一个缺失块？
5. 四块交换是否调用了完整 \(272/8/9\) 枚举，而非假设局部唯一？
6. 闭路中是否记录真实 pivot genealogy，而非仅记录相位？
7. terminal SCC 的每个分支是否明确产生：
   - 增广；
   - \(1/4\) link 负载；
   - 或完整真子无 IT 核心？
8. 所有定量损失是否进入 \(\gamma(\varepsilon)\)，并验证
   \[
   (1+\gamma)(1/4-\varepsilon)<1/4?
   \]
9. 是否避免从平均边界直接推出固定坐标？
10. 是否避免把一个局部有限枚举误当作全局有限见证定理？

# 14. 推荐的第一条待证命题

为了避免再次无限细分，建议立即集中于下面一条命题。

## Terminal defect SCC 定理

对每个 \(\varepsilon>0\)，存在 \(\delta>0\)，使得当

\[
\Delta(H)\le
\left(\frac14-\varepsilon\right)b^2
\]

且 \(H\) 块极小时，任意满足下列条件的 terminal 单缺陷 SCC：

1. 状态只含真实部分横截、唯一 pivot、唯一缺失块和第一阻断边；
2. 同一真实边容量至多一；
3. 除去至多 \(\delta\) 的质量，所有四块交换窗口属于八个正常 \(\mathcal T_4\) 相位；
4. 每步只释放阻断边的一个旧端点；

必有以下至少一项：

必有以下至少一项：

1. 存在增广出口；
2. 存在完整真子无 IT 块系统；
3. 存在 \(p,A,C\)，使
   \[
   A\times C\subseteq L_H(p),
   \qquad
   |A||C|\ge
   \left(\frac14-\frac{\varepsilon}{2}\right)b^2.
   \tag{14.1}
   \]

第三项与最大度假设矛盾。第一项使搜索继续，第二项与块极小性矛盾。因此 terminal SCC 不存在，单缺陷搜索必能完成。

这条定理不是问题的重新翻译：它把所需输出固定为一个具体 link 乘积 \(A\times C\)，并把局部输入固定为现有的 \(\mathcal T_4\) 枚举。证明若失败，失败对象就是一个明确的真实 defect SCC，可直接用于构造反例。

# 15. 最终结论

现有研究已经完成：

\[
\boxed{
\text{中位源}
+\text{真实容量}
+\text{四块局部分类}
+\text{atlas 语言}.
}
\]

这些结果足以把 \(3/20\) 压缩到一个扩张缺陷收费问题，但不足以把常数推进到 \(1/4\)。

通往 \(1/4\) 的正确下一步是：

\[
\boxed{
\text{证明单缺陷可逆修复，}
}
\]

其结构核心是：

\[
\boxed{
\text{critical link 稳定性}
+\text{pivot 全局粘合}
+\text{二进制强迫森林终局}.
}
\]

第一项应执行的具体命题是第 14 节的 Terminal defect SCC 定理。只有在其零误差版本被证明或被真实反模型否定后，才应继续做定量稳定化。

\newpage

# 附录 A：\(Q_4\) 枚举复核程序

下面程序只使用 Python 标准库，独立复核：

- 坐标完美匹配总数 \(272\)；
- 正常带标号匹配总数 \(8\)；
- 共同锚面直方图；
- 非正常匹配最少九个共同锚面。

```python
from itertools import combinations, product
from collections import Counter

D = 4
V = tuple(range(1 << D))

def neighbors(x):
    return [(x ^ (1 << d), d) for d in range(D)]

def enumerate_matchings():
    ans = []

    def rec(unmatched, edges):
        if not unmatched:
            ans.append(tuple(sorted(edges)))
            return

        x = min(unmatched)

        for y, d in neighbors(x):
            if y in unmatched:
                rec(
                    unmatched - {x, y},
                    edges + [(min(x, y), max(x, y), d)],
                )

    rec(set(V), [])
    return ans

def direction_map(matching):
    result = {}
    for x, y, direction in matching:
        result[x] = direction
        result[y] = direction
    return result

FACES = []

for free in combinations(range(D), 2):
    fixed = tuple(i for i in range(D) if i not in free)

    for fixed_values in product((0, 1), repeat=2):
        vertices = []

        for free_values in product((0, 1), repeat=2):
            bits = [0] * D

            for i, value in zip(fixed, fixed_values):
                bits[i] = value

            for i, value in zip(free, free_values):
                bits[i] = value

            vertex = sum(bits[i] << i for i in range(D))
            vertices.append(vertex)

        FACES.append(
            (free, fixed, fixed_values, tuple(vertices))
        )

def face_direction_set(matching, face):
    directions = direction_map(matching)
    return {directions[x] for x in face[3]}

def is_normal(matching):
    return all(
        len(face_direction_set(matching, face)) == 3
        for face in FACES
    )

def common_anchor_face_count(matching):
    count = 0

    for free, fixed, fixed_values, vertices in FACES:
        direction_set = face_direction_set(
            matching,
            (free, fixed, fixed_values, vertices),
        )

        if (
            len(direction_set) <= 2
            and not set(fixed).issubset(direction_set)
        ):
            count += 1

    return count

matchings = enumerate_matchings()
normal_matchings = [
    matching for matching in matchings if is_normal(matching)
]

histogram = Counter(
    common_anchor_face_count(matching)
    for matching in matchings
)

assert len(matchings) == 272
assert len(normal_matchings) == 8
assert histogram == Counter({
    0: 8,
    9: 32,
    15: 96,
    16: 48,
    20: 84,
    24: 4,
})
assert min(
    common_anchor_face_count(matching)
    for matching in matchings
    if not is_normal(matching)
) == 9

print("coordinate perfect matchings:", len(matchings))
print("normal labeled matchings:", len(normal_matchings))
print(
    "common-anchor face histogram:",
    dict(sorted(histogram.items())),
)
print(
    "minimum for nonnormal:",
    min(
        common_anchor_face_count(matching)
        for matching in matchings
        if not is_normal(matching)
    ),
)
```

预期输出：

```text
coordinate perfect matchings: 272
normal labeled matchings: 8
common-anchor face histogram: {0: 8, 9: 32, 15: 96, 16: 48, 20: 84, 24: 4}
minimum for nonnormal: 9
```

# 附录 B：关键常数

| 表达式 | 数值/意义 |
|---|---|
| \(\frac14-\frac4{27}\) | \(\frac{11}{108}\)：完整 Ferrers residual |
| \(\frac3{20}-\frac4{27}\) | \(\frac1{540}\) |
| \((1/540)/(11/108)\) | \(1/55\)：\(3/20\) 所需捕获比例 |
| \(q\ge3/(s+3-2\lambda)\) | 固定核心次数界 |
| \(s=18,\lambda=1/2\) | \(q\ge3/20\) |
| \(s=18,\lambda=1\) | \(q\ge3/19\) |
| \(r_+=(1+\sqrt{1-4c})/2\) | 单缺陷递推的正固定点 |

# 附录 C：来源与复核边界

本文综合了既有研究 handout 与后续讨论，但所有执行下一步所需的定义、公式、状态表和枚举代码均已在正文重述。

复核边界如下：

- \(Q_4\) 的 \(272/8/9\) 枚举已由附录 A 程序在本次交接中重新运行。
- 小规模 MILP 表为既有完整求解报告中的结果；本文没有重新运行全部 MILP。
- \(4/27\) 基准和拓扑 Hall/Rado 准则作为标准输入使用，正式论文需要补充准确文献引用。
- Terminal defect SCC 定理、critical link 稳定性、pivot 全局粘合和二进制强迫森林终局均保持开放。
