---
type: concept
title: "Quant Interview Prep Guide"
status: complete
created: 2026-05-22
updated: 2026-05-22
tags:
  - quant
  - interview
  - probability
  - brainteasers
  - market-making
  - mental-math
---

# Quant Interview Prep Guide

The final gate before a quant role. Top firms (Jane Street, Citadel, Optiver, IMC, SIG) run notoriously rigorous processes. Interview prep is a distinct skill that requires dedicated practice — separate from the math and programming you've already built.

## Interview Formats by Firm

| Firm | Format | Key Emphasis |
|------|--------|-------------|
| **Jane Street** | Online → phone → 4–6-round superday | Probability, trading games, how you think under uncertainty |
| **Optiver** | Mental math screen (80 in 8 min) → logic → probability → trading sim | Raw speed + accuracy; market-making intuition |
| **IMC** | Math test → probability interviews → trading games | Similar to Optiver; market-making focus |
| **SIG** | Probability + poker theory → options theory → trading | GTO poker intuition is literally assessed; expected value |
| **Citadel** | Statistics → ML/coding (LeetCode) → case studies | More research-heavy; statistics + ML background |
| **Two Sigma** | ML projects + coding → research case study | Most ML-heavy; Python coding required |
| **D.E. Shaw** | Broad: math + CS + ML + physics | PhD-level mathematical breadth; most eclectic |

**The universal rule**: Jane Street is explicit about it, but all firms value *how you think when you don't know the answer* more than whether you get the answer. Show your reasoning, calibrate uncertainty explicitly, communicate clearly.

---

## Topic 1: Mental Math (Train This First)

**Why it matters**: Optiver's pre-screen is literally 80 mental arithmetic problems in 8 minutes (6 seconds per problem). All market-making firms test arithmetic speed.

**Train daily** (15–20 min/day for 6–8 weeks):
- tradermath.org — free timed mental math drills
- Optiver's public 80-in-8 practice on YouTube
- Anki deck: multiplication tables to 25×25, squares to 30², cubes to 15³

**Key tricks**:
- **13×17**: use (15−2)(15+2) = 225−4 = 221; difference of squares shortcut
- **Large multiplication**: 87×23 = 87×20 + 87×3 = 1740 + 261 = 2001
- **Percentages**: 17% of 250 = 10% (25) + 7% (17.5) = 42.5
- **Fractions**: simplify before computing; 126/84 = 3/2
- **Square roots**: know √2 ≈ 1.414, √3 ≈ 1.732, √5 ≈ 2.236

---

## Topic 2: Probability and Expected Value (The Core Topic)

**The most heavily tested topic across all quant firms.**

### Must-Know Distributions and Their Parameters

| Distribution | Mean | Variance | Classic Application |
|-------------|------|---------|---------------------|
| Bernoulli(p) | p | p(1−p) | Single coin flip |
| Binomial(n,p) | np | np(1−p) | N coin flips |
| Geometric(p) | 1/p | (1−p)/p² | Rolls until first success |
| Poisson(λ) | λ | λ | Count of events in interval |
| Uniform(a,b) | (a+b)/2 | (b−a)²/12 | Equal probability interval |
| Normal(μ,σ²) | μ | σ² | Returns, errors (CLT justifies) |
| Exponential(λ) | 1/λ | 1/λ² | Time between events |

### Classic Problem Types (Must Solve Fluently)

**Dice and coins**:
- Expected number of rolls to see all 6 faces of a die: E = 6/6 + 6/5 + 6/4 + 6/3 + 6/2 + 6/1 = 6·H(6) ≈ 14.7 (coupon collector)
- Expected number of flips to get H/T: 1/p
- Sum of two dice: E = 7; Var = 2 × 35/12 = 35/6

**Urn problems**:
- Without replacement: hypergeometric distribution
- With replacement: binomial distribution
- Conditional on drawing red first: Bayes' theorem

**Order statistics**:
- Expected maximum of n Uniform(0,1) draws: n/(n+1)
- Expected minimum of n Uniform(0,1) draws: 1/(n+1)
- Expected k-th order statistic: k/(n+1)

**Gambler's ruin**:
- Start with $k, play until $N or bust; P(winning) = k/N (fair game)
- With bias p>0.5: P(winning) = (1−(q/p)^k) / (1−(q/p)^N) where q = 1−p

**Conditional probability (Bayes' theorem)**:
- P(A|B) = P(B|A)·P(A) / P(B)
- Monty Hall: always switch (P(win|switch) = 2/3)
- Medical test: if disease has 1% prevalence and test has 99% sensitivity, 95% specificity → P(disease|positive) ≈ 17% (not 99%!)

### Expected Value Framework
Every market-making problem reduces to EV calculation. Format your thinking:
1. What are the possible outcomes?
2. What is the probability of each?
3. What is the payoff of each?
4. EV = Σ P(outcome_i) × payoff_i

---

## Topic 3: Brainteasers and Logic

**What they test**: structured reasoning under pressure, creative thinking, communication when you're uncertain. The answer matters less than the approach.

### The 5-Step Approach
1. **Restate** the problem ("So just to confirm, the question is...")
2. **State assumptions** explicitly ("I'll assume the coins are fair...")
3. **Think aloud** — show your reasoning process continuously
4. **Solve a simpler version first** ("Let me start with just 2 prisoners...")
5. **Scale up** and check boundary cases

### Classic Brainteasers You Must Know

**Counterfeit coin** (12 coins, balance scale, 3 weighings): the classic; practice the decision tree

**Clock hands** (how many times do hour and minute hands overlap in 12 hours?): 11 times; they meet at 12:00, ~1:05, ~2:10... 

**Burning ropes** (2 ropes that burn in 60 min each, non-uniform): burn rope 1 from both ends simultaneously + rope 2 from one end; when rope 1 dies (30 min), light rope 2 from the other end → rope 2 burns in 15 more minutes = 45 min total

**Blue-eyed islanders**: induction problem; n blue-eyed people leave on night n after a common knowledge statement is made

**100 prisoners and a box**: 50% survival using the loop strategy; classic probability/strategy hybrid

**The Bridge and Torch** (4 people, different crossing times, 1 torch, 2 can cross at once): 17 minutes; always send the two slowest together

---

## Topic 4: Market Making and Trading Games

**Most relevant for**: Jane Street, Optiver, IMC, SIG prop trading roles. You will be asked to quote bids and asks on synthetic "assets" (often dice rolls, card draws, or random number ranges).

### The Structure of a Trading Game

You are told: "Consider a game where I will roll two dice and reveal neither. You are a market maker for the sum of the two dice."

**Your job**:
1. **Assess fair value**: E[sum] = 7; σ ≈ 2.4
2. **Quote a bid-ask spread**: fair = 7, quote "5 bid, 9 ask" (wide spread = safe)
3. **Update on information**: if the interviewer says they want to buy (they think it's high), skew your quotes lower
4. **Manage inventory**: if you've sold too many (you're short), widen ask and tighten bid to attract buyers

### Key Market Making Principles

| Principle | Explanation |
|-----------|------------|
| **Fair value first** | Always anchor to your best EV estimate |
| **Spread = uncertainty buffer** | Wider spread when you have less information |
| **Quote skewing** | Move quotes toward inventory-reducing trades |
| **Adverse selection** | If someone always takes your best quote, they may know more than you |
| **Information updates** | Each trade tells you something; update your estimate |

**Practice format**: play with a friend; one generates random asset values, the other makes markets. Start wide, practice tightening as skill improves.

---

## Topic 5: Statistics and Quantitative Concepts

### Key Statistical Concepts for Interviews

**Hypothesis testing**:
- Null hypothesis H₀, alternative H₁
- p-value = probability of observing results at least as extreme as these, IF H₀ is true
- If p < 0.05, reject H₀ (5% false positive rate)
- Type I error = false positive (reject H₀ when true); Type II = false negative

**Regression interpretation**:
- OLS coefficient β₁ = effect of X₁ on Y *holding all other variables constant*
- R² = fraction of variance explained; not a measure of model quality
- Multicollinearity: correlated predictors make individual coefficients unstable (but predictions fine)

**CLT and LLN**:
- CLT: √n × (x̄ − μ) → Normal(0, σ²) as n → ∞; the reason Sharpe ratios scale by √252
- LLN: sample mean converges to true mean as n → ∞; the foundation of backtesting

**Variance reduction**:
- Variance of a sum: Var(X+Y) = Var(X) + Var(Y) + 2·Cov(X,Y)
- Portfolio diversification works because Cov(X,Y) < Var(X) when correlation < 1

---

## The Interview Resource Stack

| Resource | What It Covers | Priority |
|---------|---------------|---------|
| **"A Practical Guide to Quant Finance Interviews"** — Xinfeng Zhou (Green Book) | 290+ problems across all topics with full solutions | S-tier; the bible |
| **tradermath.org** | Mental math + probability drills; timed practice | S-tier; use daily |
| **openquant.co** | Free online problem bank; community solutions | A-tier |
| **"Fifty Challenging Problems in Probability"** — Mosteller | Classic puzzle book; beautiful problems | A-tier |
| Jane Street's blog ("Bits and Pieces") | Insight into their culture + thinking style | A-tier |
| LeetCode (medium/hard) | Coding rounds at Citadel, Two Sigma | B-tier (role-dependent) |
| "Heard on the Street" — Crack | Classic brainteasers and finance questions | B-tier |

---

## 12-Week Interview Prep Schedule

| Weeks | Primary Focus | Daily Practice (45–60 min) |
|-------|-------------|--------------------------|
| 1–3 | **Mental math** | tradermath.org 20 min + Anki multiplication cards |
| 4–5 | **Probability foundations** | Green Book Ch 1–2; 5 problems/day |
| 6–7 | **Expected value and conditional prob** | Green Book Ch 3; Bayes' theorem applications |
| 8 | **Brainteasers and logic** | Green Book Ch 4; 3 new brainteasers/day |
| 9–10 | **Market making games** | Mock trading sessions with a partner |
| 11 | **Statistics concepts** | Green Book Ch 5; regression + hypothesis testing |
| 12 | **Full mock interviews** | Time yourself; record and review your explanations |

**Key rule**: You cannot study your way to market-making skill. You must *practice under pressure* — timed, with someone listening. The discomfort of performing is what you are training for.

## See Also
- [[Quantitative Finance Career Guide]]
- [[Quant Math Foundations]]
- [[Derivatives Pricing and Financial Theory]]
- [[Systematic Trading Strategies]]
