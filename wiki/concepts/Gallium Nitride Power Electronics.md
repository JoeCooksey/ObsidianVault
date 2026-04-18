---
type: concept
title: "Gallium Nitride Power Electronics"
created: 2026-04-18
updated: 2026-04-18
tags:
  - concept
  - domain/engineering
  - power-electronics
  - GaN
status: developing
complexity: advanced
domain: engineering
aliases: ["GaN", "gallium nitride", "GaN HEMT"]
related:
  - "[[Wide Bandgap Semiconductors]]"
  - "[[Silicon Carbide Power Electronics]]"
  - "[[EV Fast Charging Topologies]]"
  - "[[V2G Bidirectional Charging]]"
  - "[[Research - WBG Semiconductors in EV Fast Charging]]"
sources:
  - "[[IEEE Spectrum SiC vs GaN 2024]]"
  - "[[MDPI WBG Comparative Review 2024]]"
---
# Gallium Nitride Power Electronics

Gallium nitride (GaN) is the faster-switching [[Wide Bandgap Semiconductors|wide bandgap semiconductor]], operating at higher frequencies than SiC. Its natural home is onboard chargers (OBCs), bidirectional converters, and telecom power supplies. Its challenge is reaching the 1200V blocking voltage needed for 800V EV traction applications.

## Key Characteristics

- Switching frequency: **multiple hundreds of kilohertz** (vs ~100 kHz for SiC)
- Slew rate: ~50 V/ns
- Electron mobility: ~2,000 cm²/Vs (highest of the WBG materials)
- Current voltage range: primarily <650V devices in production; 1200V GaN commercially emerging in 2025
- Lateral device structure (vs SiC's vertical) — limits voltage scaling but enables integration

## EV Applications

### Onboard Charger (OBC) — Primary Target
GaN-based OBCs achieve:
- 96–98% efficiency at 100–500 kHz switching
- 30–60% reduction in passive component size
- 6.6kW designs at >97% efficiency (single and three-phase)

First production GaN OBCs expected in EVs by Q4 2025.

### Bidirectional V2G Charging
GaN enables compact bidirectional OBCs for [[V2G Bidirectional Charging]]. Topologies: Dual Active Bridge (DAB), CLLC resonant converter. A 10.9kW GaN bidirectional stage demonstrated high efficiency with both topologies.

Advanced GaN/Ga₂O₃ hybrid systems have demonstrated: ~99% efficiency, <0.2% grid current THD, >8 kW/L power density in three-phase grid-connected architectures.

### DC Fast Charger
Limited today (SiC dominates DCFC). GaN's 1200V roadmap could enable competition at lower power levels.

## SiC vs GaN: Which to Use

| Criterion | SiC | GaN |
|-----------|-----|-----|
| Voltage | 600–2300V (mature) | <650V mature; 1200V emerging |
| Switching freq | ~100–300 kHz | ~300 kHz–1 MHz+ |
| EV traction inverter | ✅ Dominant | ❌ Not yet viable at scale |
| OBC | ✅ Used | ✅ Preferred (higher freq) |
| DCFC infrastructure | ✅ Dominant | ❌ Limited |
| Cost trend | Declining | Lower substrate cost advantage |

## Cost Trajectory

GaN substrate costs are lower than SiC. Market projection: 1200V GaN devices will undercut comparable SiC devices on price in 2025, driven by substrate economics — despite currently requiring larger die sizes for equivalent current ratings.

## Key Acquisition
Infineon acquired GaN Systems to expand automotive GaN portfolio, signaling major industry bet on GaN for future EV power electronics.
