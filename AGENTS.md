# Explore/lab — Scientific Quick Scripts

**Purpose:** Shared scientific Python environment for rapid exploration, plotting, and computation.

## Rules (MANDATORY)

### Scripts Location
- **Quick throwaway scripts → `/tmp/`** — always. This is the default for any one-off script.
- **Scripts that need scientific libraries (numpy, matplotlib, scipy, etc.) → `~/KpihX-Labs/Explore/lab/scripts/`** — create them here and use the libs already installed.

### Dependency Management
- **100% uv in this lab. NEVER pip. NEVER `python -m pip`. NEVER `uv pip`.**
- Libraries already available: `numpy`, `matplotlib`, `scipy` (see `pyproject.toml`).
- To add a new library: `uv add <package>` from this directory.
- To run a script: `uv run scripts/your_script.py`
- Always check `pyproject.toml` before adding — the lib may already be there.

### Workflow
1. Check `pyproject.toml` for available libs.
2. If the lib you need is there → create script in `scripts/`, run with `uv run`.
3. If the lib is missing → `uv add <package>`, then create + run.
4. One-off throwaway → `/tmp/` (no lib dependency expected).
