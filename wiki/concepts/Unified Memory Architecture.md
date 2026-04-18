---
type: concept
title: "Unified Memory Architecture"
created: 2026-04-18
updated: 2026-04-18
tags:
  - computer-architecture
  - cpu
  - gpu
  - soc
  - apple-silicon
status: developing
related:
  - "[[Heterogeneous Computing]]"
  - "[[GPU Interconnects]]"
  - "[[CPU Architecture Evolution]]"
  - "[[AMD]]"
sources: []
---

# Unified Memory Architecture

A chip design where CPU, GPU, and other processors share a **single physical memory pool** on the same package, eliminating PCIe data copies and providing all processors with equal-latency access to the same data.

## The Traditional Discrete GPU Problem

In a system with a discrete GPU, CPU and GPU have **separate memory spaces**:
- CPU uses system RAM (DDR5, ~50–100 GB/s bandwidth)
- GPU uses on-card VRAM (GDDR6X/HBM, 600 GB/s – 4 TB/s)
- Data transfers between them cross PCIe (~64 GB/s for Gen5) — the bottleneck

For AI inference with large models (70B+ parameters), the model weights must reside in GPU VRAM. Consumer GPUs (8–24 GB VRAM) cannot fit them. Copies to/from system RAM across PCIe are too slow.

## Unified Memory: The Solution

**On-package unified memory** means CPU and GPU share the same DRAM pool accessible at full memory bus bandwidth — no PCIe in the path.

### Apple Silicon (M-series)

Apple Silicon is the most advanced consumer implementation:

| Chip | Unified Memory BW | Max RAM |
|------|------------------|---------|
| M1 (2020) | 68 GB/s | 16 GB |
| M2 Max (2022) | 400 GB/s | 96 GB |
| M4 (2024) | ~120 GB/s | 32 GB |
| M5 (2025) | 153 GB/s (base) / 614 GB/s (Max) | 128 GB |

CPU, GPU, and Neural Engine all access the same pool. No copy operations. For a 70B parameter LLM (requiring ~40 GB in Q4 quantization), an M5 Max with 128 GB can serve it at usable inference speeds — something no consumer discrete-GPU system can match at equivalent power. (Source: search results, memory bandwidth data)

### AMD APU (Ryzen AI Max+ 395, 2025)

AMD's Ryzen AI Max+ 395 brings the same concept to x86:
- Integrated RDNA GPU + Zen 5 CPU on same die
- Up to 128 GB unified memory pool
- Targets local AI inference workloads that previously required a discrete GPU + large VRAM

### Traditional APUs (Intel iGPU, AMD iGPU)

Standard laptop integrated graphics have shared memory but at **lower bandwidth** (DDR5 system RAM, ~50–100 GB/s) — insufficient for high-throughput GPU workloads. Apple Silicon and AMD Ryzen AI Max solve this with purpose-built high-bandwidth on-package memory (LPDDR5X or similar).

## Trade-offs vs Discrete GPU

| Factor | Unified Memory (Apple M5 Max) | Discrete GPU (RTX 4090) |
|--------|------------------------------|------------------------|
| GPU compute TFLOPS | ~10–15 TFLOPS FP32 | ~82 TFLOPS FP32 |
| Memory bandwidth | 614 GB/s | 1,008 GB/s |
| Max memory | 128 GB shared | 24 GB VRAM |
| CPU-GPU transfer cost | Zero (shared) | PCIe bottleneck |
| Power | ~60–100W (entire SoC) | 450W (GPU alone) |
| Best for | Large model inference, memory-bound AI | Compute-bound training, gaming |

Unified memory wins on **memory capacity and power efficiency**; discrete GPU wins on raw **compute throughput** for training.

## Engineering Relevance

For EE/embedded contexts: SoC designs for edge AI (phones, laptops, automotive) universally use unified memory. The cost of PCIe transfer overhead in discrete GPU systems makes them impractical at the power budgets (<5W) required for edge deployment. See [[Heterogeneous Computing]].
