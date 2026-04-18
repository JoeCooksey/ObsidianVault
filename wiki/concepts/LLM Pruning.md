---
type: concept
title: "LLM Pruning"
created: 2026-04-18
updated: 2026-04-18
tags:
  - concept
  - domain/engineering
  - compression
  - llm
status: developing
complexity: advanced
domain: engineering
aliases: ["model pruning", "sparsity", "SparseGPT", "Wanda"]
related:
  - "[[Post-Training Quantization]]"
  - "[[Knowledge Distillation for Edge LLMs]]"
  - "[[Research - LLM Quantization and Edge Hardware]]"
sources:
  - "[[Survey - Low-bit LLMs 2024]]"
---
# LLM Pruning

Pruning removes weights from a trained LLM to reduce model size and inference cost. Unlike quantization (which reduces precision), pruning induces sparsity — some weights become exactly zero.

## Sparsity Types

### Unstructured Sparsity
Any individual weight can be zeroed. Maximum flexibility but requires sparse kernels to realize speedups — standard dense MatMul ignores zeros.

### Structured Sparsity (N:M)
At most N out of every M contiguous weights are non-zero. NVIDIA's sparse tensor cores accelerate 2:4 structured sparsity (2 non-zeros per 4 weights = 50% sparsity) with no kernel changes.

## Key Methods

### SparseGPT
One-shot post-training pruning. Solves a layer-wise weight reconstruction problem derived from Optimal Brain Surgeon (OBS). Supports both unstructured and N:M structured sparsity.

- At 50% unstructured sparsity: near-lossless on large models
- Stronger than Wanda on 2:4 sparsity for small models (7B range)

### Wanda (Weights and Activations)
Prunes weights with the smallest magnitude × input activation product, per output neuron.

- **No retraining or weight updates required** — pruned model used directly
- On par with SparseGPT for 50% unstructured sparsity
- Outperforms SparseGPT on large models (30B+) for 2:4 sparsity
- Extended to N:M structured sparsity

### Recent Developments (2024-2025)
- **Wanda++**: Regional pruning improvements
- **M-Wanda**: Multilingual LLM adaptation
- **DuoGPT**: Dual sparsity via activation-aware pruning
- **OWL**: Outlier Weighed Layerwise Sparsity

## Pruning vs Quantization

| Property | Pruning | Quantization |
|----------|---------|--------------|
| Mechanism | Zero-out weights | Reduce precision |
| Memory gain | Requires sparse storage | Direct reduction |
| Hardware support | N:M needs NVIDIA | INT8/FP8 widely supported |
| Accuracy impact | Higher at same compression | Lower at same compression |
| Common combo | Both applied together | Often standalone |

## Edge Relevance

Structured N:M pruning paired with quantization (e.g., 50% sparsity + INT4) can achieve 8–16× compression ratios. However, edge NPUs often lack sparse acceleration, making quantization more practical for non-NVIDIA edge hardware.
