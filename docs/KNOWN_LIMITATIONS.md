# Known limitations

## Mathematical

本仓库没有证明一般近无损配置入口、Q-0017、Q-0016 或 \(1/4\) 定理。E-exit schema
只是统一反例和证书格式，不是 E 质量控制定理。

## Computational

- 外层 MILP 默认只运行少量 iteration；iteration limit 不是不可行证明。
- 当前 pytest 穷尽的是 F-0029 的 24 个块顺序及相关固定回归，不是所有超图。
- `scipy.optimize.milp` 的状态必须与 incumbent 证书分开解释。

## Historical archive

本版本保留研究状态所需的历史材料和最新对话。一个体量很大的非规范
`mathcal T_4` 对话导出未逐字复制；其已确认事实、失败和当前状态已经分别进入
`knowledge/FACTS.md`、`knowledge/FAILURES.md`、`knowledge/QUESTIONS.md` 和 framework 模块。历史逐字镜像不是
本版本 claim status 的依据。

## Archive recovery

`tools/fetch_upstream_archives.py` 可在联网环境补取未逐字内嵌的非规范历史文件；这些文件不会覆盖当前框架、Facts、Failures、Questions 或 Proof DAG。
