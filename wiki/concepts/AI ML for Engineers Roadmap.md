---
type: concept
title: "AI ML for Engineers Roadmap"
status: complete
created: 2026-05-09
updated: 2026-05-09
tags:
  - AI
  - machine-learning
  - deep-learning
  - roadmap
  - self-study
  - electrical-engineering
---

# AI/ML for Engineers Roadmap

> Complete self-study roadmap from EE background to practical AI/ML engineering. EE students have a head start: linear algebra, complex math, signals processing, and control theory are all foundational ML math.

---

## Why This Matters (Joe's Context)

- **EE + ML = the rarest combo in the job market.** Power electronics engineers who can write ML code are in a category of one.
- **Active research at your targets**: Ranjram's ML-CEMS (machine learning-based converter electromagnetic state) directly applies ML to power converters — the exact intersection of your two tracks.
- **AI is eating EE**: smart grid control, predictive maintenance, motor fault detection, power system optimization — all are moving to learned models.
- **Ceiling**: if you build a power converter that *learns* its own control policy (reinforcement learning for power electronics), you are doing frontier research.

---

## Math Prerequisites (You Already Have Most of These as an EE)

| Math Area | EE Equivalent | ML Use |
|-----------|--------------|--------|
| Linear algebra | Circuit matrices, state-space | Neural network layers, PCA, SVD |
| Calculus / chain rule | Circuit analysis | Backpropagation |
| Probability & statistics | Noise analysis, random signals | Loss functions, Bayesian methods |
| ODEs | Circuit transient response | Continuous-time models, neural ODEs |
| Fourier/Laplace | Signal processing | CNNs, frequency-domain analysis |

**Gap to fill**: Probability at the depth of a statistics course. Resource: *Introduction to Probability* — Blitzstein & Hwang (free online at probabilitybook.net).

---

## Phase 0 — Python for Engineers (Weeks 1–4)

If you know Python from [[EE Freshman Self-Study Stack]], skip to Phase 1. If not:

- **Automate the Boring Stuff with Python** — Al Sweigart (free online)
- **Python for Data Analysis** — Wes McKinney (covers NumPy, pandas — your primary data tools)
- **Goal**: fluent with NumPy arrays, pandas DataFrames, matplotlib plotting, and basic file I/O

---

## Phase 1 — ML Fundamentals (Months 1–4)

### Top Course: fast.ai — Practical Deep Learning for Coders
- **Free** at fast.ai/courses
- Top-down approach: build real models first, understand theory later
- Best on-ramp for engineers — practical before theoretical
- Jeremy Howard is one of the most respected ML educators in the world
- Complete all 7 lessons; do the projects

### Parallel Reading: *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow* — Aurélien Géron (3rd ed., 2022)
- The best practical ML book; covers classical ML + deep learning end to end
- Read alongside fast.ai: each chapter complements the lectures
- Chapters 1–7 = classical ML (regression, classification, trees, SVMs)
- Chapters 10–19 = deep learning (CNNs, RNNs, transformers)

### YouTube: StatQuest with Josh Starmer
- Best channel for building statistical intuition (probability, regression, dimensionality reduction)
- Watch the "ML Fundamentals" playlist first

### Key Classical Algorithms to Understand Before Phase 2
- Linear regression + gradient descent (the foundation of everything)
- Logistic regression + cross-entropy loss
- Decision trees + random forests
- K-means clustering
- PCA (dimensionality reduction — you'll use this in sensor data analysis)

---

## Phase 2 — Deep Learning Core (Months 4–9)

### Primary Resource: Andrej Karpathy — "Neural Networks: Zero to Hero"
- Free on YouTube (12+ hours); build neural networks from scratch in Python
- Most respected deep learning educational series in existence
- Start here: "The spelled-out intro to neural networks and backpropagation: building micrograd"
- Sequence: micrograd → makemore (character-level LM) → GPT from scratch

### 3Blue1Brown — "Neural Networks" Series (4 videos)
- Best visual intuition for what's happening inside a neural network
- Watch before or alongside Karpathy — Karpathy gives code, 3B1B gives geometry
- Free on YouTube

### Book: *Deep Learning* — Goodfellow, Bengio, Courville (2016)
- The theoretical bible; free at deeplearningbook.org
- Don't read cover to cover — use as a reference
- Must-read chapters: 6 (deep feedforward networks), 8 (optimization), 9 (CNNs), 10 (RNNs)

### Course: Andrew Ng's Deep Learning Specialization (Coursera/DeepLearning.AI)
- 5-course specialization; ~$50/month to certify; free to audit
- More structured than fast.ai; complementary
- Complete at minimum: Course 1 (Neural Networks) + Course 2 (Hyperparameter Tuning)

### Key Architectures to Understand
- Feedforward networks (MLP) — the building block
- CNNs (convolutional neural networks) — images, signals
- RNNs / LSTMs — time series (critical for power electronics waveform analysis)
- Transformers / attention — the dominant architecture since 2017
- Autoencoders — anomaly detection in engineering systems

---

## Phase 3 — AI Engineering (Months 9–18)

### Power Electronics × ML (Your Specialty)
- **Reinforcement Learning for control**: train an agent to control a power converter's duty cycle
- **Ranjram's ML-CEMS**: machine learning models that estimate internal electromagnetic states from external measurements — read Ranjram's papers as the starting point
- **Fault detection**: train a classifier on converter waveform data to detect inductor saturation, capacitor degradation, MOSFET failure
- **Load forecasting**: predict load demand to pre-adjust converter operating point

### Resource: *Reinforcement Learning: An Introduction* — Sutton & Barto (2nd ed., free online)
- The RL bible; free at incompleteideas.net
- Read Ch. 1–6 for foundational RL (Q-learning, policy gradient)
- Ch. 13 (policy gradient methods) — most applicable to continuous-action control

### Production ML: *AI Engineering* — Chip Huyen (2024)
- Covers deploying models to production; embedding ML into real systems
- Critical for embedded applications (STM32 + trained model on-chip)

### Edge AI for Embedded Systems
- **TensorFlow Lite**: deploy trained models to microcontrollers (STM32, Arduino)
- **CMSIS-NN**: ARM's neural network library optimized for Cortex-M processors
- **TinyML** — Pete Warden & Daniel Situnayake (O'Reilly, 2019): ML on microcontrollers

---

## Best YouTube Channels

| Channel | Focus | Level |
|---------|-------|-------|
| **3Blue1Brown** | Mathematical intuition (neural networks series) | Beginner |
| **Andrej Karpathy** | Build from scratch; frontier research | Intermediate–Advanced |
| **StatQuest (Josh Starmer)** | Statistical concepts; regression, PCA, trees | Beginner |
| **Two Minute Papers** | Recent research papers summarized | All levels |
| **Yannic Kilcher** | Deep paper reviews (transformers, RL, etc.) | Advanced |
| **Sentdex** | Python + ML tutorials (practical) | Beginner–Intermediate |
| **ML Explained (Ahlad Kumar)** | Math behind ML algorithms | Intermediate |
| **Lex Fridman** | Long-form interviews; context + big picture | All levels |

---

## Books Ranked

| Book | Phase | Use |
|------|-------|-----|
| *Hands-On ML* — Aurélien Géron | 1 | Best practical intro; read cover to cover |
| *Deep Learning* — Goodfellow et al. | 2 | Theoretical reference; don't read linearly |
| *Introduction to Probability* — Blitzstein | 0–1 | Fill the stats gap |
| *Reinforcement Learning* — Sutton & Barto | 3 | RL for control applications |
| *AI Engineering* — Chip Huyen | 3 | Production systems + embedding ML |
| *TinyML* — Warden & Situnayake | 3 | ML on microcontrollers (STM32) |
| *The Deep Learning Revolution* — Sejnowski | Any | History + context; highly readable |

---

## Free Courses (Priority Order)

1. **fast.ai** — Practical Deep Learning for Coders (free; best first course)
2. **MIT 6.034** — Artificial Intelligence (free OCW; foundational theory)
3. **CS229 Stanford** — Machine Learning (free lecture videos on YouTube; Andrew Ng)
4. **CS231n Stanford** — CNNs for Visual Recognition (free; best CNN course)
5. **Deep Learning Specialization** — Andrew Ng/Coursera (paid but auditable)

---

## Milestones

| Milestone | Target Date | Signal |
|-----------|------------|--------|
| Python + NumPy fluent | Month 1 | Can manipulate matrices and plot data |
| First real model deployed | Month 2 | fast.ai image classifier or regression model |
| Built a neural net from scratch | Month 6 | Karpathy micrograd complete |
| Trained a time-series model on waveform data | Month 9 | Power converter fault classifier |
| Reinforcement learning agent controls simulated converter | Month 15 | RL policy converges in simulation |
| Edge ML: model runs on STM32 | Month 18 | TensorFlow Lite inference on-chip |

---

## See Also
- [[AI Five-Layer Cake]]
- [[CUDA Programming Model]]
- [[EE Freshman Self-Study Stack]]
- [[STM32 Digital Control for Buck Converter]]
- [[Mike Ranjram]]
- [[Top Topics to Research — Master Guide]]
