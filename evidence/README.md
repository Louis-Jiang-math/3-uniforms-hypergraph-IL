# Evidence and implementation support

- `audits/`: independent repository or claim audits;
- `experiments/`: generated baselines, run reports, and historical outputs;
- `proofs/`: complete proof files when separated from framework documents;
- `certificates/`: machine-verifiable certificates or validation records.

Knowledge registries should link here rather than embedding full logs. Generated artifacts must be reproduced through their recorded generator and must pass `tools/check_generated_artifacts.py`.
