# Pivot-switch 与逃逸收费框架

> **状态：** 组合定义与可审计性引理已证明；逃逸收费 Hall 定理已证明；因果 incidence 集中仍开放。
> **依赖：** `SINGLE_DEFECT_FRAMEWORK.md` v0.5、真实第一阻断边、实际执行 genealogy、全局真实边单位容量。

## 1. 目的

普通 defect move 要求第一阻断边包含当前 pivot。若第一阻断边不含当前 pivot，旧框架把它记为 `off-pivot`。本文件把该情形拆成：

1. 纯组合的交换方块；
2. 真实执行中的 reroot lift；
3. 可路由的质量与容量网络。

组合定义不携带执行账本；可审计性引理说明何时组合方块可承载真实搜索质量。

## 2. 组合 pivot-switch

设 \(H\) 是三一致分块超图，\(\mathcal J\) 是活动块集。称 \((U,p,M)\) 为单缺陷组合状态，如果
\[
U\text{ 独立},\quad p\in U,\quad
\operatorname{blk}(U)=\mathcal J\setminus\{M\}.
\]

### 定义 2.1

取 \(y\in M\)。四元组
\[
\sigma=(y,z,q,f)
\]
称为从 \((U,p,M)\) 出发的组合 pivot-switch 方块，如果
\[
q,z\in U,\quad q\ne z,\quad p\notin\{q,z\},
\]
\[
f=\{q,z,y\}\in E(H),
\]
并且
\[
U^\sigma=(U-z)+y
\]
是独立部分横截。记
\[
(U,p,M)\overset\sigma\rightsquigarrow(U^\sigma,q,B(z)).
\]

### 引理 2.2（交换方块）

若 \(\sigma\) 合法，则 \(U\) 与 \(U^\sigma\) 都独立，而 \(U+y\) 不独立；并且
\[
p,q\in U^\sigma,
\qquad
\operatorname{blk}(U^\sigma)=\mathcal J\setminus\{B(z)\}.
\]

**证明。** \(f\subseteq U+y\)，故 \(U+y\) 不独立。删除的是 \(z\ne p,q\)，故 \(p,q\) 保留。加入 \(y\) 填入块 \(M\)，删除 \(z\) 使 \(B(z)\) 成为唯一缺失块。独立性由定义给出。∎

## 3. 真实 reroot lift

设 \(\widetilde D\) 是真实活动执行记录，迹为 \(U\)，当前 pivot 为 \(p\)，缺失块为 \(M\)。尝试 \(y\) 的第一阻断边为 \(f=\{q,z,y\}\)，且 \(\sigma=(y,z,q,f)\) 是组合 switch。

### 定义 3.1

一对实际执行记录 \((\widehat S'_0,\widehat S'_1)\) 称为 \(\sigma\) 的真实 reroot lift，如果：

1. \(\widehat S'_0\) 实际被搜索访问，且其迹为 \(U-z\)；
2. 从 \(\widehat S'_0\) 实际成功插入 \(z\)，得到 \(\widehat S'_1\)，其迹为 \(U\)；
3. 在 \(\widehat S'_1\) 尝试 \(y\) 的第一阻断边正是 \(f\)。

### 引理 3.2（执行可审计性）

组合 switch \(\sigma\) 加真实 reroot lift，当且仅当数据
\[
(\widehat S'_0,z,q,f,U^\sigma)
\]
可被审计为失败义务 \((\widehat S'_1,y,f)\) 的合法根单缺陷配置。

**证明。** 前向：源迹为 \(U-z\)，插入 \(z\) 实际到达 \(U\)；\(q\in U-z\)，且 \(f=\{q,z,y\}\)；组合 switch 给出 \((U-z)+y=U^\sigma\) 独立，故满足根配置全部条件。反向：合法根配置的实际父子指针给出真实 reroot lift，其释放后独立迹和根边身份给出组合 switch。∎

该引理说明：静态交换方块可以不依赖 genealogy 定义；但将它变成新的未支付 defect 根状态，必须有实际 path-lift。

## 4. 统一交换方向分类

若第一阻断边为 \(f=\{a,b,y\}\)，定义
\[
\Omega(U,y,f)=
\{(a,b):(U-b)+y\text{ 独立}\}
\cup
\{(b,a):(U-a)+y\text{ 独立}\}.
\]

### 引理 4.1

每个失败尝试恰属于：

1. \((p,z)\in\Omega\)：普通 fixed-pivot move；
2. \(\Omega\ne\varnothing\) 且无原 pivot 方向：组合 pivot-switch；
3. \(\Omega=\varnothing\)：存在不同于 \(f\) 的第二真实阻断边。

**证明。** 前两类按定义互斥。若 \(\Omega=\varnothing\)，则例如 \((U-b)+y\) 不独立，故含某边 \(g\)。由于 \(U-b\) 独立，\(g\) 必含 \(y\)；又因 \(b\notin(U-b)+y\) 而 \(b\in f\)，有 \(g\ne f\)。∎

## 5. Escape obligation 与真实 incidence

不能普通继续的失败质量记为 escape obligation \(o\)，质量为 \(\mu(o)\)。

- switch 型：每个合法方向 \((q,z)\) 提供候选 incidence \((q,f)\)；
- multi-defect 型：释放后存活的第二边 \(g\) 提供候选 incidence \((y,g)\)。

记候选集为 \(\mathcal I(o)\)。

## 6. 逃逸收费 Hall 定理

对所有 escape obligations 建立网络
\[
s\to o\to(v,e)\to e\to t,
\]
其中 \(s\to o\) 容量为 \(\mu(o)\)，中间弧容量无穷，真实边 \(e\to t\) 容量为其全局剩余容量 \(c_{\rm res}(e)\)。

### 定理 6.1

恰有以下两种结果之一：

1. 全部 escape 质量可注入真实 incidence，并满足每条真实边的全局剩余容量；
2. 存在义务子集 \(\mathcal A\) 使
   \[
   \sum_{o\in\mathcal A}\mu(o)
   >
   \sum_{e\in N_E(\mathcal A)}c_{\rm res}(e),
   \]
   即可复算的真实边 Hall/reuse 证书。

若满流存在，定义顶点负载
\[
L(v)=\sum_{o,e}x(o,v,e).
\]
在单位边容量下
\[
L(v)\le d_H(v).
\]

**证明。** 最大流—最小割给出二分。对固定 \(v\)，所有流均通过含 \(v\) 的不同真实边容量，故总量不超过 \(d_H(v)\)。∎

## 7. 未支付 fixed-pivot closure

把增广质量移入增广账本，把 escape 满流质量移入已支付账本；只有普通 move 的质量继续作为未支付活动质量。于是沿任意未支付活动路径，pivot、root projection 和“恰缺一个块”严格保持不变。若 escape 网络非满流，则输出真实边 Hall 割，而不是无声丢失 closure 质量。

这给出形式上的 closure-or-charge，但不证明逃逸费用会集中到一个 pivot。

## 8. 条件临界分裂器森林摊还

设 genealogy 森林节点质量为 \(\mu(v)\)，支付、增广和子节点满足
\[
\mu(v)=p(v)+a(v)+\sum_{u\in\operatorname{ch}(v)}\mu(u),
\]
并假设
\[
\sum_{u\in\operatorname{ch}(v)}\mu(u)
\le\frac{11}{27}\mu(v).
\]
对深度 \(h\) 截断，记累计节点质量为 \(W_h\)，fresh 容量为 \(F_h\)，reuse 溢出为 \(R_h\)，增广叶质量为 \(A_h\)，边界为 \(B_h\)。则
\[
W_h\le\frac{27}{16}(F_h+R_h+A_h)+B_h.
\]

**证明。** 每个内部节点有 \(p(v)+a(v)\ge16\mu(v)/27\)。求和并将真实支付分成 fresh 与 reuse 即得。临界几何链取等，故常数最佳。∎

注意：该定理没有证明一般 persistent blocker 满足 \(11/27\) 收缩。

## 9. Incidence 集中—增殖及其局限

满流时
\[
\sum_vL(v)=M,
\qquad
L(v)\le d_H(v)\le\Delta(H),
\]
所以
\[
|\operatorname{supp}L|\ge M/\Delta(H).
\]
这是“集中或增殖”定理：若没有大负载点，则必须出现许多收费顶点。

它不能推出子核心。取不同块中的顶点族 \(p_i,q_i,z_i,y_i\)，仅加入
\[
f_i=\{q_i,z_i,y_i\}.
\]
状态 \(U_i=\{p_i,q_i,z_i\}\) 尝试 \(y_i\) 时产生合法 switch，全部 incidence 可分散到 \((q_i,f_i)\)，最大度为 1；但该超图有 IT，也没有完整块无 IT 子核心。

因此必须额外使用无 IT、块极小、未来闭合和因果再生结构。

## 10. 当前开放命题

真正需要证明的是因果 incidence 再生/集中：若未来闭合区域中所有新 pivot 都由旧 pivot 通过可审计交换方块产生，且无 reuse、无增广、无 exact-future quotient，那么持续的 incidence 增殖必须导致大度数、完整真子核心或未覆盖未来选择。

该命题包含旧材料中的认证再生附加费和二进制强迫森林终局，目前仍开放。
