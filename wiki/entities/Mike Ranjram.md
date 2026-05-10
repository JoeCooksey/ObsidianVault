---
type: entity
subtype: person
name: Mike Ranjram
role: Assistant Professor, ASU ECEE
lab: MAPEL (Mixed-signal Architectures for Power Electronics Lab)
email: mike.ranjram@asu.edu
status: active
created: 2026-05-01
updated: 2026-05-01
tags:
  - person
  - faculty
  - power-electronics
  - magnetics
  - WBG
  - ASU
  - FURI-mentor
---

# Mike Ranjram

## Role
Assistant Professor, ASU School of Electrical, Computer and Energy Engineering.
Lab: **MAPEL** — Mixed-signal Architectures for Power Electronics Lab.

## Research Focus
Making power converters **smaller, more efficient, and more capable**. Core constraint being attacked: the magnetic bottleneck in converter miniaturization at MHz frequencies.

Primary themes:
- High-frequency power conversion (MHz operation)
- Converter architecture and topology innovation
- Magnetics design (variable inductors, planar magnetics, self-resonance)
- Gate driving and compact WBG integration
- Data-driven magnetic core-loss characterization

## Key Recent Papers

### ML-CEMS: Multi-Level Coupled Electronic and Magnetic System (ECCE 2024)
Gain variation in LLC converter at **fixed frequency** by injecting multi-level transformer voltages.
- Result: peak flux density reduced from 231 mT (frequency-modulated) → **66 mT** (ML-CEMS) at same operating point
- Importance: attacks "wide gain range → oversized magnetics" tradeoff directly
- Why it matters for Joe: connects topology + waveform synthesis + magnetic design + loss modeling in one problem

### HPPC: Harmonically Partitioned Power Converter (2025)
Single-stage ac/dc architecture using bidirectional switches.
- Targets: 120 Vrms in, 250 Vdc out, 250 W, 210 kHz
- Combines: unity PF + power-pulsation decoupling + continuous gain + galvanic isolation in one stage
- Eliminates cascaded PFC + isolated dc/dc architecture penalty

## Public Artifacts
- **Lab GitHub**: `ASU MAPEL` org — public repo `MHzCoreLossAggregateDataset` (13 source datasets, multiple ferrites, updated 2026)
- **Fulton Forge mentor page**: active student pipeline with posters on core-loss testing, pulsed-load emulation, planar inductor EM modeling
- **Centers**: PI in Global Hydrogen Production Technologies Centre; ASU EV ecosystem

## FURI Relevance
> [!key-insight] Top FURI Mentor for Joe
> Ranjram is the **#1 FURI priority**: active student pipeline, public GitHub artifacts, public Forge poster trail — most legible lab from outside. His problems (magnetics data, pulsed emulation, self-resonance-aware inductors) are all FURI-scope.

Mentor acquisition strategy:
1. Read ML-CEMS and HPPC papers (both digestible as an undergrad)
2. Visit office hours 2–3 times; show paper engagement
3. Express specific interest (e.g., core-loss dataset or HPPC closed-loop control)
4. Ask about FURI mentorship

Cold email: read 1–2 papers → 7–12 sentences → wait 7 business days → one follow-up max.

## Related Pages
- [[FURI Program Complete Guide]]
- [[Wide Bandgap Semiconductors]]
- [[Research - Power Electronics UWBG Faculty Scan 2026]]
- [[Raja Ayyanar]]
