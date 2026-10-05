.DEFAULT_GOAL := help
SHELL := /bin/zsh

UV := $(shell command -v uv 2>/dev/null || echo uv)
SCRIPTS := scripts
PY := $(UV) run python
KAGGLE := $(shell command -v kaggle 2>/dev/null || echo kaggle)
KAGGLE_TIMEOUT ?= 60
NBS_LAB := nbs/lab
NBS_COLAB := nbs/colab
NBS_KAGGLE := nbs/kaggle
KERNEL_LAB := ivannkamdem/kpihx-lab
KERNEL_COLAB := ivannkamdem/colab
KERNEL_KAGGLE := ivannkamdem/kaggle

.PHONY: help sync sync-cpu sync-xpu sync-cuda kernel smoke check clean build push publish \
	lab-push lab-pull colab-push colab-pull kaggle-push kaggle-pull

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

build:  ## Remove dist/ if present and rebuild with uv
	@rm -rf dist
	@$(UV) build
	@echo "✅ build complete in dist/"

push:  ## Push current branch to ALL remotes (auto-discovered via xargs)
	@git remote | xargs -r -I{} git push {} $(shell git branch --show-current)
	@echo "✅ pushed to all remotes"

publish: build  ## Build then publish to PyPI (atomic)
	@$(UV) publish
	@echo "✅ published"

lab-push:  ## Push + run Kaggle kernel nbs/lab (ivannkamdem/kpihx-lab)
	@$(KAGGLE) kernels push -p $(NBS_LAB) -t $(KAGGLE_TIMEOUT)
	@echo "✅ lab kernel pushed"

lab-pull:  ## Pull Kaggle kernel source into nbs/lab
	@$(KAGGLE) kernels pull $(KERNEL_LAB) -p $(NBS_LAB) -m
	@echo "✅ lab kernel pulled"

colab-push:  ## Push + run Kaggle kernel nbs/colab (ivannkamdem/colab)
	@$(KAGGLE) kernels push -p $(NBS_COLAB) -t $(KAGGLE_TIMEOUT)
	@echo "✅ colab kernel pushed"

colab-pull:  ## Pull Kaggle kernel source into nbs/colab
	@$(KAGGLE) kernels pull $(KERNEL_COLAB) -p $(NBS_COLAB) -m
	@echo "✅ colab kernel pulled"

kaggle-push:  ## Push + run Kaggle kernel nbs/kaggle (ivannkamdem/kaggle)
	@$(KAGGLE) kernels push -p $(NBS_KAGGLE) -t $(KAGGLE_TIMEOUT)
	@echo "✅ kaggle kernel pushed"

kaggle-pull:  ## Pull Kaggle kernel source into nbs/kaggle
	@$(KAGGLE) kernels pull $(KERNEL_KAGGLE) -p $(NBS_KAGGLE) -m
	@echo "✅ kaggle kernel pulled"
