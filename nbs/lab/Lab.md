---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.19.5
  kernelspec:
    display_name: lab (3.12.12)
    language: python
    name: python3
---

```python
import numpy as np
import matplotlib.pyplot as plt
```

```python
try:
    from lab.kit import Context
except ImportError:
    !uv pip install -q "git+https://github.com/kpihx/lab.git"
    from lab.kit import Context

Context.display()
```
