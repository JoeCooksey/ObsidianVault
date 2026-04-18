---
type: concept
title: "Wide Bandgap Semiconductors"
created: 2026-04-18
updated: 2026-04-18
tags:
  - concept
  - domain/engineering
  - power-electronics
  - semiconductors
status: developing
complexity: intermediate
domain: engineering
aliases: ["WBG", "wide bandgap", "SiC GaN comparison"]
related:
  - "[[Silicon Carbide Power Electronics]]"
  - "[[Gallium Nitride Power Electronics]]"
  - "[[Gallium Oxide Power Electronics]]"
  - "[[800V EV Architecture]]"
  - "[[Research - WBG Semiconductors in EV Fast Charging]]"
sources:
  - "[[IEEE Spectrum SiC vs GaN 2024]]"
  - "[[MDPI WBG Comparative Review 2024]]"
---
# Wide Bandgap Semiconductors

Wide bandgap (WBG) semiconductors have a larger energy gap between valence and conduction bands than silicon. This enables operation at higher voltages, temperatures, and switching frequencies — the three constraints that limit silicon in high-power applications like EV fast charging.

## Material Comparison

| Property | Silicon (Si) | Silicon Carbide (SiC) | Gallium Nitride (GaN) | Gallium Oxide (Ga₂O₃) |
|----------|----|-----|-----|------|
| Bandgap | 1.12 eV | 3.26 eV | 3.40 eV | 4.8 eV |
| Breakdown field | 0.3 MV/cm | 3.5 MV/cm | 3.3 MV/cm | 8 MV/cm |
| Electron mobility | 1,450 cm²/Vs | ~950 cm²/Vs | ~2,000 cm²/Vs | ~300 cm²/Vs |
| Thermal conductivity | 1.5 W/mK | 4.9 W/mK | 1.3 W/mK | 0.1–0.27 W/mK |
| Maturity | Fully mature | Production (EV, grid) | Production (OBC, telecom) | Research / early prototype |

## Why Bandgap Matters for Power Electronics

- **Higher breakdown voltage**: thinner drift layers → lower on-resistance → less conduction loss
- **Higher switching frequency**: smaller passive components (inductors, capacitors), higher power density
- **Higher junction temperature**: less cooling required, smaller thermal management systems
- **Lower switching losses**: faster turn-on/off → better efficiency at high frequency

## Technology Positioning

- **SiC dominates**: traction inverters, DC fast chargers, 800V+ systems (>600V)
- **GaN challenges**: onboard chargers (OBC), bidirectional converters, telecom (typically <650V; 1200V GaN emerging)
- **Ga₂O₃ (next generation)**: extreme voltages, early research stage — not yet in production EV systems

## Why Silicon Is Being Displaced

The IGBT (insulated-gate bipolar transistor) is the incumbent silicon device in EV power electronics. SiC MOSFETs operate at ~2× higher slew rate, deliver ~5% better vehicle energy efficiency, and enable operation at higher switching frequencies — reducing passive component size and total system cost despite higher device cost.

## Cross-Domain Connection

The physics of wide bandgap materials connects directly to [[Post-Training Quantization]] logic in ML: both fields are about doing more with less — trading device/model cost for system-level efficiency gains.
