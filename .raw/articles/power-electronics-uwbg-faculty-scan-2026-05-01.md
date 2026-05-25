---
source_type: research_report
author: ChatGPT research
fetched: 2026-05-01
subject: ASU/Rice Power Electronics and UWBG Faculty Research Scan
faculty_covered:
  - Mike Ranjram (ASU MAPEL)
  - Raja Ayyanar (ASU EVSTS)
  - Yuji Zhao (Rice WIDE Lab — formerly ASU)
context: Joe evaluating FURI mentors and grad school faculty
---

# Research Scan: Three Power Electronics and UWBG Faculty

## Executive Summary

Three faculty represent three distinct layers of the power electronics stack:
- **Mike Ranjram** (ASU MAPEL): converter architecture + MHz magnetics + miniaturization → strongest FURI fit
- **Raja Ayyanar** (ASU EVSTS): EV/PV system-level controls + grid integration → senior, industry-tied
- **Yuji Zhao** (Rice WIDE Lab, formerly ASU): GaN/β-Ga₂O₃ device physics + interface engineering → UWBG frontier

**Critical correction**: Yuji Zhao is currently at Rice University, not ASU.

---

## Mike Ranjram — ASU MAPEL

**Official role**: Assistant professor, ASU ECEE; research focus = making converters "smaller, more efficient, more capable."

### Recent Papers

**Paper 1: Harmonically Partitioned Power Converter (HPPC) Architecture (2025)**
- Single-stage ac/dc using bidirectional switches
- Combines unity PF, power-pulsation decoupling, continuous gain variation, galvanic isolation — all in one stage
- Prototype: 120 Vrms in, 250 Vdc out, 250 W, 210 kHz; 46 µF film buffer cap
- Key advance: eliminates cascaded PFC + isolated dc/dc penalty

**Paper 2: Multi-Level Coupled Electronic and Magnetic System (ML-CEMS) for Wide-Gain LLC (2024 ECCE)**
- Injects multi-level transformer voltages via coupled electronic-and-magnetic system
- Gain variation at FIXED frequency; transformer flux density stays nearly constant
- δML control comparison: frequency-modulated = 231 mT peak flux; ML-CEMS = 66 mT peak flux
- Key insight: attacks "wide gain range = oversized magnetics" tradeoff at the root

### Most Interesting Result
ML-CEMS peak flux reduction 231 mT → 66 mT at same operating point. Physically intuitive; enables magnetics miniaturization in variable-gain converters.

### Key Artifacts
- MAPEL lab page: official faculty hub
- GitHub: ASU MAPEL org; MHzCoreLossAggregateDataset (13 source datasets, multiple ferrites, updated 2026)
- Fulton Forge mentor page: active student pipeline (Jacob Anderson, Diego Puerta, Vibhas Novli projects)
- PI in Global Hydrogen Production Technologies Centre + ASU EV ecosystem

### Follow-up Research Directions
1. Closed-loop HPPC with variable passives (9–15 months)
2. Data-driven magnetic design using MAPEL core-loss repo (4–8 months to paper)
3. Self-resonance-aware planar magnetics for MHz converters (6–12 months)
4. High-CMTI isolated gate/comms link for compact WBG converters (6–10 months)

---

## Raja Ayyanar — ASU EVSTS

**Official role**: Senior professor, ASU ECEE; ASU site director, Center for Efficient Vehicles and Sustainable Transportation Systems (EVSTS).

### Recent Papers

**Paper 1: Improving PV Hosting Capacity via Coordinated Inverter Control (2025)**
- VQ-sensitivity-based coordinated controller; real-time voltage-reactive-power sensitivity matrix + iterative linear optimization
- 3× hosting capacity improvement on EPRI J1 feeder (8000+ node model)
- No active-power curtailment, no SVR setting changes
- Led by student Dhaval Dalal

**Paper 2: Volt-PF Control Mode for DER-Dense Feeder Voltage Management (2025 IEEE Access)**
- Solves inequitable reactive-support burden on inverters with low active-power output
- Q support tied to both voltage AND active power → PF stays 0.9–1.0
- Validated on real feeder with >200% DER penetration
- Led by student Madhura Sondharangalla

### Most Interesting Result
VQ-sensitivity matrix approach balances feeder observability + optimization + deployment realism in one method.

### Key Artifacts
- Official ASU Pure profile + active project list
- EVSTS center pages (multi-university, industry-facing)
- Specific project: "High Frequency Power Converters for Electric Vehicles" — ties portfolio to hardware/WBG
- NOTE: No public GitHub or Fulton Forge poster trail found

### Note on Hardware Work
Most visible recent open-access papers are feeder-control focused, NOT hardware. But EVSTS has active EV converter projects. If hardware-oriented, investigate 2024 ECCE soft-switched inverter paper.

### Follow-up Research Directions
1. State-estimation-aware coordinated volt/VAR under partial observability (8–14 months)
2. Commercial inverter implementation of volt-PF (6–12 months)
3. Fairness-aware Q-support for mixed PV + EV chargers (9–15 months)
4. Feeder-aware high-frequency charger scheduling (12–18 months)

---

## Yuji Zhao — Rice WIDE Lab (formerly ASU)

**IMPORTANT**: Zhao left ASU ~2020; current official home is Rice University (Houston). ASU pages are stale.

### Recent Papers

**Paper 1: GaN E-Mode MISHEMTs With Two-Step Etching Gate Recess (2025)**
- Compares standard ICP recess vs. high-power + low-power two-step recess
- Two-step results: Ion improved, hysteresis reduced, Dit halved (1.2–2.2 × 10¹² cm⁻²eV⁻¹), Ron 71.4 → 31.7 Ω·mm
- TDDB gate lifetime: 4.5 V → 5 V for 10-year criterion
- Key philosophy: process-tweak-as-reliability-lever

**Paper 2: Vertical β-Ga₂O₃ MIS Diodes With BN Interlayer (2023)**
- 2.8 nm BN interlayer on β-Ga₂O₃
- Breakdown voltage: 732 V (Schottky) → 1035 V (MIS) — 41% improvement
- Mechanism: passivated surface defects + reduced reverse leakage
- Demonstrates thin engineered interface → disproportionate gain in UWBG device

**Paper 3 (corroborating): Low-T CVD BN Gate Dielectric for AlGaN/GaN MISHEMTs (2024 APL)**
- 3 orders lower reverse gate leakage, Dit ~ 5–6 × 10¹¹ cm⁻²eV⁻¹
- Confirms BN interface engineering is a group-wide design philosophy, not one-off

### Most Interesting Result
Trap-limited performance improvement via deliberate interface/process design. Reusable philosophy: carefully designed interface/process → disproportionate electrical gains.

### Key Artifacts
- WIDE Lab at Rice (publications/news)
- CHIMES/JUMP 2.0 center participation
- Recent students: Shisong (DRC 2024 oral), Tao (CLEO 2024) — active BN/UWBG track
- NOTE: No public GitHub; Fulton Forge not applicable (Rice)

### Follow-up Research Directions
1. Digital twin for gate-recess damage in E-mode GaN (9–15 months)
2. BN interlayer engineering across Ga₂O₃ and GaN (9–18 months)
3. High-temperature gate/contact stack for extreme-environment electronics (8–14 months)
4. Compact trap-aware models for circuit designers (6–12 months)

---

## Cross-Faculty Synthesis

Three layers of the same future power-electronics stack:
- **Ranjram** → converter architecture + magnetics (the conversion layer)
- **Ayyanar** → system-level controls + EV/PV context (the application layer)
- **Zhao** → device physics + interface reliability (the semiconductor layer)

### Cross-Faculty Project Concepts
| Concept | Faculty |
|---------|---------|
| Feeder-aware ultra-compact EV converter | Raja + Mike + Yuji |
| High-frequency converter with data-informed magnetic design | Mike + Raja |
| Extreme-environment WBG power module | Mike + Yuji |
