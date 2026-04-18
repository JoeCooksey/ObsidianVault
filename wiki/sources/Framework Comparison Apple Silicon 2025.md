---
type: source
title: "Framework Comparison Apple Silicon 2025"
created: 2026-04-18
updated: 2026-04-18
tags:
  - source
  - llm
  - inference
  - benchmark
status: developing
source_type: paper
author: "Multiple authors"
date_published: "2025-11"
url: "https://arxiv.org/abs/2511.05502"
confidence: high
key_claims:
  - "MLX achieves highest sustained generation throughput on Apple Silicon"
  - "MLC-LLM delivers lowest TTFT for moderate prompt sizes"
  - "llama.cpp is best for lightweight single-stream use"
  - "Ollama prioritizes developer ergonomics but lags on throughput"
  - "PyTorch MPS is limited by memory constraints on large models"
related:
  - "[[llama.cpp]]"
  - "[[MLC-LLM]]"
  - "[[Research - LLM Quantization and Edge Hardware]]"
sources: []
---
# Production-Grade Local LLM Inference on Apple Silicon: A Comparative Study

arXiv:2511.05502 — Comparative benchmark of MLX, MLC-LLM, Ollama, llama.cpp, and PyTorch MPS.

## Test Setup
- Hardware: Mac Studio with M2 Ultra, 192 GB unified memory
- Model: Qwen-2.5 family
- Metrics: TTFT, throughput, latency percentiles, long-context behavior, quantization support, streaming

## Framework Rankings

| Framework | Best For | Weakness |
|-----------|---------|---------|
| MLX | Sustained throughput | Less feature-complete |
| MLC-LLM | Low TTFT, production batching | Smaller ecosystem |
| llama.cpp | Single-stream, prototyping, portability | Loses on throughput |
| Ollama | Developer ergonomics | Slowest throughput + TTFT |
| PyTorch MPS | Research | Memory limited, not production |

## Conclusion
Apple Silicon frameworks "still trail NVIDIA GPU-based systems such as vLLM in absolute performance" but are "rapidly maturing into viable, production-grade solutions for private, on-device LLM inference."
