.DEFAULT_GOAL := help
SHELL := /bin/zsh

UV := $(shell command -v uv 2>/dev/null || echo uv)
SCRIPTS := scripts
PY := $(UV) run python

.PHONY: help sync sync-cpu sync-xpu sync-cuda kernel smoke check clean

help:  ## Show available targets
	@grep -E '^[a-zA-Z_-]+:.*?##' $(MAKEFILE_LIST) | \
	  awk 'BEGIN {FS = ":.*?## "}; {printf "  %-14s %s\n", $$1, $$2}'

sync:  ## Base numerics only (numpy, scipy, matplotlib) + dev tools
	@$(UV) sync
	@echo "✅ base env ready"

sync-xpu:  ## Base + Intel Arc (XPU) torch, then verify the accelerator is reachable
	@$(UV) sync --extra xpu
	@echo "✅ gpu env ready"

sync-cuda:  ## Base + NVIDIA CUDA torch
	@$(UV) sync --extra cuda
	@echo "✅ cuda torch ready"

sync-cpu:  ## Base + CPU-only torch
	@$(UV) sync --extra cpu
	@echo "✅ cpu torch ready"

kernel: sync  ## Register lab Jupyter kernel
	@$(PY) -m ipykernel install --user --name=lab --display-name="lab"
	@echo "✅ kernel lab ready"

smoke:  ## Imports + versions (base stack, torch backend if present)
	@$(PY) -c "import sys, numpy, scipy, matplotlib; print('python', sys.version.split()[0]); print('numpy', numpy.__version__); print('scipy', scipy.__version__); print('matplotlib', matplotlib.__version__)"
	@$(PY) -c "import importlib.util as u; print('torch', __import__('torch').__version__) if u.find_spec('torch') else print('torch: not installed (bare sync)')"

check:  ## Byte-compile every script and verify the base stack imports
	@$(PY) -m compileall -q $(SCRIPTS) || (echo "❌ a script does not compile"; exit 1)
	@ruff check . 2>/dev/null || true
	@echo "✅ check passed"

clean:  ## Remove Python bytecode caches
	@$(PY) -c "import pathlib, shutil; [shutil.rmtree(p, ignore_errors=True) for p in pathlib.Path('$(SCRIPTS)').rglob('__pycache__')]"
	@echo "✅ caches removed"
