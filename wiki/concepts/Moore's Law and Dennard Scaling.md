---
type: concept
title: "Moore's Law and Dennard Scaling"
created: 2026-04-18
updated: 2026-04-18
tags:
  - computer-architecture
  - semiconductors
  - history
  - engineering
status: developing
related:
  - "[[CPU Architecture Evolution]]"
  - "[[GPU Architecture Evolution]]"
  - "[[Heterogeneous Computing]]"
  - "[[Intel]]"
sources: []
---

# Moore's Law and Dennard Scaling

Two empirical laws that jointly drove 30+ years of automatic CPU performance improvement. Their breakdown in the mid-2000s fundamentally changed computer architecture strategy.

## Moore's Law (1965)

**Observation**: The number of transistors on an integrated circuit doubles approximately every 2 years.

Formulated by Gordon Moore (Intel co-founder) in 1965. Held approximately true from 1965 to the mid-2010s.

**Effect**: Each CPU generation received roughly 2× more transistors — enabling more cores, larger caches, more complex microarchitecture.

**Current status**: Slowing but continuing. Transistor counts still grow, but at sub-2x/2-year pace. Manufacturers (TSMC, Intel, Samsung) are at 2–3nm process nodes as of 2025. "More than Moore" strategies (chiplets, 3D stacking, packaging) extend the roadmap.

## Dennard Scaling (1974)

**Observation**: As transistors shrink, power density stays constant — smaller transistors consume proportionally less power and run faster at the same voltage.

Formulated by Robert Dennard et al. (IBM) in a 1974 paper.

**Effect during golden era**: Each transistor generation was simultaneously faster *and* more power-efficient. Clock speeds doubled roughly every 18 months alongside transistor counts, with no increase in total chip power.

## The Breakdown (~2005–2007)

Dennard scaling failed at small process nodes (~65nm and below) due to:

1. **Leakage current**: transistors became so thin that current leaked even when "off" — consuming power without doing work
2. **Threshold voltage limits**: operating voltage couldn't be reduced further without unacceptable leakage
3. **Thermal runaway risk**: power density grew uncontrollably as clock speeds increased

**Result**: Clock frequencies stagnated at **4–6 GHz** (still roughly true in 2025). TDP (thermal design power) stalled at ~100–125W per high-end CPU. Simply shrinking transistors no longer produced faster chips for free.

## The Consequences

### Power Wall → Multi-Core Transition
The industry could not keep increasing single-core frequency. Response: add more cores. Multi-core CPUs became standard from 2006 onward, shifting performance scaling to **parallelism** rather than frequency.

### Shift to Heterogeneous Computing
When no single processor type could continue scaling, the industry moved to specialized processors that each do their specific task efficiently: CPU for serial code, GPU for parallel code, NPU for AI inference, DSPs for signal processing. See [[Heterogeneous Computing]].

### Rise of GPU Importance
GPUs benefited from a different physics regime — their highly parallel, regular workloads tolerate the power constraints better than CPU scalar code. Massively parallel compute moved to GPUs.

### Chiplet Architecture
Intel, AMD, and Apple moved to **chiplet designs**: separate silicon dies for compute vs. I/O, connected by high-speed on-package interconnects. AMD's Zen 2 chiplet approach (2019) reduced manufacturing cost while enabling higher core counts.

## Current Reality (2025)

Moore's Law is slowing, not dead. TSMC's 2nm class processes continue transistor density gains. But performance-per-watt gains have slowed, and clock speed is no longer the lever — architecture, memory bandwidth, and heterogeneous integration are.
