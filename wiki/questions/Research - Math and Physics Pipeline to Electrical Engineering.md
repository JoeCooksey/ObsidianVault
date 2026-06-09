---
type: synthesis
title: "Research - Math and Physics Pipeline to Electrical Engineering"
created: 2026-06-09
updated: 2026-06-09
tags:
  - research
  - electrical-engineering
  - mathematics
  - physics
  - curriculum
status: developing
related:
  - "[[Calculus in Electrical Engineering]]"
  - "[[Differential Equations in Electrical Engineering]]"
  - "[[Linear Algebra in Electrical Engineering]]"
  - "[[Classical Mechanics in Electrical Engineering]]"
  - "[[Electromagnetism Foundations for EE]]"
  - "[[University Physics 3 in Electrical Engineering]]"
  - "[[ASU EE Year 1-2 Curriculum Map]]"
sources:
  - "[[Linear Algebra in Electrical Circuits (UW Math 308)]]"
  - "[[Matrix Theory in Wireless Communications (MDPI Algorithms 2016)]]"
  - "[[ASU PHY 241 Course Description]]"
  - "[[Quantum Mechanics in Semiconductor Devices (overview)]]"
---

# Research: Math and Physics Pipeline to Electrical Engineering

## Overview

The six "weed-out" courses are not a hazing ritual — they are one connected pipeline. **The math sequence builds the language EE is written in (calculus → differential equations → linear algebra), and the physics sequence builds the content it describes (mechanics → E&M → modern physics).** Every upper-division EE course is one of these six wearing a lab coat.

## The Dependency Graph

```
MATH TRACK                      PHYSICS TRACK
Calc 1 (derivatives) ──┐
Calc 2 (integrals)     ├──→ Physics 1: Mechanics (F=ma, energy, oscillation)
Calc 3 (vector calc)   ├──→ Physics 2: E&M (fields, Maxwell)
Diff Eq (dynamics)     ├──→ Physics 3: thermo + optics + quantum
Linear Algebra (systems)┘
        │                          │
        ▼                          ▼
   THE LANGUAGE                THE CONTENT
   (how EE computes)           (what EE describes)
        └────────────┬─────────────┘
                     ▼
   Circuits (EEE 202) → Signals (350) → Devices (352)
   → Electronics (334) → EM (340) → Control (480)
```

(ASU's catalog enforces this literally: PHY 241 requires PHY 121, PHY 131, and Calc 2, with Calc 3 as co-req — Source: [[ASU PHY 241 Course Description]].)

## How Each Course Feeds EE

**1. Calculus (1-3) — the vocabulary.** Derivatives ARE component laws: $i = C\,dv/dt$, $v = L\,di/dt$. Integrals ARE energy, charge, and RMS values. Vector calculus (Calc 3) exists largely because Maxwell's equations needed it — div, curl, and surface integrals are the notation of every field problem. Detail: [[Calculus in Electrical Engineering]]. (confidence: high)

**2. Differential Equations — the dynamics.** Any circuit with a capacitor or inductor IS an ODE; KVL just writes it down. First-order → RC/RL transients and filters; second-order → RLC resonance and damping; Laplace transform → transfer functions, the central tool of signals and control. Detail: [[Differential Equations in Electrical Engineering]]. (confidence: high)

**3. Linear Algebra — the scale.** Nodal/mesh analysis turns circuits into Ax = b; Gaussian elimination solves them; SPICE is this automated (Source: [[Linear Algebra in Electrical Circuits (UW Math 308)]]). Eigenvalues of the state matrix = system poles = stability. The DFT is a matrix; SVD splits MIMO channels into independent streams (Source: [[Matrix Theory in Wireless Communications (MDPI Algorithms 2016)]]). Detail: [[Linear Algebra in Electrical Engineering]]. (confidence: high)

**4. Physics 1: Mechanics — the template.** Mass-spring-damper and RLC obey the same second-order ODE; force↔voltage, velocity↔current, mass↔inductance. Learning oscillation, damping, and resonance on blocks and springs is learning circuit transients in disguise. Plus the direct applications: motors, generators, MEMS. Detail: [[Classical Mechanics in Electrical Engineering]]. (confidence: high)

**5. Physics 2: E&M — the substance.** The direct physics parent of EE. Coulomb→capacitance, Ampere/Faraday→inductance and transformers, Lorentz→motors, Maxwell→antennas and transmission lines. Every passive component is derived from E&M first principles. Detail: [[Electromagnetism Foundations for EE]]. (confidence: high)

**6. Physics 3: thermo + optics + modern — the components.** Thermodynamics → junction temperature and thermal management (Joe's WBG packaging track is applied thermo). Wave optics → fiber, photonics, and the diffraction limit that created EUV lithography. Photons + matter waves → band theory, the quantum foundation of every diode, transistor, LED, and the literal meaning of "wide bandgap" (Source: [[Quantum Mechanics in Semiconductor Devices (overview)]]). Detail: [[University Physics 3 in Electrical Engineering]]. (confidence: high)

## The Two-Sentence Answer

> **Math track:** calculus gives the vocabulary (rates, accumulations, fields), differential equations give the grammar of change (every L/C circuit is an ODE), and linear algebra gives the scale (solving all of it simultaneously — circuits, control, DSP).
> **Physics track:** mechanics is the rehearsal (same ODEs, easier objects), E&M is the subject itself (components from first principles), and Physics 3 is the gateway below the circuit — why semiconductors, lasers, and heatsinks work.

## Key Concepts
- [[Calculus in Electrical Engineering]] — derivatives/integrals/vector calc → component laws, energy, Maxwell
- [[Differential Equations in Electrical Engineering]] — RC/RL/RLC, Laplace, control
- [[Linear Algebra in Electrical Engineering]] — Ax=b circuits, eigenvalue stability, DFT/SVD
- [[Classical Mechanics in Electrical Engineering]] — mechanical-electrical analogy, motors
- [[Electromagnetism Foundations for EE]] — fields → components → antennas
- [[University Physics 3 in Electrical Engineering]] — thermo, optics, quantum → devices

## Contradictions
- None substantive between sources. One framing tension: Spinning Numbers/Khan Academy says you can *start* EE with just algebra+trig and learn calculus concurrently, while degree prerequisite chains hard-gate courses on completed math. Both true — the resolution is that intro circuit *concepts* need little math, but credit-bearing EE coursework and anything dynamic (caps/inductors) needs the full sequence.

## Open Questions
- Probability/statistics is the seventh pillar (noise, communications, ML) — not covered in this run; candidate for a future page.
- Complex analysis (residues, contour integration) underlies Laplace/Fourier inversion — worth a page if Joe hits EEE 350 wanting deeper roots.
- Numerical methods (how SPICE actually integrates ODEs — trapezoidal rule, Newton-Raphson) would bridge the math pages to [[LTSpice Complete Skills Guide]].

## Sources
- [[Linear Algebra in Electrical Circuits (UW Math 308)]] — Taing, 2001
- [[Matrix Theory in Wireless Communications (MDPI Algorithms 2016)]] — Wang & Serpedin, 2016
- [[ASU PHY 241 Course Description]] — ASU catalog, current
- [[Quantum Mechanics in Semiconductor Devices (overview)]] — multi-source cluster, 2024
