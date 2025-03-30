# Hubble radius estimates

[![Cite ptep](https://img.shields.io/badge/PP-57-12-yellow.svg?style=flat)](http://www.ptep-online.com/2019/PP-57-12.PDF)
[![Latest PDF](https://img.shields.io/badge/PDF-latest-red.svg?style=flat)](http://www.ptep-online.com/2019/PP-57-12.PDF)
[![Cite rXiv](https://img.shields.io/badge/rXiv-1904.0218-orange.svg?style=flat)](http://rxiv.org/abs/1904.0218)
[![Cite viXra](https://img.shields.io/badge/viXra-1811.0146-green.svg?style=flat)](http://vixra.org/pdf/1811.0146v8.pdf)
[![Build Status](https://travis-ci.org/LaGuer/hubble-radius.svg?branch=master)](https://travis-ci.org/LaGuer/hubble-radius) 
[![codecov](https://codecov.io/gh/LaGuer/hubble-radius/branch/master/graph/badge.svg)](https://codecov.io/gh/LaGuer/hubble-radius)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/LaGuer/hubble-radius/master)
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/laguer/universe-age/blob/master/universe-age.ipynb)
[![nbviewer](https://img.shields.io/badge/view%20on-nbviewer-brightgreen.svg)](https://nbviewer.jupyter.org/github/LaGuer/hubble-radius/blob/master/hubble-radius.ipynb)
[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/LaGuer/hubble-radius/master?urlpath=lab%2Ftree%2Fhubble-radius-new.ipynb)

This repository contains python code and Jupyter notebooks presenting 48 Methods exhibiting the age of the universe (Hubble radius distance) using 3 physical constants excluding the speed of light.

Source Context:

The formula is derived via dimensional analysis, inspired by approaches in natural units and large-number hypotheses.

Dimensional Relationships
The quantity for length (𝐿) can be derived from the Planck constants. Using dimensional analysis:
$𝐿 ∝ ℏ𝐺 / 𝑀$
Where:
ℏ has dimensions of $ML^2$ $T^(−1)$,
𝐺 has dimensions of $L^3$ $M^(−1)$ $T^(−2)$,
𝑀 represents mass.

To incorporate the masses of fundamental particles, we treat 
𝑀 as the combination of 
$𝑚_𝑝$, $𝑚_𝑛$, and $𝑚_𝑒$ in relevant proportions (to represent universal characteristics).

These 48 formulas illustrate how one can “compute” a cosmic length scale using only ℏ, 𝐺, and the masses $𝑚_𝑒$, $𝑚_𝑛$, and $𝑚_𝑝$
 – all without an explicit appearance of the speed of light. They serve as a playground for exploring how dimensional analysis and natural unit ideas may (or may not) reflect deep physics.

Physical Interpretation: In a standard cosmological setting the Hubble radius is defined by 
$𝑅_𝐻 = 𝑐/𝐻_0$
 (which explicitly uses the speed of light). Recasting it in terms of other fundamental constants—and in particular not introducing 
𝑐
—is an approach that appears in attempts (such as those by Francis Michel Sanchez) to “derive” cosmic scales from quantum–gravitational considerations. The fact that one can match the observational scale (within a few percent, under a suitable choice of 
𝑘
) is a point of considerable debate and interest.
 
```
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

```


In addition we used Python modules such as: scipy, sympy, pandas and numpy

Fixed Constants used are:

* 𝜋=3.141592653589793... https://oeis.org/A000796
* Euler Mascheroni  𝛾=0.5772156649015329... https://oeis.org/A001620
* Atiyah's  Γ=25.178097241906... 
* Feigenbaum constant δ=4.669201609102990671853... https://oeis.org/A006890
* 2nd Feigenbaum constant α=2.50290787509589282228390287321... https://oeis.org/A006891
* Eddington Electric Constant  𝑎=137.0359990836958  also known as the inversed fine structure constant CODATA2018
* 𝑐=299792458.0  m/s CODATA2018
* ℎ=6.62607015.10−34   𝐽.𝐻𝑧−1  CODATA2018
* ℏ=1.0545718176461565.10−34   𝐽.𝑠  CODATA2018
* 𝑙𝑃=1.616255.10−35  m Planck length
* 𝑚𝑃=2.176434.10−8  kg Planck mass
* ƛ𝑒 =3.8615926796.10−13 m Reduced (Electron) Compton Wavelength CODATA2018
* ƛ𝑝 =2.10308910336.10−16 m Reduced (Proton) Compton Wavelength CODATA2018
* Mass of the electron  𝑚𝑒=9.1093837015.10−31  kg CODATA2018
* Mass of the proton  𝑚𝑝=1.67262192369.10−27  kg CODATA2018
* Boson  𝑊=80.379𝐺𝑒𝑉  ± 0.012 Particle Data Group Bosons M. Tanabashi et al. (Particle Data Group), Phys. Rev. D 98, 030001 (2018) and 2019
* Boson  𝑍=91.1876𝐺𝑒𝑉  ± 0.0023 Particle Data Group Bosons M. Tanabashi et al. (Particle Data Group), Phys. Rev. D 98, 030001 (2018) and 2019
* Lepton  𝑒=0.5109989461𝑀𝑒𝑉  Particle Data Group Leptons M. Tanabashi et al. (Particle Data Group), Phys. Rev. D 98, 030001 (2018) and 2019
* Baryon  𝑝=938.272081𝑀𝑒𝑉  Particle Data Group Baryons M. Tanabashi et al. (Particle Data Group), Phys. Rev. D 98, 030001 (2018) and 2019
* Baryon  𝑛=939.565413𝑀𝑒𝑉  Particle Data Group Baryons M. Tanabashi et al. (Particle Data Group), Phys. Rev. D 98, 030001 (2018) and 2019
* 𝐺=6.6743.10−11   𝑚3.𝑘𝑔−1.𝑠−2  Newtonian constant of gravitation CODATA2018
* 𝐺𝑞=6.6755.10−11   𝑚3.𝑘𝑔−1.𝑠−2  Newtonian constant of gravitation measured by T.Quinn et al. (2013) BIPM Sevres Improved determination of G using two methods
* 𝐺𝑏2𝑐=6.6754552.10−11   𝑚3.𝑘𝑔−1.𝑠−2  Newtonian constant of gravitation estimated by Francis M. Sanchez et al. (2019) in Back to Cosmos
* 𝐺𝑠=6.67545372.10−11   𝑚3.𝑘𝑔−1.𝑠−2  Newtonian constant of gravitation estimate by Francis M. Sanchez (Jan 2020)
