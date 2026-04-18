---
type: synthesis
title: "Research: Evolution of CPUs and GPUs"
created: 2026-04-18
updated: 2026-04-18
tags:
  - research
  - cpu
  - gpu
  - computer-architecture
  - engineering
status: developing
related:
  - "[[CPU Architecture Evolution]]"
  - "[[GPU Architecture Evolution]]"
  - "[[Moore's Law and Dennard Scaling]]"
  - "[[Heterogeneous Computing]]"
  - "[[CUDA Programming Model]]"
  - "[[GPU Interconnects]]"
  - "[[Unified Memory Architecture]]"
  - "[[Intel]]"
  - "[[AMD]]"
  - "[[NVIDIA]]"
sources:
  - "[[SIGGRAPH - Eras of GPU Development 2025]]"
---

# Research: Evolution of CPUs and GPUs

## Overview

CPUs and GPUs began as entirely separate tools — one for general computation, one for graphics — and have converged into tightly coupled heterogeneous systems. The story is fundamentally about the **end of free performance scaling** (Dennard breakdown, ~2005) forcing the industry to embrace parallelism and specialization.

## Key Findings

1. **CPU evolution was frequency-driven until ~2005, then core-count-driven.**  
   From Intel 4004 (1971, 2,300 transistors) to Ryzen AI Max+ 395 (2025, ~70B transistors), the trajectory ran: scalar → superscalar → out-of-order → multi-core → heterogeneous SoC. The transition to multi-core was *forced* by the power wall, not chosen. (Source: [[CPU Architecture Evolution]], [[Moore's Law and Dennard Scaling]])

2. **GPU performance grew faster than Moore's Law from 1970–1999 (~2.5× per year).**  
   Specialized parallelism for predictable graphics workloads enabled GPU silicon to outpace general CPU transistor-to-performance ratios. (Source: [[SIGGRAPH - Eras of GPU Development 2025]])

3. **The GPU's GPGPU transition was enabled by one API change (DirectX 8 / CUDA) and one hardware change (unified shaders).**  
   Programmable shaders (DirectX 8, 2000) made GPUs programmable. CUDA (2007) made that programmability accessible. Unified shader architecture (GeForce 8800, 2006) put all shader types on the same cores. These three changes converted a graphics chip into a parallel supercomputer. (Source: [[GPU Architecture Evolution]])

4. **CPUs are latency-optimized; GPUs are throughput-optimized — they are complementary, not competitive.**  
   CPUs use large caches and OOO execution to minimize wait per instruction. GPUs tolerate per-thread latency by switching warps. A GPU running OS-level tasks would be catastrophically slow. A CPU running matrix multiplication on a large model would take orders of magnitude longer than a GPU. (Source: [[Heterogeneous Computing]])

5. **PCIe bandwidth (~64 GB/s) is the bottleneck between CPU and discrete GPU — 30× slower than GPU's internal HBM (2 TB/s).**  
   Data-intensive workloads can be dominated by the cost of moving data across PCIe, not by computation. This is the primary motivation for unified memory architectures. (Source: [[GPU Interconnects]])

6. **NVLink 5 (Blackwell, 2024) at 1.8 TB/s is ~14× PCIe Gen5 and the reason NVIDIA dominates AI training.**  
   Multi-GPU clusters synchronize gradients across all GPUs during backpropagation. At PCIe speeds this is a severe bottleneck; at NVLink speeds it is not. (Source: [[GPU Interconnects]])

7. **Unified memory (Apple M5 Max, AMD Ryzen AI Max+) solves the discrete GPU capacity problem for inference.**  
   A 70B model at Q4 requires ~40 GB. No consumer discrete GPU has that VRAM. Apple M5 Max with 128 GB unified pool can serve it. The tradeoff: lower raw TFLOPS than a discrete GPU. (Source: [[Unified Memory Architecture]])

8. **The future bifurcates into: (a) massive datacenter GPU clusters for training, (b) efficient SoC heterogeneous chips for inference.**  
   Training requires NVLink-speed multi-GPU clusters with HBM. Inference increasingly moves to edge SoCs with unified memory, lower power, and NPUs. These are different hardware markets with different optimization targets.

## Key Entities

- [[Intel]] — invented x86 ISA (1978); multi-core transition (2006)
- [[AMD]] — led 64-bit x86 transition (2003); chiplet revolution (2019); APU unified memory (2025)
- [[NVIDIA]] — coined "GPU" (1999); CUDA (2007); NVLink 5 (2024); dominates AI training

## Key Concepts

- [[Moore's Law and Dennard Scaling]] — foundation and breakdown (~2005) that forced architecture change
- [[CPU Architecture Evolution]] — scalar → superscalar → multi-core → SoC
- [[GPU Architecture Evolution]] — fixed-function → programmable → GPGPU → AI accelerator
- [[Heterogeneous Computing]] — CPU/GPU division of labor; latency vs throughput
- [[CUDA Programming Model]] — host/device/kernel model; why NVIDIA has a moat
- [[GPU Interconnects]] — PCIe vs NVLink vs CXL; bandwidth hierarchy
- [[Unified Memory Architecture]] — Apple Silicon, AMD APU; eliminates PCIe bottleneck

## Open Questions

- How will RISC-V-based MIMD GPU architectures (if realized) change the SIMD programming model and CUDA dominance?
- At what point does SoC unified memory bandwidth match discrete GPU VRAM bandwidth — and does that make discrete GPUs obsolete for inference?
- What is the practical ceiling for NVLink scaling — how many GPUs can be connected before topology becomes a bottleneck?
- How does the NPU vs GPU trade-off evolve as transformer architectures diversify? (NPUs are optimized for specific ops; GPUs are general)
- CXL's role in AI training is currently limited — will memory pooling at rack scale change multi-GPU training economics?

## Sources

- [[SIGGRAPH - Eras of GPU Development 2025]]: authoritative GPU era framework; performance growth data
