---
type: source
title: "SIGGRAPH - Eras of GPU Development 2025"
source_type: article
author: ACM SIGGRAPH Blog
date_published: 2025-04
url: https://blog.siggraph.org/2025/04/evolution-of-gpus.html/
fetched: 2026-04-18
confidence: high
tags:
  - gpu
  - graphics
  - history
  - computer-architecture
status: developing
related:
  - "[[GPU Architecture Evolution]]"
  - "[[NVIDIA]]"
key_claims:
  - "GPU performance grew 2.5x per year from 1970s–1999, exceeding Moore's Law (1.8x)"
  - "DirectX 8.0 (2000) introduced programmable shaders — the turning point away from fixed-function"
  - "DirectX 12 Ultimate (2020) established GPU as a general-purpose computing engine"
  - "Experimental RISC-V GPU designs may shift from SIMD to MIMD architecture"
---

# SIGGRAPH: The Eras of GPU Development (2025)

**Source**: ACM SIGGRAPH Blog, April 2025  
**URL**: https://blog.siggraph.org/2025/04/evolution-of-gpus.html/

Authoritative retrospective on GPU development organized into six eras, framed around DirectX API milestones as the primary technical progression markers.

## Six Eras

| Era | DirectX | Year | Key Capability Added |
|-----|---------|------|----------------------|
| Fixed-function | DX7 | 1999 | Hardware T&L, multitexture |
| Programmable shaders | DX8 | 2000 | Vertex + pixel shaders |
| Geometry generation | DX10 | 2006 | Geometry shaders; unified architecture |
| Tessellation + Compute | DX11 | 2009 | Runtime detail enhancement; compute shaders |
| Low-level abstraction | DX12 | 2015 | Multithreaded CPU scaling; Vulkan-aligned |
| GPU as computing engine | DX12 Ultimate | 2020 | Mesh shaders; general-purpose compute |

## Notable Data Points

- GPU performance grew at **~2.5x per year** from the 1970s to 1999 — significantly exceeding Moore's Law's 1.8x prediction
- The 2006 GeForce 8800 unified separate programmable stages into a **single array of unified processors** — the first true GPGPU-capable architecture
- Future: experimental **RISC-V GPU designs** aim to shift from SIMD (Single Instruction, Multiple Data) to MIMD (Multiple Instruction, Multiple Data) architecture — a fundamental change to the parallelism model
