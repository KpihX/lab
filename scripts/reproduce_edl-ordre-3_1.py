"""Reproduit la figure p.6 de edl-ordre-3 : graphes de f_0 et f_1.

Figure d'origine (stylo bleu sur papier) : repere orthonorme (unite 1 cm),
courbe en pointilles annotee (C_0) pour f_0(x) = e^x, courbe continue
annotee (C_1) pour f_1(x) = x*e^x, avec minimum de f_1 en (-1, -e^-1),
limites lim_{x->-oo} x*e^x = 0, lim_{x->+oo} = +oo, et tableau de
variations : f_1' negative sur ]-oo,-1[, nulle en -1, positive apres.

Style impose : courbes bleu/rouge, quadrille #9db3d8, tick_params sans
etiquettes, docstrings.

Sortie : raw/analyse-fonctions/edl-ordre-3/assets/courbes-c0-c1.png

Usage :
  uv run scripts/reproduce_edl-ordre-3_1.py   (depuis ~/KpihX-Labs/Explore/lab/)

Exemples :
>>> # genere le PNG et affiche son chemin + taille
>>> # $ uv run scripts/reproduce_edl-ordre-3_1.py
>>> # OK -> .../assets/courbes-c0-c1.png (NNNNN o)
>>> # le rendu montre e^x (bleu) et x*e^x (rouge) avec minimum en -1.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

OUT = (
    Path.home()
    / "KpihX-Labs/Explore/sciencurious/raw/analyse-fonctions"
    "/edl-ordre-3/assets/courbes-c0-c1.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

BLUE, RED = "#1a3fb5", "red"


def main() -> None:
    """Trace f_0(x) = e^x et f_1(x) = x*e^x sur [-3, 2] et sauve le PNG."""
    x = np.linspace(-3.0, 2.0, 400)
    f0 = np.exp(x)
    f1 = x * np.exp(x)

    fig, ax = plt.subplots(figsize=(6.4, 4.8))
    ax.grid(True, color="#9db3d8", linewidth=0.6)  # papier quadrille bleu
    ax.set_axisbelow(True)
    ax.tick_params(labelbottom=False, labelleft=False, length=0)  # grille gardee, etiquettes masquees
    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.axhline(0, color=BLUE, linewidth=1.0)
    ax.axvline(0, color=BLUE, linewidth=1.0)
    ax.plot(x, f0, color=BLUE, linewidth=1.4, linestyle="--", label="(C0): e^x")
    ax.plot(x, f1, color=RED, linewidth=1.4, label="(C1): x*e^x")
    ax.plot(-1, -np.exp(-1), "o", color=RED, markersize=5)
    ax.text(-1, -np.exp(-1) - 0.35, "-e^-1", color=RED, fontsize=10, ha="center")
    ax.text(1.15, np.e + 0.3, "(C0)", color=BLUE, fontsize=11, ha="center")
    ax.text(1.15, np.e - 0.9, "(C1)", color=RED, fontsize=11, ha="center")
    ax.set_ylim(-1.5, 7.5)
    ax.set_title("f0(x) = e^x et f1(x) = x*e^x (tableau p.6)", color=BLUE, fontsize=11)
    ax.legend(loc="upper left", fontsize=9)

    fig.tight_layout()
    fig.savefig(OUT, dpi=150)
    print(f"OK -> {OUT} ({OUT.stat().st_size} o)")


if __name__ == "__main__":
    main()
