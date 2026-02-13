# Prime Modular Dynamics Theory (PMDT)

**Author:** Michel Monfette  
**Year:** 2026  

Prime Modular Dynamics Theory (PMDT) studies the modular dynamics of prime numbers through
the families



\[
SG(k) = \{ p \in \mathbb{P} : kp + 1 \in \mathbb{P} \}.
\]



When projected onto the 8 admissible residues modulo 30, these families reveal a rich dynamical
structure underlying the global distribution of primes. PMDT formalizes:

- a strict periodicity \(6\) in \(k\),
- three modular phases (rigid, intermediate, resonant),
- a hidden period-\(9\) resonance in gap-6 (sexy prime) transitions,
- a combined periodicity \(18\) from the interaction of periods \(6\) and \(9\).

This repository contains:

- the full LaTeX article `Prime_Modular_Dynamics_Theory.tex` and compiled PDF,  
- Python code for the complete numerical pipeline,  
- generated data (transition matrices, scores, etc.),  
- figures (heatmaps, entropy vs DB, period-9 vs k).

---

## Repository structure

```text
PMDT/
├── data/                    # .npy matrices, scores, etc.
├── figures/                 # PNG figures (heatmaps, plots)
├── src/                     # Python source code
│   ├── main.py
│   ├── sg_families_analysis.py
│   ├── heatmaps.py
│   ├── compare_sg_families.py
│   ├── cube30_orbits.py
│   ├── period9_detector.py
│   ├── period9_plot.py
│   └── pdf_report.py
├── Prime_Modular_Dynamics_Theory.tex
├── Prime_Modular_Dynamics_Theory.pdf
├── ABSTRACT.md
├── DESCRIPTION.md
├── KEYWORDS.md
├── CITATION.cff
├── LICENSE
└── README.md

cd src
python3 main.py


