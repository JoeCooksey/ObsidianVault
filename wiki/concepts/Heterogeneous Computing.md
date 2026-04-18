---
type: concept
title: "Heterogeneous Computing"
created: 2026-04-18
updated: 2026-04-18
tags:
  - computer-architecture
  - cpu
  - gpu
  - engineering
status: developing
related:
  - "[[CPU Architecture Evolution]]"
  - "[[GPU Architecture Evolution]]"
  - "[[CUDA Programming Model]]"
  - "[[Unified Memory Architecture]]"
  - "[[GPU Interconnects]]"
  - "[[Moore's Law and Dennard Scaling]]"
sources: []
---

# Heterogeneous Computing

A computing architecture that uses multiple **different types of processors** in a single system, each optimized for a different class of task. The dominant form today pairs CPUs with GPUs.

## Why Heterogeneous?

[[Moore's Law and Dennard Scaling|Dennard scaling's breakdown]] made it impossible to keep improving single-processor performance. The solution: route each type of computation to the processor that handles it most efficiently.

## CPU vs GPU: Complementary Strengths

| Property | CPU | GPU |
|---------|-----|-----|
| Core count | 8–128 high-complexity cores | 1,000–18,000 simple cores |
| Execution model | Out-of-order, speculative | In-order, SIMD (32–64 threads per warp) |
| Frequency | 3–5+ GHz | 1–2.5 GHz |
| Cache | Large (L3: 16–128 MB) | Small per SM (~64–192 KB shared) |
| Memory | Low-bandwidth DRAM (50–100 GB/s) | High-bandwidth HBM/GDDR (900 GB/s–4 TB/s) |
| Latency | Low (optimized to minimize wait) | High tolerance for latency |
| Best for | Serial code, OS, branchy logic | Parallel data-parallel code, matrix math |

CPUs are **latency-optimized**: large caches and OOO execution minimize wait time for each individual instruction. GPUs are **throughput-optimized**: tolerate high per-thread latency by switching to another thread while waiting, keeping thousands of cores busy.

## The Heterogeneous Execution Model

A typical CPU+GPU application:

1. **CPU (host)** runs the OS, manages memory, controls program flow, handles I/O
2. CPU identifies a **data-parallel section** (matrix multiply, image processing, neural network layer)
3. CPU **copies data** from system memory → GPU memory via PCIe (discrete GPU) or accesses shared pool (integrated/SoC)
4. CPU **launches a kernel** — a function that runs in parallel on thousands of GPU threads
5. GPU executes the kernel; CPU can do other work meanwhile
6. CPU **retrieves results** from GPU memory
7. Repeat

The PCIe transfer in step 3/6 is often the bottleneck for discrete GPUs — motivating unified memory architectures. See [[Unified Memory Architecture]].

## Task Allocation Strategy

- **Route to CPU**: sequential logic, OS system calls, complex branching, small datasets, low-latency responses
- **Route to GPU**: large matrix operations, image/video processing, neural network inference/training, physics simulation, any workload with massive data parallelism and simple per-element operations

## Heterogeneous System Architecture (HSA)

The **HSA Foundation** (AMD, ARM, Qualcomm) standardized APIs for CPU-GPU coherent shared memory access. HSA processors (AMD APUs, Apple Silicon) allow CPU and GPU to share the same memory address space — eliminating explicit copy operations.

Without HSA-style coherent memory, applications must manually manage two separate memory spaces (host + device) and explicitly transfer data. See [[CUDA Programming Model]].

## Modern Extensions

- **NPUs** (Neural Processing Units): dedicated matrix/convolution accelerators; present in Apple M-series, Qualcomm Snapdragon, AMD Ryzen AI — handle AI inference more efficiently than both CPU and GPU at low power
- **CXL** (Compute Express Link): coherent memory fabric allowing CPU-GPU-accelerator shared memory at datacenter scale
- **NVLink**: NVIDIA's proprietary high-bandwidth GPU-to-GPU interconnect for training clusters. See [[GPU Interconnects]].
