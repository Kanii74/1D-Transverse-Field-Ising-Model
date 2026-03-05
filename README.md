# Transverse-Field Ising Model Phase Scan (DMRG with Quimb)

This project studies the **1D Transverse-Field Ising Model (TFIM)** using the **Density Matrix Renormalization Group (DMRG)** algorithm implemented with the `quimb` tensor network library.

The goal is to numerically observe the **quantum phase transition** by scanning the transverse field strength and measuring:

* **Ground state magnetization** (order parameter)
* **Entanglement entropy** (quantum correlations)

By varying the transverse field, the simulation captures how the system transitions between an **ordered ferromagnetic phase** and a **quantum paramagnetic phase**.

---

## Model

The Hamiltonian of the **1D transverse-field Ising model** is

$$
H = -J \sum_{i} Z_i Z_{i+1} - h \sum_{i} X_i
$$

where

* $J$ is the nearest-neighbour coupling strength
* $h$ is the transverse magnetic field
* $Z_i$ and $X_i$ are **Pauli operators** acting on site $i$

The first term describes the **spin-spin interaction**, which favors aligned spins along the $z$ direction.

The second term represents the **transverse magnetic field**, which tends to flip spins and introduces **quantum fluctuations**.

At **zero temperature**, this model exhibits a **quantum phase transition** at

$$
h_c = J
$$

For this simulation we set $J = 1$, so the critical point occurs at

$$
h_c = 1
$$

The phases are:

* **Ferromagnetic phase** ($h < 1$)
  Spins align along the $z$ direction, producing a non-zero magnetization.

* **Paramagnetic phase** ($h > 1$)
  The transverse field dominates, destroying long-range order.

This transition is driven purely by **quantum fluctuations**, rather than thermal effects.

---

## What the Code Does

1. Builds the TFIM Hamiltonian as a **Matrix Product Operator (MPO)**.

2. Runs **DMRG** to approximate the ground state as a **Matrix Product State (MPS)**.

3. Computes:

   The average **$Z$-magnetization** is computed as

$$
m = \frac{1}{L}\sum_{i=1}^{L} \left| \langle Z_i \rangle \right|
$$

which serves as the **order parameter** of the system.

The **entanglement entropy** at the center bond is defined as

$$
S = -\mathrm{Tr}(\rho \log \rho)
$$

where $\rho$ is the **reduced density matrix** obtained by partitioning the system into two halves.


4. Repeats the calculation for different values of the transverse field $h$.

5. Plots magnetization and entanglement entropy as functions of $h$.

---

## Parameters

Inside the script:

```python
L = 40                       # Number of lattice sites
h_values = np.linspace(0, 2, 20)
```

* `L` controls the **system size**
* `h_values` determines the **range of transverse field strengths**

A lattice of **40 sites** is large enough to clearly observe the **quantum phase transition** while remaining computationally efficient.

---

## Simulation Results

The following figure shows how the **order parameter** and **entanglement entropy** change as the transverse field is varied.

* The **top panel** shows the magnetization.
* The **bottom panel** shows the entanglement entropy.
* The **dashed vertical line** marks the critical point $h = 1$.

Near the phase transition:

* Magnetization rapidly drops to zero.
* Entanglement entropy increases, indicating strong quantum correlations.

### Phase Transition Scan
<img width="1280" height="800" alt="Screenshot 2026-03-05 at 12 43 02 PM" src="https://github.com/user-attachments/assets/0794a442-8c77-4c1f-a9c2-63c3d4ca4099" />


---

## Numerical Results

The values obtained during the simulation are shown below.

| h    | Magnetization | Entanglement Entropy |
| ---- | ------------- | -------------------- |
| 0.00 | 0.500         | 0.000                |
| 0.11 | 0.497         | 0.000                |
| 0.21 | 0.486         | 0.002                |
| 0.32 | 0.463         | 0.012                |
| 0.42 | 0.408         | 0.053                |
| 0.53 | 0.000         | 0.562                |
| 0.63 | 0.000         | 0.322                |
| 0.74 | 0.000         | 0.230                |
| 0.84 | 0.000         | 0.176                |
| 0.95 | 0.000         | 0.142                |
| 1.05 | 0.000         | 0.117                |
| 1.16 | 0.000         | 0.098                |
| 1.26 | 0.000         | 0.084                |
| 1.37 | 0.000         | 0.073                |
| 1.47 | 0.000         | 0.064                |
| 1.58 | 0.000         | 0.057                |
| 1.68 | 0.000         | 0.051                |
| 1.79 | 0.000         | 0.046                |
| 1.89 | 0.000         | 0.041                |
| 2.00 | 0.000         | 0.038                |

---

## Physical Interpretation

The simulation clearly demonstrates the **quantum phase transition** of the TFIM.

* For **small $h$**, the interaction term dominates and the system remains **ferromagnetically ordered**, producing a large magnetization.

* Near **$h \approx 1$**, quantum fluctuations become strong and the **entanglement entropy peaks**, indicating a highly correlated many-body state.

* For **large $h$**, the transverse field dominates and the system enters a **paramagnetic phase**, where magnetization vanishes and spins align with the field.

This behavior is a hallmark of **quantum critical systems** and is widely studied in **quantum many-body physics** and **tensor network simulations**.
