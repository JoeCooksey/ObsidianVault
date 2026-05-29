---
type: source
source_type: technical-article
title: "Parasitic Inductance and Switching — Power Electronic Tips"
author: "Power Electronic Tips"
date_published: 
url: "https://www.powerelectronictips.com/how-do-parasitic-inductances-affect-switching-performance/"
created: 2026-05-29
updated: 2026-05-29
tags:
  - source
  - power-electronics
  - parasitics
status: verified
confidence: medium
related:
  - "[[Common-Source Inductance]]"
  - "[[Multi-Chip Power Module Packaging]]"
---

# Parasitic Inductance and Switching — Power Electronic Tips

Technical explainer on how parasitic inductances degrade power-switching performance.

## Key claims (confidence: medium–high)

- **Common-source inductance** induces a voltage opposing the gate drive (negative feedback), slowing turn-on/turn-off and raising switching loss (confidence: high — corroborated by Wolfspeed app notes).
- Fundamental relation **V = L·(di/dt)**; rapid current change across power-loop inductance generates turn-off voltage spikes that can exceed device ratings.
- Package bond wires contribute "several nanohenries" that matter at high switching frequency.
- Experimental: as L_S increases, di/dt falls and both turn-on and turn-off switching losses rise.

> [!gap] Undated page — flagged medium confidence per program exclusions. Physics is standard and corroborated; specific nH targets came from other sources (Wolfspeed, EPC).

## Contribution

Primary fetched anchor for [[Common-Source Inductance]] and the parasitics discussion in [[Multi-Chip Power Module Packaging]].
