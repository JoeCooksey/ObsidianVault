---
type: concept
title: "MIT 18.06 Summer Schedule"
status: complete
created: 2026-05-22
updated: 2026-05-22
tags:
  - mathematics
  - linear-algebra
  - MIT-OCW
  - fall-prep
  - joe-specific
---

# MIT 18.06 Summer Schedule
**35-lecture self-paced plan — complete before Fall 2026 MAT 343**

MIT 18.06 (Professor Gilbert Strang) is the gold-standard free linear algebra course. 35 lectures, 35–50 min each. Direct preparation for Fall 2026 MAT 343 at ASU. Also the math foundation for ML, control theory, signals, and eigenvalue-based circuit analysis simultaneously.

**Course URL:** https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/
(Use the Scholar version — includes recitation videos, problem sets, and exams)

**Total time:** 35 lectures × 45 min average + problem sets ≈ 87 days at 40 min/day, or 12 weeks at 5 lectures/week

---

## Pre-Course Visual Intuition (Do First — 3 hours)

Before starting Strang's lectures, watch **3Blue1Brown's Essence of Linear Algebra** series on YouTube. 15 short videos, ~10 min each, total ~3 hrs.

Search: "3blue1brown essence of linear algebra playlist"

**Why first:** Strang teaches algebraically. 3B1B gives the geometric/visual intuition (what a matrix *does* to space, what an eigenvector *is* geometrically) that makes every Strang lecture land 3× harder. This is 3 hours that multiplies 87 days of learning.

After 3B1B, start Strang Lecture 1.

---

## 12-Week Lecture Schedule

**Target:** 3 lectures/week = 12 weeks. Leaves buffer before Fall 2026 semester.

### Unit 1: Solving Linear Systems and Matrix Operations (Weeks 1–3)
| Lecture | Topic | Problem Set |
|---|---|---|
| 1 | Geometry of Linear Equations | PS 1 |
| 2 | Elimination with Matrices | PS 1 |
| 3 | Matrix Operations and Inverses | PS 1 |
| 4 | Factorization into A = LU | PS 2 |
| 5 | Transposes, Permutations, Spaces | PS 2 |
| 6 | Column Space and Null Space | PS 2 |
| 7 | Null Space and Pivots | PS 3 |
| 8 | Solving Ax = 0: Reduced Row Echelon | PS 3 |
| 9 | Solving Ax = b | PS 3 |

**MAT 343 connection:** The first half of MAT 343 is almost entirely this material. Getting through Week 3 before Fall semester means you'll be reviewing, not learning for the first time.

### Unit 2: Vector Spaces (Weeks 4–6)
| Lecture | Topic | Problem Set |
|---|---|---|
| 10 | Four Fundamental Subspaces | PS 4 |
| 11 | Matrix Spaces; Rank 1 | PS 4 |
| 12 | Graphs, Networks, Incidence Matrices | PS 4 |
| 13 | Orthogonal Vectors and Subspaces | PS 5 |
| 14 | Projections onto Subspaces | PS 5 |
| 15 | Projection Matrices and Least Squares | PS 5 |
| 16 | Orthogonal Matrices and Gram-Schmidt | PS 6 |
| 17 | Properties of Determinants | PS 6 |
| 18 | Determinant Formulas and Cofactors | PS 6 |

**EE connection:** Orthogonality and projections → Fourier series (PHY 131), least squares fitting (signal processing), Gram-Schmidt (QR decomposition for numerical methods).

### Unit 3: Eigenvalues and Eigenvectors (Weeks 7–9)
| Lecture | Topic | Problem Set |
|---|---|---|
| 19 | Cramer's Rule, Inverse, and Volumes | PS 7 |
| 20 | Eigenvalues and Eigenvectors | PS 7 |
| 21 | Diagonalization | PS 7 |
| 22 | Differential Equations and exp(At) | PS 8 |
| 23 | Markov Matrices; Fourier Series | PS 8 |
| 24 | Symmetric Matrices | PS 8 |
| 25 | Positive Definite Matrices | PS 9 |
| 26 | Similar Matrices and Jordan Form | PS 9 |
| 27 | Singular Value Decomposition (SVD) | PS 9 |

**This is the most important unit.** Eigenvalues = natural frequencies of circuits, poles of transfer functions, principal components of data, modes of vibration. **Lecture 22** connects directly to Laplace transforms (per [[Laplace Transform — Mathematical Foundations]]) — differential equations become algebra. **Lecture 27** (SVD) is the core of data compression, PCA, and modern ML.

### Unit 4: Applications and Review (Weeks 10–12)
| Lecture | Topic | Notes |
|---|---|---|
| 28 | Linear Transformations | Solidifies geometric intuition |
| 29 | Change of Basis | Important for coordinate systems (EEE 202 phasors) |
| 30 | Linear Systems of Equations | Review + applications |
| 31 | Exam 3 Review | Practice exam |
| 32 | Left and Right Inverses; Pseudoinverse | SVD application |
| 33 | Fourier Series, FFT, Complex Matrices | Direct EE signal processing connection |
| 34 | Complex Matrices; Fast Fourier Transform | Key for digital signal processing |
| 35 | Linear Algebra Review | Full course synthesis |

---

## How to Do Each Lecture (Protocol)

**Before the lecture:**
- Skim the lecture notes PDF (5 min) — available on OCW for each lecture

**During the lecture:**
- Pause and try to work out any example before Strang does it
- Write down the key equation or concept on paper (not typed — motor memory)
- Annotate the connection to circuits/signals/ML if you see it

**After the lecture:**
- Do at least 3 problems from the corresponding problem set before moving on
- The problem set gap (attempt → verify) is where skill acquisition happens
- Check against MIT solutions (available on OCW)

---

## Minimum Viable Version

If summer gets compressed, prioritize these 12 lectures over everything else:

1. Lecture 1 (Geometry of Linear Equations)
2. Lecture 4 (LU Decomposition)
3. Lecture 6 (Column Space and Null Space)
4. Lecture 10 (Four Fundamental Subspaces)
5. Lecture 14 (Projections — key for least squares)
6. Lecture 16 (Gram-Schmidt)
7. Lecture 20 (Eigenvalues and Eigenvectors)
8. Lecture 21 (Diagonalization)
9. Lecture 22 (Differential Equations and exp(At))
10. Lecture 24 (Symmetric Matrices)
11. Lecture 27 (SVD — key for everything modern)
12. Lecture 33 (FFT — direct EE application)

---

## MAT 343 Connection Map

| MAT 343 topic | MIT 18.06 Lectures |
|---|---|
| Matrix operations, Gaussian elimination | 1–5 |
| Vector spaces, subspaces | 6–10 |
| Basis, dimension, rank | 10–11 |
| Orthogonality, least squares | 13–16 |
| Determinants | 17–19 |
| Eigenvalues, diagonalization | 20–21 |
| Symmetric matrices, quadratic forms | 24–25 |
| Linear transformations | 28–29 |

If you complete MIT 18.06 before Fall 2026, MAT 343 is review. You can use lecture time to go deeper rather than learning for the first time.

---

## ML/AI Connection Map

| 18.06 Concept | ML Application |
|---|---|
| Eigenvalues | PCA (Principal Component Analysis) |
| SVD (L27) | Data compression, image processing, recommendation systems |
| Least squares (L14–15) | Linear regression — the simplest ML model |
| LU decomposition | Neural network weight initialization |
| Positive definite matrices | Covariance matrices, kernel methods |
| Gram-Schmidt | QR decomposition in numerical methods |

---

## Related Pages
- [[Laplace Transform — Mathematical Foundations]] — direct connection via exp(At) in L22
- [[Deep Work Task Taxonomy]] — MIT 18.06 problem sets are S-tier deep work tasks
- [[Polymath Learning System]] — mathematics as universal complement domain
- [[Summer 2026 Tier List]] — MIT 18.06 is #3 S-tier action
