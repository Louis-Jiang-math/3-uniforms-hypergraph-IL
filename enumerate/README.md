# enumerate

本目录统一存放可复算枚举代码、原始机器输出和对结果的数学分析。根目录文档可以引用这里的结论，但必须区分：

- `confirmed_computational`：由脚本和结果文件复算；
- `confirmed`：另有完整数学证明；
- `observed`：只在有限搜索中出现；
- `open`：枚举尚未覆盖的一般结构问题。

## Q-0015 文件

- `q0015_configuration_auditor.py`：依据 `SINGLE_DEFECT_FRAMEWORK.md` v0.4/v0.5 重建的真实执行审计器；包括配置枚举、root-pivot 预算 LP、对偶、固定预算槽位流、全局真实边流和外层 MILP。
- `q0015_first_execution_results.json`：首轮机器原始结果和 100 轮外层日志。
- `q0015_first_execution_report.md`：首轮可读报告及后续精确参数升级说明。
- `q0015_hall_cut_structural_analysis.json`：144 个 root group 的结构摘要。
- `q0015_hall_cut_structural_analysis.md`：Hall cut、genealogy、no-configuration 和 \((3,14,2)\) 精确排除的数学分析。
- `manifest.json`：机器文件角色、历史运行状态与后续严格结论之间的可机读索引。

## 运行

```bash
python enumerate/q0015_configuration_auditor.py \
  --iterations 100 \
  --time-limit 3
```

默认输出目录是 `enumerate/run/`；该目录只保存重新运行产物，不覆盖已归档的历史 JSON/报告。依赖版本见根目录 `requirements.txt`。脚本是依据公开 Markdown 规格的独立重建，不声称与未提交的历史实现逐字一致。

## 归档约定

后续枚举采用：

```text
enumerate/<question-id>_<experiment>.py
enumerate/<question-id>_<experiment>_results.json
enumerate/<question-id>_<experiment>_report.md
```

报告必须记录参数、版本、随机种子/确定规则、求解状态、超时与数学结论之间的区别。
