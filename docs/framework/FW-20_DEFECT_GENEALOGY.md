# FW-20 — Defect genealogy and auditable mass

- **Status:** specification
- **DAG role:** supports G1–G3

## 0. Purpose

为真实 defect 执行提供不复制质量、保留 genealogy 和容量的类型接口。

## 1. Minimal record

每个节点保存

\[
(U,M,p,\rho,\gamma)
\]

以及局部结果、真实 blocker、三份账本和未支付质量。

不同 genealogy 即使当前迹相同也不能自动合并。

## 2. AMCG status

“可审计的分数质量守恒 defect genealogy（AMCG）”可以作为严格规格：

- 节点质量来自不交执行 cylinder；
- ordinary/escape/augmentation 构成严格分割；
- 分数拆分不复制质量；
- real-edge flow 使用统一容量标度；
- provenance 可逐单位追踪。

**AMCG 是 definition/specification。**

它没有证明：

\[
\text{任意目标低度实例}\Longrightarrow\text{近无损 AMCG}.
\]

该箭头属于 Q-0002/Q-0015。

## 3. Canonical measurable refinement

有限原子执行空间可乘以 \([0,1]\) 做无原子细化，以实现任意分数质量拆分。
这只解决“如何不复制质量”，不创造新的配置预算、slot 或 real-edge 收费权。

## 4. Forbidden use

不得因为 AMCG 允许拆分，就把 ordinary continuation 的超额部分自动赋予
transition-edge capacity。可分性与收费合法性是两个不同接口。
