#!/usr/bin/env python3
"""Render the manuscript's review formulas as high-resolution monochrome PNGs."""

from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures" / "v1.2" / "equations"

EQUATIONS = {
    "eq01_global_objective": r"\min_{\boldsymbol{w}} F(\boldsymbol{w})=\sum_{k=1}^{K}\frac{n_k}{n}F_k(\boldsymbol{w}),\qquad n=\sum_{k=1}^{K}n_k.",
    "eq02_local_and_fedavg": r"\begin{aligned}\boldsymbol{w}_{k,t}^{(e+1)}&=\boldsymbol{w}_{k,t}^{(e)}-\eta_t\nabla F_k\!\left(\boldsymbol{w}_{k,t}^{(e)};\xi_{k,e}\right),\\[2pt]\boldsymbol{w}_{t+1}&=\sum_{k\in\mathcal{S}_t}\frac{n_k}{\sum_{j\in\mathcal{S}_t}n_j}\boldsymbol{w}_{k,t}^{(E)}.\end{aligned}",
    "eq03_total_communication": r"C_{\mathrm{total}}=\sum_{t=1}^{T}\!\left(B_t^{\downarrow}+\sum_{k\in\mathcal{S}_t}B_{k,t}^{\uparrow}+B_t^{\mathrm{ctrl}}\right).",
    "eq04_uplink_latency": r"\tau_{k,t}^{\mathrm{up}}=\frac{B_{k,t}^{\uparrow}}{R_{k,t}},\qquad R_{k,t}=W_{k,t}\log_2\!\left(1+\frac{p_{k,t}h_{k,t}}{N_0W_{k,t}}\right).",
    "eq05_compression_ratio": r"\rho_{k,t}=\frac{B_{k,t}^{\mathrm{comp}}}{B_{k,t}^{\mathrm{orig}}},\qquad 0<\rho_{k,t}\leq 1.",
    "eq06_aircomp": r"\boldsymbol{y}_t=\sum_{k\in\mathcal{S}_t}h_{k,t}b_{k,t}\boldsymbol{g}_{k,t}+\boldsymbol{n}_t\;\approx\;\gamma_t\sum_{k\in\mathcal{S}_t}\alpha_{k,t}\boldsymbol{g}_{k,t}+\boldsymbol{n}_t.",
    "eq07_hierarchical": r"\boldsymbol{w}_{\ell,r}=\sum_{k\in\mathcal{C}_\ell}\alpha_{k,\ell}\boldsymbol{w}_{k,r},\qquad \boldsymbol{w}_{r+1}=\sum_{\ell=1}^{L}\beta_\ell\boldsymbol{w}_{\ell,r}.",
}

TEMPLATE = r"""\documentclass[12pt,border=3pt]{standalone}
\usepackage{amsmath,amssymb,bm}
\begin{document}
$\displaystyle %s$
\end{document}
"""


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="fpwriting-equations-") as tmp_name:
        tmp = Path(tmp_name)
        for name, formula in EQUATIONS.items():
            tex = tmp / f"{name}.tex"
            tex.write_text(TEMPLATE % formula, encoding="utf-8")
            subprocess.run(
                ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "-output-directory", str(tmp), str(tex)],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.STDOUT,
            )
            subprocess.run(
                ["pdftocairo", "-png", "-singlefile", "-r", "600", str(tmp / f"{name}.pdf"), str(OUT / name)],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.STDOUT,
            )
    print(OUT)


if __name__ == "__main__":
    main()
