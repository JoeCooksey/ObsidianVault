---
type: concept
title: "Linear Algebra for AI and Quant"
created: 2026-06-04
updated: 2026-06-04
tags:
  - concept
  - mathematics
  - ai
  - machine-learning
  - quant
status: developing
related:
  - "[[Research - Most Useful Topics to Learn Now (for Joe)]]"
  - "[[Mathematics]]"
  - "[[Calculus in Electrical Engineering]]"
  - "[[Quantitative Trading]]"
  - "[[Signals and Systems — Laplace and Fourier]]"
---
# Linear Algebra for AI and Quant

Linear algebra is the **mathematical substrate of modern AI and quantitative finance**. An LLM's core operation is matrix multiplication; a quant strategy is largely linear algebra over price matrices. This is the highest-leverage math to own, and Joe's [[Mathematics]] domain currently has **zero** sources — a gap worth closing. (Source: [[The AI Revolution in Math (Quanta)]]; search synthesis)

## Why It Dominates AI

(Source: search synthesis — Coursera / edX / Medium, confidence: high)

- **89%** of top-ranked AI master's programs explicitly require linear algebra.
- A 2024 McKinsey survey: **78%** of AI professionals regularly use linear algebra + calculus; weakness here causes early-career difficulty.
- **LoRA** (Low-Rank Adaptation) — the dominant LLM fine-tuning method — is built on **rank, linear independence, and low-rank factorization**.
- **PCA / SVD** — dimensionality reduction and the engine behind embeddings, recommender systems, and noise reduction — are pure linear algebra.

## The Core Objects to Master

1. **Vectors & matrices** — the data containers.
2. **Matrix multiplication** — the forward pass of every neural net.
3. **Rank / linear independence** — why LoRA and compression work.
4. **Eigenvalues / eigenvectors** — stability, PCA, [[Signals and Systems — Laplace and Fourier|systems]].
5. **SVD** — the "Swiss Army knife": compression, pseudo-inverse, latent factors.
6. **Dot products / norms / projections** — similarity, attention, least squares.

## The Quant Connection

[[Quantitative Trading]] and [[Statistical Arbitrage]] run on covariance matrices, factor models (regression = least squares = projection), and eigen-decomposition of return matrices. The same linear algebra serves both Joe's AI and investing interests.

## Career Signal

BLS (2024 Occupational Outlook): positions requiring advanced mathematics projected to grow **~38%/yr through 2026** — >5× the all-occupation average. (Source: search synthesis, confidence: medium)

## Why This Matters For Joe

Joe is strong on *applied* tracks (EE, programming) but thin on *foundational* math. Linear algebra is the one math course that pays off simultaneously in **AI, quant finance, EE signals, and graphics** — and it's the prerequisite that gates the deeper ML/quant work he's already circling.

## Entry Points

- **3Blue1Brown — "Essence of Linear Algebra"** (free, visual intuition first).
- **DeepLearning.AI — Mathematics for Machine Learning and Data Science**.
- **Gilbert Strang (MIT 18.06)** — the canonical course.

## See Also

- [[Mathematics]] — fills the empty domain
- [[Quantitative Trading]] · [[Statistical Arbitrage]] — the finance payoff
