---
type: synthesis
title: "Research: LLM Quantization and Optimization for Edge Hardware"
created: 2026-04-18
updated: 2026-04-18
tags:
  - research
  - domain/engineering
  - quantization
  - llm
  - edge
status: developing
related:
  - "[[Post-Training Quantization]]"
  - "[[GGUF Format]]"
  - "[[LLM Pruning]]"
  - "[[Knowledge Distillation for Edge LLMs]]"
  - "[[Speculative Decoding]]"
  - "[[BitNet]]"
  - "[[llama.cpp]]"
  - "[[MLC-LLM]]"
  - "[[Survey - Low-bit LLMs 2024]]"
  - "[[Edge LLM Inference Benchmark 2026]]"
  - "[[Framework Comparison Apple Silicon 2025]]"
  - "[[Bitnet.cpp Edge Inference 2025]]"
sources:
  - "[[Survey - Low-bit LLMs 2024]]"
  - "[[Edge LLM Inference Benchmark 2026]]"
  - "[[Framework Comparison Apple Silicon 2025]]"
  - "[[Bitnet.cpp Edge Inference 2025]]"
---
# Research: LLM Quantization and Optimization for Edge Hardware

## Overview

Running LLMs on edge hardware (mobile SoCs, NPUs, embedded accelerators) requires aggressive compression. The field has converged on a toolkit of four techniques — quantization, pruning, distillation, and speculative decoding — each attacking a different constraint. As of 2025–2026, 3–8B parameter models run comfortably on flagship smartphones; 100B models can run on CPUs using ternary weights. The primary remaining bottleneck is thermal management on mobile, not computational throughput.

---

## Key Findings

1. **INT4 weight-only quantization is the practical sweet spot** for edge deployment. It halves memory vs INT8 with minimal accuracy loss and requires no specialized hardware. [[GGUF Format]] Q4_K_M is the recommended default. (Source: [[Survey - Low-bit LLMs 2024]])

2. **AWQ consistently outperforms GPTQ** on accuracy at equivalent compression. For any new deployment, prefer AWQ unless toolchain constraints require GPTQ. (Source: [[Survey - Low-bit LLMs 2024]])

3. **Thermal throttling is the dominant mobile performance limiter** — not raw TOPS. iPhone 16 Pro loses 44% throughput within 2 inference iterations. S24 Ultra hits a hard OS frequency floor at iteration 6. TOPS numbers in marketing materials are misleading for sustained inference. (Source: [[Edge LLM Inference Benchmark 2026]])

4. **The RPi 5 + Hailo-10H NPU is the most energy-efficient platform** for always-on agents: 1.87W system power, 270.5 mJ/token, 0.04% throughput variance. The RTX 4050 achieves 131.7 tok/s but requires AC power. (Source: [[Edge LLM Inference Benchmark 2026]])

5. **BitNet b1.58 (ternary weights) achieves 2.4–6× CPU speedup** and 55–82% energy reduction vs FP16 — on CPU, with no GPU needed. Can run a 100B model on a single CPU. Limitation: requires training from scratch; no FP16 conversion path. (Source: [[Bitnet.cpp Edge Inference 2025]])

6. **Framework choice matters as much as quantization method.** On Apple Silicon: MLX wins on throughput, MLC-LLM wins on latency, llama.cpp is best for portability and prototyping. (Source: [[Framework Comparison Apple Silicon 2025]])

7. **Bit-width reduction alone does not guarantee speedup.** Hardware instruction support, kernel optimization, and memory hierarchy alignment are all required. A 4-bit model may be no faster than FP16 without matching kernel support. (Source: [[Survey - Low-bit LLMs 2024]])

8. **Small models trained with knowledge distillation punch above their weight.** Phi-3-mini (3.8B) rivals GPT-3.5. Qwen3 0.6B achieves competitive benchmarks at sub-1B scale. Combining KD + quantization is the highest-compression path. (Source: [[Knowledge Distillation for Edge LLMs]])

---

## Key Entities

- [[BitNet]]: Microsoft Research's ternary LLM architecture and bitnet.cpp inference framework
- [[llama.cpp]]: Dominant C/C++ edge inference engine; de facto standard for local LLMs
- [[MLC-LLM]]: TVM-based universal deployment engine; best for batching on Apple Silicon and Android

---

## Key Concepts

- [[Post-Training Quantization]]: Primary compression technique; INT4 is practical sweet spot
- [[GGUF Format]]: llama.cpp's quantization file format; Q4_K_M recommended
- [[LLM Pruning]]: Structured (N:M) and unstructured sparsity; SparseGPT and Wanda are key methods
- [[Knowledge Distillation for Edge LLMs]]: Train small student models from large teachers; combine with quantization
- [[Speculative Decoding]]: EAGLE-2/3 and Medusa provide 2–3.6× decoding speedup on compute-bound hardware

---

## Contradictions

- [[Edge LLM Inference Benchmark 2026]] shows NPU energy efficiency (Hailo-10H) matches GPU at 19× lower throughput — suggesting NPUs are architecturally efficient per-token. However, [[Survey - Low-bit LLMs 2024]] notes NVIDIA GPU ecosystem dominates and edge hardware support is limited. These findings are consistent: NPUs are efficient but the software stack is immature.

- Marketing claims for mobile NPU TOPS (e.g., Qualcomm's 98% performance improvement claims) are contradicted by [[Edge LLM Inference Benchmark 2026]], which shows actual sustained inference on S24 Ultra is bottlenecked by thermal, not TOPS. Treat TOPS numbers as low confidence for sustained workloads.

---

## Open Questions

1. At what model size and quantization level does BitNet b1.58 match FP16 quality? Current results show competitive accuracy but systematic quality evaluation across task types is incomplete.

2. Can speculative decoding methods (EAGLE, Medusa) provide meaningful speedup on NPU hardware, where memory bandwidth rather than compute is typically the bottleneck?

3. What is the practical floor for edge LLM quality? Sub-1B models (MiniCPM4 0.5B, Qwen3 0.6B) exist, but at what parameter count does useful reasoning capability collapse?

4. How do the 2025 Snapdragon 8 Gen 4 and Apple A19 Pro NPU improvements compare in real sustained inference (not peak TOPS)?

5. Does structured N:M pruning (2:4 sparsity) provide additive gains over INT4 quantization on NVIDIA edge GPUs (RTX 4050)?

---

## Sources

- [[Survey - Low-bit LLMs 2024]]: arXiv 2409.16694, comprehensive quantization survey
- [[Edge LLM Inference Benchmark 2026]]: arXiv 2603.23640, sustained-load hardware benchmarks
- [[Framework Comparison Apple Silicon 2025]]: arXiv 2511.05502, MLX/MLC-LLM/llama.cpp comparison
- [[Bitnet.cpp Edge Inference 2025]]: arXiv 2502.11880, ternary LLM CPU inference
