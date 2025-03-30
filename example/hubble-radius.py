import math

def compute_aligned_hubble_radius():
    # Fundamental constants (CODATA 2018 values, SI units)
    hbar = 1.054571817e-34      # Reduced Planck constant in J·s
    G = 6.67430e-11             # Gravitational constant in m^3·kg^-1·s^-2
    m_e = 9.1093837015e-31       # Electron mass in kg
    m_p = 1.67262192369e-27      # Proton mass in kg
    m_n = 1.67492749804e-27      # Neutron mass in kg

    # Base combination X (has dimension of length)
    X = hbar**2 / (G * m_e * m_n * m_p)
    # With these constants, X ≈ 6.5×10^25 meters

    # Here we build a list of candidate formulas using multipliers k chosen to tune R = k * X
    # to be near JWT's measurement (~1.3e26 m, or ~13.8 Gly).
    #
    # We include simple numerical factors (e.g. 1.98, 1.99, 2.00, etc.) plus a couple of formulas
    # that use minor corrections based on mass ratios.
    
    # Precompute a useful mass-ratio quantity for minor corrections:
    correction = math.sqrt(m_e / m_p)  # a very small number ~0.0223

    candidate_factors = [
        ("1.98", 1.98),
        ("1.99", 1.99),
        ("2.00", 2.00),
        ("2.01", 2.01),
        ("2.02", 2.02),
        # Composite formulas introducing a small mass-ratio correction:
        ("2*(1 - corr/50)", 2.0 * (1 - correction/50)),
        ("2*(1 + corr/50)", 2.0 * (1 + correction/50)),
        ("2*(1 - corr/100)", 2.0 * (1 - correction/100)),
        ("2*(1 + corr/100)", 2.0 * (1 + correction/100))
    ]
    
    # Conversion factor: 1 gigalightyear (Gly) ≈ 9.461e24 meters
    conversion = 9.461e24

    results = []
    for desc, factor in candidate_factors:
        R_meters = factor * X
        R_Gly = R_meters / conversion
        results.append((desc, factor, R_meters, R_Gly))
    return results

def main():
    print("Hubble Radius formulas tuned to JWT measurement (using only hbar, G, m_e, m_n, m_p)")
    print("-----------------------------------------------------------------------")
    print(f"{'Candidate':>25} | {'k Factor':>8} | {'R (m)':>15} | {'R (Gly)':>15}")
    print("-" * 70)
    results = compute_aligned_hubble_radius()
    for desc, factor, R, R_Gly in results:
        print(f"{desc:>25} | {factor:8.4f} | {R:15.3e} | {R_Gly:15.3e}")

if __name__ == "__main__":
    main()
