---
type: concept
title: "EV Fast Charging Topologies"
created: 2026-04-18
updated: 2026-04-18
tags:
  - concept
  - domain/engineering
  - power-electronics
  - electric-vehicles
status: developing
complexity: advanced
domain: engineering
aliases: ["OBC", "onboard charger", "DC fast charger", "DCFC", "totem pole PFC", "CLLC", "DAB converter"]
related:
  - "[[Silicon Carbide Power Electronics]]"
  - "[[Gallium Nitride Power Electronics]]"
  - "[[800V EV Architecture]]"
  - "[[V2G Bidirectional Charging]]"
  - "[[Research - WBG Semiconductors in EV Fast Charging]]"
sources:
  - "[[MDPI WBG Comparative Review 2024]]"
---
# EV Fast Charging Topologies

EV charging power electronics use two-stage conversion: an AC-DC stage (PFC rectifier) followed by an isolated DC-DC stage. Wide bandgap semiconductors enable higher switching frequencies that shrink both stages.

## Two Main Architectures

### Onboard Charger (OBC)
- Mounted inside the vehicle
- Converts AC grid power → DC battery voltage
- Typical power: 3.6–22 kW
- Limited by vehicle weight and space constraints → WBG power density critical

### DC Fast Charger (DCFC / Off-board)
- Grid-connected station, external to vehicle
- Converts AC grid → high-voltage DC directly to battery
- Power: 50–350+ kW (ultra-fast chargers: 350 kW)
- Size/weight constraints less critical → SiC chosen for efficiency and reliability

## Key Circuit Stages

### AC-DC Stage: Totem Pole PFC
- Bridgeless power factor correction topology
- WBG advantage: GaN/SiC enable hard-switching at 65–100 kHz with low dead-time losses
- Si IGBTs limited to 20–50 kHz; higher freq requires WBG to avoid unacceptable switching losses
- Efficiency: >99% achievable with GaN at resonant switching

### DC-DC Stage: CLLC Resonant Converter
- Isolated, bidirectional resonant topology
- Operating frequency: 140–300 kHz (SiC), 300 kHz–1 MHz (GaN)
- Achieves soft switching (ZVS/ZCS) reducing switching losses
- SiC 22kW OBC CLLC stage: 140–250 kHz, >97% peak efficiency
- GaN 6.6kW OBC CLLC stage: 150–300 kHz, >96.5% efficiency

### DC-DC Stage: Dual Active Bridge (DAB)
- Alternative isolated bidirectional topology
- Preferred for V2G because of symmetric bidirectional characteristics
- GaN enables DAB at 300+ kHz → small transformer, high power density

## Efficiency Summary (WBG vs Si)

| Application | Si IGBT | SiC MOSFET | GaN |
|-------------|---------|-----------|-----|
| OBC peak eff | ~93–95% | ~97% | ~97–98% |
| DCFC peak eff | ~95–96% | ~97–98% | N/A (voltage limit) |
| EV range improvement | baseline | +~5% | similar |

## Power Density Gains

- SiC OBC: up to 54 W/in³ demonstrated (6.6kW design)
- GaN OBC: >8 kW/L demonstrated with advanced topologies
- Si IGBT equivalent: ~20–30 W/in³ typical

Higher switching frequency shrinks inductors, capacitors, and transformers — the dominant volume contributors in power converters.
