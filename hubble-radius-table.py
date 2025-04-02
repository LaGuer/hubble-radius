from scipy import constants
import numpy as np
import pandas as pd

# Fundamental constants
hbar = constants.hbar                # Reduced Planck constant (J·s)
G = 6.67545372e-11                   # Gravitational constant (CODATA 2018, m^3·kg^−1·s^−2)
c = constants.c                      # Speed of light (m/s)
m_e = constants.m_e                  # Electron mass (kg)
m_p = constants.m_p                  # Proton mass (kg)
light_year_m = constants.light_year  # Meters in a light-year
meters_to_gly = 1 / (light_year_m * 1e9)  # Conversion: meters to gigalight-years
meters_to_mpc = 3.24077929e-23       # Conversion: meters to megaparsecs

# JWST measured value in gigalight-years
jwst_measured_gly = 13.81

# Formula 1: Hubble radius calculation using hbar, G, m_e, and m_p
R_H_formula1_m = 2 * hbar**2 / (G * m_e * m_p**2)  # Result in meters
R_H_formula1_gly = R_H_formula1_m * meters_to_gly  # Convert to Gly
R_H_formula1_mpc = R_H_formula1_m * meters_to_mpc  # Convert to Mpc
Hubble_constant1 = c / R_H_formula1_mpc / 1e3  # Convert to km/s/Mpc

# Formula 2: Using a hypothetical exponential factor
lambdabare = hbar / (m_e * c)  # Electron Compton wavelength
R_H_formula2_m = lambdabare * np.exp(64) / 6  # Hypothetical result in meters
R_H_formula2_gly = R_H_formula2_m * meters_to_gly
R_H_formula2_mpc = R_H_formula2_m * meters_to_mpc
Hubble_constant2 = c / R_H_formula2_mpc / 1e3  # Convert to km/s/Mpc

# Formula 3: Using Planck's length and scaling factors
G_s = 6.67545372e-11  # Gravitational constant (alternative value for scaling)
l_P = np.sqrt(hbar * G_s / c**3)  # Planck length
R_H_formula3_m = 2 * l_P * c**2 / lambdabare / (1e9 * light_year_m)  # Result in meters
R_H_formula3_gly = R_H_formula3_m * meters_to_gly
R_H_formula3_mpc = R_H_formula3_m * meters_to_mpc
Hubble_constant3 = c / R_H_formula3_mpc / 1e3  # Convert to km/s/Mpc

# Create a DataFrame to organize and compare results
data = {
    "Formula": ["Formula 1", "Formula 2", "Formula 3"],
    "LaTeX Representation": [
        r"$R_H = \frac{2 \hbar^2}{G m_e m_p^2}$",
        r"$R_H = \lambda_e \cdot \exp(64) / 6$",
        r"$R_H = \frac{2 \cdot l_P \cdot c^2}{\lambda_e}$",
    ],
    "Radius (Gly)": [R_H_formula1_gly, R_H_formula2_gly, R_H_formula3_gly],
    "Radius (m)": [R_H_formula1_m, R_H_formula2_m, R_H_formula3_m],
    "Radius (Mpc)": [R_H_formula1_mpc, R_H_formula2_mpc, R_H_formula3_mpc],
    "Hubble Constant (km/s/Mpc)": [
        Hubble_constant1, Hubble_constant2, Hubble_constant3
    ],
    "JWST Deviation Factor (%)": [
        abs((R_H_formula1_gly - jwst_measured_gly) / jwst_measured_gly * 100),
        abs((R_H_formula2_gly - jwst_measured_gly) / jwst_measured_gly * 100),
        abs((R_H_formula3_gly - jwst_measured_gly) / jwst_measured_gly * 100),
    ],
}
df_results = pd.DataFrame(data)

# Print the table
print(df_results)
