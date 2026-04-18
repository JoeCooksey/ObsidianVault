---
type: entity
title: "MLC-LLM"
created: 2026-04-18
updated: 2026-04-18
tags:
  - entity
  - domain/engineering
  - inference
  - llm
status: developing
entity_type: product
role: Universal LLM deployment engine using ML compilation (TVM-based)
first_mentioned: "[[Research - LLM Quantization and Edge Hardware]]"
related:
  - "[[llama.cpp]]"
  - "[[Post-Training Quantization]]"
  - "[[Research - LLM Quantization and Edge Hardware]]"
sources:
  - "[[Framework Comparison Apple Silicon 2025]]"
---
# MLC-LLM

MLC LLM (Machine Learning Compilation for LLM) is a universal LLM deployment engine built on Apache TVM. It compiles model graphs for specific hardware targets, enabling optimized inference across diverse devices.

## Key Properties
- Hardware targets: iOS (Metal, Apple A-series), Android (OpenCL, Adreno/Mali), NVIDIA (CUDA), WebGPU
- Ahead-of-time compilation produces hardware-optimized kernels
- Supports batching and concurrency — most complete batching outside vLLM for Apple Silicon
- Backend: Apache TVM compiler stack

## Performance on Apple Silicon
From comparative study (arXiv 2511.05502):
- **Lowest time-to-first-token** for moderate prompt sizes
- Strong out-of-the-box inference features
- Best choice for: batching, concurrent requests, production deployment on Apple Silicon

## Comparison with llama.cpp
| Property | MLC-LLM | llama.cpp |
|----------|---------|-----------|
| Best for | Batching, production | Single-stream, prototyping |
| TTFT | Lowest | Higher |
| Portability | Good | Excellent |
| Ecosystem size | Smaller | Dominant |

## Relevance for Edge
Preferred for iOS app deployment and Android GPU inference. TVM compilation means the same model definition can target radically different hardware backends.
