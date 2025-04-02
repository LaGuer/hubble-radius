import scipy.constants as const

# CODATA 2022 constants
hbar = const.hbar  # Reduced Planck's constant (J·s)
G = const.G  # Gravitational constant (m^3·kg^−1·s^−2)
m_p = const.proton_mass  # Proton mass (kg)
m_e = const.electron_mass  # Electron mass (kg)
m_n = const.neutron_mass  # Neutron mass (kg)
alpha = const.alpha  # Fine-structure constant (dimensionless)
lambda_e = const.hbar / (m_e * const.c)  # Electron Compton wavelength (m)
k_B = const.Boltzmann  # Boltzmann constant (J·K^−1)

# List of 48 formulas (shortened to examples for clarity)
formulas = [
    lambda: hbar**2 / (G * m_p * m_e * m_n),  # Example 1
    lambda: hbar * m_e / (G * m_p**2),        # Example 2
    lambda: lambda_e**2 / (G * m_p),          # Example 3
    lambda: alpha * lambda_e / (m_p * m_n),   # Example 4
    # ... Continue adding formulas from the list
]

# Compute results and validate
results = []
for i, formula in enumerate(formulas, start=1):
    try:
        result = formula()
        results.append((i, result))
    except Exception as e:
        results.append((i, f"Error: {e}"))

# Display results
for i, result in results:
    print(f"Formula {i}: {result}")
