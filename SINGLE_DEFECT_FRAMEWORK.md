# SINGLE_DEFECT_FRAMEWORK

> **版本：** v0.4-auditor-grounded
> **日期：** 2026-07-27
> **状态：** 研究草稿；零误差共同预置 pivot 命题已被否定；Q-0015 首轮真实执行审计器、预算 LP、对偶 Hall 证书和回归测试已经实现；一般低度近无损配置定理、defect closure 与 terminal SCC 分类仍开放。
> **目标：** 将“单缺陷可逆修复”写成一个可证明、可反驳、可编程检查的数学对象。

---

## 0. 本文件做什么，不做什么

本文件尝试完成 `HANDOFF_CURRENT.md` 中 Q-0002 的第一部分：

1. 严格区分**源稳定执行记录**、**失败义务**、**合法根配置**、**活动缺陷状态**和**真实阻断边**；
2. 给出 \(\widehat{\mathcal S}_k,\mathcal D_k\)、第一阻断边、合法单缺陷配置和执行投影 \(\pi\) 的候选定义；
3. 证明在配置预算与投影—根边槽位容量成立时，单缺陷递推确实闭合；
4. 将唯一 pivot 降为零误差配置流的特例，并把 terminal defect graph 明确放在配置提取之后；
5. 把尚未证明的内容压缩成可由预算 LP、固定预算最大流/最小割和真实边 Hall 审计的接口；
6. 记录 Q-0015 首轮审计器已经完成的范围、计算观察和仍未解决的理论接口。

本文件**不宣称**：

- 已经构造出适用于任意块极小无 IT 实例的单缺陷搜索；
- 零误差共同预置 pivot 命题成立；该命题已被第 3 节的真实反例否定；
- 每个失败义务都存在近无损的真实配置流；
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
| `HANDOFF_CURRENT.md` | 原始单缺陷目标与投影重数接口；本版本将唯一 pivot 从源定义后移到配置提取。 |
| `old/handoff_toward_one_quarter.md` §§7–10, 14 | 单缺陷递推、critical link、pivot 粘合、二进制强迫森林。 |
| `old/chatgpt-export_第一阶段解析骨架.txt` | 保留标签的条件化不降熵；执行历史不能在汇合时无代价擦除；可逆闭路必须保留真实身份。 |
| `old/chatgpt-export_基准真实边集合证明.txt` | 语义地址、真实边容量、加权 Hall；历史依赖相位需要真实 path-lift。 |
| `old/chatgpt-export_数学语言描述_mathcal T_4图册(2).txt` | 合法刷新应使用协变运输；原始端点变化不是费用；异常必须相对于规范真实运输定义。 |
| `old/chatgpt-export_文章核心问题分析(1).txt` | 有序旋转、pivot persistence、偏轴/远端缺陷；单个轻锚局部关闭不能无条件全局重复。 |
| `old/chatgpt-export_证明主线与障碍.txt` | 历史重数不等于真实边数；SCC、代码簿与有限相位模型必须保留真实 lift。 |
| `FACTS.md`, `QUESTIONS.md`, `FAILURES.md` | F-0005、F-0022、F-0027–F-0029；Q-0002–Q-0007、Q-0014–Q-0015；A-0001–A-0004、A-0010–A-0013、A-0018、A-0020–A-0022。 |
| `q0015_configuration_auditor.py` 及其归档结果 | 实际成功执行树、失败义务、合法配置枚举、预算 LP、分数 Hall 对偶、固定预算最大流、独立真实边账本和三组回归测试。其输出是计算证书，不自动升级为一般定理。 |

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

## 3. 零误差共同预置 pivot 已被反例否定

若投影状态只记录一个无指针的独立部分横截 \(T\)，事后对所有可能 pivot 求和通常只能得到

\[
\sum_{p\in T}d_H(p)\le |T|\Delta(H),
\]

而不是所需的单个 \(\Delta(H)\) 因子。这个观察仍然正确；错误之处是把它直接升级为“每个源稳定记录必须预置一个共同唯一 pivot”。

### 命题 3.1：Q-0014 的字面零误差命题为假

令四个块为

\[
B_i=\{i_0,i_1\},\qquad i=0,1,2,3,
\]

并令 \(H_\square\) 的边为

\[
\begin{aligned}
&\{0_0,1_0,2_0\},\quad \{0_0,1_1,3_0\},\quad
  \{0_0,2_1,3_1\},\quad \{0_1,1_0,3_1\},\\
&\{0_1,1_1,2_1\},\quad \{0_1,2_0,3_0\},\quad
  \{1_0,2_1,3_0\},\quad \{1_1,2_0,3_1\}.
\end{aligned}
\tag{3.1}
\]

该超图具有以下性质。

1. 每个完整横截恰好包含一条边；因此 \(H_\square\) 无 IT，且无竞争认证。
2. 删除任意边后出现 IT，删除任意完整块后也出现 IT。
3. 由唯一阻断边遗漏的坐标得到的 \(Q_4\) 完美匹配是正常模板：每个二维面恰见三个方向。
4. 在真实执行根迹
   \[
   R=\{0_0,1_0\}
   \]
   上，加入旧端点 \(r=2_1\) 成功。
5. 随后尝试 \(x_0=3_0\) 时，唯一第一阻断边为
   \[
   \{1_0,2_1,3_0\},
   \]
   释放 \(r\) 后 \(R\cup\{3_0\}\) 独立，因此该失败强制 pivot 为 \(1_0\)。
6. 随后尝试 \(x_1=3_1\) 时，唯一第一阻断边为
   \[
   \{0_0,2_1,3_1\},
   \]
   释放 \(r\) 后 \(R\cup\{3_1\}\) 独立，因此该失败强制 pivot 为 \(0_0\)。

于是同一成功后继的两个干净失败分别要求两个不同 pivot，不存在能在两步窗口开始前预置并同时解释二者的共同 pivot。故

\[
\boxed{\text{零误差共同预置 pivot 命题不成立。}}
\tag{3.2}
\]

该反例没有使用 multi-defect、竞争、边界或释放后不独立；失败签名是

```text
normal Q4 square with individually orientable failures
but no common preassigned pivot
```

它也说明：唯一 pivot 不能作为源稳定状态的定义公理。

### 3.2 反例没有否定什么

该模型满足 \(b=2\) 且 \(\Delta(H_\square)=3\)，因此它不是
\(\Delta<(1/4-\varepsilon)b^2\) 的低度反例，也没有否定“在真实低度、块极小执行中，大部分质量可被近无损配置流吸收”的渐近稳定化命题。

反例否定的是源层共同 pivot，而不是每个失败分别存在单缺陷配置：上述两个失败单独看都具有唯一合法配置。

### 3.3 配置优先的修正入口

因此本版本采用两阶段入口：

1. **源稳定记录不带 pivot；**
2. 每个失败先生成一个带完整真实身份的义务，并枚举全部合法根配置；
3. 只有获得正配置流的分支才生成带唯一 pivot 的缺陷记录；
4. 单个 \(\Delta(H)\) 因子由配置预算与投影—根边槽位容量共同保证，而不是由源状态定义强行保证。

唯一 pivot 模型仍可作为配置预算

\[
\lambda_{\widehat S}(p_0)=1,
\qquad
\lambda_{\widehat S}(p)=0\quad(p\ne p_0)
\]

的特殊情形，但不再是普遍公理。是否存在近无损配置预算，是需要证明或由真实 Hall 最小割反驳的主接口。

## 4. 源稳定执行记录与配置化根分支

### 定义 4.1：源稳定执行记录

深度 \(k\ge0\) 的源稳定执行记录写为

\[
\widehat S=(\mathbf C,T,N,h,w),
\]

满足：

1. \(\mathbf C=(C_1,\ldots,C_k)\) 是执行块词；
2. \(T\) 是独立部分横截，且
   \[
   |T|=k,\qquad \operatorname{blk}(T)=\{C_1,\ldots,C_k\};
   \]
3. \(N\notin\operatorname{blk}(T)\) 是下一待尝试的真实块；
4. \(h\) 是由真实父记录组成的审计 genealogy；
5. \(w=w(\widehat S)>0\) 是记录携带的质量。

源稳定记录不含 pivot。成功扩张仍产生源稳定子记录；pivot 只在某个失败义务被分配到合法根配置后出现。

### 定义 4.2：压缩源稳定状态

源稳定记录的压缩签名为

\[
\widehat S^{\rm cmp}=\kappa_{\widehat S}(\widehat S)=(T,N).
\]

记所有深度 \(k\) 的源稳定执行记录为 \(\widehat{\mathcal S}_k\)。同一个压缩签名可以由多个执行记录产生；这些记录不能在未审计 genealogy 的情况下直接合并。若合并，只能把质量相加，不能重置配置槽位或真实边账本。

### 定义 4.3：配置化根分支

设 \(\widehat S_0\in\widehat{\mathcal S}_{k-2}\)。一个配置化根分支是二元组

\[
(\widehat S_0,p),\qquad p\in T(\widehat S_0),
\]

以及分配给该分支的预算质量

\[
\lambda_{\widehat S_0}(p)w(\widehat S_0).
\]

它不是新的独立搜索状态，也不能制造额外父质量；它只是配置提取后用于生成带 pivot 缺陷记录的容量分支。唯一 pivot 模型对应某个 \(p\) 的预算为一，其余为零。

### 定义 4.4：稳定总质量

\[
A_k=\sum_{\widehat S\in\widehat{\mathcal S}_k}w(\widehat S).
\]

最终 \(A_m>0\) 意味着存在至少一个覆盖全部真实块的独立横截执行记录，因此存在 IT。

---

## 5. 下一块尝试与第一阻断边

固定源稳定记录

\[
\widehat S=(\mathbf C,T,N,h,w)
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

- 若 \(\operatorname{Blk}(T,x)=\varnothing\)，称 \((\widehat S,x)\) 为成功尝试；
- 否则称为失败尝试，并记录第一阻断边 \(e_0=\beta(T,x)\)。

每个候选 \(x\in N\) 携带质量 \(w(\widehat S)\)。因此源稳定记录产生的总尝试质量为 \(b\,w(\widehat S)\)。

---

## 6. 失败义务与合法根单缺陷配置

单缺陷递推不是对任意失败边直接成立。一个失败必须先被视为义务，再枚举其全部真实两步配置。配置可以有零个、一个或多个；“恰有一个”不是定义要求。

### 定义 6.1：真实两步前驱

设

\[
\widehat S_0=(\mathbf C_0,R,M,h_0,w_0)
\in\widehat{\mathcal S}_{k-2},
\qquad r\in M.
\]

若 \(R\cup\{r\}\) 独立，并且搜索规则实际产生源稳定子记录

\[
\widehat S_1
=
\operatorname{Succ}(\widehat S_0,r)
=
(\mathbf C_0M,\ R\cup\{r\},\ N,\ h_1,\ w_0),
\]

则称 \((\widehat S_0,r)\) 是 \(\widehat S_1\) 的真实两步前驱。该定义只承认实际访问的父子记录，不允许事后删除任意端点制造前驱。

### 定义 6.2：失败义务

若从 \(\widehat S_1\) 尝试 \(x\in N\) 失败，第一阻断边为 \(e_0=\beta(T(\widehat S_1),x)\)，则定义失败义务

\[
a=(\widehat S_1,x,e_0,w_0).
\]

每个失败候选产生完整质量 \(w_0\) 的义务。第一阻断规则只使义务类别互斥，不预先选择 pivot 或释放端点。

### 定义 6.3：合法根单缺陷配置

失败义务 \(a\) 的一个合法根单缺陷配置写为

\[
c=(\widehat S_0,r,p,e_0,U),
\]

其中 \((\widehat S_0,r)\) 是定义 6.1 的真实两步前驱，\(p\in R\)，并且

\[
e_0=\{p,r,x\},
\tag{6.1}
\]

且

\[
U=R\cup\{x\}
\tag{6.2}
\]

是独立部分横截。记全部合法配置集合为 \(\mathcal C(a)\)。

配置保存真实根投影、旧端点、pivot、第一阻断边和释放后的独立迹。若 \(\mathcal C(a)=\varnothing\)，该义务进入 `no-configuration` 异常或相应最小割；若 \(|\mathcal C(a)|>1\)，不得事后任意选一个并删除其余解释。

### 定义 6.4：配置流

对每个义务 \(a\) 和 \(c\in\mathcal C(a)\)，引入

\[
q(a,c)\ge0.
\]

普通配置质量必须满足

\[
\sum_{c\in\mathcal C(a)}q(a,c)=w(a)
\tag{6.3}
\]

或明确把未分配部分计入异常质量。只有 \(q(a,c)>0\) 的配置才生成带 pivot 的根缺陷分支，其质量为 \(q(a,c)\)。

### 6.5 为什么独立性条件不可省略

可能有多条阻断边：

\[
\{x,u,v\},\qquad \{x,u',v'\}.
\]

删除第一阻断边的一个旧端点后，第二条边可能仍完整存在。此时所得集合不是独立部分横截，不能被称为“一个缺失块的单缺陷状态”。

因此下列情况必须进入异常账本或配置最小割：

1. 第一阻断边的两个旧端点都不能单独释放；
2. 两种释放都可行但没有近无损配置预算；
3. 所有可行配置集中在过少的 root-pivot-edge 槽位；
4. 释放后仍有其他完整超边；
5. 合法前驱不属于实际访问的深度 \(k-2\) 源稳定层。

把这些情况静默忽略会把多缺陷系统或配置拥塞误写成单缺陷系统。

---

## 7. 活动缺陷状态

### 定义 7.1：根缺陷执行记录

获得正配置流的合法配置产生记录

\[
\widetilde D
=
(\mathbf C_0MN,\ U,\ p,\ M,\ e_0,\ \widehat S_0,\ h_D,\ q(a,c)).
\]

其中：

- \(U=R\cup\{x\}\) 独立；
- \(p\in U\)；
- \(M\) 是唯一缺失块；
- \(e_0=\{p,r,x\}\) 是根第一阻断边；
- \(\widehat S_0\) 是实际访问的源根投影记录；
- \(h_D\) 保存真实 pivot genealogy；
- 缺陷质量为 \(q(a,c)\)，同一义务的全部配置分支质量之和由 (6.3) 控制。

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

注意：压缩签名一般不能恢复完整 genealogy；这正是需要单独记录配置投影与槽位占用的原因。

---

## 8. 缺陷移动：保留 pivot，移动缺失块

固定活动缺陷记录

\[
\widetilde D=(\mathbf C,U,p,M,e,\widehat S_0,h_D,w),
\]

其中 \(U\) 是独立部分横截，恰缺块 \(M\)。

尝试 \(y\in M\)。

### 8.1 增广出口

若 \(U\cup\{y\}\) 独立，则缺陷被修复，产生覆盖当前全部活动块的源稳定状态。这称为增广出口。

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
(\mathbf C,\ U',\ p,\ B(z),\ f,\ \widehat S_0,\ h_D',\ w).
\]

因此：

- pivot \(p\) 继承；
- 缺失块从 \(M\) 移到 \(B(z)\)；
- 新第一阻断边为 \(f\)；
- 根投影 \(\widehat S_0\) 不变；
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

## 10. 配置投影、pivot 预算与槽位容量

### 定义 10.1：执行投影

每个缺陷执行记录继承其合法配置中的源根投影：

\[
\pi_{\rm exec}(\widetilde D)=\widehat S_0
\in\widehat{\mathcal S}_{k-2}.
\]

该投影沿所有单 pivot 缺陷移动保持不变。

### 定义 10.2：根收费边

根收费边为配置中的根失败第一阻断边：

\[
e_{\rm root}(\widetilde D)=\{p,r,x\}.
\]

后续缺陷移动使用的边只作为 transition edge 记录；除非另有明确分配，不能把每条 transition edge 再次当作同一根失败的独立收费。

### 定义 10.3：源 root-pivot 预算

对每个源根投影 \(\widehat S\) 和 \(p\in T(\widehat S)\)，配置提取器给出

\[
\lambda_{\widehat S}(p)\ge0.
\]

目标预算为

\[
\sum_{p\in T(\widehat S)}\lambda_{\widehat S}(p)
\le 1+\eta.
\tag{10.1}
\]

唯一 pivot 是 \(\eta=0\) 且预算集中在一个顶点的特例。局部正常窗口可能迫使 \(\eta>0\)；这种缺口必须由全局低度、真实可达性或异常账本控制，不能从定义中删除。

### 定义 10.4：投影—pivot—根边槽位容量

对源稳定执行记录 \(\widehat S\)、pivot \(p\) 和真实边 \(e\ni p\)，要求

\[
\sum_{\substack{\widetilde D\ {\rm root}\\
\pi_{\rm exec}(\widetilde D)=\widehat S\\
p(\widetilde D)=p\\
e_{\rm root}(\widetilde D)=e}}
w(\widetilde D)
\le
(1+\gamma)\lambda_{\widehat S}(p)w(\widehat S).
\tag{10.2}
\]

当右侧非零时，可把左、右之比定义为槽位重数。任何超过预算的质量必须来自：

- 多个 genealogy 被压缩；
- 多个义务只能使用同一合法配置槽位；
- 缺陷在闭路后被重新投影；
- 同一真实测试被复制；
- 质量在分裂—汇合中未正确守恒。

式 (10.1)–(10.2) 是新的配置入口接口。旧的“每个稳定状态预置唯一 pivot、每个投影—边重数至多 \(1+\gamma\)”是其特殊情形。

### 定义 10.5：配置 Hall 缺口

固定 \(\widehat S\)，将投影到它的失败义务与合法槽位 \((p,e)\) 组成二部容量网络。满足全部需求所需的最小预算膨胀记为

\[
\eta_{\rm cfg}^{(\gamma)}(\widehat S)
=
\max\left\{0,
\inf\left\{
\sum_p\lambda_{\widehat S}(p)-1:
\text{在固定 }\gamma\text{ 下，(6.3) 与 (10.2) 可行}
\right\}
\right\}.
\]

若不可行，必须输出具体义务、合法配置邻域和容量对偶证书。该证书是待分类的真实接口障碍；不能只输出抽象相位缺口。

### 命题 10.6：配置预算接口是 LP，固定预算后才是普通最大流

固定源根投影 \(\widehat S\)。令 \(\mathcal A(\widehat S)\) 为投影到它的失败义务，令
\(\mathcal K(\widehat S)\) 为合法槽位 \(s=(p,e)\) 的集合。对每个合法配置
\(c\in\mathcal C(a)\)，记其槽位为 \(s(c)\)。

在零槽位误差 \(\gamma=0\) 时，引入

\[
q_{a,c}\ge0,\qquad y_p\ge0,
\]

并考虑

\[
\begin{aligned}
\text{最小化}\quad &t=\sum_p y_p,\\
\text{满足}\quad
&\sum_{c\in\mathcal C(a)}q_{a,c}=w(a)
&&\text{对每个 }a,\\
&\sum_{\substack{a,c\\s(c)=(p,e)}}q_{a,c}
\le y_p\,w(\widehat S)
&&\text{对每个槽位 }(p,e).
\end{aligned}
\tag{10.3}
\]

于是

\[
\eta_{\rm cfg}^{(0)}(\widehat S)=\max\{0,t_{\min}-1\}.
\tag{10.4}
\]

问题 (10.3) 一般不是单层普通最大流，因为同一 pivot 的不同根边槽位共享变量 \(y_p\)。
其对偶为

\[
\begin{aligned}
\text{最大化}\quad
&\sum_a w(a)\alpha_a,\\
\text{满足}\quad
&\alpha_a\le\beta_{p,e}
&&\text{若 }a\text{ 有使用 }(p,e)\text{ 的合法配置},\\
&\sum_{e:(p,e)\in\mathcal K(\widehat S)}\beta_{p,e}\le1
&&\text{对每个 }p,\\
&\alpha_a,\beta_{p,e}\ge0.
\end{aligned}
\tag{10.5}
\]

对偶可行解给出可独立复算的分数 Hall 证书。只有在归一化预算
\(\lambda_{\widehat S}(p)\) 已固定后，剩余网络
\(a\to(p,e)\) 才是普通最大流，槽位容量为

\[
\lambda_{\widehat S}(p)w(\widehat S).
\tag{10.6}
\]

因此完整审计器必须分别输出：

1. 预算 LP 的原始最优解；
2. 对偶 \((\alpha,\beta)\) 证书；
3. 固定归一化预算后的最大流/最小割；
4. 与其独立的全局真实边容量流。

---

## 11. 条件递推

### 定义 11.1：根失败质量

令第 \(k\) 步获得配置流的根失败总质量为

\[
\mathcal B_k
=
\sum_{\widetilde D\ {\rm root}}w(\widetilde D).
\]

未获得普通配置流的质量必须进入单独误差项 \(E_k^{\rm cfg}\)，不能从尝试总质量中消失。

### 定理 11.2：配置预算与槽位容量推出失败质量界

若每个普通根缺陷来自定义 6.3 的合法配置，并且 (10.1)–(10.2) 对所有 \(\widehat S,p,e\) 成立，则

\[
\mathcal B_k
\le
(1+\eta)(1+\gamma)\Delta(H)A_{k-2}.
\tag{11.1}
\]

**证明。** 对固定 \(\widehat S\)，按配置分支的 pivot 和根边求和：

\[
\begin{aligned}
\sum_{\pi_{\rm exec}(\widetilde D)=\widehat S}
w(\widetilde D)
&\le
(1+\gamma)w(\widehat S)
\sum_{p}\lambda_{\widehat S}(p)d_H(p)\\
&\le
(1+\gamma)(1+\eta)\Delta(H)w(\widehat S).
\end{aligned}
\]

对所有深度 \(k-2\) 的源稳定执行记录求和即得。\(\square\)

### 定理 11.3：质量递推

若：

1. 每个深度 \(k-1\) 源稳定记录对下一块的 \(b\) 个顶点各产生质量 \(w(\widehat S)\) 的尝试；
2. 所有尝试被无遗漏地分成成功、获得配置流的根失败和异常；
3. 成功质量完整进入深度 \(k\) 源稳定记录；
4. 配置未分配质量、multi-defect、boundary、reuse 等全部进入误差项 \(E_k\)；

则

\[
A_k
\ge
bA_{k-1}-\mathcal B_k-E_k.
\tag{11.2}
\]

结合 (11.1)：

\[
A_k
\ge
bA_{k-1}
-
(1+\eta)(1+\gamma)\Delta(H)A_{k-2}
-E_k.
\tag{11.3}
\]

若 \(E_k=0\) 且

\[
(1+\eta)(1+\gamma)\frac{\Delta(H)}{b^2}<\frac14,
\]

则标准正根归纳给出所有 \(A_k>0\)，最终存在 IT。

这部分仍是条件证明；未证内容集中在配置提取、源预算、槽位容量、异常控制和后续 defect closure。

---

## 12. 三种账本必须区分

### 12.1 义务—配置账本

式 (6.3) 控制每个失败义务的质量是否被完整分配到真实合法配置。其对偶是义务集合与配置槽位之间的加权 Hall 最小割。这个账本回答“失败能否进入单缺陷状态空间”，不直接回答真实边是否有全局单位容量。

### 12.2 递推槽位账本

式 (10.1)–(10.2) 控制

\[
(\text{源根投影},\ \text{pivot},\ \text{根真实边})
\]

这一槽位出现多少质量。它允许同一真实边与不同源根投影配对；这是递推中乘上 \(A_{k-2}\) 的来源。

### 12.3 全局真实边账本

若要把义务质量兑现为真实顶点度数，必须另设分数分配

\[
q_{\rm edge}(a,e)\ge0
\]

满足

\[
\sum_e q_{\rm edge}(a,e)=w(a),
\qquad
\sum_a q_{\rm edge}(a,e)\le c(e).
\tag{12.1}
\]

通常 \(c(e)\le1\)。存在这种分配等价于相应的加权 Hall 条件。

### 12.4 重要警告

“存在合法配置”只说明某个义务可以进入单缺陷分支，不说明配置预算或 (12.1) 自动成立。
“源配置 Hall 缺口为正”也不说明真实边配置 overflow 为正；义务可能通过其他真实前驱或真实边分散支付。
“每个投影—pivot—根边槽位重数至多一”不说明同一真实边在不同投影间没有被重复兑现。

因此一个完整证明必须明确说明当前使用的是：

- 义务—配置完整性；
- 递推槽位容量；
- 还是全局真实边容量。

若同时使用，必须给出三者之间的归一化、质量分裂和容量兼容证明，不得无说明切换。

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

## 14. 配置化零误差 terminal defect graph

零误差模型先假设：

- **Z1** 每个普通失败义务被配置流完整分配到合法根单缺陷配置；
- **Z2** 每个获得正流的配置分支有唯一真实 pivot，且每次缺陷继续保留该 pivot；
- **Z3** 删除一个旧端点后所得部分横截始终独立；
- **Z4** 无竞争第一认证、无边界、无不相容配置；
- **Z5** 所有四块交换方块均为八个正常模板之一；
- **Z6** 执行 genealogy 和真实边身份完整保留；
- **Z7** 配置预算与槽位容量零损失：\(\eta=\gamma=0\)；
- **Z8** terminal pivot link 在相关两块上为精确完全二部图；
- **Z9** 块极小性只对完整真实块系统使用。

### 候选零误差定理

设配置提取已经完成，且 \(\mathscr K\) 是满足 Z1–Z9 的有限 terminal defect SCC。则至少有一项：

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
| Configuration Hall cut | 某组失败义务的合法配置邻域容量不足 | 把源 pivot 缺口直接当真实边 overflow | 输出最小割；区分源预算、槽位拥塞和真实边复用 |
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
- **SD2 — 稳定独立性：** 每个源稳定迹和缺陷迹都是独立部分横截。
- **SD3 — 唯一下一块：** 每个源稳定记录有一个预先确定的下一块。
- **SD4 — pivot 后置：** 源稳定记录不带 pivot；每个获得正配置流的缺陷分支带唯一真实 pivot。
- **SD5 — 配置完备枚举：** 每个失败义务的全部合法两步配置按定义 6.3 枚举。
- **SD6 — 单端点释放：** 每个合法配置释放后所得迹独立。
- **SD7 — defect closure：** 每次非增广继续满足定义 8.2。
- **SD8 — genealogy 守恒：** root projection 沿 defect 组件不变。

### 质量与容量公理

- **MC1 — 尝试质量：** 每个候选继承父记录质量。
- **MC2 — 完备分割：** 成功、普通配置质量和异常无遗漏且互斥。
- **MC3 — 汇合守恒：** 合并只相加质量，不复制质量。
- **MC4 — 配置完整性：** 式 (6.3)，或未分配质量显式进入误差项。
- **MC5 — root-pivot 预算：** 式 (10.1)。
- **MC6 — 配置槽位容量：** 式 (10.2)。
- **MC7 — 真实边 Hall：** 若使用全局度数账本，明确证明 (12.1)。

### 局部与终局公理

- **LG1 — 正常方块：** 除受控异常外，四块交换属于正常模板。
- **LG2 — 协变一致：** 正常刷新按真实端点运输比较。
- **LG3 — terminal 分类：** 只对配置提取后得到的真实 defect graph，证明每个 terminal SCC 有增广、link 乘积或完整真子核心。
- **LG4 — 稳定化：** 全部配置损失与异常总质量进入 \(\eta(\varepsilon),\gamma(\varepsilon)\) 和 \(E_k\)，且
  \[
  (1+\eta(\varepsilon))(1+\gamma(\varepsilon))(1/4-\varepsilon)<1/4.
  \]

---

## 18. 最小反例搜索的数据格式

建议计算程序直接保存下列字段。

### StableSourceRecord

```text
stable_id
depth
block_word              # 真实块 ID 的有序列表
trace                    # [(block_id, vertex_id), ...]
next_block
weight
parent_stable_id
inserted_vertex
```

### FailureObligation

```text
obligation_id
source_stable_id
attempted_vertex
first_blocker           # 三个真实 vertex_id
weight
exception_type          # 若无普通配置或未获完整配置流
```

### RootConfiguration

```text
configuration_id
obligation_id
root_projection_id      # 实际访问的深度 k-2 StableSourceRecord
old_endpoint
pivot_vertex
root_first_blocker
released_trace
flow_mass
root_pivot_budget
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
root_configuration_id
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

### ConfigurationBudgetCertificate

```text
root_projection_id
primal_objective_t
eta_cfg
root_pivot_y
normalized_lambda
configuration_flow
dual_alpha
dual_beta
dual_objective
dual_constraints_verified
```

### ConfigurationCutCertificate

```text
cut_id
root_projection_id
obligation_ids
legal_configuration_ids
slot_labels
required_mass
available_root_pivot_edge_capacity
fixed_budget_max_flow
cut_type                # no-configuration / root-budget / slot-congestion / reuse
```

### RealEdgeCapacityCertificate

```text
obligation_ids
real_edge_ids
required_mass
available_real_edge_capacity
max_flow
feasible
```

预算 LP 对偶证书、固定预算最小割和全局真实边最小割是三个不同对象，不能只保存一个笼统的 `hall_gap` 数值。

### 必须自动检查的断言

1. 每个 trace 是真实部分横截；
2. 每个 stable/defect trace 独立；
3. 每个 blocker 是原超图真实边并含插入顶点；
4. 每个失败义务的合法配置集合完整；
5. 每个正流配置满足 \(e_0=\{p,r,x\}\) 且释放后独立；
6. root projection 是实际访问的深度 \(k-2\) 源稳定记录；
7. 每个义务的配置流守恒，未分配质量进入异常；
8. 每个源记录的 root-pivot 预算；
9. 每个 \((\widehat S,p,e)\) 的槽位占用；
10. 每条真实边的 Hall/容量占用；
11. 同一执行记录的质量守恒；
12. SCC 的所有出口；
13. 子核心是否由完整真实块组成；
14. 预算 LP 的原始—对偶目标和对偶约束可独立复算；
15. 固定预算后的普通最大流/最小割可独立复算；
16. 全局真实边容量流与配置预算证书分开保存。

---

## 19. 伪代码

```text
INPUT:
    block-minimal no-IT hypergraph H
    total orders on blocks, vertices, edges
    deterministic next-block policy

INITIALIZE source stable execution records

FOR depth k = 1,...,m:
    obligations = []

    FOR each source stable record S at depth k-1:
        N = next_block(S)

        FOR x in N:
            IF trace(S) + x is independent:
                send full attempt mass to a source stable child
            ELSE:
                e0 = first real blocker
                create failure obligation a=(S,x,e0,w(S))

                ENUMERATE all legal root configurations c:
                    S0 is an actually visited depth-(k-2) source record
                    S0 --insert r--> S
                    choose p in trace(S0)
                    e0 = {p,r,x}
                    U = trace(S0) + x is independent

                store C(a), including the empty or multiple-config cases
                append a to obligations

    SOLVE the obligation-to-configuration flow:
        full demand for each ordinary obligation
        root-pivot budgets lambda[S0,p]
        per-(S0,p,e) slot capacities

    IF the flow is infeasible:
        output an exact weighted Hall minimum cut
        classify it as no-configuration, root-budget, slot-congestion, or reuse

    FOR each configuration c with positive flow q(a,c):
        create root defect D=(U,p,B(r),e0)
        inherit root projection S0
        set defect mass to q(a,c)

    PROCESS every root defect:
        WHILE not terminal:
            choose/scan y in missing block

            IF U+y is independent:
                output source stable augmentation
            ELSE:
                f = first real blocker of U+y

                IF f={p,y,z} and U-z+y is independent:
                    move defect; keep p; missing block becomes B(z)
                ELSE:
                    send mass to a named exception ledger
                    stop this branch

    AUDIT:
        attempt and configuration-flow conservation
        root-pivot budgets
        projection-pivot-edge slot capacity
        real-edge Hall capacity
        T4 square labels
        terminal SCC exits
```

---

## 20. 当前真正需要证明的六条命题

### O1. 合法配置枚举与完备性（共同预置 pivot 已排除）

对每个失败义务，定义 6.3 枚举的 \(\mathcal C(a)\) 必须恰好包含全部真实两步单缺陷解释；无配置、多配置和释放后不独立均被显式记录，不能由字典序选择隐藏。

### O2. 投影闭包引理

每个合法配置中的 \(\widehat S_0\) 必须属于实际搜索的深度 \(k-2\) 源稳定层，而不是事后构造的未访问部分横截。

### O3. 近无损配置流或对偶障碍

除受控异常质量外，证明存在满足 (6.3)、(10.1) 和 (10.2) 的配置流，其中

\[
\eta,\gamma=o_\varepsilon(1),
\]

或输出可独立复算的加权 Hall 最小割。最小割必须保留真实义务、真实两步前驱、pivot、根边和 genealogy，不能只给相位级缺口。

### O4. 配置化 defect closure

对每个获得正配置流的根缺陷，证明后续非增广步骤保持同一真实 pivot、同一源根投影和一个缺失块；否则相应质量进入命名异常账本。

### O5. 零误差 terminal SCC 定理

仅在 Z1–Z9 和配置提取已经成立时，证明增广、完整子核心、\(1/4\) link 乘积三者之一；或给出满足全部公理的真实反模型。

### O6. 固定 \(\varepsilon\) 稳定化

仅在 O1–O5 的零误差接口明确后，把配置 Hall 缺口、multi-defect、off-pivot、non-normal、boundary、reuse 和 projection collision 的总质量控制为 \(\eta(\varepsilon),\gamma(\varepsilon)\) 与 \(E_k\)，并验证递推阈值。

---

## 21. 建议的下一项具体工作

义务—真实配置审计器和第一组回归测试已经完成。下一项工作不再是重复实现该审计器，
而是把它接到低度候选超图的外层生成器，并让内层返回四种互斥证书之一：

1. **IT 证书：** 给出一个独立完整横截；
2. **无配置证书：** 给出失败义务 \(a\) 且 \(\mathcal C(a)=\varnothing\)；
3. **配置预算证书：** 给出命题 10.6 的原始—对偶最优解和固定预算最小割；
4. **真实边复用证书：** 给出第三份账本中的真实边 Hall 最小割。

外层候选必须至少保存真实块、顶点和边、最大度上界、当前横截覆盖切平面、边极小/
块极小见证、块顺序、第一阻断边顺序和完整 genealogy。

每次出现最小割后，程序应依次区分

\[
\text{no-configuration}
\longrightarrow
\text{root-budget}
\longrightarrow
\text{slot-congestion}
\longrightarrow
\text{global real-edge reuse}.
\]

若割集中在高度重用的真实边上，下一输出必须是有限深度未来区分证书。只有能证明未来
等价保持义务、槽位和真实边账本时，才允许 quotient。

当前最小而高价值的理论问题是：

> **低度、块极小、真实可达的配置 Hall 最小割，是否必产生新鲜真实度数、合法未来等价
> quotient，或一个完整真实子核心？**

在配置最小割分类、投影闭包和 defect closure 完成前，仍不恢复 terminal SCC 枚举。

---

## 22. 验收标准

本框架可视为“完成 Q-0002 的配置入口定义阶段”，只有当下列项目均有独立证明或检查器时：

- [x] 零误差共同预置 pivot 命题由命题 3.1 的真实反例否定；
- [ ] 源稳定记录、失败义务、根配置、缺陷记录和执行词定义冻结；
- [x] 给定固定真实超图、块顺序和边顺序时，审计器可完备枚举定义 6.3 的合法配置；
- [ ] 对一般自适应搜索策略，合法配置完备性被统一证明；
- [x] 审计器对每个正流配置逐次验证单端点释放后的独立性；
- [ ] root projection 属于实际源稳定层；
- [x] 固定实例中，预算 LP、对偶 Hall 证书和固定预算最大流/最小割可复算；
- [ ] 对所有低度块极小实例证明近无损配置预算，或给出满足目标条件的反模型；
- [x] root-pivot 预算 LP、对偶变量和投影—pivot—根边槽位容量已形式化并实现；
- [ ] 质量在尝试、配置分裂、缺陷移动和汇合中严格守恒；
- [x] 审计器分别输出义务—配置、递推槽位和全局真实边三份证书；
- [ ] 每条真实边容量通过 Hall 或显式注入验证；
- [ ] terminal defect graph 只由获得正配置流的真实分支生成，并保存 pivot genealogy；
- [ ] 零误差 SCC 定理被证明或被满足全部配置公理的真实反模型否定。

在此之前，`SINGLE_DEFECT_FRAMEWORK.md` 应被视为一份候选基础设施，而不是 \(1/4\) 证明。
---

## 23. Q-0015 首轮审计器的计算状态

本节记录 `q0015_configuration_auditor.py` 的首轮输出。除命题 10.6 的 LP 对偶外，
具体数字均是可复算的计算观察，而不是一般定理。

### 23.1 F-0029 指定窗口

对第 3 节八边反例，取块顺序 \((0,1,2,3)\) 和根迹
\(R=\{0_0,1_0\}\)。审计器得到两个单位义务和两个合法配置，预算 LP 满足

\[
t_{\min}=2,\qquad \eta_{\rm cfg}^{(0)}(R)=1.
\tag{23.1}
\]

固定归一化预算
\(\lambda_R(0_0)=\lambda_R(1_0)=1/2\) 后，槽位最大流为 \(1\)，总需求为 \(2\)。

但是两个义务使用两条不同真实根边；在全局真实边账本中给每条边单位容量时，最大流为
\(2\)。因此

\[
\boxed{\text{配置 root-pivot 预算缺口不等于全局真实边 overflow。}}
\tag{23.2}
\]

### 23.2 全部固定块顺序

对同一八边模型的全部 \(24\) 个固定块顺序，程序生成 \(144\) 个带失败义务的实际
root group，分类为

\[
48\ \text{个零误差预算可行},\quad
48\ \text{个正预算缺口},\quad
48\ \text{个含 no-configuration 义务}.
\tag{23.3}
\]

因此 `no-configuration` 和正 root-budget 缺口必须分开分类。

### 23.3 九边预算修复

自动搜索找到新增真实边

\[
\{0_0,1_0,2_1\}.
\]

把它置于第一阻断优先级最前，并取块顺序 \((0,3,1,2)\)，可得到一个至少含两个失败
义务的根组，其两个义务共享同一 pivot、使用不同根边槽位，并满足

\[
\eta_{\rm cfg}^{(0)}=0.
\tag{23.4}
\]

所以八边正常模板的源预算缺口不是对额外真实认证稳定的 obstruction。

### 23.4 genealogy 压缩碰撞

两个具有相同压缩迹但不同真实 `root_projection_id` 的根记录，分别审计时都可有
\(\eta_{\rm cfg}^{(0)}=0\)。若错误合并两个 root ID，使两个单位义务共享同一
\((p,e)\) 槽位，则得到

\[
\eta_{\rm cfg}^{(0)}=1.
\tag{23.5}
\]

因此未经证明的 genealogy 压缩会人为制造槽位重数和 Hall 缺口。

### 23.5 尚未完成

首轮审计器没有证明：

- 低度一般实例存在 \(o_\varepsilon(1)\) 的配置预算；
- 固定块顺序可以避免所有 `no-configuration` 义务；
- 跨多个 root projection 的联合预算可行；
- 全局真实边复用总能收费；
- 配置流之后的 defect closure 成立；
- terminal SCC 有三出口分类。

它完成的是 Q-0015 的审计基础设施和最小回归基线。
