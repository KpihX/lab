# lab — TODO

## Train hooks (hook-oriented)

- [ ] Add a lightweight **hook-oriented** train primitive (style `torch.nn` / same gesture as `FocalLoss`): `TrainLoop` + hooks (`PrintHook`, `MetricHook`, `ValHook`, `CheckpointHook` with `freq` + `keep_last`).
- [ ] **Placement:** `src/lab/ai/` package exists (`ai.py` holds `class_eval`; `torch.py` stub). Put train hooks under that package (e.g. `lab.ai.train` or sibling module inside `lab.ai`). Do not scatter a rigid `train()` in notebooks.
- [ ] Goal: reusable space for any future DL train (optim / scheduler / val at freq / print / periodic save + rolling last-k), without a rigid one-shot function.

## Package layout & Architecture

- [x] Promote `src/lab/ai.py` → `src/lab/ai/` package (`lab.ai.ai` = `class_eval`; package `__init__` re-exports). Future: train hooks, split modules without growing a single file.
- [ ] Maintain strict encapsulation rule in all `__init__.py`: direct import only for submodules matching package name, never leak framework-specific dependencies (e.g. `torch`) into non-framework packages.

## Quality & Automation

- [ ] Fix formatting in `src/lab/ai/ai.py` (line-length and import ordering warnings under ruff).
- [ ] Audit and remove leftover temporary datasets (`/tmp/tvtest`) and clean duplicate files in `nbs/cnn-cifar10/`.
