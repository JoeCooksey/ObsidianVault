---
type: entity
title: "BitNet"
created: 2026-04-18
updated: 2026-04-18
tags:
  - entity
  - domain/engineering
  - quantization
  - llm
status: developing
entity_type: product
role: 1-bit and ternary LLM architecture and inference framework by Microsoft Research
first_mentioned: "[[Research - LLM Quantization and Edge Hardware]]"
related:
  - "[[Post-Training Quantization]]"
  - "[[Research - LLM Quantization and Edge Hardware]]"
sources:
  - "[[Bitnet.cpp Edge Inference 2025]]"
---
# BitNet

BitNet is Microsoft Research's architecture and inference framework for 1-bit and ternary (1.58-bit) large language models. It represents the extreme end of weight quantization.

## Architecture: BitNet b1.58

- Weights take only three values: **{-1, 0, +1}** (ternary = 1.58 bits per weight)
- Training from scratch with ternary-aware optimization (not post-training quantization)
- Eliminates floating-point multiply-accumulate operations — uses only additions
- Models trained as BitNet from scratch, not converted from FP16

## Inference Framework: bitnet.cpp

Official inference runtime for 1-bit LLMs. Released October 2024 (v1.0), February 2025 (with edge focus).

### Performance vs FP16 (ARM CPU)
- Speedup: **1.37×–5.07×** (larger models see greater gains)
- Energy reduction: **55.4%–70.0%**

### Performance vs FP16 (x86 CPU)
- Speedup: **2.37×–6.17×**
- Energy reduction: **71.9%–82.2%**

### Scale Capability
- Can run a **100B parameter** BitNet b1.58 model on a **single CPU** at 5–7 tokens/second (human reading speed)

## BitNet a4.8 (November 2024)
Extends BitNet with 4-bit activations alongside 1-bit weights. Enables INT4 compute units on hardware with native INT4 support.

## Status
- NPU support: listed as "coming next" as of early 2025
- GPU support: in development
- Primary target: CPU-based edge inference without GPU/NPU

## Significance
BitNet challenges the assumption that high-quality LLMs require floating-point weights. If ternary models can match FP16 quality (at sufficient scale), edge deployment becomes fundamentally cheaper.

> [!gap] BitNet models require training from scratch. No standard FP16 model can be converted to BitNet b1.58. Adoption depends on availability of pre-trained BitNet models.
