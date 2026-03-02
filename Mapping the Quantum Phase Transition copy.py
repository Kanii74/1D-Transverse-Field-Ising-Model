import quimb.tensor as qtn
import matplotlib.pyplot as plt
import numpy as np

# --- 1. Parameters ---
L = 40  # 40 sites is plenty to see the physics clearly on an M1
h_values = np.linspace(0.0, 2.0, 20) 
magnetizations = []
entropies = []

print(f"Starting Phase Scan on {L} sites...")
for h in h_values:
    # Build Hamiltonian
    H = qtn.MPO_ham_ising(L, j=1.0, bx=h)
    
    # Run DMRG
    dmrg = qtn.DMRG2(H, bond_dims=[10, 20, 40])
    dmrg.solve(verbosity=0, max_sweeps=4)
    
    # Get the resulting state (the MPS)
    mps = dmrg.state
    
    # We calculate the Z-magnetization at each site and average it
    # We use 'mags' to get the local values for operator 'Z'
    mags = [mps.magnetization(i, 'Z') for i in range(L)]
    avg_mag = np.mean(np.abs(mags))
    magnetizations.append(avg_mag)
    
    # Measure Entanglement Entropy at the center bond
    ent = mps.entropy(L // 2)
    entropies.append(ent)
    
    print(f"h={h:.2f} | Mag: {avg_mag:.3f} | Entropy: {ent:.3f}")

# --- 3. Visualization ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Magnetization Plot
ax1.plot(h_values, magnetizations, 'o-', color='crimson', label='Order (Magnetization)')
ax1.axvline(x=1.0, color='black', linestyle='--', label='Critical Point (h=1)')
ax1.set_ylabel("Order Parameter |<Z>|")
ax1.legend()
ax1.grid(alpha=0.3)

# Entropy Plot
ax2.plot(h_values, entropies, 's-', color='royalblue', label='Quantum Complexity')
ax2.axvline(x=1.0, color='black', linestyle='--')
ax2.set_ylabel("Entanglement Entropy")
ax2.set_xlabel("Transverse Field (h)")
ax2.legend()
ax2.grid(alpha=0.3)

plt.tight_layout()
plt.show()


