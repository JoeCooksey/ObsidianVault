---
type: concept
title: "MAT 343 Applied Linear Algebra — Topics and Prep"
created: 2026-05-01
updated: 2026-05-01
tags:
  - linear-algebra
  - mathematics
  - ASU
  - fall-2026
status: developing
related:
  - "[[Circuit Theory Fundamentals]]"
  - "[[Fall 2026 Summer Study Plan — Joe]]"
  - "[[MIT 18.06 Linear Algebra OCW]]"
---

# MAT 343 Applied Linear Algebra — Topics and Prep

**Instructor**: Espanol
**Software**: MATLAB throughout the course

## Topic Map (in order)

| # | Unit | Core Skills |
|---|------|-------------|
| 1 | **Linear Systems** | Represent Ax=b; row reduction to REF/RREF |
| 2 | **Matrix Operations** | Addition, multiplication, transpose, inverse |
| 3 | **LU Factorization** | Factor A = LU; forward/back substitution |
| 4 | **Determinants** | det(A), cofactor expansion, geometric interpretation |
| 5 | **Vector Spaces** | Subspaces, span, linear independence, basis, dimension |
| 6 | **Linear Transformations** | Maps between vector spaces, kernel, image |
| 7 | **Eigenvalues & Eigenvectors** | Characteristic polynomial, diagonalization |
| 8 | **Norms & Inner Products** | Dot product, orthogonality, projection, Gram-Schmidt |
| 9 | **Decompositions** | QR, SVD, PCA applications |
| 10 | **Applications** | Least squares, Markov chains, network analysis |

## Why This Matters for EE

| Linear Algebra Tool | EE Application |
|--------------------|----------------|
| Ax = b (linear system) | Nodal analysis of large multi-mesh circuits |
| LU factorization | Efficient repeated circuit solves (SPICE algorithm) |
| Eigenvalues | Stability analysis — poles of transfer functions |
| SVD | Signal processing, PCA, image/data compression |
| Orthogonal projection | Least-squares circuit parameter fitting |
| State-space matrices | Control systems: ẋ = Ax + Bu |

## Must-Know Before Day 1

- Solve 3×3 system by hand (substitution or Gaussian elimination)
- Basic MATLAB: `A = [1 2; 3 4]`, `A*b`, `det(A)`, `inv(A)`, `eig(A)`
- Dot product and vector magnitude (from calculus/physics)

## Best Free Resources

| Resource | What it covers | Time |
|----------|---------------|------|
| 3Blue1Brown "Essence of Linear Algebra" (YouTube, 16 episodes) | All units conceptually; best visualization | ~4 hrs |
| MIT 18.06 OCW — Gilbert Strang (34 lectures) | Full course, university-level | ~40 hrs (selective) |
| MIT 18.06SC OCW — Problem sets with solutions | Drill practice with feedback | ongoing |
| MATLAB Onramp (MathWorks, free) | MATLAB syntax basics | ~2 hrs |

## Summer Prep Priority

1. **3Blue1Brown first** — watch all 16 episodes to build geometric intuition (6-8 hours)
2. **MATLAB basics** — before class starts, be able to: solve Ax=b, compute eig(A), plot vectors
3. **Row reduction by hand** — essential for first 3 weeks of the course
4. **Eigenvalues conceptually** — most important unit for EE; understand what Av = λv means geometrically

## Key Insight

Eigenvalues tell you how a matrix "stretches" space along special directions. In circuits: the eigenvalues of the circuit's system matrix are the natural frequencies (poles). A stable circuit has all eigenvalues with negative real parts.
