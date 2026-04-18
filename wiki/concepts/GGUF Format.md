---
type: concept
title: "GGUF Format"
created: 2026-04-18
updated: 2026-04-18
tags:
  - concept
  - domain/engineering
  - quantization
  - llm
status: developing
complexity: intermediate
domain: engineering
aliases: ["GGUF", "K-quants", "llama.cpp quantization"]
related:
  - "[[Post-Training Quantization]]"
  - "[[llama.cpp]]"
  - "[[Research - LLM Quantization and Edge Hardware]]"
sources:
  - "[[Survey - Low-bit LLMs 2024]]"
---
# GGUF Format

GGUF (GPT-Generated Unified Format) is the quantization file format used by [[llama.cpp]]. It is the dominant format for running LLMs locally on consumer hardware and edge devices.

## Two Format Families

### Legacy Integer Formats
Block-wise integer quantization. Simple, widely supported.

| Format | Bits | Notes |
|--------|------|-------|
| Q4_0 | 4 | Basic 4-bit, fast kernels |
| Q4_1 | 4 | Adds min value per block |
| Q5_0 / Q5_1 | 5 | Higher accuracy, larger |
| Q8_0 | 8 | Near-lossless, used as baseline |

### K-Quant Formats (Recommended)
Hierarchical super-block structure. Partitions weights into 256-value super-blocks with multiple scale/min parameters per sub-block. Higher quality at same bit-width.

| Format | Avg Bits | Size (7B) | Recommendation |
|--------|----------|-----------|----------------|
| Q2_K | ~2.67 | ~2.8 GB | Not recommended — quality loss |
| Q3_K_S/M/L | ~3.3 | ~3.3 GB | Aggressive compression |
| Q4_K_S | ~4.0 | ~4.1 GB | Fast, lower quality |
| Q4_K_M | ~4.1 | ~4.3 GB | **Recommended default** |
| Q5_K_S/M | ~5.0 | ~5.2 GB | Good accuracy |
| Q6_K | ~6.0 | ~6.2 GB | Near-lossless |
| Q8_0 | 8.0 | ~8.5 GB | Reference baseline |

**Suffix meaning:** _S = small (faster kernels), _M = medium (balanced), _L = large (best quality)

## Practical Guidance

- **Edge devices with <4 GB RAM**: Q2_K or Q3_K_S (with accuracy penalty)
- **General use / 4-8 GB RAM**: Q4_K_M — best quality-size tradeoff
- **Quality-sensitive tasks**: Q5_K_M or Q6_K
- **Benchmarking / reference**: Q8_0

## Related

See [[llama.cpp]] for the runtime that loads GGUF files. GGUF is also supported by Ollama, LM Studio, and Jan.
