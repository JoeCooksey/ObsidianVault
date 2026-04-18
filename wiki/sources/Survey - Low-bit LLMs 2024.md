---
type: source
title: "Survey - Low-bit LLMs 2024"
created: 2026-04-18
updated: 2026-04-18
tags:
  - source
  - quantization
  - llm
status: developing
source_type: paper
author: "Multiple authors"
date_published: "2024-09"
url: "https://arxiv.org/html/2409.16694v1"
confidence: high
key_claims:
  - "GPTQ and AWQ dominate across frameworks; AWQ consistently outperforms GPTQ on accuracy"
  - "Bit-width reduction alone does not guarantee inference speedup without hardware support"
  - "Weight-only quantization works at arbitrary bit-widths; W&A quantization is constrained by hardware instruction sets"
  - "HQQ achieves calibration-free quantization in minutes"
  - "FP8 is essentially lossless; INT8 W&A shows only 1-3% accuracy degradation"
related:
  - "[[Post-Training Quantization]]"
  - "[[GGUF Format]]"
  - "[[BitNet]]"
sources: []
---
# Survey: A Survey of Low-bit Large Language Models: Basics, Systems, and Algorithms

arXiv:2409.16694 — Comprehensive survey of quantization techniques for LLMs.

## Key Contributions

- Taxonomizes quantization into weight-only, weight+activation (W&A), and KV cache categories
- Documents hardware compatibility constraints for each precision level
- Surveys GPTQ, AWQ, SmoothQuant, HQQ, and emerging formats (NF4, Flint, Abfloat)
- Identifies practical limitation: bit-width reduction ≠ inference speedup without kernel support

## Notable Data Points

- FP16 LLaMA 3-8B on H100: 135 tok/s → INT8: 158 tok/s → INT4: 211 tok/s
- Gemma 3 27B: BF16 = 54 GB → INT4 = 14.1 GB
- AWQ outperforms GPTQ on ARC-c and GSM8K benchmarks

## What It Covers

NVIDIA GPU focus; limited AMD/edge coverage. Strong on algorithmic details, weaker on deployment frameworks.
