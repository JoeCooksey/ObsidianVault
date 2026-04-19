---
type: concept
title: "Accelerated Computing"
created: 2026-04-18
updated: 2026-04-18
tags:
  - nvidia
  - computing
  - gpu
  - ai
  - hardware
status: developing
related:
  - "[[NVIDIA]]"
  - "[[Jensen Huang]]"
  - "[[CUDA Programming Model]]"
  - "[[GPU Architecture Evolution]]"
  - "[[Moore's Law and Dennard Scaling]]"
  - "[[Heterogeneous Computing]]"
sources:
  - "[[Darkesh-Patel-Jensen-Huang-Nvidia-2025]]"
---

# Accelerated Computing

Nvidia's mission and market positioning: accelerating specific computation-heavy workloads by offloading them from general-purpose CPUs to specialized parallel processors (GPUs). Distinct from AI-specific accelerators (TPUs, ASICs).

## Why It Exists

General-purpose computing (CPU) scaled well under **Dennard Scaling** until ~2005. Since then, transistor counts still grow but clock speeds cannot — energy density hits thermal limits. See [[Moore's Law and Dennard Scaling]].

The solution: **domain-specific acceleration**. Offload parallelizable computation to hardware optimized for it. CPU handles serial, branchy logic; GPU handles massive parallel computation.

## Scope Beyond AI

This is Jensen's key distinction from "AI accelerator":

| Domain | Application |
|--------|-------------|
| Computer graphics | Real-time rendering, ray tracing |
| Molecular dynamics | Drug discovery, protein folding |
| Computational fluid dynamics | Engineering simulation |
| Quantum chromodynamics | Particle physics |
| Seismic processing | Energy exploration |
| Data processing | Structured + unstructured data, ETL |
| Computational lithography | cuLitho — photomask simulation |
| AI/ML | Training and inference |

"Even if AI doesn't exist today, Nvidia would be very, very large." — Jensen Huang

## CUDA as the Platform
CUDA is what transforms a GPU from a graphics chip into an accelerated computing platform. Each domain gets domain-specific libraries (cuDNN for AI, cuLitho for lithography, etc.). See [[CUDA Programming Model]].

## Nvidia's Role in the Ecosystem
Jensen's philosophy: **"Do as much as needed, as little as possible."**
- Build what only Nvidia can build: CUDA, NVLink, domain libraries, supply chain relationships
- Partner for everything else: clouds, ODMs, foundries, memory
- Don't compete with customers (not a hyperscaler; not a foundation lab)

## Electrons → Tokens Mental Model
Nvidia's business summarized: transform electrons into tokens. Every dollar of capital spending on Nvidia hardware converts grid power into AI output. The company's job is to maximize the value of that transformation per watt, per dollar, per rack.

## See Also
- [[CUDA Ecosystem Flywheel]]
- [[AI Five-Layer Cake]]
- [[GPU vs TPU Trade-offs]]
- [[Moore's Law and Dennard Scaling]]
