---
type: meta
title: "Hot Cache"
updated: 2026-04-18T00:00:00
tags:
  - meta
---
# Recent Context

## Last Updated
2026-04-18 — Autoresearch: Evolution of CPUs and GPUs

## Key Recent Facts

### CPU / GPU Architecture (newest)
- **CPU performance scaling broke ~2005** — Dennard scaling failed; clock frequencies stalled at 4–6 GHz; forced transition to multi-core and then heterogeneous SoC
- **CPU is latency-optimized; GPU is throughput-optimized** — CPUs: OOO execution, large caches, low latency per instruction. GPUs: SIMD, thousands of simple cores, high throughput via warp switching
- **GPU evolution in 6 eras**: fixed-function (1999) → programmable shaders (2000) → unified architecture (2006) → compute shaders (2009) → low-level APIs (2015) → general computing engine (2020)
- **CUDA (2007)** unlocked GPGPU; enabled deep learning revolution; NVIDIA's primary competitive moat
- **PCIe Gen5 x16 = ~64 GB/s** — 30× slower than H100 HBM2e (2 TB/s); the CPU↔GPU data transfer bottleneck
- **NVLink 5 (Blackwell 2024) = 1.8 TB/s** — ~14× PCIe Gen5; reason NVIDIA dominates AI training clusters
- **Unified memory (Apple M5 Max at 614 GB/s, AMD Ryzen AI Max+ at 128 GB pool)** — eliminates PCIe bottleneck for inference; can serve 70B models locally
- **GPU performance historically grew 2.5×/year** (1970s–1999), exceeding Moore's Law 1.8×

### Habits / Neuroscience (previous)
- Limbic friction, task bracketing, three-phase day framework, 21-day system — see [[Huberman Lab Essentials - Habit Formation and Breaking]]

### Health / Supplements (previous)
- Creatine, caffeine+L-theanine, vitamin D deficiency — see [[Research - Supplements for Young Male Health and Learning]]

## Recent Changes
- Created: [[SIGGRAPH - Eras of GPU Development 2025]], [[Intel]], [[AMD]], [[NVIDIA]]
- Created: [[CPU Architecture Evolution]], [[GPU Architecture Evolution]], [[Moore's Law and Dennard Scaling]], [[Heterogeneous Computing]], [[CUDA Programming Model]], [[GPU Interconnects]], [[Unified Memory Architecture]]
- Created: [[Research - Evolution of CPUs and GPUs]] (synthesis)
- Updated: [[Wiki Index]], [[Wiki Log]]

## Active Threads
- CPU/GPU architecture: fully researched and filed
- Cross-domain connection: [[CUDA Programming Model]] + [[Post-Training Quantization]] — quantized LLMs run on GPU via CUDA; edge inference (llama.cpp) uses CPU with limited CUDA offload
- Cross-domain connection: [[Unified Memory Architecture]] links to edge LLM inference (Apple Silicon M-series is currently best consumer edge LLM platform)
- Personal context: 19-year-old male EE student
- Open: RISC-V MIMD GPU future; NVLink scaling ceiling; NPU vs GPU for transformer inference
