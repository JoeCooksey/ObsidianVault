---
type: concept
title: "Knowledge Distillation for Edge LLMs"
created: 2026-04-18
updated: 2026-04-18
tags:
  - concept
  - domain/engineering
  - compression
  - llm
status: developing
complexity: intermediate
domain: engineering
aliases: ["KD", "small language models", "SLMs"]
related:
  - "[[Post-Training Quantization]]"
  - "[[LLM Pruning]]"
  - "[[Research - LLM Quantization and Edge Hardware]]"
sources:
  - "[[Survey - Low-bit LLMs 2024]]"
---
# Knowledge Distillation for Edge LLMs

Knowledge distillation (KD) trains a small "student" model to replicate the behavior of a large "teacher" model. The result is a smaller model that punches above its parameter count, making it the preferred approach for edge deployment when model architecture can be chosen.

## Two Approaches

### White-box KD
Student has access to teacher's internal activations, logits, and intermediate representations. Richer signal; requires open-weight teacher.

### Black-box KD
Student learns only from teacher's outputs (predictions, completions). Works with proprietary models (GPT-4o, Claude 3.5, Gemini 1.5). Techniques: in-context learning, chain-of-thought, instruction following.

Black-box KD is widely adopted because most powerful teachers are proprietary.

## Notable Edge-Oriented Models (2024-2025)

| Model | Params | Notes |
|-------|--------|-------|
| Phi-3-mini | 3.8B | Rivals Mixtral 8x7B and GPT-3.5; locally deployable on phones |
| Gemma 3 1B | 1B | Google; designed for mobile deployment |
| Qwen3 0.6B / 1.7B | 0.6-1.7B | Strong reasoning at minimal size |
| Llama 3.2 1B / 3B | 1-3B | Meta; distilled from Llama 3.1 70B/405B |
| MiniCPM4 0.5B | 0.5B | Sub-1B with competitive benchmarks |
| MobileLLM | varies | Systematic depth/width exploration for constrained devices |

## Architecture Insights for Edge

- **Depth over width**: Deeper narrow models outperform shallow wide models at same parameter count (MobileLLM finding)
- **Grouped-query attention (GQA)**: Reduces KV cache memory — critical for edge where RAM is tight
- **Sliding window attention**: Limits context length memory growth for long-context edge scenarios

## Strong-to-Weak Distillation

Emerging approach: distill from a reasoning model (e.g., DeepSeek-R1) into a smaller model. Edge-side models using this approach outperform same-size baselines trained without it.

## Comparison with Quantization

KD produces a fundamentally smaller model. Quantization compresses an existing model.

Best practice: train/select a small model via KD first, then quantize it. Combining both achieves the highest compression.
