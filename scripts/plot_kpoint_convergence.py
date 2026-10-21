import csv
import matplotlib.pyplot as plt

k_mesh = []
total_energy = []

with open("kpoints/kpoint_convergence.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        k_mesh.append(int(row["k_mesh"]))
        total_energy.append(float(row["total_energy_Ry"]))

plt.figure(figsize=(8, 5))
plt.plot(k_mesh, total_energy, marker="o", linestyle="-")

plt.xlabel("K-point mesh (N × N × N)")
plt.ylabel("Total energy (Ry)")
plt.title("K-point Convergence of Bulk Silicon")
plt.xticks(k_mesh)
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig("figures/energy_vs_kpoints.png", dpi=300)
print("Plot saved to figures/energy_vs_kpoints.png")

plt.show()
