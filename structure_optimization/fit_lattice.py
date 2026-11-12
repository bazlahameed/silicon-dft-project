import csv
import numpy as np
import matplotlib.pyplot as plt

# Read calculation results
with open("structure_optimization/lattice_energy.csv") as f:
    reader = csv.DictReader(f)
    data = list(reader)

a = np.array([float(row["lattice_parameter_bohr"]) for row in data])
E = np.array([float(row["total_energy_ry"]) for row in data])

# Fit the points close to the energy minimum
mask = (a >= 10.30) & (a <= 10.36)
coefficients = np.polyfit(a[mask], E[mask], 2)

# Calculate the minimum of the fitted quadratic
a_eq = -coefficients[1] / (2 * coefficients[0])
E_min = np.polyval(coefficients, a_eq)

# Convert Bohr to Angstrom
bohr_to_angstrom = 0.5291772109
a_eq_angstrom = a_eq * bohr_to_angstrom

# Generate smooth curve
a_fit = np.linspace(10.29, 10.37, 300)
E_fit = np.polyval(coefficients, a_fit)

# Plot
plt.figure(figsize=(8, 5))
plt.plot(a, E, "o", label="DFT calculations")
plt.plot(a_fit, E_fit, "-", label="Quadratic fit")
plt.axvline(a_eq, linestyle="--", label=f"Minimum = {a_eq:.5f} Bohr")
plt.xlabel("Lattice parameter (Bohr)")
plt.ylabel("Total energy (Ry)")
plt.title("Silicon: Energy vs Lattice Parameter")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("structure_optimization/energy_vs_lattice.png", dpi=300)
plt.show()

print(f"Estimated equilibrium lattice parameter: {a_eq:.6f} Bohr")
print(f"Estimated equilibrium lattice parameter: {a_eq_angstrom:.6f} Angstrom")
print(f"Minimum fitted energy: {E_min:.8f} Ry")
