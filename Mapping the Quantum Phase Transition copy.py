import quimb.tensor as qtn
import matplotlib.pyplot as plt
import numpy as np

# -----------------------------
# 1. Parameters
# -----------------------------
L = 40
h_values = np.linspace(0.0, 2.0, 20)

magnetizations = []
entropies = []

print(f"Starting Phase Scan on {L} sites...\n")

# -----------------------------
# 2. Phase Scan Loop
# -----------------------------
for h in h_values:

    # Build TFIM Hamiltonian
    H = qtn.MPO_ham_ising(L, j=1.0, bx=h)

    # Run DMRG
    dmrg = qtn.DMRG2(H, bond_dims=[10, 20, 40])
    dmrg.solve(verbosity=0, max_sweeps=4)

    mps = dmrg.state

    # Magnetization
    mags = [mps.magnetization(i, 'Z') for i in range(L)]
    avg_mag = np.mean(np.abs(mags))
    magnetizations.append(avg_mag)

    # Entanglement entropy
    ent = mps.entropy(L // 2)
    entropies.append(ent)

    print(f"h={h:.2f} | Mag: {avg_mag:.3f} | Entropy: {ent:.3f}")

# -----------------------------
# 3. Plot Styling
# -----------------------------
plt.style.use("seaborn-v0_8-whitegrid")

fig, (ax1, ax2) = plt.subplots(
    2, 1,
    figsize=(10, 8),
    sharex=True
)

# -----------------------------
# Magnetization Plot
# -----------------------------
ax1.plot(
    h_values,
    magnetizations,
    marker='o',
    markersize=6,
    linewidth=2,
    color='crimson',
    label='Order Parameter (Magnetization)'
)

ax1.axvline(
    x=1.0,
    color='black',
    linestyle='--',
    linewidth=1.5,
    label='Critical Point ($h_c = 1$)'
)

ax1.set_ylabel("Order Parameter $|\\langle Z \\rangle|$", fontsize=12)

ax1.set_title(
    "Quantum Phase Transition in the 1D Transverse-Field Ising Model",
    fontsize=14,
    weight='bold'
)

ax1.legend()
ax1.grid(alpha=0.3)

# -----------------------------
# Entropy Plot
# -----------------------------
ax2.plot(
    h_values,
    entropies,
    marker='s',
    markersize=6,
    linewidth=2,
    color='royalblue',
    label='Entanglement Entropy'
)

ax2.axvline(
    x=1.0,
    color='black',
    linestyle='--',
    linewidth=1.5
)

ax2.set_ylabel("Entanglement Entropy $S$", fontsize=12)
ax2.set_xlabel("Transverse Field $h$", fontsize=12)

ax2.legend()
ax2.grid(alpha=0.3)

# -----------------------------
# Layout
# -----------------------------
plt.tight_layout()

plt.savefig(
    "tfim_phase_scan.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
