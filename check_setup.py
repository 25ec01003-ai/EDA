import numpy as np
import matplotlib.pyplot as plt

# MOSFET parameters
beta = 3.07e-3       # A/V^2
Vth = -0.260         # V

# VDS range
VDS = np.linspace(0, 4, 1000)

# VGS values
VGS_values = [1, 2, 3]

plt.figure(figsize=(5, 5))

for VGS in VGS_values:

    Vov = VGS - Vth       # VGS - VTH
    VDS_sat = Vov

    ID = np.zeros_like(VDS)

    # Linear region
    linear = VDS < VDS_sat
    ID[linear] = beta * (
        Vov * VDS[linear] -
        0.5 * VDS[linear]**2
    )

    # Saturation region
    saturation = VDS >= VDS_sat
    ID[saturation] = 0.5 * beta * Vov**2

    # Plot in mA
    plt.plot(VDS, ID * 1000, label=f'VGS = {VGS} V')

plt.xlabel('VDS (V)')
plt.ylabel('ID (mA)')
plt.title('NMOS ID-VDS Characteristics - SPICE Level 1')
plt.grid(True)
plt.legend()

plt.show()






