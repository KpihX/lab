.DEFAULT_GOAL := help
SHELL := /bin/zsh

UV := $(shell command -v uv 2>/dev/null || echo uv)
SRC := src
SCRIPTS := scripts
PY := $(UV) run python
KAGGLE := $(shell command -v kaggle 2>/dev/null || echo kaggle)
KAGGLE_TIMEOUT ?= 3000
NBS_LAB := nbs/lab
NBS_COLAB := nbs/colab
NBS_KAGGLE := nbs/kaggle
NBS_CIFAR := nbs/cnn-cifar10
KERNEL_LAB := ivannkamdem/kpihx-lab
KERNEL_COLAB := ivannkamdem/colab
KERNEL_KAGGLE := ivannkamdem/kaggle
KERNEL_CIFAR := ivannkamdem/cnn-cifar10

.PHONY: help sync sync-cpu sync-xpu sync-cuda kernel smoke check clean build push publish \
	lab-push lab-pull colab-push colab-pull kaggle-push kaggle-pull cifar-push cifar-pull

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

kernel: ## Register lab Jupyter kernel
	@$(PY) -m ipykernel install --user --name=lab --display-name="lab"
	@echo "✅ kernel lab ready"

check:  ## Auto-format and lint code (imports sort, format, then check on $(SCRIPTS) and $(SRC))
	@echo "📦 Sorting imports with ruff..."
	@$(UV) run ruff check --select I --fix $(SCRIPTS) $(SRC)
	@echo "📐 Formatting code with ruff format..."
	@$(UV) run ruff format $(SCRIPTS) $(SRC)
	@echo "🔍 Running final lint checks with ruff check..."
	@$(UV) run ruff check $(SCRIPTS) $(SRC)
	@echo "✅ make check passed cleanly"

build: check## Remove dist/ if present and rebuild with uv
	@rm -rf dist
	@$(UV) build
	@echo "✅ build complete in dist/"

push: check## Push current branch to ALL remotes (auto-discovered via xargs)
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

cifar-push:  ## Push + run Kaggle kernel nbs/cnn-cifar10 (ivannkamdem/cnn-cifar10)
	@$(KAGGLE) kernels push -p $(NBS_CIFAR) -t $(KAGGLE_TIMEOUT)
	@echo "✅ cifar kernel pushed"

cifar-pull:  ## Pull Kaggle kernel source into nbs/cnn-cifar10
	@$(KAGGLE) kernels pull $(KERNEL_CIFAR) -p $(NBS_CIFAR) -m
	@echo "✅ cifar kernel pulled"
