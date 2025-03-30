import math

def compute_aligned_hubble_radius():
    # Fundamental constants (CODATA 2018 values, SI units)
    hbar = 1.054571817e-34      # Reduced Planck constant (J·s)
    G = 6.67430e-11             # Gravitational constant (m^3·kg^-1·s^-2)
    m_e = 9.1093837015e-31       # Electron mass (kg)
    m_p = 1.67262192369e-27      # Proton mass (kg)
    m_n = 1.67492749804e-27      # Neutron mass (kg)

    # Base length combination (has dimensions of length)
    X = hbar**2 / (G * m_e * m_n * m_p)
    # For our constant values, X ≈ 6.53×10^25 meters

    # We'll tune the result to be near the JWT measurement by choosing k ~ 2.
    # Here are several candidate factors around 2:
    candidate_factors = [
        ("1.95",    1.95),
        ("1.96",    1.96),
        ("1.97",    1.97),
        ("1.98",    1.98),
        ("1.99",    1.99),
        ("2.00",    2.00),
        ("2.01",    2.01),
        ("2.02",    2.02),
        # A formula that incorporates a tiny correction using the mass ratio:
        ("2*(1 - sqrt(m_e/m_p)/10)", 2.0 * (1 - math.sqrt(m_e/m_p)/10)),
        ("2*(1 + sqrt(m_e/m_p)/50)", 2.0 * (1 + math.sqrt(m_e/m_p)/50))
    ]
    
    # Conversion: 1 gigalightyear (Gly) ≈ 9.461×10^24 meters.
    conversion = 9.461e24

    results = []
    for desc, factor in candidate_factors:
        R_meters = factor * X
        R_Gly = R_meters / conversion
        results.append((desc, factor, R_meters, R_Gly))
    return results

def main():
    results = compute_aligned_hubble_radius()
    
    print("Aligned Hubble Radius formulas (excluding c) tuned near JWT measurement:")
    print("{:>35} | {:>8} | {:>15} | {:>15}".format("Formula description", "Factor", "R (m)", "R (Gly)"))
    print("-" * 80)
    for desc, factor, R_m, R_Gly in results:
        print("{:>35} | {:8.4f} | {:15.3e} | {:15.3e}".format(desc, factor, R_m, R_Gly))
    
if __name__ == "__main__":
    main()
