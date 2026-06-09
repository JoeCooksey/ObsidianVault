---
type: concept
title: "Linear Algebra in Electrical Engineering"
status: developing
created: 2026-06-09
updated: 2026-06-09
tags:
  - mathematics
  - linear-algebra
  - electrical-engineering
  - foundations
related:
  - "[[Linear Algebra for AI and Quant]]"
  - "[[Calculus in Electrical Engineering]]"
  - "[[Differential Equations in Electrical Engineering]]"
---

# Linear Algebra in Electrical Engineering

Linear algebra is the "many things at once" math of EE. Calculus handles one signal changing in time; linear algebra handles **n equations, n unknowns simultaneously** — which is what every real circuit, control system, and communication channel is. It shows up in three escalating roles.

---

## Role 1 — Circuit Analysis: Ax = b

Nodal and mesh analysis turn any linear circuit into a system of equations. A 3-loop resistive circuit becomes (Source: [[Linear Algebra in Electrical Circuits (UW Math 308)]]):

$$\begin{bmatrix} 76 & -25 & -50 \\ -25 & 56 & -1 \\ -50 & -1 & 106 \end{bmatrix} \begin{bmatrix} i_1 \\ i_2 \\ i_3 \end{bmatrix} = \begin{bmatrix} 10 \\ 0 \\ 0 \end{bmatrix}$$

- Each row = one KVL loop equation (or KCL node equation); the matrix is the resistance (or conductance) matrix.
- **Gaussian elimination** row-reduces to the solution: $i_1 = 0.245$ A, etc.
- Substitution works for 2-3 unknowns; beyond that it drowns. Matrix form + a computer scales to circuits with hundreds of thousands of components — **this is literally what SPICE does internally** every time you run a simulation. (confidence: high)

This is why MAT 242/342 is a prerequisite for circuits-heavy coursework: nodal analysis IS solving Ax = b.

---

## Role 2 — State-Space and Eigenvalues: Dynamics as Matrices

When circuits have caps/inductors, the coupled ODEs of [[Differential Equations in Electrical Engineering]] get packed into one matrix equation:

$$\dot{\mathbf{x}} = A\mathbf{x} + B\mathbf{u}, \quad \mathbf{y} = C\mathbf{x} + D\mathbf{u}$$

where $\mathbf{x}$ is the state vector (capacitor voltages, inductor currents).

- **Eigenvalues of A = the poles of the system.** They determine stability and natural response — the same damping/oscillation behavior as the RLC characteristic equation, generalized to any size system. (confidence: high)
- **Eigenvectors = the modes** — the natural "shapes" of response.
- A 2-loop motor controller and a 50-state power grid model use the identical framework. This is the backbone of modern control (EEE 480), MIMO systems, and Kalman filtering.

---

## Role 3 — Signal Processing and Communications: Transforms as Matrices

- **The DFT is a matrix multiplication**: $X = W x$, where $W$ is the DFT matrix. The FFT is a fast factorization of $W$. OFDM (Wi-Fi, 5G, LTE) is built directly on DFT/IDFT operations. (Source: [[Matrix Theory in Wireless Communications (MDPI Algorithms 2016)]], confidence: high)
- **Filtering and convolution** are linear transformations — FIR filters are matrix-vector products.
- **SVD decomposes a MIMO wireless channel** into independent parallel single-input single-output channels — this is how a 4×4 MIMO router sends 4 simultaneous streams without interference. Channel capacity = sum over singular values. (confidence: high)
- **PCA/SVD** for noise reduction, feature extraction (radar, speech), and compression — the same math as [[Linear Algebra for AI and Quant]] (LoRA, embeddings).

---

## Summary Table

| LA Tool | EE Application | Course Where Used |
|---|---|---|
| Ax = b, Gaussian elimination | Nodal/mesh analysis; SPICE internals | EEE 202 |
| Matrix inverse / determinants | Thevenin equivalents, two-port networks | EEE 202 |
| Eigenvalues/eigenvectors | Stability, poles, natural modes | EEE 350, 480 |
| State-space (A, B, C, D) | Control systems, observers, Kalman filters | EEE 480 |
| DFT matrix | OFDM, spectrum analysis, FFT | EEE 350, 407 |
| SVD | MIMO channels, PCA, model reduction | EEE 407, ML courses |
| Complex vectors/phasors | AC steady-state analysis | EEE 202 |

---

## The One-Sentence Version

> Calculus describes **one** component changing in time; linear algebra solves **all of them at once** — and eigenvalues tell you whether the whole system rings, decays, or blows up.

---

## Related
- [[Linear Algebra for AI and Quant]] — same math, AI/quant applications
- [[Differential Equations in Electrical Engineering]] — state-space packs these ODEs into matrices
- [[Calculus in Electrical Engineering]]
- [[Research - Math and Physics Pipeline to Electrical Engineering]]
