---
type: research
title: "Research - ASU EE Major Map Semiconductor Connection"
created: 2026-05-04
updated: 2026-05-04
tags:
  - ASU
  - electrical-engineering
  - semiconductors
  - curriculum
  - WBG
  - research
status: complete
---
# Research — ASU EE Major Map Semiconductor Connection

How all 120 credits of the ASU EE BSE (ESEEEBSE, 2025–2026 catalog) connect to semiconductor theory and application.

Source map: [[ASU EE BSE 2025-2026 Major Map]]
Concept page: [[ASU EE Major Map Semiconductor Connection]]

---

## 8 Key Findings

**1. EEE 352 is the entire first half's destination — Terms 1–4 are coordinated runway.**
Every math and physics course in Terms 1–4 is building toward EEE 352 "Properties of Electronic Materials." CHM 114 teaches crystal structure and covalent bonding. PHY 241 (Modern Physics) teaches Fermi-Dirac statistics and band theory. EEE 241 teaches the electric fields that drive carrier drift. MAT 267 and MAT 275 provide the vector calculus and differential equations needed to solve carrier continuity equations. Terms 1–4 are not disconnected prerequisites — they are a coordinated 60-credit runway to the moment you understand why silicon conducts differently from copper or glass.

**2. PHY 241 (Modern Physics) is the most underestimated course in the EE curriculum.**
This is the course that answers the fundamental question: "Why is silicon a semiconductor rather than a conductor or insulator?" The answer requires quantum mechanics — energy bands arise from quantum-mechanical interference of electron wavefunctions in a periodic crystal lattice. The Fermi-Dirac distribution, which PHY 241 introduces, predicts exactly how many electrons can thermally jump the 1.1 eV silicon bandgap at 300K (~1.5 × 10¹⁰ cm⁻³ intrinsic carriers). Without PHY 241, EEE 352 is a collection of empirical rules with mysterious equations. With it, EEE 352 is derived from first principles that a student already understands.

**3. EEE 334 creates a deliberate pedagogical inversion — use the device before understanding the physics.**
EEE 334 (Circuits II) appears in Term 5, typically before a student takes EEE 352 (Term 5–6 pathway) or EEE 436 (elective). Students learn to USE diodes and transistors as ideal circuit models before they understand the semiconductor physics. This "top-down then bottom-up" strategy is intentional: circuit intuition developed in EEE 334 (rectifiers, amplifiers, current mirrors) makes the device physics in EEE 352/436 immediately applicable rather than abstract. Students know WHY they care about p-n junctions because they've already used diode rectifiers and MOSFET amplifiers.

**4. The 7 Area Pathways are 7 distinct application domains of semiconductor physics.**
EEE 304 (Signals) = semiconductor amplifiers and DSPs processing information; EEE 335 (Analog Circuits) = transistor-level analog IC design; EEE 341 (EM Waves) = semiconductors at RF and microwave frequencies; EEE 352 (Physical Electronics) = semiconductor physics from first principles; EEE 360 (Power) = power semiconductors (SiC, GaN) switching kilowatts; EEE 333 (Computer Engineering) = MOSFETs as digital switches in programmable logic; EEE 394 (Quantum Engineering) = semiconductor quantum devices (quantum dots, qubits). Choosing your 4 pathways is equivalent to choosing which domain of semiconductor application you specialize in. The combination EEE 352 + EEE 360 + EEE 304 + EEE 333 gives the strongest WBG power electronics foundation.

**5. EEE 350 (Random Signal Analysis) is the noise physics course in disguise.**
EEE 350 is often perceived as abstract probability theory, but every major noise source in electronics has a semiconductor quantum-mechanical origin: thermal noise (Johnson-Nyquist) traces to Fermi-Dirac carrier statistics → kT/q; shot noise traces to charge quantization → Q = ne, with individual electron crossings across a p-n junction being Poisson-distributed; 1/f (flicker) noise comes from carrier trapping and release at the SiO₂/Si interface in MOSFETs, dominating at low frequency in all CMOS circuits. EEE 350 is a prerequisite for EEE 488 because every senior design project must specify a noise floor, and that floor is set by the semiconductor devices in the signal chain.

**6. The Power track (EEE 360 → EEE 470 → EEE 472) shows semiconductors at their physical extremes.**
Power electronics uses semiconductor devices at the limits of safe operation: blocking voltages of 650–10,000V, peak currents of 100–3,000A, switching frequencies of 10 kHz–10 MHz. Silicon MOSFETs hit fundamental limits imposed by their 1.1 eV bandgap — higher voltage requires longer drift regions, which increase conduction resistance. Wide bandgap materials (SiC at 3.2 eV, GaN at 3.4 eV) dramatically shrink the required drift region, enabling 10× lower on-resistance for the same blocking voltage. EEE 352 explains WHY a larger bandgap enables higher breakdown voltage (Ec ∝ E_g^2.5 approximately). EEE 436 explains how the device is structured. EEE 472 teaches converter design using these properties.

**7. EEE 120 → EEE 333 → EEE 425 traces how a single transistor becomes a modern processor.**
This chain is the most tangible manifestation of semiconductor physics at civilizational scale. EEE 120 shows how Boolean logic gates are realized using CMOS transistor pairs. EEE 333 teaches Verilog/HDL to describe digital systems abstractly and synthesize them to standard ASIC cells (which are ultimately CMOS transistor arrangements). EEE 425 returns to transistor-level VLSI to show how 3-nm CMOS processes achieve >10 billion switches on a chip the size of a thumbnail, with timing closure at GHz frequencies. One MOSFET (EEE 352 explains it), tiled 10 billion times (EEE 425 shows how), programmed in Verilog (EEE 333 teaches it), implementing Boolean functions (EEE 120 defines them) — this is the full chain from semiconductor physics to modern computation.

**8. EEE 488/489 (Senior Design) is the forced integration — all semiconductor knowledge converges into a physical system.**
The prerequisites for EEE 488 are carefully chosen: EEE 241 (electromagnetic constraints on the physical design), EEE 334 (semiconductor circuit models for design), EEE 350 (noise limits on system specifications), and 3 Area Pathways (domain expertise in at least 3 semiconductor application areas). No single course teaches system-level integration — the senior project does. Every EE senior project is ultimately a system built on semiconductor devices: a PCB with CMOS ICs processing signals, a power supply switching with SiC MOSFETs, an FPGA implementing a control algorithm, or a transceiver using GaN RF amplifiers. EEE 488/489 is where semiconductor physics becomes a physical object you can hold.

---

## Course-by-Course Semiconductor Role Map

### Mathematics (Terms 1–4)
| Course | Key Semiconductor Tool It Provides |
|--------|-------------------------------------|
| MAT 265 Calculus I | I-V derivatives; energy and charge integrals |
| MAT 266 Calculus II | Carrier density integrals; device model approximations |
| MAT 267 Calculus III | Vector calculus for Maxwell's equations and 3D carrier transport |
| MAT 275 Diff. Equations | RC/RL/RLC transients; carrier continuity equations (same PDE structure) |
| MAT 342/343 Linear Algebra | SPICE circuit matrix solvers; quantum mechanical operators; state-space control |

### Physics (Terms 1–4)
| Course | Semiconductor Physics Provided |
|--------|-------------------------------|
| CHM 114 | Crystal structure, covalent bonds, atomic orbitals — origin of doping concept |
| PHY 121/122 | Energy conservation, forces — conceptual bridge to quantum mechanics |
| PHY 131/132 | Electric/magnetic fields (macroscopic Maxwell) — carrier drift and device physics |
| PHY 241 | Band theory, Fermi-Dirac statistics, quantum tunneling — WHY semiconductors work |

### EE Core (Terms 2–5)
| Course | Semiconductor Role |
|--------|-------------------|
| EEE 120 | MOSFET as Boolean switch; CMOS logic families |
| EEE 202 | Ideal device models; AC circuit analysis framework |
| EEE 203 | Transfer functions model semiconductor amplifier frequency response |
| EEE 241 | Maxwell's equations — carrier transport, transformer physics, antenna connection |
| EEE 334 | Use diodes, BJTs, MOSFETs in circuits before knowing why they work |
| EEE 350 | Noise physics: thermal, shot, 1/f — all semiconductor-origin |

### Area Pathways (Terms 5–6)
| Pathway | Semiconductor Domain |
|---------|---------------------|
| EEE 304 | DSP — implemented on semiconductor chips |
| EEE 333 | FPGA/ASIC — MOSFET lookup tables and standard cells |
| EEE 335 | Analog IC — transistor-level CMOS design |
| EEE 341 | RF/microwave — GaN HEMT amplifiers |
| EEE 352 | Semiconductor physics core — the gateway course |
| EEE 360 | Power semiconductors — SiC/GaN switching applications |
| EEE 394 | Quantum devices — semiconductor heterostructures as qubits |

### Technical Electives
| Course | Semiconductor Content |
|--------|----------------------|
| EEE 425 | VLSI CMOS at transistor level |
| EEE 433 | Analog IC design — multi-transistor circuits |
| EEE 434 | Solar cell device physics |
| EEE 435 | CMOS fabrication process |
| EEE 436 | Full semiconductor device physics (MOSFET, BJT, power devices) |
| EEE 437 | Optoelectronics (LED, laser, photodetector) |
| EEE 439 | III-V and WBG compound semiconductors |
| EEE 460 | Power distribution — semiconductor protection devices |
| EEE 463 | Power system protection |
| EEE 465 | WBG device-level loss analysis |
| EEE 470 | Power device comparison: IGBT vs. SiC vs. GaN |
| EEE 472 | Converter design using power semiconductor switches |
| EEE 473 | Advanced soft-switching converters |
| EEE 480 | Feedback control for semiconductor-based power converters |
| EEE 481 | Digital control on semiconductor DSPs |
| EEE 404 | Real-time DSP on semiconductor silicon |
| EEE 405 | ML inference on FPGA fabric |
| EEE 407 | Advanced digital filter design |
| EEE 443 | Antenna design for semiconductor RF front-ends |
| EEE 445 | Microwave transistor amplifiers (GaN HEMT) |
| EEE 455 | Communications systems on semiconductor transceivers |
| EEE 459 | Digital communications channel coding |

---

## 5 Open Questions

1. Does ASU offer EEE 439 (Compound Semiconductor Devices — GaAs, GaN, InP) regularly, or is it irregular like EEE 472 and EEE 473 (listed as "N = Not regularly")? This matters for WBG specialization planning.
2. What is the recommended 4-pathway combination for a student specifically targeting Ranjram's MAPEL Lab — is EEE 352 + EEE 360 + EEE 304 + EEE 333 the dominant choice, or is EEE 341 (for EMI/magnetics expertise) more valuable?
3. Can EEE 352 and EEE 394 (Quantum Engineering) be taken in the same semester to directly compare classical semiconductor physics to quantum device engineering — and is this synergy utilized in ASU's course planning?
4. How does EEE 465 (Solid-State Power Conversion) relate to EEE 472 (Power Electronics) — are they complementary (take both) or overlapping (take one)? The course numbers suggest EEE 465 is device-level and EEE 472 is system-level.
5. What is the minimum EEE coursework background needed to contribute meaningfully to Ranjram's MAPEL Lab research in MHz magnetics and converter architecture — can a student with only EEE 202 + EEE 334 contribute as a first-year FURI participant?
