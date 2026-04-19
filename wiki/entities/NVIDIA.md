---
type: entity
entity_type: organization
title: "NVIDIA"
created: 2026-04-18
updated: 2026-04-18
tags:
  - organization
  - gpu
  - ai
  - semiconductors
status: developing
related:
  - "[[GPU Architecture Evolution]]"
  - "[[CUDA Programming Model]]"
  - "[[GPU Interconnects]]"
  - "[[CUDA Ecosystem Flywheel]]"
  - "[[AI Five-Layer Cake]]"
  - "[[Accelerated Computing]]"
  - "[[Jensen Huang]]"
sources:
  - "[[SIGGRAPH - Eras of GPU Development 2025]]"
  - "[[Darkesh-Patel-Jensen-Huang-Nvidia-2025]]"
---

# NVIDIA

Semiconductor company and the dominant GPU manufacturer. Founded 1993. Creator of the CUDA parallel computing platform (2007), which enabled general-purpose GPU programming and positioned NVIDIA at the center of AI/ML infrastructure.

## Key Products and Milestones

| Year | Product / Event | Significance |
|------|----------------|--------------|
| 1999 | GeForce 256 | First product marketed as a "GPU"; 17M transistors; first consumer hardware T&L |
| 2006 | GeForce 8800 | First unified shader architecture; enabled GPGPU |
| 2007 | CUDA | First widely-adopted general-purpose GPU programming model |
| 2022 | H100 (Hopper) | NVLink 4 at 900 GB/s; dominant AI training GPU |
| 2024 | B100/B200 (Blackwell) | NVLink 5 at 1.8 TB/s per GPU; ~14x PCIe Gen5 bandwidth |

## Interconnect Leadership

NVIDIA's **NVLink** proprietary GPU interconnect provides dramatically higher bandwidth than PCIe for multi-GPU clusters. NVLink 5.0 (Blackwell, 2024) delivers **1.8 TB/s** — roughly 14× PCIe Gen5 x16. This bandwidth advantage is the primary reason NVIDIA dominates AI training workloads where GPUs must share parameters and gradients frequently.

## Competitive Position (2025)

NVIDIA holds dominant market share in AI training GPU market. AMD Instinct and Intel Gaudi are the primary competitors in GPGPU/AI accelerator space.

## Strategy and Philosophy (Jensen Huang)

**Mental model**: "Electrons → Tokens." Nvidia transforms grid power into AI output; the job is to maximize value of that transformation.

**Company philosophy**: "Do as much as needed, as little as possible." Build what only Nvidia can (CUDA, NVLink, domain libraries); partner for everything else (clouds, ODMs, foundries).

**Why not a hyperscaler**: If Nvidia didn't build CUDA, nobody would. If Nvidia didn't build a cloud, somebody would. Focus on the irreplaceable work.

**Investment strategy**: Invest in every major foundation lab (OpenAI ~$30B, Anthropic ~$10B); don't pick winners.

**GPU allocation**: FIFO by purchase order; never highest-bidder pricing — "I prefer to be dependable, to be the foundation of the industry."

## Chip Roadmap (as of 2025)
- **Hopper** (H100/H200) — current deployed fleet; "most models today are trained on Hopper"
- **Blackwell** (B100/B200) — 50× more efficient than Hopper (architecture + algorithms, not just transistors)
- **Vera Rubin** — next generation
- **Vera Rubin Ultra**
- **Feynman**

## Supply Chain Moat
- $100B+ in explicit purchase commitments with foundries, memory, packaging
- Implicit commitments: CEO-level relationships convincing upstream partners to invest (Micron/HBM example)
- Resolved past bottlenecks: CoWoS (packaging), HBM memory — "swarmed" with investment
- Invested in silicon photonics ecosystem (Lumentum, Coherent) for future interconnect scale
- Partnered on TSMC COUPE packaging technology; licensed patents to keep supply chain open
- Real bottleneck identified: **energy** — takes years, not 2–3 years like chips/packaging

## China and Export Controls (Jensen's view)
Jensen argues against aggressive export controls:
- China has enough compute already (Huawei Ascend at scale, abundant energy to gang older chips)
- 50% of world's AI researchers are Chinese; algorithm advances > raw hardware
- Conceding China's market accelerates their domestic chip ecosystem (telecom precedent)
- Goal: keep Chinese AI developers on the American tech stack (CUDA) vs. diverging to Huawei stacks
