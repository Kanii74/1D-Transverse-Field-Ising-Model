import numpy as np
from scipy.linalg import eigh
from functools import reduce
import itertools
import csv
import matplotlib.pyplot as plt

# Parameters
number_of_spins = 8               
coupling_strength = 1.0              
magnetic_field_values = np.linspace(0.0, 2.0, 21)  

# Pauli matrices
pauli_x = np.array([[0, 1], [1, 0]], dtype=float)
pauli_z = np.array([[1, 0], [0, -1]], dtype=float)
identity_2x2 = np.eye(2, dtype=float)

# Kronecker helper
def kron_list(matrix_list):
    """Kronecker product of a list of matrices (left to right)."""
    return reduce(np.kron, matrix_list)


# Precompute single-site operators Z_i and X_i (dense matrices)
total_dimension = 2 ** number_of_spins
z_operator_list = []
x_operator_list = []

print(f"Precomputing single-site operators for L = {number_of_spins} (dimension {total_dimension}x{total_dimension})...")
for site_index in range(number_of_spins):
    # build operator lists with identity except operator at 'site'
    matrices_for_z = [identity_2x2 if i != site_index else pauli_z for i in range(number_of_spins)]
    matrices_for_x = [identity_2x2 if i != site_index else pauli_x for i in range(number_of_spins)]
    z_operator_list.append(kron_list(matrices_for_z))
    x_operator_list.append(kron_list(matrices_for_x))
print("Done.\n")

# Transverse Ising Field Model Hamiltonian 
def build_hamiltonian(field_strength):
    hamiltonian_matrix = np.zeros((total_dimension, total_dimension), dtype=float)

    # ZZ interaction on nearest neighbours (open boundary)
    for i in range(number_of_spins - 1):
        hamiltonian_matrix += -coupling_strength * (z_operator_list[i] @ z_operator_list[i + 1])

    # transverse field
    for i in range(number_of_spins):
        hamiltonian_matrix += -field_strength * x_operator_list[i]
    return hamiltonian_matrix

# Utility: entanglement entropy from pure state psi (bipartition center)
def bipartite_entropy(wavefunction, L):
    # partition A = sites [0..L//2-1], B = rest
    mid_point = L // 2
    dim_a = 2 ** mid_point
    dim_b = 2 ** (L - mid_point)
    reshaped_psi = wavefunction.reshape((dim_a, dim_b))

    # reduced density matrix rho_A = psi_mat @ psi_mat^\dagger
    reduced_density_matrix = reshaped_psi @ reshaped_psi.conj().T
    eigenvalues = np.linalg.eigvalsh(reduced_density_matrix)
    eigenvalues = eigenvalues[eigenvalues > 1e-12]  # drop tiny negative/noise
    entropy_value = -np.sum(eigenvalues * np.log(eigenvalues))
    
    # entanglement spectrum (entanglement energies) = -log(eigenvalues)
    entanglement_energies = -np.log(eigenvalues)
    entanglement_energies.sort()  # ascending entanglement energies (largest weights first)
    return entropy_value, entanglement_energies

# Storage and header print
simulation_results = []
table_header = (
    f"{'h':>6} | {'E0':>12} | {'Avg|Z|':>8} | {'M_corr':>8} | "
    f"{'S(mid)':>8} | {'<ZZ>_nn':>8} | {'top-ent (first 6)':>30}"
)
separator_line = "-" * len(table_header)
print("Exact diagonalization TFIM (verbose output)\n")
print(table_header)
print(separator_line)

# Main loop over h
for idx, h_val in enumerate(magnetic_field_values):
    current_hamiltonian = build_hamiltonian(h_val)

    # diagonalize (full) -> ground state
    energies, states = eigh(current_hamiltonian)
    ground_state_energy = float(energies[0])
    ground_state_vector = states[:, 0]   # ground state vector (normalized by eigh)

    # single-site expectation values <Z_i>
    local_magnetizations = np.array([np.vdot(ground_state_vector, (z_operator_list[i] @ ground_state_vector)).real for i in range(number_of_spins)])
    average_magnetization = float(np.mean(np.abs(local_magnetizations)))

    # two-point correlations <Z_i Z_j> matrix and M_corr as in paper eq. (2)
    total_correlation_sum = 0.0
    # we will also compute nearest-neighbour average <Z_i Z_{i+1}>
    nearest_neighbor_correlations = []
    for i in range(number_of_spins):
        for j in range(number_of_spins):
            correlation_value = float(np.vdot(ground_state_vector, (z_operator_list[i] @ z_operator_list[j]) @ ground_state_vector))
            total_correlation_sum += correlation_value
        if i < number_of_spins - 1:
            nearest_neighbor_correlations.append(float(np.vdot(ground_state_vector, (z_operator_list[i] @ z_operator_list[i + 1]) @ ground_state_vector)))
    correlation_order_parameter = np.sqrt(total_correlation_sum / (number_of_spins ** 2))

    # entanglement entropy and spectrum (center cut)
    mid_entropy, spectrum_energies = bipartite_entropy(ground_state_vector, number_of_spins)
    # prepare printable top-6 entanglement energies
    top_spectrum = spectrum_energies[:6] if len(spectrum_energies) >= 6 else spectrum_energies
    spectrum_string = ", ".join(f"{v:.4f}" for v in top_spectrum)

    # nearest-neighbour average
    average_nn_correlation = float(np.mean(nearest_neighbor_correlations)) if nearest_neighbor_correlations else 0.0

    # Save result
    simulation_results.append({
        "h": float(h_val),
        "E0": ground_state_energy,
        "avg_abs_Z": average_magnetization,
        "M_corr": float(correlation_order_parameter),
        "S_mid": float(mid_entropy),
        "avg_ZZ_nn": average_nn_correlation,
        "top_ent": spectrum_string
    })

    # Nicely formatted print
    print(
        f"{h_val:6.3f} | {ground_state_energy:12.6f} | {average_magnetization:8.4f} | {correlation_order_parameter:8.4f} | "
        f"{mid_entropy:8.4f} | {average_nn_correlation:8.4f} | {spectrum_string:>30}"
    )

print(separator_line)

# Plots
h_axis = [res["h"] for res in simulation_results]
energy_axis = [res["E0"] for res in simulation_results]
mcorr_axis = [res["M_corr"] for res in simulation_results]
entropy_axis = [res["S_mid"] for res in simulation_results]

plt.style.use("seaborn-v0_8-whitegrid")
fig, axes = plt.subplots(3, 1, figsize=(8, 10), sharex=True)

axes[0].plot(h_axis, energy_axis, "-o", color="black")
axes[0].set_ylabel("Ground state energy E0")
axes[0].grid(True)

axes[1].plot(h_axis, mcorr_axis, "-o", color="red", label="M_corr")
axes[1].set_ylabel("Order parameter $M_{corr}$")
axes[1].grid(True)

axes[2].plot(h_axis, entropy_axis, "-o", color="blue", label="S(mid)")
axes[2].set_xlabel("Transverse field h")
axes[2].set_ylabel("Entanglement entropy (center cut)")
axes[2].legend()
axes[2].grid(True)

plt.tight_layout()
plt.show()
