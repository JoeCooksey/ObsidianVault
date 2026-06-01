---
type: concept
title: "Wearable Health Metric Validity"
created: 2026-06-01
updated: 2026-06-01
tags:
  - concept
  - domain/health
  - wearables
  - tracking
  - sleep
status: developing
related:
  - "[[Health Metrics Master Tier List (Price, Frequency, Worth-It)]]"
  - "[[Biohacking Tier List]]"
---
# Wearable Health Metric Validity

What consumer wearables (Oura, Whoop, Apple Watch, Garmin, Fitbit) actually measure well vs poorly, per 2025 validation studies against gold standards (PSG, ECG) (Source: [[Wearable Sleep and HRV Validation 2025]]).

## Reliability by Metric

| Metric | Accuracy | Verdict |
|--------|----------|---------|
| **Sleep vs wake** | >90% sensitivity | **Trust it** — total sleep time is reliable |
| **Resting heart rate** | High; Oura Gen 3/4 best | **Trust it** |
| **HRV (resting, stationary)** | Approximates ECG at rest; Oura highest accuracy | **Trust the trend**, not absolute values |
| **HRV (during movement)** | Degrades — only valid stationary | Use only at rest/sleep |
| **Step count** | Good | Reliable enough |
| **Sleep staging (REM/deep/light)** | 50–80% vs polysomnography | **Don't over-trust** the breakdown |
| **VO2 max estimate** | Reasonable proxy | Good enough for trend tracking |

## Sleep Staging — The Weak Spot

Four-stage sleep classification accuracy runs only **60–75%** (some devices lower) (confidence: **high**):
- **Oura Ring** — strongest, ~79% agreement with PSG
- **Whoop 4.0** — ~70% (2025 independent study)
- **Apple Watch** — ~51% (2025 study)

> [!gap] Funding source matters: many favorable wearable studies are manufacturer-sponsored. Treat company-backed accuracy claims as **medium** confidence.

## Practical Takeaways

1. Use wearables for **trends in RHR, HRV, and total sleep** — these are the validated, actionable signals.
2. Ignore precise REM/deep-sleep numbers; the nightly stage split is noisy.
3. Oura currently leads for RHR/HRV accuracy among ring/wrist devices.
4. A $150–350 device replaces several lab metrics (RHR, VO2max estimate) for free thereafter — strong value.
