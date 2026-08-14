# =====================================================================
# E12. n-channel MOSFET I_D-V_DS curves computed from device physics,
# using SPICE Level 1 (Shichman-Hodges) and SPICE Level 3 equations.
#
# Given: tox = 10 nm, N_A = 1e16 cm^-3, Q_F = 1e12 cm^-2,
#        W = 4 um, L = 0.18 um, Al gate (phi_M = 4.1 eV), mu_n = 400 cm^2/V.s
#
# This script is fully self-contained -- it does NOT read any CSV file,
# so a missing/mismatched data file cannot be the source of an error here.
#
# NOTE on the computed V_T: with these specific given parameters, V_T
# comes out negative (~ -0.49 V). This is a genuine result of the physics
# (Al gate work function + positive fixed oxide charge pull V_FB very
# negative) -- it is not a bug. It means this particular device is
# depletion-mode (normally on). If your course expects an enhancement-mode
# device, double-check with your TA whether different Q_F/work-function
# values were intended.
#
# Channel-length modulation lambda = 0.1 V^-1 is given. Level 3 also
# needs mobility-degradation theta and saturation velocity v_max, which
# are still not given in the problem statement -- typical silicon
# values are assumed for those and clearly marked below.
# =====================================================================
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------------
# Given device parameters
# ---------------------------------------------------------------
tox    = 10e-7     # cm      (10 nm)
NA     = 1e16       # cm^-3
QF     = 1e12        # cm^-2   (fixed oxide charge density)
W      = 4e-4         # cm      (4 um)
L      = 0.18e-4        # cm      (0.18 um)
phi_M  = 4.1              # eV      (Aluminum gate work function)
mu_n   = 400               # cm^2/V.s

# ---------------------------------------------------------------
# Physical constants
# ---------------------------------------------------------------
q      = 1.602e-19    # C
eps0   = 8.854e-14     # F/cm
eps_ox = 3.9 * eps0
eps_si = 11.7 * eps0
kT     = 0.0259          # eV, at 300 K
ni     = 1.5e10            # cm^-3, silicon intrinsic concentration
chi_si = 4.05                # eV, silicon electron affinity
Eg     = 1.12                  # eV, silicon bandgap at 300 K

# ---------------------------------------------------------------
# Derived MOS parameters
# ---------------------------------------------------------------
Cox      = eps_ox / tox                                  # F/cm^2
phi_F    = kT * np.log(NA / ni)                            # V, Fermi potential
phi_S    = chi_si + Eg / 2 + phi_F                           # eV, semiconductor work function
phi_MS   = phi_M - phi_S                                       # V
Qdep_max = np.sqrt(2 * eps_si * q * NA * 2 * phi_F)              # C/cm^2, max depletion charge
Vfb      = phi_MS - (q * QF) / Cox                                 # V, flat-band voltage
VT       = Vfb + 2 * phi_F + Qdep_max / Cox                          # V, threshold voltage

kp = mu_n * Cox   # A/V^2, process transconductance parameter

print(f"C_ox  = {Cox * 1e9:.4f} nF/cm^2")
print(f"phi_F = {phi_F:.4f} V")
print(f"V_FB  = {Vfb:.4f} V")
print(f"V_T   = {VT:.4f} V")
print(f"k'    = {kp * 1e6:.4f} uA/V^2")

# ---------------------------------------------------------------
# Short-channel parameters
# ---------------------------------------------------------------
lam   = 0.1      # 1/V, channel-length modulation (given)
theta = 0.1        # 1/V, mobility degradation with V_GS (Level 3 only, assumed)
vmax  = 1e7          # cm/s, carrier saturation velocity (Level 3 only, assumed)
Esat  = 2 * vmax / mu_n   # V/cm, critical field for velocity saturation

# ---------------------------------------------------------------
# SPICE Level 1 (Shichman-Hodges)
# ---------------------------------------------------------------
def id_level1(vgs, vds):
    vov = vgs - VT
    id_ = np.zeros_like(vds)
    if vov <= 0:
        return id_
    triode = vds < vov
    id_[triode] = kp * (W / L) * (vov * vds[triode] - vds[triode] ** 2 / 2) * (1 + lam * vds[triode])
    sat = ~triode
    id_[sat] = 0.5 * kp * (W / L) * vov ** 2 * (1 + lam * vds[sat])
    return id_

# ---------------------------------------------------------------
# SPICE Level 3 (simplified): adds mobility degradation with V_GS
# and velocity saturation on top of Level 1.
# ---------------------------------------------------------------
def id_level3(vgs, vds):
    vov = vgs - VT
    id_ = np.zeros_like(vds)
    if vov <= 0:
        return id_
    mu_eff = mu_n / (1 + theta * vov)     # mobility degradation
    kp3 = mu_eff * Cox
    vdsat = vov / (1 + vov / (Esat * L))    # reduced saturation voltage

    # I_D at the triode/saturation boundary, evaluated with the SAME
    # triode expression used just below vdsat. Using this (instead of
    # the textbook 0.5*kp3*vdsat^2 form) guarantees the curve is
    # continuous at vds = vdsat -- no jump/spike at the boundary.
    id_dsat = kp3 * (W / L) * (vov * vdsat - vdsat ** 2 / 2)

    triode = vds < vdsat
    id_[triode] = kp3 * (W / L) * (vov * vds[triode] - vds[triode] ** 2 / 2)
    sat = ~triode
    id_[sat] = id_dsat * (1 + lam * (vds[sat] - vdsat))
    return id_

# ---------------------------------------------------------------
# Sweep and plot
# ---------------------------------------------------------------
vds = np.linspace(0, 4, 400)
vgs_list = [1, 2, 3]

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

for vgs in vgs_list:
    id_mA = id_level1(vgs, vds) * 1e3  # A -> mA
    axes[0].plot(vds, id_mA, linewidth=2, label=f'$V_{{GS}}$ = {vgs} V')

for vgs in vgs_list:
    id_mA = id_level3(vgs, vds) * 1e3  # A -> mA
    axes[1].plot(vds, id_mA, linewidth=2, label=f'$V_{{GS}}$ = {vgs} V')

axes[0].set_title('SPICE Level 1', fontweight='bold')
axes[1].set_title('SPICE Level 3', fontweight='bold')
for a in axes:
    a.set_xlabel('$V_{DS}$ (V)')
    a.set_ylabel('$I_D$ (mA)')
    a.grid(True, linestyle='--', alpha=0.6)
    a.legend()

plt.tight_layout()
plt.savefig('mosfet_idvds_level1_level3.png', dpi=350)
plt.show()
