import csv
import numpy as np
import matplotlib.pyplot as plt

# Read the calculated lattice parameters and total energies
with open("structure_optimization/final_lattice_energy.csv") as f:
    reader = csv.DictReader(f)
    data = list(reader)

a = np.array([float(row["lattice_parameter_Bohr"]) for row in data])
E = np.array([float(row["total_energy_Ry"]) for row in data])

# Fit a quadratic polynomial to all five points
coefficients = np.polyfit(a, E, 2)
fit = np.poly1d(coefficients)

# Find the minimum of the fitted parabola
a0 = -coefficients[1] / (2 * coefficients[0])
E_min = fit(a0)

# Convert Bohr to Angstrom
a0_angstrom = a0 * 0.529177210903

print("Quadratic fit using all five data points")
print(f"Estimated equilibrium lattice parameter: {a0:.6f} Bohr")
print(f"Estimated equilibrium lattice parameter: {a0_angstrom:.6f} Angstrom")
print(f"Estimated minimum energy: {E_min:.8f} Ry")

# Generate fitted curve
a_smooth = np.linspace(min(a), max(a), 300)
E_smooth = fit(a_smooth)

plt.figure(figsize=(8, 5))
plt.scatter(a, E, label="DFT calculated points")
plt.plot(a_smooth, E_smooth, label="Quadratic fit")
plt.scatter(a0, E_min, marker="*", s=150, label="Estimated minimum")
plt.xlabel("Lattice parameter (Bohr)")
plt.ylabel("Total energy (Ry)")
plt.title("Silicon: Total Energy vs. Lattice Parameter")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("structure_optimization/final_energy_vs_lattice.png", dpi=300)
plt.show()
