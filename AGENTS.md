# Explore/lab — kpihx-lab

**Purpose:** Shared scientific and AI exploration environment (package `lab`, CLI `lab`, notebooks, scripts). Rapid prototyping across local / Colab / Kaggle with one `Context`.

**PyPI name:** `kpihx-lab` · **Import / CLI:** `lab`

## Rules (MANDATORY)

### Scripts Location
- **Quick throwaway scripts → `/tmp/`** — always. This is the default for any one-off script.
- **Scripts that need scientific libraries (numpy, matplotlib, scipy, etc.) → `scripts/`** in this lab — create them here and use the libs already installed.
- **Do not inventory every new `.py` / `.ipynb` in README.md.** README stays generic (roles + how to run). Notebooks live under `nbs/`; durable scripts under `scripts/`.

### Package and CLI
- Installable package is `src/lab/` (import `lab`). Entry point: `lab` → `lab.cli:app`.
- CLI command `lab context` calls `Context.display()` only (uses `Context.LOGO`). No logo selection in the CLI. No root/default app command that prints logos.
- Public API surface: `Context`, `pred_eval`, `Logo` families (see `lab/__init__.py`).

### Dependency Management
- **100% uv in this lab. NEVER pip. NEVER `python -m pip`. NEVER `uv pip` for agent work.**
- Base stack and optional extras (`cpu` / `xpu` / `cuda`) live in `pyproject.toml`. Check it before adding.
- To add a library: `uv add <package>` from this directory.
- To run a script: `uv run scripts/your_script.py`
- Hardware: at most one torch backend extra (`make sync-cpu` / `sync-xpu` / `sync-cuda`, or `uv sync --extra …`).

### Makefile (atomic targets)
- `make build` — wipe `dist/` then `uv build`
- `make push` — push current branch to all remotes (`git remote | xargs`)
- `make publish` — `build` then bare `uv publish` (no secret wrappers in the Makefile; the runner supplies credentials)
- Do not fold repo creation or remote bootstrap into `publish`.
- Kaggle kernels (see `docs/KAGGLE.md`): `make lab-push` / `lab-pull`, `colab-push` / `colab-pull`, `kaggle-push` / `kaggle-pull`. Kernel outputs default to `assets/outputs/` (`../../assets/outputs` from `nbs/<name>/`).

### Assets vs notebooks
- `assets/` is gitignored (local inputs / results). Prefer `assets/inputs/` for dataset sources and `assets/outputs/` for kernel run artefacts.
- `nbs/` is tracked. Keep notebooks; do not put heavy artefacts under `nbs/`.
- Kaggle ops for this lab: `docs/KAGGLE.md` (distill). Full CLI inventory: `k-ai/references/kaggle.md`.

### Workflow
1. Check `pyproject.toml` for available libs.
2. If the lib you need is there → create script in `scripts/`, run with `uv run`.
3. If the lib is missing → `uv add <package>`, then create + run.
4. One-off throwaway → `/tmp/` (no lab-lib dependency expected).
5. Need runtime banner / path root → `from lab import Context` then `Context.display()` / `Context.resolve(Path(...))`.
