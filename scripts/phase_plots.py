import numpy as np
import matplotlib.pyplot as plt

# ---------------------------
# Define scattering angle (0° = forward scattering, 180° = back scattering)
# ---------------------------
theta = np.linspace(0, 2*np.pi, 500)  # radians

# ---------------------------
# Define phase functions
# ---------------------------
# Rayleigh scattering phase function: P(θ) ∝ 1 + cos²θ
P_rayleigh = 1 + np.cos(theta)**2  # normalized shape

# Mie scattering: here we simulate a forward-peaked distribution
# This is not an exact Mie computation, just a common approximation
w = 0.5 # asymmetry parameter (0=Rayleigh, 1=strong forward)
P_mie = (w/(1+w-np.cos(theta)))**2

w = 0.01  # asymmetry parameter (0=Rayleigh, 1=strong forward)
P_sun = (w/(1+w-np.cos(theta)))**2


# Normalize both so max = 1 (for plotting comparison)
P_rayleigh /= P_rayleigh.max()
P_mie /= P_mie.max()
P_sun /= P_sun.max()

# ---------------------------
# Create side-by-side polar plots
# ---------------------------
fig, axes = plt.subplots(1, 3, subplot_kw=dict(polar=True), figsize=(10, 5))

# Plot Rayleigh
axes[0].plot(theta, P_rayleigh, color='blue', lw=2)
axes[0].set_title("Rayleigh Phase Function", va='bottom')
axes[0].set_rticks([0.5, 1])
axes[0].set_yticklabels([])
axes[0].grid(True)

# Plot Mie
axes[1].plot(theta, P_mie, color='green', lw=2)
axes[1].set_title("Mie Phase Function (w=0.5)", va='bottom')
axes[1].set_rticks([0.5, 1])
axes[1].set_yticklabels([])
axes[1].grid(True)

# Plot Sun
if True:
    axes[2].plot(theta, P_sun, color='red', lw=2)
    axes[2].set_title("Mie Phase Function (w=0.01)", va='bottom')
    axes[2].set_rticks([0.5, 1])
    axes[2].set_yticklabels([])
    axes[2].grid(True)

plt.tight_layout()
plt.savefig("assets/phase_functions.jpg", dpi=300)
plt.show()

