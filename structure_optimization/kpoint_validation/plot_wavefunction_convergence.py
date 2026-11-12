import csv
import matplotlib.pyplot as plt

filename = "structure_optimization/kpoint_validation/wavefunction_convergence.csv"

cutoffs = []
energies = []

with open(filename, newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        cutoffs.append(float(row["ecutwfc_Ry"]))
        energies.append(float(row["total_energy_Ry"]))

plt.figure(figsize=(8, 5))
plt.plot(cutoffs, energies, marker="o")
plt.xlabel("Wavefunction cutoff (Ry)")
plt.ylabel("Total energy (Ry)")
plt.title("Wavefunction Cutoff Convergence")
plt.grid(True)
plt.tight_layout()

plt.savefig(
    "structure_optimization/kpoint_validation/wavefunction_convergence.png",
    dpi=300
)

plt.show()
