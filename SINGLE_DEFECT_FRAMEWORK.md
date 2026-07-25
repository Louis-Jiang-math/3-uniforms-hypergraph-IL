# SINGLE_DEFECT_FRAMEWORK

> **版本：** v0.1-definition-first  
> **日期：** 2026-07-25  
> **状态：** 研究草稿；定义与条件递推可审计，搜索方案存在性与 terminal SCC 分类仍开放。  
> **目标：** 将“单缺陷可逆修复”写成一个可证明、可反驳、可编程检查的数学对象。

---

## 0. 本文件做什么，不做什么

本文件尝试完成 `HANDOFF_CURRENT.md` 中 Q-0002 的第一部分：

1. 严格区分**执行记录**、**稳定状态**、**活动缺陷状态**和**真实阻断边**；
2. 给出 \(\mathcal S_k,\mathcal D_k\)、第一阻断边、单缺陷因子化和投影 \(\pi\) 的候选定义；
3. 证明在投影重数界成立时，单缺陷递推确实闭合；
4. 定义 terminal defect graph 的零误差版本；
5. 把尚未证明的内容压缩成明确公理和反例搜索目标。

本文件**不宣称**：

- 已经构造出适用于任意块极小无 IT 实例的单缺陷搜索；
- 第一阻断边自动具有真实边单位容量；
- 正常 \(\mathcal T_4\) 相位自动全局粘合；
- monodromy、bounded width、条件化或相位一致性自动产生费用；
- terminal SCC 已经被分类；
- \(1/4\) 已被证明。

---

## 1. 来源与采用的原则

本框架综合采用以下材料中的后期结论，并以较新的 handoff 和失败审计优先：

| 来源 | 本文件采用的内容 |
|---|---|
| `HANDOFF_CURRENT.md` | 冻结单缺陷状态空间；先做零误差 terminal SCC；投影重数是主接口。 |
| `old/handoff_toward_one_quarter.md` §§7–10, 14 | 单缺陷递推、critical link、pivot 粘合、二进制强迫森林。 |
| `old/chatgpt-export_第一阶段解析骨架.txt` | 保留标签的条件化不降熵；执行历史不能在汇合时无代价擦除；可逆闭路必须保留真实身份。 |
| `old/chatgpt-export_基准真实边集合证明.txt` | 语义地址、真实边容量、加权 Hall；历史依赖相位需要真实 path-lift。 |
| `old/chatgpt-export_数学语言描述_mathcal T_4图册(2).txt` | 合法刷新应使用协变运输；原始端点变化不是费用；异常必须相对于规范真实运输定义。 |
| `old/chatgpt-export_文章核心问题分析(1).txt` | 有序旋转、pivot persistence、偏轴/远端缺陷；单个轻锚局部关闭不能无条件全局重复。 |
| `old/chatgpt-export_证明主线与障碍.txt` | 历史重数不等于真实边数；SCC、代码簿与有限相位模型必须保留真实 lift。 |
| `FACTS.md`, `QUESTIONS.md`, `FAILURES.md` | F-0005、F-0022–F-0024；Q-0002–Q-0007；A-0001–A-0004、A-0010–A-0013、A-0018。 |

### 1.1 三条设计原则

**原则 P1：所有组合对象必须有真实身份。**  
块、顶点、超边、插入顶点、释放顶点和缺失块均来自原超图。相位、类型和代码只能作为注释，不能替代真实对象。

**原则 P2：执行记录可以保存真实 genealogy，但不得制造容量。**  
为了定义深度、父子关系和“两步投影”，可以保存由真实块和真实顶点组成的执行词。该执行词不是额外 sheet，也不允许把同一真实边复制成多份容量。

**原则 P3：递推账本与真实边度数账本必须分开。**  
递推需要控制的是每个“投影状态—真实边”对的出现重数；把义务兑现到顶点度数时，还需要独立的真实边容量/Hall 账本。两者不能混为一谈。

---

## 2. 基础对象

设 \(H\) 是三一致等块分块超图：

\[
V(H)=B_1\sqcup\cdots\sqcup B_m,\qquad |B_i|=b,
\]

且每条边与三个不同块各交一个顶点。记顶点 \(v\) 所在块为 \(B(v)\)。

固定：

1. 块的全序 \(\prec_{\mathcal B}\)；
2. 每个块内顶点的全序；
3. 真实边的全序 \(\prec_E\)。

这些全序只用于消除并列，不承担任何估计。

### 2.1 部分横截

集合 \(T\subseteq V(H)\) 称为部分横截，若每个块至多贡献一个顶点。写

\[
\operatorname{blk}(T)=\{B(v):v\in T\}.
\]

若 \(H[T]\) 无边，则称 \(T\) 独立。

### 2.2 执行块词

一个长度为 \(k\) 的执行块词是互异真实块组成的有序词

\[
\mathbf C=(C_1,\ldots,C_k).
\]

执行词的作用是记录当前搜索实际暴露了哪些块以及暴露次序。它必须由真实块组成；不能用抽象相位名或 sheet 代替。

---

## 3. 为什么稳定状态必须是“有指针的”

若投影状态只记录一个无指针的独立部分横截 \(T\)，则对所有可能 pivot 求和通常只能得到

\[
\sum_{p\in T}d_H(p)\le |T|\Delta(H),
\]

而不是所需的 \(\Delta(H)\)。

因此，为得到

\[
|\mathcal B_k|\lesssim \Delta(H)|\mathcal S_{k-2}|,
\]

每个投影状态必须预先带有一个唯一的真实 pivot。该 pivot 不是失败后临时选择的自由参数；它必须在相关两步窗口开始前已经固定。

这是一项必要的定义修正。

---

## 4. 稳定执行记录与压缩稳定状态

### 定义 4.1：稳定执行记录

深度 \(k\ge1\) 的稳定执行记录写为

\[
\widetilde S=(\mathbf C,T,p,N,h,w),
\]

满足：

1. \(\mathbf C=(C_1,\ldots,C_k)\) 是执行块词；
2. \(T\) 是独立部分横截，且
   \[
   |T|=k,\qquad \operatorname{blk}(T)=\{C_1,\ldots,C_k\};
   \]
3. \(p\in T\) 是唯一活动 pivot；
4. \(N\notin\operatorname{blk}(T)\) 是下一待尝试的真实块；
5. \(h\) 是由真实父记录组成的审计 genealogy；
6. \(w=w(\widetilde S)>0\) 是记录携带的质量。

深度 \(0\) 的根记录允许 \(p=\bot\)。

### 定义 4.2：压缩稳定状态

稳定记录的压缩签名为

\[
S=\kappa_S(\widetilde S)=(T,p,N).
\]

记所有深度 \(k\) 的压缩稳定状态为 \(\mathcal S_k\)。

同一个压缩签名可以由多个执行记录产生；这些记录不能在未审计 genealogy 的情况下直接合并。若合并，只能把质量相加，不能重置任何真实边账本。

### 定义 4.3：稳定总质量

\[
A_k=\sum_{\widetilde S\in\widetilde{\mathcal S}_k}w(\widetilde S).
\]

最终 \(A_m>0\) 意味着存在至少一个覆盖全部真实块的独立横截执行记录，因此存在 IT。

---

## 5. 下一块尝试与第一阻断边

固定稳定记录

\[
\widetilde S=(\mathbf C,T,p,N,h,w)
\]

及 \(x\in N\)。

定义阻断边集合

\[
\operatorname{Blk}(T,x)
=
\{e\in E(H):e\subseteq T\cup\{x\}\}.
\]

### 引理 5.1：每条阻断边都含新顶点

若 \(T\) 独立，则每个 \(e\in\operatorname{Blk}(T,x)\) 都含 \(x\)。

**证明。** 若 \(x\notin e\)，则 \(e\subseteq T\)，与 \(T\) 独立矛盾。 \(\square\)

### 定义 5.2：第一阻断边

若 \(\operatorname{Blk}(T,x)\ne\varnothing\)，定义

\[
\beta(T,x)
=
\min_{\prec_E}\operatorname{Blk}(T,x).
\]

第一阻断边使每次失败有确定证书，但它**不自动意味着**不同失败使用不同真实边。

### 定义 5.3：成功与失败尝试

- 若 \(\operatorname{Blk}(T,x)=\varnothing\)，称 \((\widetilde S,x)\) 为成功尝试；
- 否则称为失败尝试，并记录第一阻断边 \(e_0=\beta(T,x)\)。

每个候选 \(x\in N\) 携带质量 \(w(\widetilde S)\)。因此稳定记录产生的总尝试质量为 \(b\,w(\widetilde S)\)。

---

## 6. 两步单缺陷因子化

单缺陷递推不是对任意失败边直接成立。一个失败必须能够解释为：

1. 从深度 \(k-2\) 的有指针状态加入旧端点 \(r\)；
2. pivot \(p\) 在该成功步骤中保持；
3. 再尝试新端点 \(x\)；
4. 第一阻断边恰为 \(\{p,r,x\}\)；
5. 只释放 \(r\) 后重新得到一个独立、只缺一个块的状态。

### 定义 6.1：pivot-persistent 成功步骤

设

\[
\widetilde S_0=(\mathbf C_0,R,p,M,h_0,w_0)
\in\widetilde{\mathcal S}_{k-2},
\qquad r\in M.
\]

若 \(R\cup\{r\}\) 独立，并且搜索规则产生稳定子记录

\[
\widetilde S_1
=
\operatorname{Succ}(\widetilde S_0,r)
=
(\mathbf C_0M,\ R\cup\{r\},\ p,\ N,\ h_1,\ w_0),
\]

则称该步骤 pivot-persistent。注意 pivot 仍为同一个真实顶点 \(p\)。

### 定义 6.2：根单缺陷因子化

设从 \(\widetilde S_1\) 尝试 \(x\in N\) 失败，第一阻断边为 \(e_0\)。

称该失败具有根单缺陷因子化，若存在 \(\widetilde S_0,r\) 如上，使：

\[
e_0=\{p,r,x\},
\tag{6.1}
\]

且

\[
U=(R\cup\{r\}\setminus\{r\})\cup\{x\}
=R\cup\{x\}
\tag{6.2}
\]

是独立部分横截。

此时：

- 活动块集合增加了 \(M,N\)；
- \(U\) 覆盖 \(N\)，但缺失 \(M\)；
- 只释放阻断边中的旧端点 \(r\)；
- pivot \(p\) 被保留。

### 6.3 为什么独立性条件不可省略

可能有多条阻断边：

\[
\{x,u,v\},\qquad \{x,u',v'\}.
\]

删除第一阻断边的一个旧端点后，第二条边可能仍完整存在。此时所得集合不是独立部分横截，不能被称为“一个缺失块的单缺陷状态”。

因此下列情况必须进入异常账本：

1. 第一阻断边的两个旧端点都不能单独释放；
2. 两种释放都可行但无法规范定向；
3. 可行释放与预先固定 pivot 不相容；
4. 释放后仍有其他完整超边。

把这些情况静默忽略会把多缺陷系统误写成单缺陷系统。

---

## 7. 活动缺陷状态

### 定义 7.1：根缺陷执行记录

具有根单缺陷因子化的失败产生记录

\[
\widetilde D
=
(\mathbf C_0MN,\ U,\ p,\ M,\ e_0,\ \widetilde S_0,\ h_D,\ w_0).
\]

其中：

- \(U=R\cup\{x\}\) 独立；
- \(p\in U\)；
- \(M\) 是唯一缺失块；
- \(e_0=\{p,r,x\}\) 是根第一阻断边；
- \(\widetilde S_0\) 是根投影记录；
- \(h_D\) 保存真实 pivot genealogy；
- 缺陷质量为 \(w_0\)。

### 定义 7.2：压缩缺陷签名

\[
D=\kappa_D(\widetilde D)=(U,p,M,e),
\]

其中 \(e\) 是当前步骤记录的第一真实阻断边。记深度 \(k\) 的压缩缺陷状态集合为 \(\mathcal D_k\)。

### 引理 7.3：根缺陷数据可恢复

对根缺陷 \(D=(U,p,M,e_0)\)：

1. \(r\) 是 \(e_0\) 中位于 \(M\) 的唯一顶点；
2. \(x\) 是 \(e_0\cap(U\setminus\{p\})\) 中的唯一顶点；
3. 根投影的真实横截迹为
   \[
   R=U\setminus\{x\}.
   \]

**证明。** 三个端点位于不同块；\(r\notin U\)、\(x,p\in U\)，且 \(M=B(r)\)。 \(\square\)

注意：压缩签名一般不能恢复完整 genealogy；这正是需要单独记录投影重数的原因。

---

## 8. 缺陷移动：保留 pivot，移动缺失块

固定活动缺陷记录

\[
\widetilde D=(\mathbf C,U,p,M,e,\widetilde S_0,h_D,w),
\]

其中 \(U\) 是独立部分横截，恰缺块 \(M\)。

尝试 \(y\in M\)。

### 8.1 增广出口

若 \(U\cup\{y\}\) 独立，则缺陷被修复，产生覆盖当前全部活动块的稳定状态。这称为增广出口。

### 8.2 单 pivot 继续

若 \(U\cup\{y\}\) 不独立，令

\[
f=\beta(U,y).
\]

单缺陷继续要求存在唯一 \(z\in U\setminus\{p\}\)，使

\[
f=\{p,y,z\},
\tag{8.1}
\]

并且

\[
U'=(U\setminus\{z\})\cup\{y\}
\tag{8.2}
\]

独立。

此时产生新缺陷

\[
\widetilde D'
=
(\mathbf C,\ U',\ p,\ B(z),\ f,\ \widetilde S_0,\ h_D',\ w).
\]

因此：

- pivot \(p\) 继承；
- 缺失块从 \(M\) 移到 \(B(z)\)；
- 新第一阻断边为 \(f\)；
- 根投影 \(\widetilde S_0\) 不变；
- 质量守恒。

### 8.3 link 图解释

定义 pivot link

\[
L_H(p):
\quad yz\in E(L_H(p))
\iff \{p,y,z\}\in E(H).
\]

式 (8.1) 表明一次缺陷移动正是沿 \(L_H(p)\) 的边 \(yz\) 执行交换：

\[
z\longmapsto y.
\]

因为 \(U\) 独立，\(U\setminus\{p\}\) 在 \(L_H(p)\) 中是独立集。单缺陷过程是在固定 pivot link 中移动一个缺失块。

### 8.4 必须单独记录的异常

若出现以下任一情况，不能生成普通 defect edge：

- 第一阻断边不含当前 pivot；
- 第一阻断边含两个可能释放端点且无法唯一取向；
- 删除任一候选端点后仍不独立；
- 需要同时释放两个以上旧端点；
- 目标块或真实顶点离开当前活动块域；
- 同一步存在不相容的第一认证配置；
- 真实边身份在压缩后无法恢复。

这些分别对应 off-pivot、orientation、branching、boundary、config、reuse 等异常。

---

## 9. 执行缺陷图与压缩 terminal defect graph

### 定义 9.1：执行缺陷图

执行缺陷图 \(\widetilde G_k\) 的：

- 顶点是深度 \(k\) 的缺陷执行记录；
- 有向边是式 (8.1)–(8.2) 的合法单 pivot 继续；
- 边标签至少包含
  \[
  (y,z,f,\text{源缺失块},\text{目标缺失块},\text{真实 pivot}).
  \]

执行图保留完整 root projection 和 genealogy。

### 定义 9.2：压缩缺陷图

压缩图 \(G_k\) 的顶点是签名

\[
D=(U,p,M,e).
\]

若某条执行边在压缩后从 \(D\) 到 \(D'\)，则在 \(G_k\) 中加入对应有向边，并保留所有真实标签。

不同执行边可以压缩成同一条图边，但它们的质量和 root projection 不能被删除。

### 定义 9.3：terminal SCC

一个强连通分量 \(\mathscr K\subseteq G_k\) 称为 terminal，若它没有：

1. 增广出口；
2. 指向分量外的普通单缺陷继续边；
3. 已被异常账本吸收的正质量边界流。

“terminal”必须相对于完整执行账本定义；只在相位商图中无出口是不够的。

---

## 10. 投影与 genealogy

### 定义 10.1：执行投影

每个缺陷执行记录继承根投影：

\[
\pi_{\rm exec}(\widetilde D)=\widetilde S_0
\in\widetilde{\mathcal S}_{k-2}.
\]

该投影沿所有单 pivot 缺陷移动保持不变。

### 定义 10.2：根收费边

根收费边为根失败的第一阻断边：

\[
e_{\rm root}(\widetilde D)=\{p,r,x\}.
\]

后续缺陷移动使用的边只作为 transition edge 记录；除非另有明确分配，不能把每条 transition edge 再次当作同一根失败的独立收费。

### 定义 10.3：投影—边重数

对稳定执行记录 \(\widetilde S\) 和真实边 \(e\ni p(\widetilde S)\)，定义

\[
\operatorname{mult}_k(\widetilde S,e)
=
\frac{
\sum\limits_{\substack{\widetilde D\ {\rm root}\\
\pi_{\rm exec}(\widetilde D)=\widetilde S\\
e_{\rm root}(\widetilde D)=e}}
w(\widetilde D)
}{
w(\widetilde S)
}.
\tag{10.1}
\]

目标是

\[
\operatorname{mult}_k(\widetilde S,e)\le1+\gamma.
\tag{10.2}
\]

在完全不压缩、两步执行记录唯一且每个候选质量等于父质量的理想模型中，给定 \((\widetilde S,e)\) 后，两个非 pivot 端点的块次序决定 \(r,x\)，故重数应为 \(1\)。任何超过 \(1\) 的质量都必须来自：

- 多个 genealogy 被压缩；
- pivot/块次序存在多种合法解释；
- 缺陷在闭路后被重新投影；
- 同一真实测试被复制；
- 质量在分裂—汇合中未正确守恒。

这就是 Q-0002 中应被证明的“投影重数”，而不是抽象状态数。

---

## 11. 条件递推

### 定义 11.1：根失败质量

令第 \(k\) 步根失败总质量为

\[
\mathcal B_k
=
\sum_{\widetilde D\ {\rm root}}w(\widetilde D).
\]

### 定理 11.2：投影重数推出失败质量界

若每个根缺陷满足两步单缺陷因子化，且 (10.2) 对所有 \(\widetilde S,e\) 成立，则

\[
\mathcal B_k
\le
(1+\gamma)\Delta(H)A_{k-2}.
\tag{11.1}
\]

**证明。** 对固定 \(\widetilde S\)，所有根收费边都含其唯一 pivot \(p(\widetilde S)\)。因此

\[
\begin{aligned}
\sum_{\pi_{\rm exec}(\widetilde D)=\widetilde S}
w(\widetilde D)
&=
\sum_{e\ni p(\widetilde S)}
\sum_{\substack{\pi_{\rm exec}(\widetilde D)=\widetilde S\\
e_{\rm root}(\widetilde D)=e}}
w(\widetilde D)\\
&\le
(1+\gamma)d_H(p(\widetilde S))w(\widetilde S)\\
&\le
(1+\gamma)\Delta(H)w(\widetilde S).
\end{aligned}
\]

对所有深度 \(k-2\) 的稳定执行记录求和即得。 \(\square\)

### 定理 11.3：质量递推

若：

1. 每个深度 \(k-1\) 稳定记录对下一块的 \(b\) 个顶点各产生质量 \(w(\widetilde S)\) 的尝试；
2. 所有尝试被无遗漏地分成成功和根失败；
3. 成功质量完整进入深度 \(k\) 稳定记录；
4. 所有异常质量已包含在 \(\mathcal B_k\) 或单独加入误差项 \(E_k\)；

则

\[
A_k
\ge
bA_{k-1}-\mathcal B_k-E_k.
\tag{11.2}
\]

若 \(E_k=0\)，结合 (11.1)：

\[
A_k
\ge
bA_{k-1}
-
(1+\gamma)\Delta(H)A_{k-2}.
\tag{11.3}
\]

若

\[
(1+\gamma)\frac{\Delta(H)}{b^2}<\frac14,
\]

则标准正根归纳给出所有 \(A_k>0\)，最终存在 IT。

这部分是条件证明；未证内容全部集中在搜索方案存在、异常控制和 (10.2)。

---

## 12. 两种容量账本必须区分

### 12.1 递推出现账本

式 (10.1) 控制的是：

\[
(\text{投影执行记录},\ \text{根真实边})
\]

这一对出现多少质量。它允许同一真实边与不同投影状态配对；这是递推中乘上 \(A_{k-2}\) 的来源。

### 12.2 全局真实边账本

若要把义务质量兑现为真实顶点度数，必须另设分数分配

\[
q(a,e)\ge0
\]

满足

\[
\sum_e q(a,e)=w(a),
\qquad
\sum_a q(a,e)\le c(e).
\tag{12.1}
\]

通常 \(c(e)\le1\)。存在这种分配等价于相应的加权 Hall 条件。

### 12.3 重要警告

“选择了确定的第一阻断边”只说明证书唯一，不说明 (12.1) 自动成立。  
“每个投影—边对重数至多一”也不说明同一真实边在不同投影间没有被重复兑现。

因此一个完整证明必须明确说明：

- 当前是在使用递推出现账本；
- 还是在使用全局真实边容量；
- 若两者同时使用，归一化和容量分割如何兼容。

不得在两种账本之间无说明切换。

---

## 13. \(\mathcal T_4\) 相位在本框架中的唯一合法用途

考虑两个缺陷交换在四个真实块上可交换的方块。剥离竞争认证、边界和真实身份不一致后，局部第一阻断方向形成 \(Q_4\) 坐标完美匹配。

### 13.1 方块标签

每个干净交换方块记录：

1. 四个真实块；
2. 四个角的真实部分横截；
3. 每条边对应的插入顶点和释放顶点；
4. 第一真实阻断边；
5. pivot 是否保持；
6. \(272\) 类中的匹配编号；
7. 若正常，八相位中的相位编号。

### 13.2 相位不是容量

正常相位只能说明局部交换类型。它不说明：

- 两条路径返回同一真实执行记录；
- 真实支持是笛卡尔积；
- 同一真实边未重复；
- monodromy 有费用；
- 投影 genealogy 唯一。

### 13.3 协变比较

合法刷新 \(z\mapsto y\) 本来就会改变真实端点名称。比较两个相邻状态时，应先应用规范运输：

- 未刷新真实端点保持；
- 被释放端点移除；
- 新插入端点加入；
- pivot 保持；
- 禁止任意重新匹配无关端点。

只有目标第一阻断边不等于规范运输预测时，才产生 Config、Reuse、Boundary 或其他异常。不能使用原始端点分布差直接收费。

---

## 14. 零误差 terminal defect graph

零误差模型先假设：

- **Z1** 每个失败都有唯一两步单缺陷因子化；
- **Z2** 每次缺陷继续都保留同一真实 pivot；
- **Z3** 删除一个旧端点后所得部分横截始终独立；
- **Z4** 无竞争第一认证、无边界、无不相容配置；
- **Z5** 所有四块交换方块均为八个正常模板之一；
- **Z6** 执行 genealogy 和真实边身份完整保留；
- **Z7** 投影—边重数恰为 \(1\)；
- **Z8** terminal pivot link 在相关两块上为精确完全二部图；
- **Z9** 块极小性只对完整真实块系统使用。

### 候选零误差定理

设 \(\mathscr K\) 是满足 Z1–Z9 的有限 terminal defect SCC。则至少有一项：

1. **增广叶：** 执行展开中存在可修复到稳定状态的叶；
2. **完整真子核心：** 某组完整真实块诱导无 IT 子实例；
3. **link 乘积：** 存在真实 pivot \(p\) 和两个真实块中的集合 \(A,C\)，使
   \[
   A\times C\subseteq L_H(p),
   \]
   且在精确平衡情形
   \[
   |A|=|C|=\frac b2,
   \qquad
   d_H(p)\ge|A||C|=\frac{b^2}{4}.
   \]

“二进制强迫森林”应理解为：把压缩 SCC 按执行 genealogy 展开后，每个非增广节点由完全二部 link 的两侧产生二元强迫分支；若展开没有叶出口，分支闭包必须形成完整 link 乘积或完整块子核心。

该定理目前开放。若为假，反模型必须同时给出真实块、真实顶点、真实边、执行词、pivot、缺失块和每一步第一阻断边。

---

## 15. 异常分类与拟议账本

| 异常 | 精确定义 | 不能使用的错误替代 | 拟议处理 |
|---|---|---|---|
| Multi-defect | 释放第一阻断边任一旧端点后仍不独立 | 假装只剩一个 pivot | 真实新边/分叉账本 |
| Off-pivot | 第一阻断边不含当前 pivot | 事后自由更换 pivot | pivot-change 事件或异常质量 |
| Orientation ambiguity | 两个旧端点都可释放且无规范唯一方向 | 任意选一个并忘记另一解释 | 投影重数/相位粘合 |
| Projection failure | 无深度 \(k-2\) 的两步真实因子化 | 直接删去两个任意旧端点 | 搜索策略失败 |
| Competition | 同一尝试存在多种不相容第一认证配置 | 只保留字典序证书并忽略其余 | Config/Hall |
| Reuse | 多个义务兑现到同一真实边容量 | 把历史次数当不同边 | 加权 Hall |
| Boundary | 缺陷移动离开当前真实活动块域 | 在抽象相位图中继续 | 边界误差 |
| Non-normal square | 四块窗口不是八个正常模板 | 假设局部唯一 | 九面共同锚证书 |
| Reversible monodromy | 闭路为真实可逆置换 | 自动收费 | 保留 genealogy，不收费 |
| Correlated codebook | 相位一致但支持非乘积 | 使用块极小性 | 证明单坐标扩张完整性 |
| Light-anchor reuse | 同一轻锚服务线性多个兄弟状态 | 只计算被激活的一条路径 | 静态真实度数累积 |

---

## 16. 可直接证明的定义性引理

### 引理 16.1：缺陷移动保持一个缺失块

若 \(U\) 覆盖活动块集合除 \(M\) 外的所有块，选择 \(y\in M\)，释放 \(z\in U\)，则

\[
U'=(U-z)+y
\]

覆盖同一活动块集合除 \(B(z)\) 外的所有块。

### 引理 16.2：pivot link 忠实性

在单 pivot 继续中，真实 transition edge \(f=\{p,y,z\}\) 与 link 边 \(yz\in L_H(p)\) 一一对应。不同真实三边不会被同一对 \((p,y,z)\) 表示。

### 引理 16.3：第一阻断分割不等于容量分割

第一阻断规则把失败尝试分成互斥类，但同一真实边仍可作为许多不同尝试的第一阻断边。因此单位容量必须另证。

### 引理 16.4：闭路压缩不得擦除 genealogy

若执行闭路在压缩签名上返回同一 \(D=(U,p,M,e)\)，但 root projection 不同，则两个执行记录仍必须保留为不同记录，或把合并质量计入投影重数。相位名相同不构成合并依据。

---

## 17. 搜索方案公理清单

一个可用于 \(1/4-\varepsilon\) 的单缺陷搜索方案至少应验证：

### 结构公理

- **SD1 — 真实执行性：** 所有记录只使用真实块、顶点和边。
- **SD2 — 稳定独立性：** 每个稳定迹和缺陷迹都是独立部分横截。
- **SD3 — 唯一下一块：** 每个稳定记录有一个预先确定的下一块。
- **SD4 — 唯一 pivot：** 每个深度至少一的稳定/缺陷记录有唯一真实 pivot。
- **SD5 — 两步因子化：** 每个非异常失败具有定义 6.2 的因子化。
- **SD6 — 单端点释放：** 释放后所得迹独立。
- **SD7 — defect closure：** 每次非增广继续满足定义 8.2。
- **SD8 — genealogy 守恒：** root projection 沿 defect 组件不变。

### 质量与容量公理

- **MC1 — 尝试质量：** 每个候选继承父记录质量。
- **MC2 — 完备分割：** 成功、普通缺陷和异常无遗漏且互斥。
- **MC3 — 汇合守恒：** 合并只相加质量，不复制质量。
- **MC4 — 投影重数：** 式 (10.2)。
- **MC5 — 真实边 Hall：** 若使用全局度数账本，明确证明 (12.1)。

### 局部与终局公理

- **LG1 — 正常方块：** 除受控异常外，四块交换属于正常模板。
- **LG2 — 协变一致：** 正常刷新按真实端点运输比较。
- **LG3 — terminal 分类：** 每个 terminal SCC 有增广、link 乘积或完整真子核心。
- **LG4 — 稳定化：** 全部异常总质量进入 \(\gamma(\varepsilon)\)，且
  \[
  (1+\gamma(\varepsilon))(1/4-\varepsilon)<1/4.
  \]

---

## 18. 最小反例搜索的数据格式

建议计算程序直接保存下列字段。

### StableRecord

```text
stable_id
depth
block_word              # 真实块 ID 的有序列表
trace                    # [(block_id, vertex_id), ...]
pivot_vertex
next_block
weight
parent_stable_id
inserted_vertex
```

### DefectRecord

```text
defect_id
depth
active_block_word
trace
pivot_vertex
missing_block
current_first_blocker   # 三个真实 vertex_id
root_first_blocker
root_projection_id
weight
predecessor_defect_id
inserted_vertex
released_vertex
```

### DefectTransition

```text
source_defect_id
target_defect_id
inserted_vertex
released_vertex
real_edge
source_missing_block
target_missing_block
pivot_vertex
t4_square_id
t4_matching_id
t4_phase_id
exception_type
```

### 必须自动检查的断言

1. 每个 trace 是真实部分横截；
2. 每个 stable/defect trace 独立；
3. 每个 blocker 是原超图真实边；
4. 每个 blocker 含插入顶点；
5. 普通 defect transition 的 blocker 含 pivot；
6. 只释放一个真实旧端点；
7. root projection 的两步重构正确；
8. 同一执行记录的质量守恒；
9. 每个 \((\widetilde S,e)\) 的投影重数；
10. 每条真实边的 Hall/容量占用；
11. SCC 的所有出口；
12. 子核心是否由完整真实块组成。

---

## 19. 伪代码

```text
INPUT:
    block-minimal no-IT hypergraph H
    total orders on blocks, vertices, edges
    deterministic next-block and pivot policy

INITIALIZE stable execution records

FOR depth k = 1,...,m:
    FOR each stable record S at depth k-1:
        N = next_block(S)

        FOR x in N:
            IF trace(S) + x is independent:
                send full attempt mass to a stable child
            ELSE:
                e0 = first real blocker

                FIND all two-step single-defect factorizations
                    S0 --insert r, preserve pivot p--> S
                    e0 = {p,r,x}
                    U = trace(S0) + x is independent

                IF exactly one factorization:
                    create root defect D=(U,p,B(r),e0)
                    inherit root projection S0
                ELSE:
                    send mass to a named exception ledger

    PROCESS every root defect:
        WHILE not terminal:
            choose/scan y in missing block

            IF U+y is independent:
                output stable augmentation
            ELSE:
                f = first real blocker of U+y

                IF f={p,y,z} and U-z+y is independent:
                    move defect; keep p; missing block becomes B(z)
                ELSE:
                    send mass to a named exception ledger
                    stop this branch

    AUDIT:
        mass conservation
        projection-edge multiplicity
        real-edge Hall capacity
        T4 square labels
        terminal SCC exits
```

---

## 20. 当前真正需要证明的五条命题

### O1. 两步定向引理

除 \(o(1)\) 或 \(O_\varepsilon(\delta)\) 质量外，每个失败尝试都能被唯一写成

\[
\widetilde S_0
\xrightarrow{\,r\,}
\widetilde S_1
\xrightarrow[\text{fail}]{\,x\,},
\qquad
e_0=\{p,r,x\},
\]

且释放 \(r\) 后所得 \(R+x\) 独立。

这是“单缺陷降秩”的严格版本。

### O2. 投影闭包引理

上述 \(\widetilde S_0\) 必须属于实际搜索的深度 \(k-2\) 稳定记录，而不是事后构造的未访问部分横截。

### O3. 投影重数引理

对所有 \(\widetilde S,e\)：

\[
\operatorname{mult}_k(\widetilde S,e)\le1+\gamma.
\]

这需要正常 \(\mathcal T_4\) 方块的全局 pivot 粘合，并必须保留真实 genealogy。

### O4. 零误差 terminal SCC 定理

在 Z1–Z9 下证明增广、完整子核心、\(1/4\) link 乘积三者之一；或给出满足全部公理的真实反模型。

### O5. 固定 \(\varepsilon\) 稳定化

仅在 O4 成功后，把 multi-defect、off-pivot、non-normal、boundary、reuse 和 projection collision 的总质量控制为 \(\gamma(\varepsilon)\)。

---

## 21. 建议的下一项具体工作

最小而高价值的下一项不是直接枚举 terminal SCC，而是先验证 O1 的零误差版本：

> **零误差两步定向命题。**  
> 在一个所有相关四块交换均正常、无竞争认证、无边界的执行组件中，能否为每个稳定记录预先指定唯一 pivot，并为每次成功扩张指定 pivot-persistent 后继，使每个随后的失败第一阻断边都包含该 pivot 与刚加入的旧端点，且释放该旧端点后恢复独立性？

若此命题为假，最小反模型会直接展示：

- 一个不可避免的 multi-defect；
- 一个不可全局定向的正常相位方块；
- 或一个需要投影重数 \(>1\) 的真实闭路。

这比在尚未定义清楚的 terminal SCC 上继续做相位枚举更有诊断价值。

---

## 22. 验收标准

本框架可视为“完成 Q-0002 的定义阶段”，只有当下列项目均有独立证明或检查器时：

- [ ] 稳定记录、缺陷记录和执行词定义冻结；
- [ ] 每个失败被完备地分类；
- [ ] 普通失败具有唯一两步单缺陷因子化；
- [ ] 释放一个端点后独立性被逐次验证；
- [ ] root projection 属于实际稳定层；
- [ ] 质量在分裂、移动、汇合中严格守恒；
- [ ] 投影—边重数定义和计算无歧义；
- [ ] 递推账本与全局真实边账本分离；
- [ ] 每条真实边容量通过 Hall 或显式注入验证；
- [ ] terminal defect graph 保存真实 pivot genealogy；
- [ ] 零误差 SCC 定理被证明或被真实反模型否定。

在此之前，`SINGLE_DEFECT_FRAMEWORK.md` 应被视为一份候选基础设施，而不是 \(1/4\) 证明。
