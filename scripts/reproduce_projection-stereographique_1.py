"""Reproduit le fond de projection-stereographique : cercle, tangente en S, rayons depuis N.
Manuscrit : M(x,y), droite m tan(theta), formules f = ... , tableau de var. de f.
Vue : cercle unite, pole N(haut), point M sur cercle, projete m sur tangente basse.
Sortie : raw/geometrie/projection-stereographique/assets/projection-stereo.png
Usage : uv run scripts/reproduce_projection-stereographique_1.py (depuis ~/KpihX-Labs/Explore/lab/)
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

OUT = Path.home() / "KpihX-Labs/Explore/sciencurious/raw/geometrie/projection-stereographique/assets/projection-stereo.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

th = np.linspace(0, 2 * np.pi, 400)
fig, ax = plt.subplots(figsize=(6.5, 6))
ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-1.6, 2.2)
ax.set_aspect("equal")
ax.grid(True, color="#9db3d8", linewidth=0.6)
ax.set_axisbelow(True)
ax.tick_params(labelbottom=False, labelleft=False, length=0)
for s in ax.spines.values():
    s.set_visible(False)

ax.plot(np.cos(th), np.sin(th), color="#1a3fb5", linewidth=1.8)
N = np.array([0.0, 1.0])
S = np.array([0.0, -1.0])
for ang in (35, 60, 110, 145):
    a = np.deg2rad(ang)
    M = np.array([np.cos(a), np.sin(a)])
    t = (S[1] - N[1]) / (M[1] - N[1])
    P = N + t * (M - N)
    ax.plot([N[0], P[0]], [N[1], P[1]], color="red", linewidth=1.0, alpha=0.8)
    ax.plot(M[0], M[1], "o", color="#1a3fb5", markersize=5)
ax.plot(N[0], N[1], "o", color="red", markersize=8)
ax.axhline(-1, color="black", linewidth=1.2)
ax.text(0.08, 1.05, "N (pole)", color="red", fontsize=10)
ax.text(0.08, -1.25, "tangente en S", color="black", fontsize=10)
ax.text(-1.7, 0.4, "M(x,y) -> m", color="#1a3fb5", fontsize=10)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
