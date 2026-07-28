# Acceptance fix: packaging, documentation integrity, and protocol split

- **Mode:** implementation
- **Canonical mathematical status promotion:** none
- **Scope:** repository engineering and documentation governance

## Changes

1. Add `pyproject.toml` and a test extra so editable installation works.
2. Upgrade the CI workflow and install from the package metadata.
3. Replace the duplicated long `agent.md` with a short mandatory protocol.
4. Keep detailed explanations and templates in `WORKFLOW.md`.
5. Add a repository check enforcing `agent.md <= 260` lines.
6. Repair Markdown/LaTeX control-character corruption.
7. Restore root compatibility pointers.
8. Distinguish local patch validation from post-merge GitHub Actions status.
9. Extend repository checks for packaging, CI, control characters, and protocol length.

## Acceptance criteria

```text
python -m pip install -e ".[test]" --no-build-isolation
python -m compileall -q src enumerate tools tests
python -m pytest -q
python tools/check_repository.py
python tools/check_generated_artifacts.py
```

GitHub Actions must be green after the patch is merged.

No canonical mathematical status was promoted.
