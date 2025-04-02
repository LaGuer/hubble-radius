import scipy.constants as const
import numpy as np

# CODATA 2022 constants
hbar = const.hbar  # Reduced Planck's constant (J·s)
G = const.G  # Gravitational constant (m^3·kg^−1·s^−2)
m_p = const.proton_mass  # Proton mass (kg)
m_e = const.electron_mass  # Electron mass (kg)
m_n = const.neutron_mass  # Neutron mass (kg)
alpha = const.alpha  # Fine-structure constant (dimensionless)
lambda_e = const.hbar / (m_e * const.c)  # Electron Compton wavelength (m)
L_planck = np.sqrt(hbar * G / const.c**3)  # Planck length (m)
k_B = const.Boltzmann  # Boltzmann constant (J·K^−1)

# Conversion constants
meters_to_gly = 1 / (const.c * 3.1536e16 * 1e9)  # Convert meters to gigalight-years

# Calculate P
P = lambda_e / L_planck  # Ratio of Compton wavelength to Planck length

# Formula to evaluate: precision theory formula
def precision_formula(P, alpha, lambdabare):
    return (lambdabare * np.exp((np.e**(4 * np.e - 1 / alpha) - np.log(P**4 / alpha**3)**2) / 2))**0.5

# JWST measured value (placeholder)
jwst_measured_value = 1.31871e+25  # Replace with actual measured value in meters

# Calculate and compare precision
result_precision = precision_formula(P, alpha, lambda_e)
result_precision_gly = result_precision * meters_to_gly  # Convert to gigalight-years
precision_difference = abs(result_precision - jwst_measured_value) / jwst_measured_value

# Display results
print(f"Calculated precision formula result: {result_precision:.5e} meters ({result_precision_gly:.5e} Gly)")
print(f"JWST measured value: {jwst_measured_value:.5e} meters ({result_precision_gly:.5e} Gly)")
print(f"Precision difference (relative error): {precision_difference:.5%}")
