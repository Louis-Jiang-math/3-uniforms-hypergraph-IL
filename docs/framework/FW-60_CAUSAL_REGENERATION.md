# FW-60 — Causal incidence regeneration

- **Status:** open
- **Question:** Q-0016
- **DAG node:** G3

## Problem

escape Hall 可将质量注入真实 incidence，但费用可能分散到不断出生的新 pivot。
必须解释这种再生为何不能长期无损。

## Desired outputs

在无 reuse、无 augmentation、无 exact-future quotient 的未来闭合区域中，至少出现：

1. 正比例 fresh real-edge capacity；
2. 回到有界旧锚集合并结合基准负载得到高点度数；
3. 完整真块无 IT 核心；
4. 未覆盖合法未来选择；
5. 明确 slot/edge reuse、Hall cut 或 quotient 证书。

## Known limits

- F-0035：只能无条件得到“集中或收费顶点增殖”。
- 对角分散模型：增殖不自动给出 \(1/4\) 或核心。
- 深度二有限枚举未发现精确 \(11/27\) 等号结构，但这只是计算观察。
- 在人为 AMCG + transition charging 中得到的 fresh 常数不是 Q-0016 证明。

## Next admissible work

只有在 G1/G2 提供真实、未预装收费权的两层近临界模块后，才证明深度二再生。
每个出口必须指明真实容量来源与 genealogy 注入。
