---
type: concept
title: "CUDA Programming Model"
created: 2026-04-18
updated: 2026-04-18
tags:
  - gpu
  - programming
  - parallel-computing
  - nvidia
status: developing
related:
  - "[[GPU Architecture Evolution]]"
  - "[[Heterogeneous Computing]]"
  - "[[GPU Interconnects]]"
  - "[[NVIDIA]]"
  - "[[CUDA Ecosystem Flywheel]]"
  - "[[GPU vs TPU Trade-offs]]"
sources:
  - "[[Darkesh-Patel-Jensen-Huang-Nvidia-2025]]"
---

# CUDA Programming Model

CUDA (Compute Unified Device Architecture) is NVIDIA's parallel computing platform and programming model, released in 2007. It was the first widely-adopted framework enabling general-purpose programming on GPUs without graphics API knowledge.

## Host and Device Model

CUDA programs divide execution between two distinct systems:

- **Host**: the CPU and its DRAM. Runs the main program, OS calls, serial logic.
- **Device**: the GPU and its VRAM. Runs parallel kernels.

Both maintain **separate memory spaces**. Data must be explicitly copied between them (unless using unified memory).

## Execution Flow

A typical CUDA program:

```
1. Allocate memory on host (CPU RAM)
2. Allocate memory on device (GPU VRAM)
3. Copy input data: host → device  [PCIe transfer — often the bottleneck]
4. Launch kernel: CPU tells GPU to start N threads
5. GPU executes kernel in parallel across all N threads
6. Copy results: device → host  [PCIe transfer]
7. Free memory
```

The CPU proceeds (or waits) while the GPU executes. This asynchrony allows overlapping computation on both processors.

## Kernels and Thread Organization

A **kernel** is a function written in CUDA C that runs on the GPU. When launched, it spawns a **grid** of threads:

```
Grid
└── Thread Blocks (e.g., 1024 blocks)
    └── Threads per block (e.g., 256 threads)
        = 262,144 total parallel threads
```

**Warps**: Hardware groups 32 threads into a **warp** — the actual unit of SIMD execution. All 32 threads in a warp execute the same instruction simultaneously on different data. Divergent branches within a warp cause serialization (warp divergence).

## Memory Hierarchy on GPU

| Memory Type | Scope | Speed | Size |
|-------------|-------|-------|------|
| Registers | Per thread | Fastest | ~255 per thread |
| Shared memory | Per block | Fast (~1 cycle) | 48–164 KB per SM |
| L1/L2 cache | Device-wide | Medium | 32–192 KB / 50 MB |
| Global memory (VRAM) | Device-wide | Slow (hundreds of cycles) | 16–192 GB |
| Host memory | CPU RAM | Very slow (via PCIe) | 32–2000+ GB |

Efficient CUDA programming minimizes global memory accesses and maximizes shared memory reuse.

## Unified Memory

CUDA 6 (2014) introduced **Unified Memory**: a single virtual address space accessible from both CPU and GPU. The runtime handles data migration automatically. Simplifies programming but may have performance overhead compared to explicit transfers in latency-sensitive code.

## OpenCL: The Open Alternative

**OpenCL** (Open Computing Language) is an open standard (Khronos Group) equivalent to CUDA, supporting GPUs from NVIDIA, AMD, Intel, and other vendors. Less ecosystem support than CUDA but vendor-neutral.

## Why CUDA Matters (Engineering Context)

Before CUDA (2007), GPGPU required reformulating problems as graphics operations — a severe constraint. CUDA abstracted the GPU as a parallel processor, opening GPU computing to physics simulations, neural networks, financial modeling, and cryptography. This was the prerequisite for the deep learning revolution that began ~2012.

Every major deep learning framework (PyTorch, TensorFlow) has CUDA as its primary GPU backend. NVIDIA's CUDA ecosystem lock-in is a significant competitive moat.
