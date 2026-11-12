import csv
import matplotlib.pyplot as plt

filename = "structure_optimization/kpoint_validation/charge_density_convergence.csv"

cutoffs = []
energies = []

with open(filename, newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if float(row["ecutwfc_Ry"]) == 130:
            cutoffs.append(float(row["ecutrho_Ry"]))
            energies.append(float(row["total_energy_Ry"]))

reference_energy = energies[-1]
differences = [(energy - reference_energy) * 13605.693 for energy in energies]

plt.figure(figsize=(8, 5))
plt.plot(cutoffs, differences, marker="o")
plt.xlabel("Charge-density cutoff (Ry)")
plt.ylabel("Energy difference (meV/cell)")
plt.title("Charge-Density Cutoff Convergence (ecutwfc = 130 Ry)")
plt.grid(True)
plt.tight_layout()

plt.savefig(
    "structure_optimization/kpoint_validation/charge_density_energy_difference.png",
    dpi=300
)

plt.show()
