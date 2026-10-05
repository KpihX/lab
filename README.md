# kpihx-lab

Scientific and AI exploration environment: one installable package (`lab`), a small CLI, notebooks, and scripts sharing the same runtime context across local, Colab, and Kaggle.

| | |
|---|---|
| **PyPI** | [`kpihx-lab`](https://pypi.org/project/kpihx-lab/) |
| **Import** | `lab` |
| **CLI** | `lab` |

## Idea

One environment, three runtimes, same code. `lab.Context` detects where you run (local venv, Colab `/content`, Kaggle `/kaggle/working`), resolves paths from the project root, and reports OS / host / Python / accelerator (CPU, CUDA, or Intel XPU). Notebooks and scripts import the same package; throwaway experiments stay out of the package itself.

## Layout

```
lab/
├── src/lab/       # installable package
├── scripts/       # durable scientific scripts (uv run)
├── nbs/           # notebooks (local / Colab / Kaggle)
├── assets/        # local data and results (gitignored)
├── docs/          # project docs (e.g. Kaggle workflow)
├── Makefile
└── pyproject.toml
```

Add scripts and notebooks freely. Do not list them here.

## Install

```bash
uv pip install kpihx-lab
# or from a clone:
uv sync
```

Hardware backends are optional extras (pick at most one torch backend):

```bash
uv sync --extra cpu    # or: make sync-cpu
uv sync --extra xpu    # or: make sync-xpu
uv sync --extra cuda   # or: make sync-cuda
```

```bash
make kernel   # register Jupyter kernel "lab"
```

## CLI

```bash
lab --help
lab context    # Context.display() using Context.LOGO (no flags)
```

The CLI does not select logos; `context` only calls `Context.display()`.

## Python API

```python
from pathlib import Path
from lab import Context, pred_eval, Logo

Context.display()
path = Context.resolve(Path("assets/inputs/example"))

results, axs = pred_eval(gts, preds, probas)
```

Default banner: `Context.LOGO` (`Logo.KπX_Labs`). Logo families and size variants live in `lab.logo`.

## Make targets

| Target | Action |
|--------|--------|
| `make sync` / `sync-cpu` / `sync-xpu` / `sync-cuda` | Sync env (base or + one torch backend) |
| `make kernel` | Register Jupyter kernel `lab` |
| `make smoke` / `check` / `clean` | Smoke imports, compileall, caches |
| `make build` | Wipe `dist/` then `uv build` |
| `make push` | Push current branch to all remotes (`git remote \| xargs`) |
| `make publish` | `build` then `uv publish` |
| `make lab-push` / `lab-pull` | Kaggle kernel `nbs/lab` ↔ `ivannkamdem/kpihx-lab` |
| `make colab-push` / `colab-pull` | Kaggle kernel `nbs/colab` ↔ `ivannkamdem/colab` |
| `make kaggle-push` / `kaggle-pull` | Kaggle kernel `nbs/kaggle` ↔ `ivannkamdem/kaggle` |

`make publish` expects PyPI credentials already in the environment of whoever runs it. The Makefile does not wrap secrets.

Kaggle kernels / datasets / mounts / outputs: see [`docs/KAGGLE.md`](docs/KAGGLE.md).

## Scripts workflow

1. Check `pyproject.toml` before adding a dependency.
2. Durable scripts that need the lab stack go in `scripts/` and run with `uv run`.
3. Missing lib: `uv add <package>` from this directory (never system `pip`).
4. One-off throwaways without lab libs go to `/tmp/`.

## Gitignore

`assets/` and `dist/` are ignored. `nbs/` stays tracked. `.venv/` is local-only.
