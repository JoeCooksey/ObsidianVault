---
type: source
source_type: paper
title: "Linear Algebra in Electrical Circuits (UW Math 308)"
author: "Seamleng Taing"
date_published: 2001-12-02
url: "https://sites.math.washington.edu/~king/coursedir/m308a01/Projects/m308a01-pdf/taing.pdf"
confidence: high
created: 2026-06-09
updated: 2026-06-09
tags:
  - source
  - linear-algebra
  - circuits
key_claims:
  - "Nodal and loop analysis convert circuits into n equations with n unknowns"
  - "Gaussian elimination on the augmented matrix replaces tedious substitution"
  - "Computers + matrices analyze circuits with hundreds of thousands of components"
---

# Linear Algebra in Electrical Circuits (UW Math 308)

University of Washington Math 308 project paper (2001). Old, but foundational content — the math hasn't changed. Walks the exact pipeline from circuit to matrix solution with fully worked examples.

## What It Contributes

- **The method**: simple circuits → series/parallel reduction + Ohm's law; larger circuits → loop current or nodal voltage analysis → system of linear equations → augmented matrix → Gaussian elimination.
- **Worked 6-loop example**: loop equations collected into a 6×7 augmented matrix, row-reduced to give all six mesh currents (i₁ = 0.478 A …).
- **Worked nodal example**: 2 node equations → 2×3 matrix → V₁ = 75 V, V₃ = 50 V.
- **The scaling argument**: substitution dies past ~3 unknowns; matrix form + computers handle "ridiculously large circuits" — the conceptual basis of SPICE.

## Used By
- [[Linear Algebra in Electrical Engineering]]
- [[Research - Math and Physics Pipeline to Electrical Engineering]]
