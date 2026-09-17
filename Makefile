.DEFAULT_GOAL := help
SHELL := /bin/zsh

UV := $(shell command -v uv 2>/dev/null || echo uv)
SCRIPTS := scripts
PY := $(UV) run python

.PHONY: help sync sync-llm sync-vision sync-notebook sync-gpu sync-cpu check list run clean

help:  ## Show available targets
	@grep -E '^[a-zA-Z_-]+:.*?##' $(MAKEFILE_LIST) | \
	  awk 'BEGIN {FS = ":.*?## "}; {printf "  %-14s %s\n", $$1, $$2}'

# ── Environments ────────────────────────────────────────────────────────────

sync:  ## Base numerics only (numpy, scipy, matplotlib) + dev tools
	@$(UV) sync
	@echo "✅ base env ready"

sync-llm:  ## Base + transformers/accelerate for HF model work
	@$(UV) sync --extra llm
	@echo "✅ llm env ready"

sync-vision:  ## Base + pillow/opencv
	@$(UV) sync --extra vision
	@echo "✅ vision env ready"

sync-notebook:  ## Base + JupyterLab + kernel
	@$(UV) sync --extra notebook
	@$(UV) run python -m ipykernel install --user --name lab --display-name "lab" >/dev/null 2>&1 || true
	@echo "✅ notebook env ready (kernel: lab)"

sync-gpu:  ## Base + Intel Arc (XPU) torch, then verify the accelerator is reachable
	@$(UV) sync --extra gpu-intel
	@$(UV) run python -c "import torch; ok = torch.xpu.is_available(); print('torch', torch.__version__, '| xpu available:', ok); raise SystemExit(0 if ok else 1)" \
	  || (echo "❌ torch did not get the XPU build. Check [tool.uv.index]/[tool.uv.sources] in pyproject.toml"; exit 1)
	@echo "✅ gpu env ready"

sync-cpu:  ## Base + CPU-only torch
	@$(UV) sync --extra cpu
	@echo "✅ cpu torch ready"

# ── Daily use ───────────────────────────────────────────────────────────────

list:  ## List available scripts
	@ls -1 $(SCRIPTS)/*.py 2>/dev/null | sed 's|^|  |' || echo "  (no scripts yet)"

run:  ## Run a script: make run SCRIPT=scripts/plot.py
	@test -n "$(SCRIPT)" || (echo "usage: make run SCRIPT=scripts/your_script.py"; exit 2)
	@$(UV) run $(SCRIPT)

check:  ## Byte-compile every script and verify the base stack imports
	@$(PY) -m compileall -q $(SCRIPTS) || (echo "❌ a script does not compile"; exit 1)
	@$(PY) -c "import numpy, scipy, matplotlib" || (echo "❌ base stack broken, run: make sync"; exit 1)
	@echo "✅ check passed"

clean:  ## Remove Python bytecode caches
	@$(PY) -c "import pathlib, shutil; [shutil.rmtree(p, ignore_errors=True) for p in pathlib.Path('$(SCRIPTS)').rglob('__pycache__')]"
	@echo "✅ caches removed"
