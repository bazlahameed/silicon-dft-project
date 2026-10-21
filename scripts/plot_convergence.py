import csv
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

project_dir = Path(__file__).resolve().parent.parent
data_file = project_dir / "convergence" / "convergence_results.csv"
output_file = project_dir / "figures" / "energy_vs_cutoff.png"

cutoffs = []
energies = []

with data_file.open(newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        cutoffs.append(float(row["ecutwfc_Ry"]))
        energies.append(float(row["total_energy_Ry"]))

reference_energy = energies[-1]
energy_differences_meV = [
    (energy - reference_energy) * 13605.693
    for energy in energies
]

fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))

axes[0].plot(cutoffs, energies, "o-", color="navy")
axes[0].set_xlabel("Wavefunction cutoff (Ry)")
axes[0].set_ylabel("Total energy (Ry)")
axes[0].set_title("Silicon cutoff convergence")
axes[0].grid(True, alpha=0.3)

axes[1].plot(cutoffs, energy_differences_meV, "s-", color="darkred")
axes[1].set_xlabel("Wavefunction cutoff (Ry)")
axes[1].set_ylabel("Energy above 70 Ry result (meV/cell)")
axes[1].set_title("Energy difference from 70 Ry")
axes[1].grid(True, alpha=0.3)

fig.tight_layout()
fig.savefig(output_file, dpi=300)
print(f"Plot saved to: {output_file}")
