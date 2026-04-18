---
type: source
title: "Edge LLM Inference Benchmark 2026"
created: 2026-04-18
updated: 2026-04-18
tags:
  - source
  - edge
  - llm
  - benchmark
status: developing
source_type: paper
author: "Multiple authors"
date_published: "2026-03"
url: "https://arxiv.org/html/2603.23640v1"
confidence: high
key_claims:
  - "Thermal throttling is the primary performance limiter on mobile — not raw TOPS"
  - "iPhone 16 Pro loses 44% throughput within 2 inference iterations due to thermal"
  - "RPi 5 + Hailo-10H NPU achieves lowest energy per token (270.5 mJ) at only 1.87W system power"
  - "RTX 4050 laptop GPU achieves highest throughput (131.7 tok/s) but requires AC power"
  - "Hailo-10H achieves 0.04% throughput variance; iPhone achieves 20.8%"
related:
  - "[[Post-Training Quantization]]"
  - "[[Research - LLM Quantization and Edge Hardware]]"
sources: []
---
# Edge LLM Inference Benchmark 2026

arXiv:2603.23640 — Empirical benchmark of LLM inference across edge platforms under sustained load.

## Test Setup
- Model: Qwen 2.5 1.5B, 4-bit quantized
- Platforms: RPi 5 + Hailo-10H NPU, Samsung Galaxy S24 Ultra, iPhone 16 Pro, NVIDIA RTX 4050 laptop

## Results Table

| Platform | Throughput | System Power | Energy/Token | Stability |
|----------|-----------|-------------|--------------|-----------|
| RTX 4050 | **131.7 tok/s** | 34.1 W | 297.3 mJ | Battery-throttled |
| iPhone 16 Pro | 22.6 tok/s (hot) | N/A | N/A | 44% degradation, 2 iterations |
| S24 Ultra | 9.93 tok/s | N/A | N/A | Hard OS frequency floor at 6 iterations |
| RPi + Hailo-10H | 6.9 tok/s | **1.87 W** | **270.5 mJ** | 0.04% variance — most stable |

## Key Insight

> [!key-insight] Thermal throttling dominates mobile edge performance
> Raw NPU TOPS numbers are misleading. iPhone 16 Pro and S24 Ultra both suffer thermal collapse under sustained load. The RPi + Hailo-10H is the only platform that maintains stable sub-2W continuous operation indefinitely.

## Deployment Recommendations (from paper)
- **Always-on agents**: RPi + Hailo-10H (only viable <2W platform)
- **Intermittent queries**: iPhone 16 Pro (with thermal recovery between sessions)
- **AC-powered interactive**: RTX 4050
- **High-frequency agents**: Dedicated edge NPU only

## Limitations
Results are platform-level (hardware + software combined), single model, single prompt type. Framework choice (MLC-LLM vs MLX vs llama.cpp) significantly changes results.
