# Notation and type discipline

## Core mathematical objects

- \(H=(V,E)\)：有限三一致分块超图。
- \(\mathcal P=\{B_1,\ldots,B_m\}\)：真实块划分。
- \(U\)：独立部分横截。
- \(M\)：当前唯一缺失真实块。
- \(p\in U\)：当前 pivot。
- \(e\in E(H)\)：真实超边，跨全部执行历史只有一份全局容量。
- \(\rho\)：实际 root projection。
- \(\gamma\)：完整 genealogy。

## Execution record type

规范执行记录至少为

\[
\widehat D=(U,M,p,\rho,\gamma,\mathcal L),
\]

其中 \(\mathcal L\) 包含三份账本的当前占用。仅有 \((U,M,p)\) 是组合状态，
不能自动代表实际可执行记录。

## Transformations

```text
actual execution record
  --forget provenance-->
combinatorial state

combinatorial switch
  --actual reroot lift required-->
new executable record

actual records
  --ledger-preserving exact-future equivalence required-->
quotient state
```

逆箭头均不自动成立。

## Capacity types

### Root/configuration budget

按义务、配置和 pivot 分配的质量。控制是否保住单个 \(\Delta(H)\) 因子。

### Slot capacity

\[
(\rho,p,e_{\rm root})
\]

或项目冻结的等价完整标签。不同 genealogy/projection 不能无证明合并。

### Global real-edge capacity

每条真实边的全局剩余容量。无论出现在多少 projection、history、switch 或
escape 中，都通过同一个资源节点。

## Support types

- vertex projection support；
- phase/code support；
- compressed state support；
- complete real-block support。

只有最后一类在覆盖每个完整横截且 blocker 内部时可调用块极小性。

## Mass types

- obligation mass；
- positive configuration-flow mass；
- unpaid active defect mass；
- paid root/transition/escape mass；
- exceptional/error mass。

分裂必须守恒，支付后不得重新作为 unpaid mass。质量守恒不自动赋予真实边收费权。
