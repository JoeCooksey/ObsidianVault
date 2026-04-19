---
type: research
title: "EE Physical Side Skills — Semiconductors and Power Electronics"
created: 2026-04-19
updated: 2026-04-19
tags:
  - research
  - domain/engineering
  - semiconductors
  - power-electronics
  - career
  - actionable-plan
status: developing
---
# EE Physical Side Skills — Semiconductors and Power Electronics

**Research question:** As an electrical engineer hiring for the physical side (semiconductors and power), what skills would you look for — and what's the actionable improvement plan?

## Key Findings

1. **Device physics fluency is the non-negotiable baseline.** Employers screen for understanding of P-N junctions, MOSFET/IGBT operation, and WBG material properties (SiC, GaN) before anything else. You must know *why* SiC has lower switching losses, not just *that* it does.

2. **Power topology breadth + one specialty.** Hiring managers want broad familiarity with converter families (buck, boost, flyback, LLC, CLLC, DAB, totem-pole PFC) but deep expertise in one area — typically either DC-DC or inverter-side. For EV/automotive, inverter + fast charger topologies are the highest-demand specialty.

3. **Double pulse test (DPT) is the "can you bench?" litmus test.** If you've never set up or interpreted a DPT — measuring Eon, Eoff, reverse recovery — you will not pass a power lab interview. This is the industry-standard switching characterization method for all WBG devices.

4. **PCB layout for high-frequency power is a force multiplier.** A brilliant circuit design fails in silicon if the power loop has 50 nH of stray inductance. Kelvin source connections, minimizing commutation loop area, and gate loop control separate juniors from seniors.

5. **WBG-specific tools and application notes matter.** Wolfspeed, Infineon, STMicro, Onsemi, and GaN Systems all publish detailed app notes for their devices. Engineers who have read and applied these are immediately more productive than those who haven't.

6. **Thermal design is under-valued but critical.** Junction temperature directly determines reliability and derating. Engineers who can calculate Rth(j-c) from a datasheet, size a heatsink, and specify TIM correctly are significantly more hireable in the 2025–2026 market.

7. **Digital control on a DSP is increasingly required.** TI C2000 series (F28379D) is the dominant automotive-grade power control DSP. STM32 G4/H7 for industrial. Knowing how to implement PI/PID in a fixed-point DSP, tune deadband, and handle ADC sampling synchronization is a hard differentiator.

8. **Reliability and qualification standards signal production-readiness.** AEC-Q101 (automotive semiconductors), JEDEC JESD47 (qualification), and IEC 62477 (power electronics systems safety) separate candidates who have touched real product from those who have only done academic projects.

## What Separates Good From Great Candidates

| Junior Signal | Senior Signal |
|---|---|
| Knows MOSFET I-V curves | Can derive switching loss from gate charge + dv/dt |
| Simulates in LTspice | Validates simulation vs. DPT bench measurement |
| Uses a development board | Designs and spins a 4-layer power PCB |
| Reads Wolfspeed datasheet | Has applied Wolfspeed/Infineon app note to real circuit |
| Knows thermal resistance exists | Designs for Tjmax with 20°C derating margin |
| Wrote code for Arduino | Implemented PI current control on TI C2000 |

## Industry Context (2025–2026)

- **70,000 new direct semiconductor jobs** projected by 2026 in the US alone
- **SiC traction inverter engineers** are the single highest-demand specialty in automotive (Wolfspeed, Onsemi, STMicro, BorgWarner, Aptiv)
- **GaN OBC engineers** are the second hottest specialty (Navitas, GaN Systems, EPC, Texas Instruments GaN)
- Employers increasingly value **demonstrated skill over credentials** due to talent shortage
- Salary range for power electronics engineers (US, 2025): $112k–$230k depending on seniority and domain

## Actionable Improvement Plan

See [[EE Physical Side — Actionable Skill Plan]] for the complete 18-month roadmap.

### Phase 1: Foundations (Months 0–3)
- **Device physics**: Neamen *Semiconductor Physics and Devices* (Chs. 1–9) or Streetman & Banerjee
  - Focus: P-N junction, MOSFET structure and I-V, IGBT operation, bandgap theory
- **Power electronics fundamentals**: Erickson & Maksimovic *Fundamentals of Power Electronics* (Chs. 1–6)
  - Focus: buck, boost, flyback — steady-state and small-signal analysis
- **Simulation**: LTspice (free from Analog Devices) — simulate every converter topology you read about
- **Target milestone**: Build and test a 12V→5V, 10W synchronous buck converter on a PCB

### Phase 2: Core Power Design (Months 3–6)
- **Magnetics**: Erickson Ch. 13–14; Wurth Electronics Core Selector Tool; practice winding a transformer
- **Gate driver design**: read TI *Gate Driver Fundamentals* (SLUA618); pick a WBG-compatible gate driver IC (e.g., TI UCC21710 for SiC)
- **Coursera Power Electronics Specialization** — Dr. Robert Erickson, CU Boulder (free audit available)
- **Double pulse test**: read Wolfspeed DPT app note (AN-1175 or equivalent); understand Eon, Eoff, Qrr methodology
- **Target milestone**: Set up a basic DPT bench (or simulate it in LTspice with SiC MOSFET model) and extract switching energies

### Phase 3: WBG Specialization (Months 6–12)
- **SiC app notes**: Wolfspeed AN-011 (SiC MOSFET primer), STMicro SiC application note series, Infineon SiC MOSFET application note AN2015-04
- **GaN app notes**: EPC eGaN FETs application notes; GaN Systems GS-DS-038; Navitas NVS4020 app note
- **IEEE TPEL papers**: scan 2023–2025 papers on SiC traction inverters and GaN OBC topologies
- **800V fast charger topology**: study totem-pole PFC + CLLC resonant converter design (two-stage approach)
- **PCB layout practice**: design a 4-layer power board in Altium or KiCad; review with power loop inductance mindset
- **Target milestone**: Complete a full SiC-based converter design (schematic → BOM → PCB → test) at >1 kW

### Phase 4: Advanced (Months 12–18)
- **Digital control**: TI C2000 F28379D + MotorControl SDK; implement PI current control loop; understand ADC synchronization
- **EMC/EMI**: study IEC 61000-4 series; read "EMC for Power Electronics" by Henry Ott
- **Thermal simulation**: ANSYS Icepak (university license) or SolidWorks Flow Simulation; validate vs. IR camera measurement
- **Reliability**: read AEC-Q101 standard; understand HTGB, HTRB, THB qualification tests
- **Target milestone**: Pass a behavioral interview with specific project stories covering all four Phase 1–4 areas

## Key Resources

### Textbooks
- Erickson & Maksimovic — *Fundamentals of Power Electronics* (3rd ed.) — THE reference
- Neamen — *Semiconductor Physics and Devices* — best device physics intro
- Sze & Ng — *Physics of Semiconductor Devices* — graduate level; use as reference

### Courses
- Coursera Power Electronics Specialization (CU Boulder, Erickson)
- nanoHUB Semiconductor Fundamentals (free, Purdue)
- Coursera *Introduction to Power Semiconductor Switches* (covers SiC/GaN)

### App Notes (Free, High Value)
- Wolfspeed: AN-1175 (DPT), SiC MOSFET application guide
- Infineon: AN2015-04 (SiC MOSFET), AN2017-04 (GaN HEMT)
- Texas Instruments: SLUA618 (gate driver fundamentals), C2000 MotorControl SDK docs
- GaN Systems: GS-DS-038 design guide

### Simulation Tools
- LTspice (free) — workhorse for power circuit simulation
- MATLAB/Simulink (student/university license) — system-level modeling
- Altium Designer or KiCad — PCB design

## Open Questions
1. Will 1200V GaN eclipse SiC in traction inverter applications before 2030?
2. How will Ga₂O₃ device maturity affect the SiC/GaN duopoly timeline?
3. What does the shortage of SiC wafer supply mean for system designers hedging between devices?
4. Is TI C2000 being displaced by RISC-V-based industrial MCUs at the control layer?
5. How does ISO 26262 ASIL-D interact with power electronics software design for automotive?

## Related Pages
- [[Wide Bandgap Semiconductors]]
- [[Silicon Carbide Power Electronics]]
- [[Gallium Nitride Power Electronics]]
- [[800V EV Architecture]]
- [[EV Fast Charging Topologies]]
- [[WBG Thermal Management]]
- [[Research - WBG Semiconductors in EV Fast Charging]]
- [[EE Physical Side — Actionable Skill Plan]]
