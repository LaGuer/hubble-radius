import scipy.constants as const
import numpy as np

# Constants (CODATA 2018/2022 values for consistency)
hbar = const.hbar  # Reduced Planck constant (J·s)
G = const.G        # Gravitational constant (m^3·kg^−1·s^−2)
m_e = const.electron_mass  # Electron mass (kg)
m_p = const.proton_mass    # Proton mass (kg)
m_n = const.neutron_mass   # Neutron mass (kg)
alpha = const.alpha        # Fine-structure constant (dimensionless)

# Conversion constants
meters_per_lightyear = 9.461e15  # Approximate meters in one light-year
meters_to_gly = 1 / (meters_per_lightyear * 1e9)  # Convert meters to gigalight-years

# JWST measured value (placeholder, in meters)
jwst_measured_value = 1.308e+26  # Approximate JWST value (corresponding to 13.81 Gly)

# Ratio of Compton wavelength to Planck length
lambda_e = hbar / (m_e * const.c)  # Electron Compton wavelength (m)
L_planck = np.sqrt(hbar * G / const.c**3)  # Planck length (m)
P = lambda_e / L_planck

# Precision formula
def precision_formula(P, alpha, lambdabare):
    """
    Precision theory formula for calculation.
    P: Ratio of Compton wavelength to Planck length
    alpha: Fine-structure constant
    lambdabare: Bare constant input
    """
    term1 = np.e**(4 * np.e - 1 / alpha)
    term2 = np.log(P**4 / alpha**3)**2
    exponent = np.sqrt((term1 - term2) / 2)
    return np.exp(exponent) * lambdabare

# Corrected formula: R = 2 * hbar^2 / (G * m_e * m_n * m_p)
def corrected_formula(hbar, G, m_e, m_p, m_n):
    """
    Calculates the Hubble radius using the corrected formula.
    """
    return 2 * hbar**2 / (G * m_e * m_n * m_p)

# Adjusted lambdabare value for scaling
lambdabare = 1e-5  # Example value in meters

# Calculate corrected formula result
corrected_result = corrected_formula(hbar, G, m_e, m_p, m_n)
corrected_result_gly = corrected_result * meters_to_gly  # Convert to gigalight-years

# Calculate precision formula result
precision_result = precision_formula(P, alpha, lambdabare)
precision_result_gly = precision_result * meters_to_gly  # Convert to gigalight-years

# Calculate precision difference (JWST deviation)
precision_difference = abs(corrected_result_gly - 13.81) / 13.81

# Output results
print("Hubble Radius Calculation:")
print(f"Corrected Formula:")
print(f"R (meters) = {corrected_result:.3e} m")
print(f"R (gigalight-years) = {corrected_result_gly:.3f} Gly")

print("\nPrecision Formula Calculation:")
print(f"R (meters) = {precision_result:.3e} m")
print(f"R (gigalight-years) = {precision_result_gly:.3f} Gly")

print("\nJWST Measured Value:")
print(f"JWST Value (meters) = {jwst_measured_value:.3e} m")
print(f"JWST Value (gigalight-years) = {jwst_measured_value * meters_to_gly:.3f} Gly")

print(f"\nPrecision Difference (Relative Error): {precision_difference:.5%}")
