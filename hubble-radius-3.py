import scipy.constants as const
import numpy as np

# Constants (CODATA 2018/2022 values for consistency)
hbar = const.hbar        # Reduced Planck constant (J·s)
G = const.G              # Gravitational constant (m^3·kg^−1·s^−2)
m_e = const.electron_mass  # Electron mass (kg)
m_p = const.proton_mass    # Proton mass (kg)
m_n = const.neutron_mass   # Neutron mass (kg)

# Conversion constant: meters to gigalight-years (Gly)
meters_per_lightyear = 9.461e15  # Approximate meters in one light-year
meters_to_gly = 1 / (meters_per_lightyear * 1e9)  # Convert meters to gigalight-years

# JWST measured value (placeholder, in meters)
jwst_measured_value = 1.308e+26  # Approximate JWST value (corresponding to 13.81 Gly)

# Correct formula: R = 2 * hbar^2 / (G * m_e * m_n * m_p)
def corrected_formula(hbar, G, m_e, m_p, m_n):
    """
    Calculates the Hubble radius using the corrected formula.
    """
    return 2 * hbar**2 / (G * m_e * m_n * m_p)

# Calculate corrected formula result
corrected_result = corrected_formula(hbar, G, m_e, m_p, m_n)
corrected_result_gly = corrected_result * meters_to_gly  # Convert to gigalight-years

# Calculate precision difference (JWST deviation)
precision_difference = abs(corrected_result - jwst_measured_value) / jwst_measured_value

# Output results
print("Hubble Radius Calculation:")
print(f"R (meters) = {corrected_result:.3e} m")
print(f"R (gigalight-years) = {corrected_result_gly:.3f} Gly")
print("\nJWST Measured Value:")
print(f"JWST Value (meters) = {jwst_measured_value:.3e} m")
print(f"JWST Value (gigalight-years) = {jwst_measured_value * meters_to_gly:.3f} Gly")
print(f"\nPrecision Difference (Relative Error): {precision_difference:.5%}")
