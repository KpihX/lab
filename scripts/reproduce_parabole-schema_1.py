"""Reproduit le fond de parabole-schema : cone coupe par un plan -> parabole.
Image : rendu 3D (cone orange, plan bleu, courbe parabole, reperes).
Vue : cone y^2+z^2=(x)^2/4, plan oblique, intersection parabole rouge.
Sortie : raw/geometrie/parabole-schema/assets/cone-plan-parabole.png
Usage : uv run scripts/reproduce_parabole-schema_1.py (depuis ~/KpihX-Labs/Explore/lab/)
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

OUT = Path.home() / "KpihX-Labs/Explore/sciencurious/raw/geometrie/parabole-schema/assets/cone-plan-parabole.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

th = np.linspace(0, 2 * np.pi, 80)
z = np.linspace(0.15, 2.6, 40)
TH, Z = np.meshgrid(th, z)
R = Z / 2.2
X = R * np.cos(TH)
Y = R * np.sin(TH)

t = np.linspace(-1.15, 1.15, 200)
xp = t
yp = 0.55 * t ** 2 - 0.35
zp = 0.9 * t ** 2 + 0.55

fig = plt.figure(figsize=(7.5, 5))
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X, Y, Z, color="#e8a06a", alpha=0.55, edgecolor="none")
xx, yy = np.meshgrid(np.linspace(-1.4, 1.4, 20), np.linspace(-1.6, 0.6, 20))
zz = 0.9 * yy + 1.15
ax.plot_surface(xx, yy, zz, color="#9db3d8", alpha=0.35, edgecolor="none")
ax.plot(xp, yp, zp, color="red", linewidth=2.5)
ax.text(0, 0, 2.75, "cone", color="#a34d00", fontsize=10)
ax.text(1.2, -1.3, 0.2, "plan -> parabole", color="red", fontsize=10)
ax.tick_params(labelbottom=False, labelleft=False, length=0)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
