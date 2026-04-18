---
type: concept
title: "CPU Architecture Evolution"
created: 2026-04-18
updated: 2026-04-18
tags:
  - computer-architecture
  - cpu
  - history
  - engineering
status: developing
related:
  - "[[Moore's Law and Dennard Scaling]]"
  - "[[Heterogeneous Computing]]"
  - "[[GPU Architecture Evolution]]"
  - "[[Intel]]"
  - "[[AMD]]"
sources:
  - "[[SIGGRAPH - Eras of GPU Development 2025]]"
---

# CPU Architecture Evolution

The CPU (Central Processing Unit) is the general-purpose serial processor at the heart of every computer. Its evolution spans five decades, driven first by transistor scaling, then by architectural innovation, and most recently by heterogeneous integration.

## Era 1: Single-Core Scalar (1971–1992)

The Intel 4004 (1971) contained 2,300 transistors and executed 60,000 operations per second. Each generation roughly doubled transistor count per [[Moore's Law and Dennard Scaling|Moore's Law]], enabling higher clock speeds and wider data paths:

- 1978: Intel 8086 — established **x86 ISA**; 16-bit; 29,000 transistors
- 1985: Intel 80386 — first 32-bit x86; enabled protected memory and modern OSes
- 1993: Intel Pentium — **superscalar execution** (multiple instructions per clock); 3.1M transistors

## Era 2: Superscalar + Out-of-Order Execution (1993–2004)

Modern high-performance CPUs use two key techniques to extract more work per clock cycle:

**Superscalar execution**: Fetch and issue multiple instructions simultaneously to separate execution units (ALU, FPU, memory). A modern CPU can issue 4–6 instructions per cycle.

**Out-of-order execution (OOO)**: Execute instructions in the order data becomes *available*, not program order, to avoid stalls. The CPU maintains a **reorder buffer** to retire results in original order.

**Pipeline stages**: Instruction Fetch → Decode → Execute → Memory Access → Write-back. Contemporary designs use 14–20 pipeline stages and operate above 5 GHz.

**Cache hierarchy**: L1 (fastest, ~32–64 KB per core) → L2 (~256 KB–1 MB per core) → L3 (shared, 16–64+ MB). Each level trades capacity for latency. A cache miss to DRAM costs ~100ns vs ~4 clock cycles for L1.

## Era 3: The Power Wall and Multi-Core (2004–2015)

[[Moore's Law and Dennard Scaling|Dennard scaling]] broke down around 2005: shrinking transistors no longer reduced power proportionally. Clock frequencies stalled at 4–6 GHz. The **power wall** forced the industry to change strategy.

Response: **multi-core processors** — multiple complete CPU cores on one die, each at moderate frequency, rather than one fast core. Intel's Core 2 Duo (2006) marked the mainstream transition.

By 2017, AMD's Ryzen 7 delivered **8 cores / 16 threads** to consumers — previously only in workstations. AMD's Zen 2 (2019) introduced **chiplet architecture**: separate dies (compute chiplets + I/O die) connected by high-bandwidth fabric, dramatically improving manufacturing yield and cost.

## Era 4: Heterogeneous SoC (2015–present)

CPUs are no longer standalone processors — they are components in **SoCs** (Systems-on-Chip) that integrate:
- CPU cores (high-performance + efficiency cores)
- Integrated GPU
- Neural Processing Units (NPUs)
- Memory controllers
- Signal processors

Apple Silicon (M-series, 2020–present) is the most advanced consumer example: CPU, GPU, and Neural Engine share a **unified memory pool** at 400–600+ GB/s. AMD's Ryzen AI Max+ 395 (2025) takes the same approach for Windows/Linux. See [[Unified Memory Architecture]].

## Key Architectural Metrics Over Time

| Year | Transistors | Clock Speed | Cores | Process Node |
|------|------------|-------------|-------|-------------|
| 1971 (4004) | 2,300 | 740 kHz | 1 | 10,000 nm |
| 1993 (Pentium) | 3.1M | 60–200 MHz | 1 | 800 nm |
| 2006 (Core 2 Duo) | 291M | 2.4 GHz | 2 | 65 nm |
| 2017 (Ryzen 7 1700) | 4.8B | 3.0–3.7 GHz | 8 | 14 nm |
| 2025 (Ryzen AI Max+ 395) | ~70B est. | 5 GHz+ | 16 | 4 nm |
