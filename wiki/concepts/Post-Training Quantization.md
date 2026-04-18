---
type: concept
title: "Post-Training Quantization"
created: 2026-04-18
updated: 2026-04-18
tags:
  - concept
  - domain/engineering
  - quantization
  - llm
status: developing
complexity: advanced
domain: engineering
aliases: ["PTQ", "LLM quantization"]
related:
  - "[[GGUF Format]]"
  - "[[BitNet]]"
  - "[[LLM Pruning]]"
  - "[[Research - LLM Quantization and Edge Hardware]]"
sources:
  - "[[Survey - Low-bit LLMs 2024]]"
  - "[[Edge LLM Inference Benchmark 2026]]"
---
# Post-Training Quantization

Quantization reduces a trained model's weight and/or activation precision from FP16/BF16 to lower bit-widths (INT8, INT4, INT2) without retraining. It is the primary technique for fitting LLMs onto edge hardware.

## Three Categories

### 1. Weight-Only Quantization
Weights quantized; activations remain FP16. Dequantization happens before MatMul.

- Enables arbitrary bit-widths (2–8 bit) since no hardware instruction constraints
- Reduces memory footprint and memory bandwidth bottleneck
- Does not require specialized hardware support — works on any device
- Examples: GPTQ, AWQ, GGUF formats

### 2. Weight + Activation (W&A) Quantization
Both weights and activations quantized. Actual compute in low precision.

- Greater acceleration than weight-only, but requires hardware INT8/FP8 MatMul support
- Viable only when compute savings exceed runtime quantization overhead
- Static (calibration required, faster) vs dynamic (no calibration, overhead at runtime)
- Examples: SmoothQuant (W8A8), FP8 on NVIDIA H100/RTX 50-series

### 3. KV Cache Quantization
Quantizes the key-value attention cache. Supports 2–8 bit. Most frameworks default to FP16.

## Key Methods

### GPTQ
Second-order post-training quantization. Solves a layer-wise weight reconstruction problem. Practical and scalable. Integrated into TensorRT-LLM, vLLM, Transformers.

### AWQ (Activation-Aware Weight Quantization)
Per-channel weight scaling guided by activation statistics. Consistently outperforms GPTQ in accuracy, especially on reasoning tasks (ARC-c, GSM8K). Widely used.

### SmoothQuant
Addresses outlier activations via mathematically equivalent transformations that shift quantization difficulty from activations to weights. Enables W8A8 INT8.

### HQQ (Half-Quadratic Quantization)
Calibration-free. Completes in minutes vs hours for GPTQ/AWQ. Useful for rapid experimentation.

## Accuracy vs Compression Trade-offs

| Format | Bits | Memory (7B model) | Accuracy Loss |
|--------|------|-------------------|---------------|
| FP16 | 16 | ~14 GB | baseline |
| INT8 (W8A8) | 8 | ~7 GB | ~1-3% |
| INT4 (W4A16) | 4 | ~3.5 GB | competitive with INT8 |
| INT2 | 2 | ~1.75 GB | significant degradation |

Example: Gemma 3 27B in BF16 = 54 GB; INT4 = 14.1 GB (Source: [[Survey - Low-bit LLMs 2024]])

LLaMA 3-8B throughput on H100: FP16 = 135 tok/s → INT8 = 158 tok/s → INT4 = 211 tok/s

## Critical Insight

> [!key-insight] Bit-width reduction alone is insufficient
> Some quantization methods reduce bit-width but do not accelerate inference. Actual speedup requires hardware instruction support, optimized kernels, and synchronized memory hierarchy support. (Source: [[Survey - Low-bit LLMs 2024]])

## Emerging Formats

- **FP8**: Essentially lossless. Natively supported on NVIDIA H100, RTX 50-series. Best accuracy at sub-FP16.
- **MXFP4**: NVIDIA RTX 50-series only. E2M1 format, symmetric per-group quantization (group size 32).
- **NormalFloat (NF4)**: Fixed FP format for weight-only scenarios assuming normal weight distributions.
