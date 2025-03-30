import math

def compute_aligned_hubble_radius_multipliers():
    # Fundamental constants (CODATA 2018 values, SI units)
    hbar = 1.054571817e-34      # Reduced Planck constant (J·s)
    G = 6.67430e-11             # Gravitational constant (m^3·kg^-1·s^-2)
    m_e = 9.1093837015e-31       # Electron mass (kg)
    m_p = 1.67262192369e-27      # Proton mass (kg)
    m_n = 1.67492749804e-27      # Neutron mass (kg)

    # Base combination X (has dimension of length, in meters)
    X = hbar**2 / (G * m_e * m_n * m_p)
    # With these constants, X is roughly ~6.53×10^25 meters.

    # For a fine tuning, we sometimes wish to include a minor correction using the mass ratio.
    correction = math.sqrt(m_e / m_p)  # ≈ 0.0223 (small correction factor)

    # Candidate formulas: using multipliers near 2 so that R = k * X
    candidate_factors = [
        ("1.98", 1.98),
        ("1.99", 1.99),
        ("2.00", 2.00),
        ("2.01", 2.01),
        ("2.02", 2.02),
        # Composite formulas with a small correction based on the mass ratio:
        ("2*(1 - corr/50)", 2.0 * (1 - correction/50)),
        ("2*(1 + corr/50)", 2.0 * (1 + correction/50)),
        ("2*(1 - corr/100)", 2.0 * (1 - correction/100)),
        ("2*(1 + corr/100)", 2.0 * (1 + correction/100))
    ]
    
    # Conversion factors:
    conversion_Gly = 9.461e24   # 1 Gly in meters
    conversion_Mpc = 3.086e22   # 1 Mpc in meters

    results = []
    for desc, factor in candidate_factors:
        R_meters = factor * X
        R_Gly = R_meters / conversion_Gly
        R_Mpc = R_meters / conversion_Mpc
        results.append((desc, factor, R_meters, R_Gly, R_Mpc))
    return results

def main():
    results = compute_aligned_hubble_radius_multipliers()
    
    header = f"{'Candidate':>25} | {'k Factor':>8} | {'R (m)':>15} | {'R (Gly)':>15} | {'R (Mpc)':>15}"
    print("Hubble Radius formulas (excluding c) tuned to JWT measurement:")
    print(header)
    print("-" * len(header))
    for desc, factor, R_m, R_Gly, R_Mpc in results:
        print(f"{desc:>25} | {factor:8.4f} | {R_m:15.3e} | {R_Gly:15.3e} | {R_Mpc:15.3e}")

if __name__ == "__main__":
    main()

