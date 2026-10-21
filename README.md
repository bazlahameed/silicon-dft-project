First-Principles Study of Bulk Silicon Using DFT

A computational materials science project investigating the total-energy convergence of crystalline silicon using Density Functional Theory (DFT) and Quantum ESPRESSO.

Methods

Self-consistent field (SCF) calculations using the PBE exchange-correlation functional

Plane-wave cutoff convergence study (30–70 Ry)

Brillouin-zone k-point convergence study (4×4×4 to 12×12×12)

Python-based visualization of convergence results

Key Results

Identified 60 Ry as a reasonable provisional wavefunction cutoff.

Evaluated total-energy convergence across k-point meshes, with 12×12×12 selected as a provisional sampling grid.

Documented calculation inputs, output logs, numerical data, and convergence plots for reproducibility.

Tools

Quantum ESPRESSO · DFT · Python · Matplotlib · Linux/WSL · Git/GitHub

Repository Contents

convergence/ — cutoff study data and calculation files

kpoints/ — k-point study data and calculation files

figures/ — convergence plots

scripts/ — Python plotting scripts

Scope: Establishes baseline SCF calculations and numerical convergence tests for future electronic-structure analysis.
