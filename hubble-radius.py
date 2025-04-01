# Define updated physical constants (CODATA 2022)
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
hbar = 1.054571817e-34  # Reduced Planck's constant (J s)
m_p = 1.67262192369e-27  # Proton mass (kg)
m_n = 1.67492749804e-27  # Neutron mass (kg)
m_e = 9.1093837015e-31  # Electron mass (kg)

# Conversion factors
meters_to_ly = 1.057e-16       # 1 meter = 1.057e-16 lightyears
meters_to_mpc = 3.24078e-23    # 1 meter = 3.24078e-23 megaparsecs

# Approximation formula for the Hubble radius (R_H)
R_H_meters = (hbar**2) / (G * m_p * (m_n + m_e))  # Hubble radius in meters

# Convert to gigalightyears (Gly)
R_H_ly = R_H_meters * meters_to_ly  # Convert meters to lightyears
R_H_gly = R_H_ly / 1e9              # Convert lightyears to gigalightyears

# Convert to megaparsecs (Mpc)
R_H_mpc = R_H_meters * meters_to_mpc  # Convert meters to megaparsecs

# Output results
print("Approximate Hubble Radius (CODATA 2022):")
print(f"R_H in meters: {R_H_meters:.3e} m")
print(f"R_H in lightyears: {R_H_ly:.3e} ly")
print(f"R_H in gigalightyears: {R_H_gly:.3f} Gly")
print(f"R_H in megaparsecs: {R_H_mpc:.3f} Mpc")
