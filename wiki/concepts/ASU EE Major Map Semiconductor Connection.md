---
type: concept
title: "ASU EE Major Map — How Every Course Connects to Semiconductors"
created: 2026-05-04
updated: 2026-05-04
tags:
  - ASU
  - electrical-engineering
  - semiconductors
  - curriculum
  - cross-reference
  - WBG
status: complete
---
# ASU EE Major Map — How Every Course Connects to Semiconductors

Source map: [[ASU EE BSE 2025-2026 Major Map]]
Research synthesis: [[Research - ASU EE Major Map Semiconductor Connection]]
See also: [[Semiconductor Device Fundamentals]], [[Wide Bandgap Semiconductors]], [[EE Topic Depth Priority Map]]

---

## The Core Insight

Every course in the EE BSE is doing one of four things:

1. **Building the mathematical language** needed to describe semiconductor physics (Calculus, DiffEQ, Linear Algebra)
2. **Describing the physics** that makes semiconductors work (PHY series, CHM 114)
3. **Teaching you to USE** semiconductor devices in circuits before knowing why they work (EEE 202, EEE 334)
4. **Applying** semiconductor devices to a specific domain — power, digital, RF, optical, control

**EEE 352 (Properties of Electronic Materials)** is the central gateway. It is the course where chemistry (crystal structure, bonding), quantum mechanics (energy bands, Fermi levels), and electromagnetics (drift/diffusion in fields) converge to explain *why* silicon conducts differently than copper or glass.

Everything in Terms 1–4 is building toward EEE 352. Everything after is an application of what EEE 352 reveals.

---

## Layer 1 — The Mathematical Language (Terms 1–4)

Semiconductor physics is described by differential equations, quantum wavefunctions, and statistical distributions. This layer builds the tools.

| Course | Role in Semiconductor Understanding |
|--------|--------------------------------------|
| MAT 265 Calculus I | Derivatives for V-I relations (I = C·dV/dt); integrals for charge, energy, magnetic flux |
| MAT 266 Calculus II | Integration techniques for carrier density integrals; Taylor/power series for device model approximations |
| MAT 267 Calculus III | Vector calculus (gradient, divergence, curl) — prerequisite for Maxwell's equations and 3D carrier transport |
| MAT 275 Differential Equations | Solves RC/RL/RLC transients; semiconductor carrier continuity equations are PDEs of the same form |
| MAT 342/343 Linear Algebra | Matrix methods (SPICE circuit solvers); quantum mechanical operators; state-space models for power converter control |
| CSE 100/110 Programming | SPICE scripting; Python for device characterization data; MATLAB for control and signal analysis |

---

## Layer 2 — The Physics Foundation (Terms 1–4)

Semiconductors are physics before they are engineering. These courses answer "why does silicon conduct under some conditions and not others?"

| Course | Role in Semiconductor Understanding |
|--------|--------------------------------------|
| CHM 114 Chemistry I | Atomic structure; covalent bonding; crystal lattice of silicon; the concept of **doping** (adding trace impurity atoms to control conductivity) originates in atomic electron orbital theory covered here |
| PHY 121/122 Physics I (Mechanics) | Energy conservation, momentum, forces — sets up the concept of particle motion in a potential well; conceptual prerequisite before quantum mechanics |
| PHY 131/132 Physics II (E&M) | Electric fields, Coulomb's law, Gauss's law, magnetic forces, Faraday's law — the macroscopic field equations that describe carrier transport and device operation |
| **PHY 241 Modern Physics** | **THE quantum foundation of semiconductors**: wave-particle duality; energy quantization; Bohr model; Fermi-Dirac statistics; energy band theory; the photoelectric effect; quantum tunneling; explains *why* Si has a 1.1 eV bandgap and what a bandgap physically means |

**PHY 241 → EEE 352 direct connection**: PHY 241 introduces Fermi-Dirac statistics and band theory conceptually. EEE 352 applies them quantitatively to calculate intrinsic carrier concentrations, predict doping effects, and derive the p-n junction I-V equation from first principles.

---

## Layer 3 — The Semiconductor Core (EEE 352 + Electives)

### EEE 352: Properties of Electronic Materials (Area Pathway)
*Prerequisites: CHM 114, EEE 241, PHY 241*

This is the central semiconductor course. It covers:
- Silicon crystal structure and covalent bonding lattice
- Intrinsic carrier concentration (n_i at room temperature)
- Fermi level and Fermi-Dirac distribution applied to solids
- N-type (donor, e.g. phosphorus) and P-type (acceptor, e.g. boron) doping
- Carrier transport: **drift** (electric field) and **diffusion** (concentration gradient)
- The p-n junction: built-in potential, depletion region, diode I-V equation (Shockley equation)
- Minority carrier recombination and generation
- Introduction to BJT and MOSFET operation at the physics level

### Deep-Dive Semiconductor Electives
| Course | What It Adds |
|--------|-------------|
| EEE 436 Solid-State Devices | Full device physics: Ebers-Moll BJT from carrier physics; MOSFET threshold voltage derivation; short-channel effects; power MOSFET body diode; JFET; goes beyond EEE 334's circuit models to the quantum mechanical reality |
| EEE 435 CMOS and MEMS | How semiconductors are *fabricated*: photolithography, oxide growth (SiO₂), ion implantation, dry/wet etching, metallization, CMOS process flow; MEMS devices |
| EEE 437 Optoelectronics | Semiconductor-light interactions: LED (radiative recombination), laser diode (stimulated emission, optical gain), photodetector, solar cell (photovoltaic effect) |
| EEE 439 Compound Semiconductors | GaN, GaAs, InP, SiC device physics — the wide bandgap and III-V pathways for RF and power applications |
| EEE 465 Solid-State Power Conversion | Bridge between device physics and power converter design — conduction loss and switching loss at the device level in power MOSFETs, IGBTs, SiC MOSFETs, GaN HEMTs |
| EEE 394 Quantum Engineering | Next-generation: quantum dots, qubits implemented as semiconductor heterostructures, quantum key distribution, quantum information on semiconductor platforms |

---

## Layer 4 — Using Semiconductor Devices in Circuits (Terms 3–6)

Before studying the physics (EEE 352 is a Term 5–6 pathway), students learn to *use* semiconductor devices as ideal models. This is deliberate.

| Course | How It Uses Semiconductor Devices |
|--------|-----------------------------------|
| EEE 202 Circuits I | Treats diodes and transistors as ideal elements; Thevenin models of real sources; AC analysis and phasors set up amplifier frequency response analysis |
| EEE 334 Circuits II | Diode circuit analysis (rectifiers, clamps, clippers); BJT and MOSFET DC biasing (Q-point); small-signal amplifier analysis; op-amp circuits; active filters — the "user manual" for semiconductor devices |
| EEE 335 Analog and Digital Circuits (Pathway) | CMOS logic gate transistor implementation; differential amplifier; current mirror; op-amp frequency response and stability; transistor-level analog IC design |
| EEE 433 Analog Integrated Circuits (Tech Elect) | Full IC design: multistage amplifiers, folded cascode, bandgap voltage reference, transimpedance amplifier — all built from bipolar and MOSFET semiconductor transistors |
| EEE 425 Digital Systems and Circuits (Tech Elect) | VLSI: how CMOS gates are physically timed and optimized at transistor level; static vs. dynamic logic; SRAM bit cell design; memory arrays |

---

## Layer 5 — Semiconductor Applications by Domain

### Power Electronics Track (WBG Focus — Joe's Priority)

Power electronics uses semiconductors at their physical extremes — high voltage, high current, high frequency. **Wide bandgap devices (SiC, GaN) are the frontier here.**

| Course | Power Semiconductor Content |
|--------|---------------------------|
| EEE 360 Energy Systems and Power Electronics (Pathway) | Three-phase circuits; transformers; AC/DC machines; introduces power semiconductor switches (diodes, SCRs, power MOSFETs, IGBTs); switching basics |
| EEE 470 Electric Power Devices (Tech Elect) | Power device comparison in depth: Si MOSFET vs. IGBT vs. SiC MOSFET vs. GaN HEMT; thyristors; packaging and thermal management; gate drive design |
| EEE 472 Power Electronics and Power Management (Tech Elect) | DC-DC converters (buck, boost, buck-boost, SEPIC); AC-DC rectifiers; single-phase and three-phase inverters; duty cycle, switching frequency, efficiency — all implemented with power semiconductor switches |
| EEE 473 Advanced Power Electronics (Tech Elect) | Soft-switching; resonant converters; multilevel inverters; digital control of switching converters; advanced WBG device applications |
| EEE 465 Solid-State Power Conversion (Tech Elect) | Device-level view of power converter losses: conduction loss, switching loss, body diode reverse recovery; how SiC and GaN reduce all three |
| EEE 463 Power System Protection (Tech Elect) | Semiconductor-based protection devices; fault current limiters; grid-connected inverter protection |

**WBG Connection Chain:**
```
PHY 241 (band theory + energy gap) 
  → EEE 352 (semiconductor physics + p-n junction) 
  → EEE 436 (device physics: MOSFET, power MOSFET structure) 
  → EEE 439/465 (SiC and GaN device characteristics) 
  → EEE 470 (power device circuit behavior) 
  → EEE 472 (converter design using WBG devices)
  → EEE 473 (advanced WBG system-level design)
```

### Digital / Computer Engineering Track

| Course | Semiconductor Logic Connection |
|--------|-------------------------------|
| EEE 120 Digital Design Fundamentals | Boolean algebra realized in CMOS gates (each gate IS semiconductor transistors); K-maps; combinational and sequential logic; flip-flops; intro to Verilog |
| EEE 333 Hardware Design Languages (Pathway) | Verilog/SystemVerilog to program FPGAs (semiconductor lookup tables); RTL synthesis to ASIC standard cells |
| EEE 425 Digital Systems and Circuits (Tech Elect) | VLSI: CMOS transistor-level implementation of logic; layout; timing analysis; memory bit cells |
| EEE 405 ML with FPGAs (Tech Elect) | Neural network inference implemented in semiconductor FPGA fabric |
| EEE 404 Real-Time DSP Systems (Tech Elect) | Real-time DSP algorithms running on semiconductor DSP chips and FPGAs |

**The transistor→computer chain:** EEE 120 shows how Boolean logic gates are built from MOSFETs. EEE 333 abstracts to HDL (one step up). EEE 425 goes back down to transistor-level to show how modern VLSI achieves billions of switches on a die. This chain is how Moore's Law built civilization.

### Signals and Communications Track

| Course | Semiconductor Role |
|--------|-------------------|
| EEE 203 Signals and Systems I | Transfer functions model how semiconductor amplifiers and filters shape signal spectra |
| EEE 304 Signals and Systems II (Pathway) | Discrete-time DSP — implemented in semiconductor DSP/FPGA; Z-transform, DFT, digital filter design |
| EEE 350 Random Signal Analysis | **Noise in semiconductor devices**: thermal noise (kT/q from Fermi-Dirac statistics), shot noise (charge quantization Q=ne), flicker/1/f noise (MOSFET oxide-semiconductor interface carrier trapping) |
| EEE 407 Digital Signal Processing (Tech Elect) | Advanced filter design for semiconductor DSP implementation |
| EEE 455 Communication Systems (Tech Elect) | Analog/digital modulation; noise analysis; channel capacity — implemented in semiconductor RF transceivers |
| EEE 459 Digital Communications (Tech Elect) | Channel coding, equalization — all running on semiconductor silicon |
| EEE 480 Feedback Systems (Tech Elect) | Classical control theory (PID, root locus, Bode, stability) — used to control power converters and motor drives built on semiconductor switches |
| EEE 481 Computer-Controlled Systems (Tech Elect) | Digital control; Z-domain design; state-space; real-time implementation on semiconductor DSPs |

### Electromagnetics Track

| Course | EM Connection to Semiconductors |
|--------|--------------------------------|
| EEE 241 Fundamentals of Electromagnetics | Maxwell's equations applied to EE: Gauss's law relates charge density to electric fields (directly relevant to p-n junction depletion region); Faraday's law describes transformer and inductor action |
| EEE 341 Electromagnetic Fields and Waves (Pathway) | Wave propagation; transmission line theory (critical for high-speed PCB traces carrying semiconductor signals); prerequisite for microwave transistor amplifier design |
| EEE 443 Antennas (Tech Elect) | Antenna feed networks driven by semiconductor RF amplifiers; antenna impedance matching to transistor output |
| EEE 445 Microwaves (Tech Elect) | Microwave transistor amplifiers; S-parameters; matching networks; GaN HEMT is the dominant microwave power semiconductor |

### Optoelectronics and Photonics Track

| Course | Semiconductor–Photonics Content |
|--------|--------------------------------|
| PHY 241 Modern Physics | Photoelectric effect; photon-electron interaction; the quantized nature of light |
| EEE 352 (Pathway) | Semiconductor optical absorption coefficient; radiative recombination rate; direct vs. indirect bandgap (Si is indirect → bad LED; GaAs is direct → good LED) |
| EEE 437 Optoelectronics (Tech Elect) | LEDs (injection electroluminescence); laser diodes (population inversion, optical gain, Fabry-Perot cavity); photodetectors (PIN, avalanche photodiode); solar cells (photovoltaic effect, fill factor, efficiency limits) |
| EEE 434 Photovoltaic Systems (Tech Elect) | Solar cell device physics (EEE 352 extended) plus system integration — inverters, MPPT, grid tie |
| EEE 439 Compound Semiconductors (Tech Elect) | GaAs, InP for fiber optic communications; GaN for high-brightness LEDs and blue lasers |

---

## The Prerequisite Graph — Path to Semiconductor Mastery

```
Term 1:  CHM 114 ───────────────────────────────────────────────────────────┐
Term 1:  MAT 265 ─→ Term 2: MAT 266 ─→ Term 3: MAT 267, MAT 275           │
Term 2:  PHY 121/122 ─→ Term 3: PHY 131/132 ─→ Term 4: PHY 241 ───────────┤
Term 3:  EEE 202 ─→ (needed for EEE 360, EEE 333 pathways)                │
Term 4:  EEE 241 ──────────────────────────────────────────────────────────┤
                                                                            ↓
                                              EEE 352 (Properties of Electronic Materials)
                                                   ↓              ↓              ↓             ↓
                                             EEE 436          EEE 435        EEE 437        EEE 465
                                          (Device Physics)  (Fabrication)  (Optoelectronics) (Power Conv.)
                                                   ↓
                                             EEE 439 (Compound Semicond.)
                                                   ↓
                                          EEE 470 / EEE 472 / EEE 473 (WBG Power)
```

Terms 1–4 are entirely prerequisite runway. The entire first half of the EE degree is building toward the moment EEE 352 reveals WHY semiconductors work.

---

## EEE 334 — The Deliberate Pedagogical Inversion

EEE 334 (Circuits II) appears in Term 5, typically *before* a student takes EEE 352 (semiconductor physics). This creates a deliberate "top-down then bottom-up" learning strategy:

1. **Use devices first** (EEE 334): diodes as ideal rectifiers, transistors as current-controlled amplifiers, MOSFET as voltage-controlled switch — circuit models only
2. **Learn why they work** (EEE 352 / EEE 436): p-n junction physics, threshold voltage derivation, channel charge, breakdown mechanisms
3. **Design with them** (EEE 335, EEE 433, EEE 470, EEE 472): now the physics directly informs design choices

Students know *why they care* about EEE 352 because they've already built rectifiers, amplifiers, and switches in EEE 334.

---

## EEE 350 — Why Noise Is a Semiconductor Physics Problem

EEE 350 (Random Signal Analysis) is often seen as abstract probability theory. In practice, it is the mathematical foundation for understanding every noise source in an EE system — and every major noise source has a semiconductor quantum-mechanical origin:

| Noise Type | Physical Origin | Semiconductor Connection |
|-----------|-----------------|--------------------------|
| Thermal noise (Johnson-Nyquist) | Thermal agitation of charge carriers | kT/q — traces to Fermi-Dirac statistics in a resistor material |
| Shot noise | Discreteness of electric charge | Q = ne — individual electron crossings across a p-n junction barrier are Poisson-distributed |
| 1/f (flicker) noise | Carrier trapping and release | Defects at the SiO₂/Si interface in MOSFETs trap and release carriers randomly — dominates at low frequency in all CMOS circuits |
| Generation-recombination noise | Carrier recombination events | Minority carriers randomly recombine in the p-n junction depletion region |

EEE 350's stochastic process tools (PSD, autocorrelation, noise figure) are the required language for designing low-noise RF amplifiers, ADCs, and sensor interfaces — all built from semiconductor transistors.

---

## EEE 488/489 — The Integration Synthesis

The prerequisites for EEE 488 are deliberately chosen:
- **ENG 102** — can write a technical spec and communicate with a team
- **EEE 241** — can model electromagnetic constraints (EMI, transmission lines, magnetics)
- **EEE 334** — can design circuits using semiconductor device models
- **EEE 350** — can account for noise in the signal chain and specify SNR
- **3 Area Pathways** — has domain expertise in at least 3 semiconductor application areas

No single course teaches system integration. EEE 488/489 forces it: a real PCB, a programmed FPGA, a motor controller, a power supply, a software-defined radio — all ultimately built on semiconductor devices and constrained by semiconductor physics.

---

## Joe's Optimal WBG-Focused Pathway Selection

Given Joe's FURI target (Ranjram MAPEL Lab — MHz magnetics + WBG converter architecture):

### Area Pathways (4 required):
1. **EEE 352** — Physical Electronics (mandatory — this IS the semiconductor foundation for WBG work)
2. **EEE 360** — Power Systems (EV/grid application context; introduces switching devices)
3. **EEE 304** — Signals and Systems II (control theory mathematics for digital converter control)
4. **EEE 333** — Computer Engineering (Verilog for FPGA-based digital controller, OR **EEE 341** Electromagnetics for EMI/magnetics analysis)

### Technical Electives (15 credits — 5 courses):
1. **EEE 436** — Solid-State Devices (SiC/GaN device physics from first principles)
2. **EEE 472** — Power Electronics and Power Management (converter topology design)
3. **EEE 470** — Electric Power Devices (power semiconductor comparison: IGBT vs. SiC vs. GaN)
4. **EEE 480** — Feedback Systems (control theory for switching converters)
5. **EEE 465** — Solid-State Power Conversion (device-level loss analysis) OR **EEE 473** — Advanced Power Electronics (soft-switching, resonant converters)

This stack = direct path to contributing to Ranjram's MHz magnetics / WBG converter research.
