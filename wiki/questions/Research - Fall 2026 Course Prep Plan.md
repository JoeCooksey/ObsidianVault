---
type: synthesis
title: "Research: Fall 2026 Course Prep Plan"
created: 2026-05-01
updated: 2026-05-01
tags:
  - research
  - fall-2026
  - ASU
  - circuits
  - linear-algebra
  - physics
  - study-plan
status: developing
related:
  - "[[EEE 202 Circuits I — Topics and Prep]]"
  - "[[MAT 343 Applied Linear Algebra — Topics and Prep]]"
  - "[[PHY 131 University Physics II EM — Topics and Prep]]"
  - "[[Fall 2026 Summer Study Plan — Joe]]"
  - "[[Circuit Theory Fundamentals]]"
  - "[[Electromagnetism Foundations for EE]]"
  - "[[MIT 18.06 Linear Algebra OCW Gilbert Strang]]"
  - "[[EEE 202 Course Page ASU Tsakalis]]"
sources:
  - "[[EEE 202 Course Page ASU Tsakalis]]"
  - "[[MIT 18.06 Linear Algebra OCW Gilbert Strang]]"
---

# Research: Fall 2026 Course Prep Plan

## Overview

Joe's Fall 2026 schedule is three-course heavy in foundational math/physics/EE: EEE 202 Circuits I (Vasileska, lab Myhajlenko), MAT 343 Applied Linear Algebra (Espanol), and PHY 131/132 University Physics II E&M (Qing, lab Reaves). This research maps the full topic sequence for each course, identifies the best free preparation resources, and produces a 16-week summer study plan. The three courses share deep topic overlap that makes combined study highly efficient.

## Key Findings

- **EEE 202 is the most critical course to prepare for**: 8 units from KVL/KCL through Laplace transforms; the first 3 units (fundamentals, nodal/mesh analysis, Thevenin/Norton) are front-loaded in Week 1-4 and must be solid before Day 1 (Source: [[EEE 202 Course Page ASU Tsakalis]])
- **PHY 131 and EEE 202 overlap ~40% by topic**: DC circuits (KVL/KCL) and RL/RLC transients appear in both courses simultaneously; studying them together is the single highest-efficiency move available (Source: PHY 131 ASU Syllabus)
- **MAT 343 eigenvalues = EEE 202 poles = PHY 131 natural frequencies**: This is the cross-course insight that ties all three together — the eigenvalues of a circuit's system matrix are its natural frequencies; overdamped/critically damped/underdamped maps directly to real/repeated/complex eigenvalue cases
- **3Blue1Brown + MIT 18.06 is the optimal free linear algebra stack**: 3B1B builds geometric intuition (4 hrs); MIT 18.06SC adds rigor and problem-set drill; together they exceed any textbook-only approach (Source: [[MIT 18.06 Linear Algebra OCW Gilbert Strang]])
- **MATLAB literacy before Day 1 is mandatory for MAT 343**: The course uses MATLAB throughout; students who arrive knowing `eig()`, `inv()`, `null()`, and `plot()` skip the first 2 weeks of tutorial friction
- **Gauss's Law is the hardest single topic in PHY 131**: The vector flux integral requires multivariable calculus intuition; the workaround is to master the 3 symmetric geometries (sphere, cylinder, plane) cold before class
- **PSpice prep = LTSpice**: EEE 202 uses PSpice; LTSpice is free and compatible enough for summer practice; build 10+ circuits in LTSpice before using PSpice for the first time
- **16 weeks is sufficient**: At 15–20 hrs/week, all three courses can be meaningfully previewed; the key is Phase 1 (Weeks 1–6) which must be treated as non-negotiable minimum

## Key Entities

- [[Dragica Vasileska]]: EEE 202 Circuits I lecture instructor, Fall 2026
- [[Quan Qing]]: PHY 131 lecture instructor, office hrs Tue 1:30 PM PSB 147
- Espanol: MAT 343 Applied Linear Algebra instructor
- Myhajlenko: EEE 202 Lab instructor
- Reaves: PHY 132 Lab instructor

## Key Concepts

- [[EEE 202 Circuits I — Topics and Prep]]: 8-unit topic map, textbook, software, resource list
- [[MAT 343 Applied Linear Algebra — Topics and Prep]]: 10-unit topic map, EE applications, resource ladder
- [[PHY 131 University Physics II EM — Topics and Prep]]: 16-unit topic map, critical overlap with EEE 202
- [[Fall 2026 Summer Study Plan — Joe]]: 3-phase, 16-week schedule with weekly deliverables

## Cross-Course Synergy Table

| PHY 131 Chapter | EEE 202 Unit | Topic | Study Both Simultaneously |
|----------------|--------------|-------|--------------------------|
| Ch 25–26 | Units 1–3 | KVL/KCL, Thevenin/Norton | Yes — identical content |
| Ch 30 | Units 4–5 | RLC transient response | Yes — identical ODE structure |
| Ch 31 | Unit 6 | AC phasors, impedance | Yes — identical technique |
| (state-space) | Unit 8 | Laplace / eigenvalues | MAT 343 eigenvalues = EEE poles |

## Contradictions

None found. Topic maps from ASU syllabi are internally consistent. Instructor (Vasileska vs. Tsakalis) does not change the core topic sequence.

## Open Questions

- What is Espanol's grading style / exam format for MAT 343? — check RateMyProfessors before semester
- What PSpice version does ASU license for EEE 202? — confirm at orientation to ensure compatible install
- Does PHY 131 Qing curve exams? — check Studocu for past class reports
- Is Lay's *Linear Algebra and Its Applications* the required MAT 343 textbook? — not confirmed from search; verify on Day 1

## Sources

- [[EEE 202 Course Page ASU Tsakalis]]: Tsakalis, ASU faculty page, 2024
- [[MIT 18.06 Linear Algebra OCW Gilbert Strang]]: Strang, MIT OCW, 2010
- ASU PHY 131 Syllabus (Fall 2022 online version)
- ASU MAT 343 syllabi (multiple semesters, consistent)
