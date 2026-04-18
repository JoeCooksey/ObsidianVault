---
type: entity
title: "llama.cpp"
created: 2026-04-18
updated: 2026-04-18
tags:
  - entity
  - domain/engineering
  - inference
  - llm
status: developing
entity_type: product
role: Cross-platform C/C++ LLM inference engine with GGUF quantization support
first_mentioned: "[[Research - LLM Quantization and Edge Hardware]]"
related:
  - "[[GGUF Format]]"
  - "[[MLC-LLM]]"
  - "[[Research - LLM Quantization and Edge Hardware]]"
sources:
  - "[[Framework Comparison Apple Silicon 2025]]"
---
# llama.cpp

llama.cpp is a C/C++ LLM inference engine by Georgi Gerganov. It is the most widely used framework for local and edge LLM deployment. Supports [[GGUF Format]] quantized models.

## Key Properties
- No external dependencies — pure C/C++
- Cross-platform: Linux, macOS, Windows, Android, iOS
- Hardware backends: CPU (ARM NEON + x86 AVX), Metal (Apple Silicon GPU), CUDA, Vulkan, OpenCL
- CPU+GPU hybrid inference for models exceeding VRAM
- Supports 1.5-bit through 8-bit quantization (GGUF)
- First-class Apple Silicon optimization (ARM NEON, Accelerate, Metal)

## Performance on Apple Silicon
From comparative study (arXiv 2511.05502):
- **"Highly efficient for lightweight single-stream use"**
- Loses to MLX on sustained throughput
- Loses to MLC-LLM on time-to-first-token
- Best choice for: minimal deployment, rapid prototyping, cross-platform portability

## Ecosystem
- Powers Ollama, LM Studio, Jan, and most consumer LLM apps
- Intel IPEX-LLM extends llama.cpp to Intel CPUs and iGPUs
- llm.npu: NPU extension for Qualcomm Hexagon, achieving 18–38× prefill speedup vs CPU

## Relevance for Edge
The de facto standard for edge LLM deployment. If a device can run any LLM, it almost certainly runs via llama.cpp or a derivative.
