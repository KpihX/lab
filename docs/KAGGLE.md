# Kaggle workflow (kpihx-lab)

Canonical CLI detail lives in `k-ai/references/kaggle.md`. This page is the lab-facing distill: kernels, datasets, mounts, outputs.

## Layout

| Path | Role |
|---|---|
| `nbs/lab` · `nbs/colab` · `nbs/kaggle` | Kernel folders (`kernel-metadata.json` + notebook) |
| `assets/inputs/` | Local dataset sources (gitignored) |
| `assets/outputs/` | **Default sink** for kernel run artefacts |

From a notebook folder, outputs are always `../../assets/outputs`.

## Kernels (push / pull / output)

| Name | Folder | Slug |
|---|---|---|
| lab | `nbs/lab` | `ivannkamdem/kpihx-lab` |
| colab | `nbs/colab` | `ivannkamdem/colab` |
| kaggle | `nbs/kaggle` | `ivannkamdem/kaggle` |

```bash
# from repo root
make lab-push      # kaggle kernels push -p nbs/lab -t 60
make lab-pull      # kaggle kernels pull ivannkamdem/kpihx-lab -p nbs/lab -m
make colab-push
make colab-pull
make kaggle-push
make kaggle-pull

# outputs of a finished run → assets/outputs
kaggle kernels output ivannkamdem/colab -p assets/outputs
# or from nbs/colab:
kaggle kernels output ivannkamdem/colab -p ../../assets/outputs

kaggle kernels status <owner>/<slug>
kaggle kernels logs <owner>/<slug> -f
```

Slug comes from the notebook URL (`kaggle.com/code/owner/KERNEL-SLUG`), length ≥ 5. Wrong slug → permission / 404.

## Datasets (create / version / download)

There is **no** `kaggle datasets pull`. Use `download` or `kagglehub`.

```bash
kaggle datasets init -p assets/inputs/mail-sample   # → dataset-metadata.json
# edit metadata, then first publish:
kaggle datasets create -p assets/inputs/mail-sample          # private
kaggle datasets create -p assets/inputs/mail-sample -u       # -u = public

kaggle datasets version -p assets/inputs/mail-sample -m "notes"
kaggle datasets metadata ivannkamdem/mail-sample -p assets/inputs/mail-sample --update

kaggle datasets download ivannkamdem/mail-sample -p assets/inputs/mail-sample --unzip
kaggle datasets list -m
```

## Stacking on a Kaggle notebook

| Mechanism | Effect |
|---|---|
| `dataset_sources` / Add Input | Dataset mounted under `/kaggle/input/...` |
| `kernel_sources` | Upstream kernel outputs mounted under `/kaggle/input/<slug>/` |
| `kagglehub.dataset_download` **on Kaggle** | Cache attach/mount; returns `/kaggle/input/datasets/...` |

On a Kaggle notebook, `output_dir` and `force_download` are **ignored** (by design). Read the returned path (or the Add Input mount). Locally, those flags work via the HTTP resolver.

```python
import kagglehub
from pathlib import Path

root = Path(kagglehub.dataset_download("ivannkamdem/mail-sample"))
# optional lazy: polars.scan_csv(root / "mail_sample.csv")
```

Background download is not a kagglehub flag: run a separate process if you need it. On Kaggle, attach/mount is usually enough.

## Make vs CLI

| Make | Equivalent |
|---|---|
| `make lab-push` / `lab-pull` | push/pull `nbs/lab` ↔ `ivannkamdem/kpihx-lab` |
| `make colab-push` / `colab-pull` | push/pull `nbs/colab` ↔ `ivannkamdem/colab` |
| `make kaggle-push` / `kaggle-pull` | push/pull `nbs/kaggle` ↔ `ivannkamdem/kaggle` |

Timeout default: `KAGGLE_TIMEOUT=60` (override: `make lab-push KAGGLE_TIMEOUT=300`).
