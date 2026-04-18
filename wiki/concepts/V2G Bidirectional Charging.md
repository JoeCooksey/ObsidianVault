---
type: concept
title: "V2G Bidirectional Charging"
created: 2026-04-18
updated: 2026-04-18
tags:
  - concept
  - domain/engineering
  - electric-vehicles
  - power-electronics
status: seed
complexity: intermediate
domain: engineering
aliases: ["V2G", "vehicle to grid", "V2L", "bidirectional OBC", "bidirectional charging"]
related:
  - "[[EV Fast Charging Topologies]]"
  - "[[Gallium Nitride Power Electronics]]"
  - "[[Silicon Carbide Power Electronics]]"
  - "[[Research - WBG Semiconductors in EV Fast Charging]]"
sources:
  - "[[MDPI WBG Comparative Review 2024]]"
---
# V2G Bidirectional Charging

Vehicle-to-Grid (V2G) allows an EV to discharge energy back to the power grid, functioning as a distributed battery storage asset. Vehicle-to-Load (V2L) allows powering external devices directly from the EV battery. Both require bidirectional onboard chargers.

## Why WBG Enables V2G

Bidirectional power flow requires symmetric AC-DC and DC-AC conversion. SiC and GaN devices operate at high frequency in both directions without the reverse-recovery losses that plague silicon PiN diodes at high switching speeds. This enables compact, efficient bidirectional OBCs that previously weren't feasible with silicon.

## Key Topologies

- **CLLC Resonant Converter**: Symmetric, bidirectional — preferred for OBC. GaN enables 150–300 kHz operation.
- **Dual Active Bridge (DAB)**: Symmetric bidirectional isolated DC-DC. GaN DAB converters at >300 kHz.

## Demonstrated Performance

- **SiC 22kW bidirectional OBC**: >97% efficiency in both charge and discharge modes
- **GaN 6.6kW bidirectional OBC**: integrated 1kW 12V auxiliary DC-DC; >97% efficiency; 54 W/in³
- **GaN V2G charger with supercapacitor**: hybrid battery-supercapacitor energy management demonstrated

## Grid Implications

Bidirectional OBCs enable:
- **Peak shaving**: discharge during grid peak demand, charge at off-peak
- **Frequency regulation**: rapid response to grid frequency deviations
- **Emergency backup power** (V2L → house loads during outages)

Bidirectional OBCs projected to become the dominant OBC architecture as smart grid infrastructure matures.

> [!gap] Widespread V2G deployment requires standardized grid communication protocols (ISO 15118), utility incentive programs, and battery degradation management. The power electronics are ready; the grid integration ecosystem is the bottleneck.
