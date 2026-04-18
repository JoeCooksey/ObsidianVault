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
sources:
  - "[[SIGGRAPH - Eras of GPU Development 2025]]"
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
