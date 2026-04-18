---
type: concept
title: "GPU Interconnects"
created: 2026-04-18
updated: 2026-04-18
tags:
  - gpu
  - computer-architecture
  - networking
  - ai-infrastructure
status: developing
related:
  - "[[GPU Architecture Evolution]]"
  - "[[Heterogeneous Computing]]"
  - "[[NVIDIA]]"
  - "[[CPU Architecture Evolution]]"
sources: []
---

# GPU Interconnects

The communication links between CPU and GPU (or between multiple GPUs) are a critical bottleneck in heterogeneous computing. Higher bandwidth = faster data movement = better utilization of compute.

## PCIe (PCI Express)

The standard CPU-to-GPU interface for discrete graphics cards. Present in every desktop/server with a discrete GPU.

| Generation | Bandwidth (x16 slot) | Year Common |
|-----------|---------------------|------------|
| PCIe 3.0 | ~16 GB/s | 2011 |
| PCIe 4.0 | ~32 GB/s | 2019 |
| PCIe 5.0 | ~64 GB/s | 2022 |
| PCIe 6.0 | ~128 GB/s | 2025 (server) |

PCIe is the bottleneck for large data transfers between CPU RAM and GPU VRAM. An H100 GPU has ~2 TB/s HBM bandwidth internally — PCIe 5.0 at 64 GB/s is ~30× slower, making data movement the limiting factor for memory-bound workloads.

## NVLink (NVIDIA)

Proprietary GPU-to-GPU (and GPU-to-CPU) interconnect developed by NVIDIA. Used in multi-GPU server nodes.

| Generation | Bandwidth per GPU | GPU | Year |
|-----------|------------------|-----|------|
| NVLink 1 | 160 GB/s | P100 | 2016 |
| NVLink 2 | 300 GB/s | V100 | 2017 |
| NVLink 3 | 600 GB/s | A100 | 2020 |
| NVLink 4 | 900 GB/s | H100 | 2022 |
| NVLink 5 | 1,800 GB/s | B100/B200 | 2024 |

NVLink 5 on Blackwell provides **~14× the bandwidth of PCIe Gen5 x16**. For AI training, this means gradient synchronization across GPUs is no longer bottlenecked by interconnect — enabling efficient 100B+ parameter model training across GPU clusters.

**NVSwitch**: NVIDIA's switch chip that connects multiple NVLink GPUs in an all-to-all fabric within a node (e.g., 8× H100 GPUs in a DGX H100 each connected to all others at full NVLink bandwidth).

## CXL (Compute Express Link)

An open standard (Intel-led consortium) built on top of PCIe physical layer. Provides **cache-coherent memory access** between CPUs and accelerators/memory expanders.

Use cases:
- **Memory pooling**: attach external memory banks shared coherently across CPUs and GPUs
- **Memory expansion**: add more DRAM to a server than fits in CPU sockets
- **Accelerator coherency**: GPU can access CPU memory with cache coherency, eliminating explicit copy operations

CXL 4.0 (November 2025): 128 GT/s, up to 1.5 TB/s via bundled ports.

> [!note] CXL vs NVLink
> CXL targets memory coherency and capacity expansion; NVLink targets raw GPU-to-GPU bandwidth for training. They solve different problems. CXL is vendor-neutral; NVLink is NVIDIA-proprietary. For 2025 AI training workloads, NVLink is the only production-ready high-bandwidth option.

## UALink

An industry consortium alternative to NVLink for GPU-to-GPU interconnect — AMD, Intel, Qualcomm, Broadcom, Google, Meta, Microsoft. Published specification in 2024. No production silicon yet as of early 2026.

## Interconnect Hierarchy Summary

```
Within a GPU:           HBM / GDDR memory  ~1–4 TB/s
GPU-to-GPU (NVLink 5):                     1.8 TB/s
GPU-to-GPU (UALink):            TBD (targeting NVLink parity)
CPU-to-GPU (PCIe 5.0 x16):                64 GB/s
CPU-to-memory expansion (CXL 4):          up to 1.5 TB/s
CPU-to-GPU (PCIe 6.0 x16):               128 GB/s
```
