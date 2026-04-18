---
type: source
title: "Bitnet.cpp Edge Inference 2025"
created: 2026-04-18
updated: 2026-04-18
tags:
  - source
  - quantization
  - llm
  - edge
status: developing
source_type: paper
author: "Microsoft Research"
date_published: "2025-02"
url: "https://arxiv.org/pdf/2502.11880"
confidence: high
key_claims:
  - "ARM CPU speedup: 1.37×–5.07× vs FP16; energy reduction 55.4%–70.0%"
  - "x86 CPU speedup: 2.37×–6.17× vs FP16; energy reduction 71.9%–82.2%"
  - "100B BitNet b1.58 runs on a single CPU at 5-7 tokens/sec (human reading speed)"
  - "NPU support listed as coming next; GPU support in development"
related:
  - "[[BitNet]]"
  - "[[Post-Training Quantization]]"
sources: []
---
# Bitnet.cpp: Efficient Edge Inference for Ternary LLMs

arXiv:2502.11880 — Official framework paper for bitnet.cpp, Microsoft's CPU inference runtime for 1-bit LLMs.

## Key Result
Ternary (1.58-bit) LLMs achieve dramatic CPU speedups while maintaining quality. The result challenges the assumption that edge LLM deployment requires GPU/NPU acceleration.

## Limitation
BitNet b1.58 models must be trained from scratch using the BitNet training recipe. No conversion path from existing FP16 models exists.
