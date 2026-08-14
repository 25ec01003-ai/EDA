import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv(r"C:\EDA LAB\datasets\MOSFET_ID_VGS.csv")

VDS_values = [0.1, 1, 3, 5]

plt.figure(figsize=(10, 6))

for VDS in VDS_values:


    VGS = data[f"V_GS ({VDS}V)"].to_numpy()
    ID = data[f"I_D ({VDS}V)"].to_numpy()


    mask = VGS >= 2.0

    VGS_linear = VGS[mask]
    ID_linear = ID[mask]


    sqrt_ID = np.sqrt(ID_linear)


    m, c = np.polyfit(VGS_linear, sqrt_ID, 1)


    VT = -c / m

    print(f"VDS = {VDS} V  -->  VT = {VT:.3f} V")


    plt.plot(VGS, np.sqrt(ID), 'o-', label=f'VDS = {VDS} V')


    x_fit = np.linspace(VT, max(VGS_linear), 100)
    y_fit = m * x_fit + c

    plt.plot(x_fit, y_fit, '--')


    plt.scatter(VT, 0, s=70)


    plt.annotate(
        f'VT={VT:.2f} V',
        xy=(VT, 0),
        xytext=(VT + 0.2, 0.5),
        arrowprops=dict(arrowstyle='->')
    )

plt.xlabel(r'$V_{GS}$ (V)')
plt.ylabel(r'$\sqrt{I_D}$')
plt.title(r'Linear Extrapolation for $V_T$')
plt.grid()
plt.legend()
plt.show()










