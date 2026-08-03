# Decisions

## D-0001 — Keep one active proof node

- **Status:** superseded by D-0006
- **Former decision:** `G1c / Q-0015` was the only active main-proof node.
- **Reason for supersession:** the near-lossless charging contract was found to
  conflate a sufficient recurrence mechanism with the expected mechanism of the
  \(1/4\) stability theorem.

## D-0002 — Keep three capacity ledgers separate

- **Status:** active
- **Decision:** root/configuration budget, projection-sensitive slot capacity,
  and global real-edge capacity are different resource types.
- **Reason:** feasibility in one ledger does not imply feasibility in another.
- **Consequences:** code uses distinct types and tests cross-ledger misuse.

## D-0003 — Treat raw conversations as immutable sources

- **Status:** active
- **Decision:** move raw conversations to `sources/raw/conversations/` and do not
  rewrite them.
- **Reason:** corrections belong in canonical registries and audits, while source
  chronology must remain inspectable.

## D-0004 — Reject status promotion from transition capping

- **Status:** active
- **Decision:** ordinary transition capping is not accepted as a proof of Q-0016
  or Q-0017.
- **Reason:** the required independent charging right has not been derived.
- **Related:** `knowledge/FAILURES.md`,
  `docs/framework/FW-50_PERSISTENT_BLOCKER.md`.

## D-0005 — Generated artifacts are script-owned

- **Status:** active
- **Decision:** committed experiment baselines and reports must identify their
  generator, parameters, result type, source commit, and payload hash.
- **Reason:** generated evidence must be reproducible and must not be manually
  edited.

## D-0006 — Make Route B the active proof strategy

- **Status:** active
- **Decision:** `S1 / Q-0018` is the only active main-proof node. Route B studies
  faithful global execution, exact zero-defect structure, reversible-core
  saturation, and quantitative stability.
- **Reason:** \(1/4\) need not be a \(100\%\) residual-charging theorem. Large
  unresolved mass may be evidence of a rigid critical structure rather than a
  debt that must receive an independent capacity entitlement.
- **Consequences:**
  - Q-0002/Q-0015 and the F-0042 heavy-excess recurrence are suspended as a main
    route;
  - Q-0017 is retargeted to zero-defect global normal form;
  - Q-0016 is retargeted to actual-support reversible-core saturation;
  - Q-0003–Q-0007 move into the main stability spine.
- **Reactivation rule:** Route A may be reactivated only by a new explicit
  decision and synchronized updates to `AGENTS.md`, `README.md`,
  `docs/PROJECT_STATE.yaml`, `docs/PROOF_DAG.md`, `knowledge/QUESTIONS.md`,
  `tools/check_repository.py`, and `HANDOFF_CURRENT.md`.

## D-0007 — Prove the exact theorem before the epsilon theorem

- **Status:** active
- **Decision:** Route B must first classify zero-defect faithful execution
  objects. Quantitative \(\varepsilon\)-stability is downstream.
- **Reason:** otherwise each new anomaly class risks becoming another unproved
  charging obligation, reproducing the Route-A drift.
- **Consequences:** a new defect definition is accepted only if its terms are
  natural and independently auditable; the desired binary forest, product
  support, or terminal contradiction cannot be inserted into the definition.

## D-0008 — Preserve Route-A results as supporting modules

- **Status:** active
- **Decision:** F-0034 and F-0036–F-0044 remain valid within their stated
  hypotheses and may be used inside Route B.
- **Reason:** changing the proof strategy does not refute exact mass identities,
  faithful lifts, Lyapunov laws, Hall orthogonalization, or conditional
  recurrence criteria.
- **Consequences:** using one of these modules does not reactivate the
  near-lossless charging acceptance criterion.

## D-0009 — Use pathwise Round-or-Core as the S1 finite interface

- **Status:** active
- **Decision:** `S1 / Q-0018` may use the pathwise dynamic Round-or-Core interface of F-0055. The max-flow algorithm selects a final no-copy actual-edge assignment; reverse residual arcs are not required to be actual blocker-release transitions. Root/configuration, projection-sensitive slot, and global real-edge capacities remain separate, and the first two must be fixed and verified before the actual-edge flow is invoked.
- **Reason:** the finite network theorem and pathwise realization isolate the legitimate LP content without granting every residual atom an independent charging entitlement. Any unrouteable positive mass remains actual history and must become a named exit, a stable-atlas actual core, or explicit overflow.
- **Consequences:**
  - critical-profile identification and heavy-pair aggregation remain necessary subcontracts for the global entrance/Round backend, but are not separate final endgames;
  - once a zero- or vanishing-loss faithful Round estimate is supplied, F-0038, F-0051, and F-0042 are the available conditional stability backend rather than a fourth independent immediate gap;
  - the current genuine closure map is: global faithful entrance/Round compatibility; overflow conversion; actual-support Core Endgame (Q-0016);
  - Q-0016, Q-0017, Q-0018, and the one-quarter theorem remain open.
- **Nonclaim:** F-0055 does not construct the global execution object, prove overflow structure, or classify recurrent cores.
- **Related:** D-0002, D-0006, D-0007, F-0055, Q-0016, Q-0017, Q-0018
- **Last updated:** 2026-08-01

## D-0010 — Audit chat-derived claims before canonical promotion

- **Status:** active
- **Decision:** 对话中关于 E1/E2/E3、harmonic scheduler、target-follow 或 core closure 的陈述，只有在仓库内获得自足证明或显式反例后才可登记；条件对象不得提升为 global closure。
- **Reason:** 同一讨论中多次出现先宣称闭合、随后因 release-completeness、normalization 或 actual-support 问题而降级的情况。
- **Consequences:** F-0056–F-0067 只按其精确范围登记；A-0036–A-0041 保存被否定的升级。
- **Related:** D-0007, Q-0016, Q-0018
- **Last updated:** 2026-08-03

## D-0011 — Freeze the Core bottleneck at saturated actual switch matching

- **Status:** active
- **Decision:** 不再为 Q-0016 的同一剩余箭头增加新的 core-gap 名称。当前严格子问题固定为：从饱和 completion–switch fractional matching 与实际三端点 incidence 推出 real terminal outcome 或 quantitative recurrence loss。
- **Reason:** F-0067 已完成纯匹配层的同步—分散二分；A-0041 证明纯分散不产生容量 slack，A-0042 证明继续换名不会改变 proof obligation。
- **Accepted progress:** actual expansion completeness、near-\(1/4\) link、pairwise incompatible exact cover、complete-block reduction、可计算的 strict Hall slack，或满足全部实际条件的反模型。
- **Nonprogress:** 新 phase/atlas/cut/Latin 名称，或只使用 \(P_e\) 边际的另一二分。
- **Related:** Q-0016, F-0063–F-0067, A-0041, A-0042
- **Last updated:** 2026-08-03
