---
type: concept
title: "Power Module Ceramic Substrates"
created: 2026-05-29
updated: 2026-05-29
tags:
  - concept
  - domain/engineering
  - power-electronics
  - packaging
  - reliability
status: developing
complexity: advanced
domain: engineering
aliases: ["DBC", "AMB", "DBC vs AMB", "AlN substrate", "Si3N4 substrate", "ceramic substrate power module"]
related:
  - "[[Multi-Chip Power Module Packaging]]"
  - "[[Silver Sintering Die-Attach]]"
  - "[[Heterogeneous Integration (Power Electronics)]]"
  - "[[WBG Thermal Management]]"
  - "[[Silicon Carbide Power Electronics]]"
---

# Power Module Ceramic Substrates

The ceramic substrate provides **electrical isolation + heat spreading + mechanical support** under the power dice. Two axes define the choice: the **ceramic** (AlN / Si₃N₄ / Al₂O₃) and the **metallization process** (DBC vs AMB).

## The ceramics

| Ceramic | Thermal cond. (W/m·K) | CTE (ppm/K) | Fracture toughness | Note |
|---|---|---|---|---|
| **Al₂O₃** (alumina) | ~24 | ~7 | low | cheap, legacy, poor heat |
| **AlN** (aluminum nitride) | ~170–180 | ~4.5 | ~3–4 MPa·√m (brittle) | best heat spreader |
| **Si₃N₄** (silicon nitride) | ~70–90 | ~3.2 | ~6–7 MPa·√m (tough) | best CTE match + reliability |

AlN's conductivity nearly matches SiC itself (~120–200 W/m·K); Al₂O₃ is ~7× worse (Source: web search synthesis; confidence: high).

## DBC vs AMB metallization

- **DBC (Direct Bonded Copper):** Cu bonded to ceramic via a copper-oxide eutectic at ~1065 °C. Standard, lower cost. Dominant for **AlN** high-performance SiC modules.
- **AMB (Active Metal Brazing):** Cu brazed with an active filler (e.g. Ti) for a stronger, more thermal-cycle-robust bond. The route of choice for **Si₃N₄**, enabling thicker Cu and the highest reliability.

## The reliability twist

AlN spreads heat better, but **Si₃N₄ AMB wins automotive reliability**:

- Si₃N₄ CTE (~3.2 ppm/K) is the **closest industrial match to SiC** (~4 ppm/K) → lower interfacial stress (see [[Silver Sintering Die-Attach]]).
- Si₃N₄ AMB survives **3,000–5,000+ cycles (−40 → 250 °C)**; reliability improved by a **factor of ~50** vs conventional DBC ceramic (Source: web search synthesis; confidence: high).
- Si₃N₄ at **half the ceramic thickness** (0.32 mm vs 0.63 mm AlN) reaches similar thermal resistance — the thinness offsets its lower conductivity.
- AlN is more **brittle** and cracks under severe cycling with conventional DBC.

> [!tip] Rule of thumb
> **AMB on Si₃N₄** is preferred when thermal-cycling life must exceed ~10,000 cycles or ΔT > 200 °C — i.e. automotive-grade SiC/GaN traction inverters. **DBC on AlN** remains common where peak heat-spreading matters more than fatigue life.
