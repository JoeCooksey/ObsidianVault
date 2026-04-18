---
type: concept
title: "Speculative Decoding"
created: 2026-04-18
updated: 2026-04-18
tags:
  - concept
  - domain/engineering
  - inference
  - llm
status: developing
complexity: advanced
domain: engineering
aliases: ["speculative sampling", "draft-then-verify", "Medusa", "EAGLE"]
related:
  - "[[Post-Training Quantization]]"
  - "[[llama.cpp]]"
  - "[[Research - LLM Quantization and Edge Hardware]]"
sources:
  - "[[Survey - Low-bit LLMs 2024]]"
---
# Speculative Decoding

Speculative decoding accelerates LLM inference by generating multiple draft tokens cheaply, then verifying them in parallel with the full model. It does not change output distribution — results are mathematically identical to standard decoding.

## Core Idea

Standard autoregressive decoding generates one token per forward pass. Speculative decoding:
1. A small "draft" model generates N candidate tokens cheaply
2. The large target model verifies all N tokens in a single forward pass
3. All accepted tokens are kept; generation resumes from the first rejection

Net result: multiple tokens per effective forward pass of the large model, when draft quality is high.

## Key Methods

### Medusa
Adds multiple extra prediction heads to the target LLM. No separate draft model needed.
- Only the new heads are fine-tuned; the base model is frozen
- Achieves **2.2–3.6× speedup** over standard decoding
- Simple to integrate

### EAGLE (Extrapolation Algorithm for Greater Language-model Efficiency)
Extrapolates second-top-layer contextual features to predict next tokens. Three generations:

| Version | Venue | Key Improvement |
|---------|-------|-----------------|
| EAGLE-1 | ICML 2024 | Feature extrapolation baseline |
| EAGLE-2 | EMNLP 2024 | Dynamic draft trees via confidence-based acceptance rate approximation |
| EAGLE-3 | NeurIPS 2025 | Fuses low/mid/high semantic features; training-time test simulation |

EAGLE-2 achieves the highest speedup ratios across tested datasets and models.

### VSD (Variational Speculative Decoding)
Improves acceptance length ~9.6% over EAGLE-3. As of 2025, state of the art.

### PEARL (Parallel Speculative Decoding with Adaptive Draft Length)
ICLR 2025. Parallelizes the draft and verify phases further.

## Edge Relevance

Speculative decoding is most effective when the target model is compute-bound (GPU). On memory-bandwidth-bound edge devices (NPUs, mobile), the benefit may be reduced. The draft model must also fit alongside the target model in limited edge RAM.

> [!gap] Limited benchmarks on speculative decoding specifically targeting edge NPU deployments. Most results are from server GPU settings.
