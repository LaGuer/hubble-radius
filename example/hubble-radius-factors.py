import math

def compute_hubble_radius_factors():
    # Fundamental Constants (SI units; CODATA 2018 values)
    hbar = 1.054571817e-34      # Reduced Planck constant, J·s
    G = 6.67430e-11             # Gravitational constant, m^3·kg^-1·s^-2
    m_e = 9.1093837015e-31       # Electron mass, kg
    m_p = 1.67262192369e-27      # Proton mass, kg
    m_n = 1.67492749804e-27      # Neutron mass, kg

    # Base combination X (has dimensions of length)
    X = hbar**2 / (G * m_e * m_n * m_p)  # ~6.525e25 meters

    # Precomputed mass ratios (dimensionless)
    mu_p_over_e = m_p / m_e            # ~1836.15
    mu_n_over_e = m_n / m_e            # ~1838.00 (approximately)
    ratio_p_n = m_p / m_n              # ≈ 0.9988

    # List of 47 formulas as (description, factor)
    formulas = [
       ("1", 1),
       ("2", 2),
       ("3", 3),
       ("4", 4),
       ("5", 5),
       ("6", 6),
       ("7", 7),
       ("8", 8),
       ("9", 9),
       ("10", 10),
       ("pi", math.pi),
       ("2*pi", 2 * math.pi),
       ("3*pi", 3 * math.pi),
       ("4*pi", 4 * math.pi),
       ("5*pi", 5 * math.pi),
       ("sqrt(2)", math.sqrt(2)),
       ("2*sqrt(2)", 2 * math.sqrt(2)),
       ("3*sqrt(2)", 3 * math.sqrt(2)),
       ("4*sqrt(2)", 4 * math.sqrt(2)),
       ("5*sqrt(2)", 5 * math.sqrt(2)),
       ("sqrt(pi)", math.sqrt(math.pi)),
       ("2*sqrt(pi)", 2 * math.sqrt(math.pi)),
       ("3*sqrt(pi)", 3 * math.sqrt(math.pi)),
       ("4*sqrt(pi)", 4 * math.sqrt(math.pi)),
       ("5*sqrt(pi)", 5 * math.sqrt(math.pi)),
       ("e", math.e),
       ("2*e", 2 * math.e),
       ("3*e", 3 * math.e),
       ("4*e", 4 * math.e),
       ("5*e", 5 * math.e),
       ("pi*e", math.pi * math.e),
       ("2*pi*e", 2 * math.pi * math.e),
       ("3*pi*e", 3 * math.pi * math.e),
       ("4*pi*e", 4 * math.pi * math.e),
       ("5*pi*e", 5 * math.pi * math.e),
       ("m_p/m_e", mu_p_over_e),
       ("m_n/m_e", mu_n_over_e),
       ("m_p/m_n", ratio_p_n),
       ("sqrt(m_p/m_e)", math.sqrt(mu_p_over_e)),
       ("sqrt(m_n/m_e)", math.sqrt(mu_n_over_e)),
       ("sqrt(m_p/m_n)", math.sqrt(ratio_p_n)),
       ("(m_p/m_e)^(2/3)", mu_p_over_e**(2/3)),
       ("(m_n/m_e)^(2/3)", mu_n_over_e**(2/3)),
       ("2+pi", 2 + math.pi),
       ("pi+sqrt(2)", math.pi + math.sqrt(2)),
       ("2*pi+sqrt(2)", 2 * math.pi + math.sqrt(2)),
       ("3*pi+sqrt(2)", 3 * math.pi + math.sqrt(2))
    ]
    
    # Conversion factor: 1 Gly ~ 9.461e24 meters.
    conversion_factor = 9.461e24  # meters per Gly
    
    results = []
    for desc, factor in formulas:
        # Here we compute R = factor * X
        R_meters = factor * X
        R_Gly = R_meters / conversion_factor
        results.append((desc, factor, R_meters, R_Gly))
    
    return results

def main():
    results = compute_hubble_radius_factors()
    # Print header
    header = f"{'Index':>5}  {'Description':>20}  {'Factor':>12}  {'R (m)':>15}  {'R (Gly)':>15}"
    print("Computed cosmic length scales (as candidates for the Hubble radius):")
    print(header)
    print("-" * len(header))
    for i, (desc, factor, R_meters, R_Gly) in enumerate(results, start=1):
        print(f"{i:5d}  {desc:>20}  {factor:12.4f}  {R_meters:15.3e}  {R_Gly:15.3e}")
    
if __name__ == "__main__":
    main()
hubb
