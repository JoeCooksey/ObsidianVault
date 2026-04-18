---
type: concept
title: "GPU Architecture Evolution"
created: 2026-04-18
updated: 2026-04-18
tags:
  - computer-architecture
  - gpu
  - history
  - graphics
  - gpgpu
status: developing
related:
  - "[[CPU Architecture Evolution]]"
  - "[[CUDA Programming Model]]"
  - "[[Heterogeneous Computing]]"
  - "[[GPU Interconnects]]"
  - "[[NVIDIA]]"
  - "[[AMD]]"
sources:
  - "[[SIGGRAPH - Eras of GPU Development 2025]]"
---

# GPU Architecture Evolution

The GPU (Graphics Processing Unit) began as a fixed-function chip for rendering graphics and evolved into the dominant platform for massively parallel computation — from AI training to scientific simulation.

## Era 1: Fixed-Function Hardware (1980s–1999)

Early graphics hardware performed only specific predetermined operations: rasterization, texture mapping, z-buffering. No programmability existed. The developer could only configure pre-wired pipelines.

**NVIDIA GeForce 256 (1999)**: First chip marketed as a "GPU." 17 million transistors. Introduced hardware **Transform & Lighting (T&L)** — offloading geometry transformation from CPU to GPU for the first time. DirectX 7.0 formalized this capability.

GPU performance grew at **~2.5× per year** from the 1970s to 1999 — exceeding Moore's Law (1.8×) due to the predictable regularity of graphics workloads enabling specialized parallelism. (Source: [[SIGGRAPH - Eras of GPU Development 2025]])

## Era 2: Programmable Shaders (2000–2006)

**DirectX 8.0 (November 2000)** introduced **vertex shaders** and **pixel shaders** — small programmable programs that run per-vertex and per-pixel. Developers could now write custom code executed in parallel on the GPU.

This was the turning point: the GPU was no longer purely fixed-function. However, vertex and pixel shader processors were still *separate* hardware units.

## Era 3: Unified Shader Architecture (2006–2009)

**NVIDIA GeForce 8800 (2006)** / **DirectX 10** introduced the **unified shader architecture**: all previously separate shader stages (vertex, geometry, pixel) were mapped to a single array of identical processing units called **streaming multiprocessors (SMs)**.

This meant the GPU could dynamically allocate processing resources to whatever stage was most needed. It also enabled general-purpose GPU computation (GPGPU) — the same cores used for shading could compute arbitrary parallel programs.

**CUDA (2007)**: NVIDIA released CUDA, the first widely adopted GPU programming model, making GPGPU accessible to scientists and engineers without graphics expertise. See [[CUDA Programming Model]].

## Era 4: Compute Shaders + Tessellation (2009–2015)

**DirectX 11 (2009)** added:
- **Tessellation**: runtime geometric detail generation on GPU, not CPU — reducing vertex data sent over PCIe
- **Compute shaders**: formal general-purpose compute path within the graphics pipeline

GPUs became serious HPC accelerators during this era — used for physics simulation, molecular dynamics, deep learning inference.

## Era 5: Low-Level APIs + AI Acceleration (2015–2020)

**DirectX 12 (2015)** / Vulkan reduced CPU overhead by providing lower-level API access. CPUs had been a bottleneck for GPU submission — DX12 allowed multi-threaded command recording, reducing CPU utilization.

NVIDIA Pascal (2016) and Volta (2017) architectures added **Tensor Cores** — dedicated matrix multiply units for AI training. This bifurcated GPU design: gaming-focused CUDA cores + AI-focused Tensor Cores on the same die.

## Era 6: GPU as General Computing Engine (2020–present)

**DirectX 12 Ultimate (2020)** added mesh shaders and sampler feedback, fully establishing the GPU as a programmable computing device that happens to also render graphics.

Modern datacenter GPUs (NVIDIA H100, AMD MI300X) are designed almost entirely around compute, not graphics. They feature:
- **HBM memory** (High Bandwidth Memory) on-package: 3–4 TB/s vs ~900 GB/s for GDDR7
- Tensor Core generations with FP8/INT8/BF16 support for AI
- NVLink interconnects at 900 GB/s–1.8 TB/s for multi-GPU scaling

## SIMD Architecture

GPUs use **SIMD (Single Instruction, Multiple Data)** execution: one instruction is issued to a **warp** (NVIDIA) or **wavefront** (AMD) of 32–64 threads, all executing the same instruction simultaneously on different data. This is the source of GPU throughput — thousands of simple parallel threads, not dozens of complex serial threads.

> [!gap] Future MIMD architectures
> Experimental RISC-V-based GPU designs aim to shift from SIMD to MIMD (Multiple Instruction, Multiple Data), where each processor can execute a different instruction. If realized, this would fundamentally change the GPU parallelism model. (Source: [[SIGGRAPH - Eras of GPU Development 2025]])
