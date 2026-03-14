# Overview

This project studies the **one-dimensional Transverse-Field Ising Model (TFIM)** using several computational techniques. The goal is to understand how different numerical and quantum algorithms capture the **quantum phase transition** that occurs in this model.

The TFIM is a simple but important model in quantum many-body physics. By changing the strength of the transverse magnetic field, the system moves from a **ferromagnetic phase**, where spins tend to align with each other, to a **paramagnetic phase**, where the external field dominates and destroys the magnetic order.

In this project, we analyze this transition using multiple approaches, including:

- **Exact Diagonalization (ED)** – used for small systems to obtain exact reference results  
- **Density Matrix Renormalization Group (DMRG)** – a tensor network method used to study larger spin chains  
- **Variational Quantum Eigensolver (VQE)** – a quantum algorithm that approximates the ground state using parameterized quantum circuits  
- **Analytical results** of the TFIM where available  

For each method, we compute and compare important physical quantities such as:

- **Ground-state energy**
- **Magnetic order parameter**
- **Entanglement entropy**
- **Spin correlation functions**

By comparing results from different techniques, the project demonstrates how classical numerical methods and quantum algorithms can be used to study **quantum phase transitions in many-body systems**.

----------------------------
# Transverse Field Ising Model (TFIM)

The **one–dimensional transverse-field Ising model (TFIM)** is one of the most important models in **condensed matter physics** and **quantum many-body theory**. It is widely used to study phenomena such as **quantum phase transitions**, **entanglement**, and **quantum criticality**.

Despite its simple mathematical form, the TFIM captures a deep physical idea: **a competition between interactions that try to order a system and quantum fluctuations that try to disorder it**. Understanding this competition is central to many areas of modern physics.

---

## Model Hamiltonian

The Hamiltonian of the one–dimensional TFIM is

$$
\large
H = -J \sum_{i} Z_i Z_{i+1} - h \sum_{i} X_i
$$

This Hamiltonian describes a **chain of spin-1/2 particles** arranged on a one-dimensional lattice.

Each site \( i \) corresponds to a quantum spin that can point either **up** or **down** along the \( z \)-axis. The operators $$\( Z_i \)$$ and $$\( X_i \)$$ are **Pauli matrices** acting on the spin at site \( i \).

---

## Physical Meaning of the Parameters

| Symbol | Meaning |
|------|------|
| $$\(J\)$$ | Strength of the nearest-neighbour spin interaction |
| $$\(h\)$$ | Strength of the transverse magnetic field |
| $$\(Z_i\)$$ | Pauli-Z operator acting on spin \(i\) |
| $$\(X_i\)$$ | Pauli-X operator acting on spin \(i\) |

The Hamiltonian consists of **two competing physical terms**, each representing a different physical effect.

---

## Spin–Spin Interaction Term

The first term in the Hamiltonian is

$$
J \sum_i Z_i Z_{i+1}
$$

This represents the **interaction between neighbouring spins**.

If \(J>0\), the interaction is **ferromagnetic**, meaning the system prefers neighbouring spins to align in the same direction along the \(z\)-axis.

The lowest-energy configurations of the system correspond to states where **all spins are aligned in the same direction**. These two degenerate ground states are

$$
\large
|\uparrow \uparrow \uparrow \cdots \uparrow \rangle
$$

and

$$
\large
|\downarrow \downarrow \downarrow \cdots \downarrow \rangle
$$

In both configurations, every spin points in the same direction along the \(z\)-axis, which minimizes the interaction energy of the term,

$$
J \sum_i Z_i Z_{i+1}
$$

In these states all spins point in the same direction, minimizing the interaction energy.

This ordered configuration corresponds to the **ferromagnetic phase**, where the system develops a **macroscopic magnetization along the \(z\)-direction**.

---

## Transverse Field Term

The second term in the Hamiltonian is

$$
h \sum_i X_i
$$

This represents the effect of an **external magnetic field applied along the \(x\)-direction**, which is perpendicular to the spin-interaction axis.

The Pauli operator \(X\) flips spin states:

$$
\large
X|\uparrow\rangle = |\downarrow\rangle
$$

$$
\large
X|\downarrow\rangle = |\uparrow\rangle
$$

Because of this property, the transverse field causes spins to **continuously flip between up and down states**.

These flips introduce **quantum fluctuations**, which disrupt the ordered ferromagnetic configuration produced by the interaction term.

---

## Competition Between Order and Quantum Fluctuations

The essential physics of the TFIM comes from the **competition between two tendencies**:

| Interaction Term | Physical Effect |
|---|---|
| $$\( -J \sum Z_i Z_{i+1} \)$$ | Encourages **spin alignment** and long-range order |
| $$\( -h \sum X_i \)$$ | Introduces **quantum fluctuations** that flip spins |

If the interaction dominates, the system prefers **aligned spins**.

If the transverse field dominates, spins fluctuate strongly and **long-range order disappears**.

---

## Quantum Phase Transition

At **zero temperature**, changing the field strength \(h\) drives a **quantum phase transition**.

Unlike classical phase transitions (which are driven by temperature), a quantum phase transition occurs because the **ground state of the Hamiltonian changes as a parameter varies**.

For the one-dimensional TFIM, the critical point occurs at

$$
h_c = J
$$

In our simulations we choose

$$
J = 1
$$

so the critical point occurs at

$$
h_c = 1
$$

---

## Phases of the Model

The system exhibits two distinct quantum phases depending on the value of the transverse field.

| Regime | Phase | Physical Behavior |
|------|------|------|
| \(h < 1\) | Ferromagnetic phase | Spins align along the \(z\)-direction and long-range correlations appear |
| \(h > 1\) | Paramagnetic phase | Spins align mainly along the \(x\)-direction due to the transverse field |
| \(h = 1\) | Critical point | Correlation length diverges and the system becomes scale-invariant |

---

## Quantum Criticality

At the critical point

$$
\large
h = 1
$$

the system becomes **quantum critical**.

Several important properties appear at this point:

- The **correlation length diverges**
- Fluctuations occur at **all length scales**
- Observables exhibit **power-law behaviour**
- The system becomes highly **entangled**

Many quantities show clear signatures of this critical behavior, including:

- spin correlation functions
- entanglement entropy
- excitation gap
- order parameters

---

## Importance of the TFIM

The transverse-field Ising model is extremely important because it is one of the **simplest models that exhibits a quantum phase transition**.

Despite its simplicity, it connects to many major areas of physics, including

- quantum spin chains  
- fermionic lattice models (via the **Jordan–Wigner transformation**)  
- conformal field theory  
- quantum information theory  
- quantum simulation

Because of this, the TFIM is frequently used as a **benchmark system for numerical methods**, including

- **Exact diagonalization**
- **Density Matrix Renormalization Group (DMRG)**
- **Time-Evolving Block Decimation (TEBD)**
- **Tensor network algorithms**
  
These methods allow us to study the ground state, entanglement structure, and critical behaviour of the model in detail. For this reason, the TFIM serves as a fundamental playground for exploring many-body quantum physics and quantum phase transitions.

# Comparing Different Methods: Exact Diagonalization, DMRG, and VQE

This repository implements three different computational approaches to study the **one–dimensional Transverse Field Ising Model (TFIM)** and compares their ability to compute ground state properties and detect the quantum phase transition.

The TFIM Hamiltonian used throughout the simulations is

$$
H = -J \sum_{i=1}^{L-1} Z_i Z_{i+1} - h \sum_{i=1}^{L} X_i
$$

where:

- \(J\) is the Ising coupling strength  
- \(h\) is the transverse magnetic field  
- \(Z_i, X_i\) are Pauli operators acting on site \(i\)  
- \(L\) is the number of spins in the chain  

The system exhibits a **quantum phase transition at \(h/J = 1\)** between:

- **Ferromagnetic phase** (\(h < 1\))
- **Paramagnetic phase** (\(h > 1\))

To study this transition, the following observables are computed:

- Ground state energy \(E_0\)
- Local magnetization \( \langle |Z| \rangle \)
- Correlation-based order parameter \(M_{corr}\)
- Nearest-neighbour correlations \( \langle Z_i Z_{i+1} \rangle \)
- Bipartite entanglement entropy \(S(L/2)\)
- Entanglement spectrum

---

# Methods Implemented

## 1. Exact Diagonalization (ED)

Exact diagonalization constructs the **full Hamiltonian matrix** and directly solves the eigenvalue problem to obtain the ground state.

The Hamiltonian is represented as a dense matrix of size:

$$
2^L \times 2^L
$$

For each value of the transverse field \(h\):

1. The full Hamiltonian is constructed.
2. The eigenvalue problem is solved using linear algebra routines.
3. The **ground state vector** is extracted.
4. Physical observables such as magnetization, correlations, and entanglement entropy are computed.

This approach provides **numerically exact results**, but the Hilbert space grows exponentially:

| System Size | Hilbert Space |
|--------------|---------------|
| L = 8 | 256 |
| L = 12 | 4096 |
| L = 16 | 65536 |

Because of this exponential scaling, exact diagonalization is typically limited to **small systems**.

---

## 2. DMRG-style Ground State Solver (Lanczos + Sparse Methods)

The second approach uses **sparse Hamiltonians and iterative eigensolvers** to approximate the ground state efficiently.

Instead of diagonalizing the full matrix, the code:

1. Builds the Hamiltonian using **sparse matrices**
2. Uses the **Lanczos algorithm** (`scipy.sparse.linalg.eigsh`)
3. Extracts the **lowest energy eigenstate**

This approach follows the philosophy behind **Density Matrix Renormalization Group (DMRG)** methods used for one–dimensional quantum systems.

Once the ground state is obtained, the following quantities are computed:

- Correlation based order parameter
- Entanglement entropy from Schmidt values
- Entanglement spectrum
- Local magnetization
- Correlation functions

DMRG-type methods are powerful because they exploit the fact that **low-energy states of 1D systems have low entanglement**, allowing simulations of much larger systems than exact diagonalization.

Advantages:

- Works for **much larger system sizes**
- Efficient for **1D gapped systems**
- Captures entanglement structure

---

## 3. Variational Quantum Eigensolver (VQE)

The third approach implements a **hybrid quantum-classical algorithm** using Qiskit.

Instead of solving the Hamiltonian directly, the ground state is approximated using a **parameterized quantum circuit (ansatz)**.

Workflow:

1. Construct the TFIM Hamiltonian using **Pauli operators**
2. Prepare a parameterized quantum circuit consisting of:
   - Rotation layers
   - Entangling CNOT gates
3. Compute the energy expectation value

$$
E(\theta) = \langle \psi(\theta) | H | \psi(\theta) \rangle
$$

4. Use a classical optimizer (**COBYLA**) to minimize the energy

The optimized circuit approximates the ground state wavefunction.

Once the state is obtained, the code computes:

- Ground state energy
- Magnetization
- Correlation order parameter
- Entanglement entropy
- Entanglement spectrum

---

# Observables Used to Detect the Phase Transition

## Ground State Energy

The ground state energy changes smoothly but shows a change in curvature near the critical point.

## Correlation Order Parameter

A correlation-based magnetization is defined as

$$
M_{corr} = \sqrt{\frac{1}{L^2} \sum_{i,j} \langle Z_i Z_j \rangle}
$$

This quantity distinguishes the two phases:

- Large in the **ferromagnetic phase**
- Small in the **paramagnetic phase**

---

## Entanglement Entropy

The bipartite entanglement entropy is computed by splitting the chain into two halves:

$$
S = - \sum_i \lambda_i^2 \log(\lambda_i^2)
$$

where \(\lambda_i\) are the Schmidt coefficients.

At the **critical point**, the entropy typically **peaks**, reflecting enhanced quantum correlations.

---

# Comparison of Methods

| Method | Accuracy | Scalability | Hardware |
|------|------|------|------|
| Exact Diagonalization | Exact | Poor (exponential scaling) | Classical |
| DMRG / Lanczos | Very High | Excellent for 1D | Classical |
| VQE | Approximate | Designed for quantum hardware | Hybrid quantum-classical |

Key takeaways:

- **Exact diagonalization** provides a benchmark solution.
- **DMRG-style methods** scale to larger systems and are standard in condensed matter physics.
- **VQE** demonstrates how quantum computers may eventually simulate many-body systems.

