import inspect
import math
import os
import platform
import socket
import sys
from enum import Enum
from pathlib import Path

try:
    from IPython.display import display
except ImportError:
    display = print

from lab.logo import Logo


def var_name(obj, depth: int = 1) -> str | None:
    """Name of the variable `depth` frames above the caller that holds obj.

    Matching is by identity, never equality, so tensors that cannot be compared
    and arrays that merely share values never collide. Module dunders are
    skipped, which is what keeps `None` from being reported as `__doc__`.

    Args:
        obj: The object to name.
        depth: How many frames to walk back from the caller of this function.
            0 names obj from the caller's own frame.

    Returns:
        The variable name, or None when no frame in range binds it.
    """
    frame = inspect.currentframe()
    for _ in range(depth + 1):
        if frame is None:
            return None
        frame = frame.f_back
    while frame is not None:
        for scope in (frame.f_locals, frame.f_globals):
            for name, value in scope.items():
                if not (name.startswith("__") and name.endswith("__")) and value is obj:
                    return name
        frame = frame.f_back
    return None


def _readable(value: int) -> str:
    """Byte count in human units, exact value kept in parentheses."""
    scaled = float(value)
    for unit in ("B", "KB", "MB", "GB", "TB", "PB"):
        if abs(scaled) < 1024:
            exact = f"{value:,} B"
            return exact if unit == "B" else f"{scaled:,.1f} {unit} ({exact})"
        scaled /= 1024
    return f"{scaled:,.1f} EB ({value:,} B)"


def show(*objects, names=None, auto: bool = True, full: bool = False) -> None:
    """Print a header per object, then its repr through IPython.display.

    Works on any object: numpy array, torch tensor, list, tuple, dict, set,
    scalar. Everything is read through the attributes Python already exposes,
    so each line appears only when the object actually carries it: type,
    shape, element count, len, dtype, bytes on disk, device, and for tensors
    the autograd state (requires_grad, leaf or attached, gradient node).

    nbytes resolves in four steps, from the most faithful to the least:
    torch storage (exact), the object's own nbytes (exact for numpy and
    pandas), pandas memory_usage (exact), then sys.getsizeof (shallow).
    The last one is the size of the Python object itself and ignores whatever
    it references, so a list of three ints reports the container only, not the
    three int objects. Treat it as the object's own footprint, never as the
    footprint of a graph of objects. The same caveat applies to numel on a
    container: it is the len, and the bytes behind those elements are elsewhere.

    Args:
        objects: Any mix of objects, including a single one.
        names: Optional one-per-object names. None or missing entries fall back
            to variable detection, then to the object type.
        auto: If True, a header with no given name is resolved by var_name from
            this caller frame. False skips that lookup, so the header falls
            straight back to the object type.
        full: If True, hand each object to IPython.display so notebooks render
            rich output. False keeps only the headers.
    """
    for index, obj in enumerate(objects):
        given = names[index] if names is not None and index < len(names) else None
        title = given or (var_name(obj) if auto else None) or type(obj).__name__
        shape = getattr(obj, "shape", None)
        dtype = getattr(obj, "dtype", None)
        device = getattr(obj, "device", None)
        sized = getattr(obj, "__len__", None)
        ndim = getattr(obj, "ndim", None)
        numel = (
            obj.numel()
            if hasattr(obj, "numel")
            else (
                math.prod(obj.shape)
                if hasattr(obj, "shape")
                else (
                    sized()
                    if sized is not None and ndim != 0
                    else (1 if sized is not None else None)
                )
            )
        )
        nbytes = (
            obj.untyped_storage().nbytes()
            if hasattr(obj, "untyped_storage")
            else (
                obj.nbytes
                if hasattr(obj, "nbytes")
                else (
                    int(obj.memory_usage(deep=True).sum())
                    if hasattr(obj, "memory_usage")
                    else (sys.getsizeof(obj))
                )
            )
        )
        print(f"=== {title} ===")
        print(f"type={type(obj).__module__}.{type(obj).__name__}")
        if shape is not None:
            print(f"shape={tuple(shape)}")
        if numel is not None:
            print(f"numel={numel:,}")
        if sized is not None and ndim != 0:
            print(f"len={sized()}")
        if dtype is not None:
            print(f"dtype={dtype}")
        if nbytes is not None:
            print(f"nbytes={_readable(nbytes)}")
        if device is not None:
            print(f"device={device}")
        if hasattr(obj, "requires_grad"):
            leaf = obj.is_leaf
            print(f"requires_grad={obj.requires_grad} leaf={leaf}")
            print(f"grad_fn={obj.grad_fn.name() if obj.grad_fn else None}")
        if hasattr(obj, "named_children") and hasattr(obj, "parameters"):
            total_params = sum(p.numel() for p in obj.parameters())
            trainable_params = sum(p.numel() for p in obj.parameters() if p.requires_grad)
            line = f"\n[Layers & Parameters] total={total_params:,}"
            print(f"{line} (trainable={trainable_params:,})")
            for child_name, child in obj.named_children():
                child_total = sum(p.numel() for p in child.parameters())
                child_trainable = sum(p.numel() for p in child.parameters() if p.requires_grad)
                tag = f"  • {child_name} ({type(child).__name__}): {child_total:,} params"
                print(f"{tag} (trainable={child_trainable:,})")
        if full:
            if hasattr(obj, "named_children") and hasattr(obj, "parameters"):
                print("\n[Full Architecture & Detailed Parameters Breakdown]")
                for child_name, child in obj.named_children():
                    child_total = sum(p.numel() for p in child.parameters())
                    child_trainable = sum(p.numel() for p in child.parameters() if p.requires_grad)
                    hdr = f"\n  ┌─ {child_name} ({type(child).__name__})"
                    line = f"{hdr} ─── subtotal: {child_total:,} params"
                    print(f"{line} (trainable: {child_trainable:,})")
                    sub_children = list(child.named_children())
                    if sub_children:
                        for sub_name, sub in sub_children:
                            sub_tot = sum(p.numel() for p in sub.parameters())
                            print(f"  │  ├─ {sub_name}: {sub} -> {sub_tot:,} params")
                    else:
                        for p_name, param in child.named_parameters(recurse=False):
                            line = f"  │  ├─ {p_name}: shape={tuple(param.shape)}"
                            print(f"{line} -> {param.numel():,} params")
                    print("  └────────────────────────────────────────────────────────")
                non_trainable = total_params - trainable_params
                summary = (
                    f"\n[Model Summary] Total Parameters: {total_params:,} | "
                    f"Trainable: {trainable_params:,} | Non-trainable: {non_trainable:,}\n"
                )
                print(summary)
            else:
                display(obj)


class Runtime(Enum):
    """Where the lab code is executing."""

    LOCAL = "local"
    COLAB = "colab"
    KAGGLE = "kaggle"
    UNKNOWN = "unknown"


class Context:
    """Runtime execution context and sovereign environment detection for KπX-Labs."""

    # PEP 405 Axiom: local runtime runs in a dedicated virtualenv, cloud runtimes share the system Python
    IS_LOCAL = sys.prefix != sys.base_prefix
    ROOT = Path(sys.prefix).parent if IS_LOCAL else Path.cwd()

    # Default ASCII banner: KπX_π_COMPACT size 8 with KπX-Labs badge
    LOGO = Logo.KπX_Labs

    @classmethod
    def runtime(cls) -> Runtime:
        """Detect LOCAL / COLAB / KAGGLE; UNKNOWN otherwise (former get_info runtime chain)."""
        if cls.IS_LOCAL:
            return Runtime.LOCAL
        elif os.environ.get("KAGGLE_KERNEL_RUN_TYPE") is not None:
            return Runtime.KAGGLE
        elif os.environ.get("COLAB_RELEASE_TAG") is not None:
            return Runtime.COLAB
        else:
            return Runtime.UNKNOWN

    @classmethod
    def resolve(cls, rel_path: Path) -> Path:
        """Resolve a path relative to the project root, irrespective of the active runtime."""
        return cls.ROOT / rel_path

    @classmethod
    def device(cls, full: bool = False) -> str:
        """Detect compute device (torch CUDA/XPU, else nvidia presence, else CPU).

        Args:
            full: If True, return a human-readable description
                (e.g. ``Intel XPU (Intel(R) Arc(TM) Graphics)``).
                If False (default), return a torch-usable device string
                (``xpu:0``, ``cuda:0``, or ``cpu``).
        """
        short = "cpu"
        detail = "CPU"
        try:
            import torch

            if torch.cuda.is_available():
                short = "cuda:0"
                detail = f"CUDA {torch.version.cuda} ({torch.cuda.get_device_name(0)})"
            elif getattr(torch, "xpu", None) and torch.xpu.is_available():
                short = "xpu:0"
                detail = f"Intel XPU ({torch.xpu.get_device_name(0)})"
            else:
                short = "cpu"
                detail = "CPU (torch)"
        except Exception:
            if Path("/proc/driver/nvidia/version").exists():
                detail = "Nvidia GPU present"
        return detail if full else short

    @classmethod
    def info(cls) -> dict[str, str]:
        """Collect diagnostic and hardware specs across local and cloud environments."""
        return {
            "OS": f"{platform.system()} {platform.release()} ({platform.machine()})",
            "Host": socket.gethostname(),
            "Runtime": cls.runtime().value,
            "Python": f"{platform.python_version()} @ {sys.executable}",
            "Base": str(sys.base_prefix),
            "Root": str(cls.ROOT),
            "Device": cls.device(full=True),
        }

    @classmethod
    def display(cls, logo_str: str | None = None, stream=None) -> None:
        """Render the KπX Fastfetch-style banner and runtime metadata side-by-side."""
        info = cls.info()
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
