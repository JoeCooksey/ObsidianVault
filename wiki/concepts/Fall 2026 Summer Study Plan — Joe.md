---
type: concept
title: "Fall 2026 Summer Study Plan — Joe"
created: 2026-05-01
updated: 2026-05-01
tags:
  - study-plan
  - fall-2026
  - ASU
  - circuits
  - linear-algebra
  - physics
status: developing
related:
  - "[[EEE 202 Circuits I — Topics and Prep]]"
  - "[[MAT 343 Applied Linear Algebra — Topics and Prep]]"
  - "[[PHY 131 University Physics II EM — Topics and Prep]]"
  - "[[Research - Fall 2026 Course Prep Plan]]"
---

# Fall 2026 Summer Study Plan — Joe

**Target**: Enter Fall 2026 ahead in all three subjects — not just familiar, but able to solve problems from day one.

**Courses**:
- EEE 202 Circuits I (Vasileska) + Lab (Myhajlenko)
- MAT 343 Applied Linear Algebra (Espanol)
- PHY 131/132 University Physics II E&M (Qing/Reaves)

**Timeline**: ~May 5 – August 23, 2026 (16 weeks)
**Weekly load**: 15–20 hours/week (2–3 hrs/day, 6 days/week)

---

## Weekly Schedule Template

| Day | Subject | Session (min) |
|-----|---------|--------------|
| Mon | Primary (Circuits) | 90 |
| Tue | Secondary (Physics E&M) | 90 |
| Wed | Primary (Circuits) | 90 |
| Thu | Linear Algebra | 90 |
| Fri | Secondary (Physics E&M) | 90 |
| Sat | MATLAB / LTSpice / Problem sets | 90–120 |
| Sun | Rest or light review | 0–30 |

**Rule**: Never study the same subject more than 90 min in one sitting. Switch to reset focus.

---

## Phase 1: Foundations (Weeks 1–6, May 5 – June 15)

**Goal**: Master circuit analysis core (Units 1–3) + electrostatics basics + linear algebra orientation.

### Weeks 1–2: Circuit Theory Core
- KVL, KCL, Ohm's Law — Khan Academy DC Circuits (~6 hrs)
- Nodal analysis and mesh analysis (~4 hrs)
- Thevenin and Norton equivalents + source transformation (~4 hrs)
- **Deliverable**: Solve a 3-mesh DC circuit by hand; verify in LTSpice

### Weeks 3–4: Electrostatics (PHY 131 Units 1–4)
- Coulomb's Law, electric field E from point charges (~3 hrs)
- Electric potential V, ΔV, V-E relation (~3 hrs)
- Gauss's Law — 3 canonical geometries: sphere, cylinder, infinite plane (~5 hrs)
- Khan Academy E&M: Electrostatics section (full)
- **Deliverable**: Derive E-field for a uniformly charged sphere using Gauss's Law

### Weeks 5–6: Linear Algebra Orientation
- 3Blue1Brown "Essence of Linear Algebra" — all 16 episodes (~4 hrs)
- MATLAB basics: matrix creation, A*B, det(A), inv(A), eig(A), plot (~3 hrs)
- Row reduction by hand: REF and RREF for 3×3 and 4×4 systems (~4 hrs)
- **Deliverable**: Row-reduce a 4×4 augmented matrix; run eig() on 2×2 matrix in MATLAB

---

## Phase 2: Depth (Weeks 7–12, June 16 – July 27)

**Goal**: AC circuit analysis, magnetic fields, linear algebra depth (vector spaces + eigenvalues).

### Weeks 7–8: Phasors and AC Circuits
- Complex number arithmetic: magnitude, phase, conjugate, Euler's formula (~3 hrs)
- Impedance: Z_R = R, Z_L = jωL, Z_C = 1/jωC (~2 hrs)
- AC steady-state phasor analysis, KVL/KCL in phasor domain (~4 hrs)
- LTSpice: build RC voltage divider, verify AC magnitude and phase (~3 hrs)
- **Deliverable**: Find V_out/V_in phasor for RC low-pass filter at 3 frequencies

### Weeks 9–10: Magnetic Fields and Induction
- Magnetic force on moving charge, circular motion in B field (~3 hrs)
- Biot-Savart Law — infinite wire, circular coil (~3 hrs)
- Faraday's Law and Lenz's Law — 10+ problems including changing area and changing B (~5 hrs)
- RL circuits: natural response i(t) = I₀ e^(-t/τ), τ = L/R (~3 hrs)
- **Deliverable**: Explain transformer operation using Faraday's Law; solve RL step response

### Weeks 11–12: Linear Algebra Depth
- MIT 18.06 Lectures 1–15: systems → vector spaces → LU → column/null space (~12 hrs selective)
- MATLAB: solve Ax = b, null(), orth(), rank() (~3 hrs)
- Problem sets from MIT 18.06SC with solutions (~5 hrs)
- **Deliverable**: State the 4 fundamental subspaces of a matrix; solve underdetermined system

---

## Phase 3: Integration (Weeks 13–16, July 28 – August 23)

**Goal**: Laplace transforms, eigenvalues, RLC circuits — the hard end of all three courses. Full integration.

### Weeks 13–14: Laplace Transforms and RLC
- Paul's Online Notes — Laplace transform: definition, properties, pairs table (~4 hrs)
- S-domain circuit models: replace L→sL, C→1/sC, apply KVL in s-domain (~4 hrs)
- Partial fractions and inverse Laplace (~3 hrs)
- RLC second-order response: overdamped, critically damped, underdamped (~4 hrs)
- PSpice: install + first simulation (DC and transient) (~2 hrs)
- **Deliverable**: Find v(t) for RLC series circuit step input using Laplace; verify in LTSpice

### Weeks 15–16: Eigenvalues + Final Integration Review
- MIT 18.06 Lectures 21–24 (eigenvalues, eigenvectors, diagonalization) (~6 hrs)
- Connect eigenvalues to circuit natural frequencies: poles = eigenvalues of system matrix (~2 hrs)
- Final review: Thevenin/Norton, phasors, Faraday/Ampere, Gauss symmetry cases (~3 hrs)
- Practice exam sets: 1 EEE 202-style + 1 MAT 343-style + 1 PHY 131-style (~6 hrs)
- **Deliverable**: Eigenvalues of 3×3 state-space matrix; connect to overdamped/underdamped RLC

---

## Synergies to Exploit

| Study Both | Reason |
|-----------|--------|
| EEE 202 Units 1–3 + PHY 131 Ch 25–26 | KVL/KCL appears in both; same circuit laws, same week |
| EEE 202 Units 4–5 + PHY 131 Ch 30 | RLC transient response is identical in both courses |
| EEE 202 Unit 6 + PHY 131 Ch 31 | AC phasors appear in both; studying once covers both |
| MAT 343 LU/linear systems + EEE 202 nodal analysis | Large nodal circuits solved by Ax=b; studying LA makes circuits feel trivial |

---

## Resource Quick-Reference

| Resource | Subject | Free? | Hours needed |
|----------|---------|-------|-------------|
| Khan Academy DC Circuits | Circuits Units 1–3 | Yes | 6 |
| Khan Academy E&M | PHY 131 Units 1–14 | Yes | 20 |
| Paul's Online Math Notes — Laplace | Circuits Units 7–8 | Yes | 5 |
| 3Blue1Brown Essence of Linear Algebra | MAT 343 overview | Yes | 4 |
| MIT 18.06 OCW (selective lectures) | MAT 343 depth | Yes | 15 |
| LTSpice (simulation) | Circuits verification | Yes | ongoing |
| MATLAB (practice) | MAT 343 software | Yes (ASU license) | 8 |
| Young & Freedman textbook | PHY 131 primary | Canvas | primary |
| Irwin textbook | EEE 202 primary | Purchase/rent | primary |

---

## Key Principles

1. **Solve problems, not just watch videos** — active recall beats passive review 3:1 for retention
2. **LTSpice and MATLAB are the "lab"** — simulate every circuit you solve; verify everything numerically
3. **EEE 202 + PHY 131 overlap** — studying them together in Phases 2–3 is the highest-efficiency move in this schedule
4. **Eigenvalues connect everything** — MAT 343 eigenvalues = poles of EEE 202 transfer functions = natural frequencies of PHY 131 RLC circuits; when you see this connection, all three courses click
