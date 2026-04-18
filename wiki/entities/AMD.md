---
type: entity
entity_type: organization
title: "AMD"
created: 2026-04-18
updated: 2026-04-18
tags:
  - organization
  - cpu
  - gpu
  - semiconductors
status: developing
related:
  - "[[CPU Architecture Evolution]]"
  - "[[GPU Architecture Evolution]]"
  - "[[Unified Memory Architecture]]"
sources: []
---

# AMD

Advanced Micro Devices. Semiconductor company producing both CPUs (Ryzen, EPYC) and GPUs (Radeon, Instinct). Founded 1969. Uniquely positioned to produce **APUs** (Accelerated Processing Units) — chips integrating CPU and GPU on the same die with unified memory.

## CPU Milestones

| Year | Product | Significance |
|------|---------|--------------|
| 2003 | Opteron / Athlon 64 | Led 64-bit x86 transition; x86-64 adopted by Intel |
| 2017 | Ryzen (Zen) | Broke Intel's multi-core performance dominance; 8-core mainstream |
| 2019 | EPYC Rome (Zen 2) | First chiplet-based CPU; fundamentally changed CPU manufacturing economics |
| 2023 | Ryzen 7000 (Zen 4) | 5nm; integrated RDNA 2 iGPU |
| 2025 | Ryzen AI Max+ 395 | APU SoC with unified memory; up to 128 GB shared CPU+GPU pool |

## GPU / APU

AMD's **Ryzen AI Max+ 395** (2025) is a landmark APU: large unified memory pool accessible by both CPU and GPU without PCIe data copies. Targets the same use case as Apple Silicon M-series for local AI inference. See [[Unified Memory Architecture]].

AMD Instinct GPUs (MI300X, etc.) compete with NVIDIA in the AI datacenter space using HBM memory and ROCm open-source compute platform.
