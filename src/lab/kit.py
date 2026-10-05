import os
import platform
import socket
import sys
from pathlib import Path

from lab.logo import Logo


class Context:
    """Runtime execution context and sovereign environment detection for KπX-Labs."""

    # PEP 405 Axiom: local runtime runs in a dedicated virtualenv, cloud runtimes share the system Python
    IS_LOCAL = sys.prefix != sys.base_prefix
    ROOT = Path(sys.prefix).parent if IS_LOCAL else Path.cwd()

    # Default ASCII banner: KπX_π_COMPACT size 8 with KπX-Labs badge
    LOGO = Logo.KπX_Labs

    @classmethod
    def resolve(cls, *path_segments: str) -> Path:
        """Resolve a path relative to the project root, irrespective of the active runtime."""
        return cls.ROOT.joinpath(*path_segments)

    @classmethod
    def get_info(cls) -> dict[str, str]:
        """Collect diagnostic and hardware specs across local and cloud environments."""
        if cls.IS_LOCAL:
            runtime = f"Local ({Path(sys.prefix).name})"
        elif Path("/kaggle/working").exists():
            runtime = "Kaggle Cloud Container"
        elif Path("/content").exists():
            runtime = "Google Colab Cloud"
        else:
            runtime = "Remote Server"

        device = "CPU"
        try:
            import torch
            if torch.cuda.is_available():
                device = f"CUDA {torch.version.cuda} ({torch.cuda.get_device_name(0)})"
            elif getattr(torch, "xpu", None) and torch.xpu.is_available():
                device = f"Intel XPU ({torch.xpu.get_device_name(0)})"
            else:
                device = "CPU (torch)"
        except Exception:
            if Path("/proc/driver/nvidia/version").exists():
                device = "Nvidia GPU present"

        return {
            "OS": f"{platform.system()} {platform.release()} ({platform.machine()})",
            "Host": socket.gethostname(),
            "Runtime": runtime,
            "Python": f"{platform.python_version()} @ {sys.executable}",
            "Base": str(sys.base_prefix),
            "Root": str(cls.ROOT),
            "Device": device,
        }

    @classmethod
    def display(cls, logo_str: str | None = None, stream=None) -> None:
        """Render the KπX Fastfetch-style banner and runtime metadata side-by-side."""
        info = cls.get_info()
        chosen = logo_str or cls.LOGO
        raw_art = chosen.value if hasattr(chosen, "value") else str(chosen)
        logo_lines = raw_art.rstrip("\n").splitlines()
        items = list(info.items())
        key_width = max(len(k) for k, _ in items)
        logo_width = max(len(line) for line in logo_lines)

        out = stream or sys.stdout
        print(file=out)
        total_lines = max(len(logo_lines), len(items))
        for i in range(total_lines):
            left = logo_lines[i] if i < len(logo_lines) else " " * logo_width
            if i < len(items):
                k, v = items[i]
                right = f"\033[1;36m{k:<{key_width}}\033[0m : {v}"
            else:
                right = ""
            print(f"  \033[1;34m{left}\033[0m   {right}", file=out)
        print(file=out)
