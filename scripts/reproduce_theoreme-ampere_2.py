"""Complete theoreme-ampere : Cas 1 + Cas 2 (haricot, compensation 2 a 2) + forme locale.

Manuscrit : Cas 2 = contour en haricot NON enlacant le fil I ; un rayon issu de O
coupe le contour en dl (rayon r) et dl' (rayon r') avec dl/r = dl'/r' (= dtheta),
sens de parcours opposes -> B.dl + B.dl' = 0, d'ou C = 0 en sommant 2 a 2.
Style impose : grille #9db3d8, tick_params sans etiquettes, jamais axis("off").

Sortie : raw/physique/theoreme-ampere/assets/ampere-contours.png (3 panneaux)
Usage : uv run scripts/reproduce_theoreme-ampere_2.py (depuis ~/KpihX-Labs/Explore/lab/)
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

OUT = Path.home() / "KpihX-Labs/Explore/sciencurious/raw/physique/theoreme-ampere/assets/ampere-contours.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
for ax in (ax1, ax2, ax3):
    ax.set_aspect("equal")
    ax.grid(True, color="#9db3d8", linewidth=0.6)
    ax.set_axisbelow(True)
    ax.tick_params(labelbottom=False, labelleft=False, length=0)
    for s in ax.spines.values():
        s.set_visible(False)

# --- Cas 1 : fil en O, B orthoradial, contour (Gamma) enlace -> C = mu0.I
th = np.linspace(0, 2 * np.pi, 300)
for r in (0.8, 1.4, 2.0):
    ax1.plot(r * np.cos(th), r * np.sin(th), color="#1a3fb5", linewidth=1.1, alpha=0.7)
ax1.plot([0], [0], "o", color="red", markersize=10)
ax1.text(0.12, 0.12, "I", color="red", fontsize=13)
tg = np.linspace(0, 2 * np.pi, 200)
ax1.plot(1.7 * np.cos(tg), 1.7 * np.sin(tg), color="black", linewidth=2.0)
ax1.annotate("", xy=(-1.7, 0.15), xytext=(-1.55, 0.7),
             arrowprops=dict(arrowstyle="->", color="black", lw=1.6))
ax1.text(1.75, 0.1, "(G)", fontsize=12)
ax1.text(-2.6, 2.6, "C = mu0.I", color="black", fontsize=11)
ax1.set_xlim(-3, 3)
ax1.set_ylim(-3, 3)
ax1.set_title("Cas 1 : courant enlace", fontsize=11)

# --- Cas 2 : haricot non enlace, compensation 2 a 2 -> C = 0
t = np.linspace(0, 2 * np.pi, 600)
bx = 2.1 + 0.95 * np.cos(t) + 0.25 * np.cos(2 * t)
by = 1.25 * np.sin(t) - 0.25 * np.sin(2 * t)
ax2.plot(bx, by, color="black", linewidth=2.0)
# rayon issu de O (y = 0) : intersections proches/lointaines
idx = np.where(np.diff(np.sign(by)))[0]
cross = []
for i in idx:
    a = (0 - by[i]) / (by[i + 1] - by[i])
    cross.append(bx[i] + a * (bx[i + 1] - bx[i]))
cross = sorted(x for x in cross if x > 0.3)
r_near, r_far = cross[0], cross[-1]
# cercles de B passant par les deux traversées
for r in (r_near, r_far):
    a = np.linspace(-0.35, 0.35, 60)
    ax2.plot(r * np.cos(a), r * np.sin(a), color="#1a3fb5", linewidth=1.4)
    ax2.annotate("", xy=(r * np.cos(0.35), r * np.sin(0.35)),
                 xytext=(r * np.cos(0.22), r * np.sin(0.22)),
                 arrowprops=dict(arrowstyle="->", color="#1a3fb5", lw=1.4))
# rayon de coupe
ax2.plot([0, r_far + 0.6], [0, 0], color="black", linewidth=0.8, linestyle="--")
# elements dl (sens contour) opposes, B de meme sens
ax2.annotate("", xy=(r_near, -0.55), xytext=(r_near, 0.35),
             arrowprops=dict(arrowstyle="->", color="black", lw=1.8))
ax2.annotate("", xy=(r_far, 0.55), xytext=(r_far, -0.35),
             arrowprops=dict(arrowstyle="->", color="black", lw=1.8))
ax2.plot([r_near], [0], "o", color="black", markersize=5)
ax2.plot([r_far], [0], "o", color="black", markersize=5)
ax2.text(r_near - 0.75, 0.75, "dl, r", fontsize=10)
ax2.text(r_far + 0.08, -1.0, "dl', r'", fontsize=10)
ax2.plot([0], [0], "o", color="red", markersize=10)
ax2.text(0.12, 0.15, "I (O)", color="red", fontsize=11)
ax2.text(0.1, -2.55, "dl/r = dl'/r' -> C = 0", color="black", fontsize=11)
ax2.set_xlim(-1.2, 4.2)
ax2.set_ylim(-3, 3)
ax2.set_title("Cas 2 : haricot, compensation 2 a 2", fontsize=11)

# --- Forme locale : surface (S) traversee par j, bordee par (Gamma)
sx = np.array([-1.5, 1.5, 1.5, -1.5, -1.5])
sy = np.array([-1.2, -1.2, 1.2, 1.2, -1.2])
ax3.fill(sx, sy, color="#1a3fb5", alpha=0.12)
ax3.plot(sx, sy, color="black", linewidth=2.0)
for xx in np.linspace(-1.1, 1.1, 6):
    ax3.annotate("", xy=(xx, -0.4), xytext=(xx, -1.6),
                 arrowprops=dict(arrowstyle="->", color="red", lw=1.4))
ax3.text(0.15, 1.35, "(S), j", color="red", fontsize=11)
ax3.text(1.6, 0.0, "(G)", fontsize=12)
ax3.text(-2.6, -2.5, "mu0.j = rot(B)", color="black", fontsize=11)
ax3.set_xlim(-3, 3)
ax3.set_ylim(-3, 3)
ax3.set_title("Forme locale", fontsize=11)

fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"OK -> {OUT} ({OUT.stat().st_size} o)")
