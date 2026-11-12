# First-Principles Investigation of Bulk Silicon Using Density Functional Theory

## Project Overview

This project investigates the electronic-structure calculation workflow and ground-state total energy of bulk silicon using Density Functional Theory (DFT) with Quantum ESPRESSO.

The work focuses on understanding how computational parameters influence the reliability of self-consistent field (SCF) total-energy calculations. It includes plane-wave cutoff convergence, charge-density cutoff convergence, k-point sampling convergence, and lattice-parameter optimisation.

This is an independent computational learning and portfolio project.

## Objectives

- Perform first-principles SCF calculations for crystalline silicon.
- Investigate convergence with respect to plane-wave kinetic-energy cutoff.
- Examine the effect of charge-density cutoff on total energy.
- Study Brillouin-zone sampling using different Monkhorst-Pack k-point meshes.
- Estimate the equilibrium lattice parameter through total-energy calculations and quadratic fitting.
- Develop experience in computational materials physics, data analysis, and scientific visualisation.

## Computational Methodology

- **Method:** Density Functional Theory (DFT)
- **Software:** Quantum ESPRESSO (`pw.x`)
- **Exchange-correlation functional:** Perdew-Burke-Ernzerhof (PBE) within the GGA
- **Pseudopotential:** Si PBE ultrasoft pseudopotential
- **Crystal structure:** Diamond-cubic silicon
- **Calculation type:** Self-consistent field (SCF)
- **Convergence threshold:** `1.0 × 10⁻⁸`

The calculations use a two-atom primitive cell of silicon.

## Convergence Studies

### 1. Plane-Wave Cutoff Convergence

The wavefunction kinetic-energy cutoff (`ecutwfc`) was varied from 30 to 70 Ry while keeping the charge-density cutoff and k-point mesh fixed.

The study examines the change in total energy as the plane-wave basis set is increased.

Results and plots are available in:
- `convergence/convergence_results.csv`
- `figures/energy_vs_cutoff.png`

### 2. K-Point Convergence

Brillouin-zone sampling was investigated using 4×4×4, 6×6×6, 8×8×8, 10×10×10, and 12×12×12 k-point meshes.

Results and plots are available in:
- `kpoints/kpoint_convergence.csv`
- `figures/energy_vs_kpoints.png`

### 3. Higher-Cutoff Validation

Additional calculations were performed using higher wavefunction and charge-density cutoffs to examine the stability of the total-energy results.

These tests are documented in:
- `structure_optimization/kpoint_validation/`

## Lattice-Parameter Optimisation

Total-energy calculations were performed at different conventional cubic lattice parameters.

A refined scan used the following settings:

| Parameter | Value |
|---|---:|
| Wavefunction cutoff | 130 Ry |
| Charge-density cutoff | 720 Ry |
| K-point mesh | 16×16×16 |
| SCF threshold | 1.0 × 10⁻⁸ |

The total energies from five lattice parameters were fitted with a quadratic polynomial to estimate the minimum-energy lattice parameter.

### Final Results

| Quantity | Result |
|---|---:|
| Fitted lattice parameter | 10.332584 Bohr |
| Fitted lattice parameter | 5.467768 Å |
| Fitted minimum total energy | −20.43944368 Ry |
| Lowest directly calculated energy | −20.43944318 Ry |
| Lattice parameter of lowest sampled point | 10.33 Bohr |

The fitted lattice parameter is an estimate obtained from the sampled total-energy data. It is not a full Birch-Murnaghan equation-of-state determination.

The final dataset and plot are available in:
- `structure_optimization/final_lattice_energy.csv`
- `structure_optimization/final_energy_vs_lattice.png`

## Repository Structure

```text
.
├── convergence/
│   ├── convergence_results.csv
│   └── SCF input and output files
├── figures/
│   ├── energy_vs_cutoff.png
│   └── energy_vs_kpoints.png
├── kpoints/
│   ├── kpoint_convergence.csv
│   └── SCF input and output files
├── scripts/
│   └── plotting scripts
├── structure_optimization/
│   ├── final_lattice_energy.csv
│   ├── final_energy_vs_lattice.png
│   ├── fit_final_lattice.py
│   └── SCF input and output files
├── si.scf.in
└── si.scf.out
```

## Tools and Skills

- Quantum ESPRESSO
- Density Functional Theory
- Computational Condensed Matter Physics
- Python
- NumPy
- Matplotlib
- CSV-based data analysis
- Scientific plotting
- Linux command-line workflows
- Convergence testing and numerical analysis

## Limitations and Future Work

This project focuses on ground-state total-energy calculations and numerical convergence for bulk silicon.

Further work could include:
- Electronic band-structure calculations.
- Density of states (DOS).
- Comparison of calculated structural properties with published reference values.
- Phonon calculations and dynamical stability analysis.
- Extension to semiconductor materials and two-dimensional systems.

## Author

**Bazla Hameed**

GitHub: https://github.com/bazlahameed/silicon-dft-project
