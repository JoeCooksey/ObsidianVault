---
type: concept
title: "Daily Caloric Intake Calculator"
status: developing
created: 2026-05-02
updated: 2026-05-02
tags:
  - nutrition
  - calories
  - tdee
  - weight-loss
  - muscle-gain
  - fitness
---

# Daily Caloric Intake Calculator

TDEE (Total Daily Energy Expenditure) is the total number of calories your body burns in 24 hours. It is the single number that determines whether you gain weight, lose weight, or maintain. Every goal-based calorie target is calculated as an offset from TDEE.

---

## Step 1 — Calculate BMR (Basal Metabolic Rate)

BMR = calories burned at complete rest. Three formulas, in order of preference:

### Mifflin-St Jeor (recommended — most accurate for general population)

| Sex | Formula |
|-----|---------|
| Male | `(10 × kg) + (6.25 × cm) − (5 × age) + 5` |
| Female | `(10 × kg) + (6.25 × cm) − (5 × age) − 161` |

Validated as most likely to predict resting metabolic rate within 10% of measured values across diverse populations.

### Katch-McArdle (best if you know your body fat %)

`BMR = 370 + (21.6 × Lean Body Mass in kg)`

LBM = total weight × (1 − body fat fraction)

Superior for lean and athletic individuals because it removes metabolically inactive fat mass from the equation.

### Harris-Benedict (original, 1919 — classic, use as backup)

| Sex | Formula |
|-----|---------|
| Male | `66.5 + (13.75 × kg) + (5.003 × cm) − (6.75 × age)` |
| Female | `655.1 + (9.563 × kg) + (1.850 × cm) − (4.676 × age)` |

Tends to overestimate by ~5% in overweight populations.

---

## Step 2 — Apply Activity Multiplier → TDEE

| Activity Level | Description | Multiplier |
|---|---|---|
| Sedentary | Desk job, little/no exercise | × 1.2 |
| Lightly active | Light exercise 1–3 days/week | × 1.375 |
| Moderately active | Moderate exercise 3–5 days/week | × 1.55 |
| Very active | Hard exercise 6–7 days/week | × 1.725 |
| Extra active | Physical job + hard daily exercise | × 1.9 |

> **Tip:** Most people overestimate their activity level. When in doubt, select one tier lower and adjust based on real weight-trend data over 2–4 weeks.

**TDEE = BMR × Activity Multiplier**

---

## Step 3 — Set Goal-Specific Calorie Target

### Weight Loss

| Deficit Size | Kcal/day | Expected Loss |
|---|---|---|
| Moderate | −500 kcal | ~0.45 kg (1 lb)/week |
| Aggressive | −750 to −1,000 kcal | ~0.7–0.9 kg (1.5–2 lb)/week |
| Hard floor | 1,200 kcal (women), 1,500 kcal (men) | Never go below |

- Safe rate: no more than 0.5–1% of body weight per week
- Diet breaks: return to maintenance for 1–2 weeks every 8–12 weeks (MATADOR study — improves fat loss, reduces muscle loss vs. continuous restriction)

### Muscle Gain / Bulk

| Approach | Surplus | Expected Lean Gain |
|---|---|---|
| Clean/lean bulk | +250–500 kcal/day (~10–20% above TDEE) | 0.1–0.25 kg/week |
| Dirty bulk (avoid) | >+500 kcal/day | Similar muscle, much more fat |

Research: larger surpluses produced similar strength and muscle gains as small surpluses, but significantly greater fat accumulation. A clean surplus is the evidence-based choice.

Beginners and those returning after a layoff can gain muscle at or near maintenance ("recomposition") with adequate protein and progressive training.

### Maintenance

1. Start at TDEE estimate
2. Track body weight trend for 2–4 weeks
3. If weight trends up: reduce by 100–150 kcal/day
4. If weight trends down: add 100–150 kcal/day
5. Repeat until weight stabilizes

---

## Protein Targets

| Goal | Daily Protein |
|---|---|
| General health / maintenance | 0.8–1.2 g/kg body weight |
| Weight loss (muscle preservation) | 1.6–2.2 g/kg body weight |
| Muscle gain (resistance training) | 1.6–2.2 g/kg body weight |
| Upper safe limit (normal kidney function) | ~2.2 g/kg |

US convenience: **0.7–1.0 g/lb** covers the evidence-based range for active people.

Meta-analysis of 49 studies: muscle gain maximizes at ~1.6 g/kg/day; the 97.5th percentile of individuals benefits up to 2.2 g/kg/day. Beyond 2.2 g/kg yields no additional muscle benefit.

---

## Macro Splits by Goal

These are starting-point ranges. Always set protein in grams first (from the g/kg targets above), then fill remaining calories with carbs and fat to preference.

| Goal | Protein | Carbs | Fat |
|---|---|---|---|
| Weight loss | 30–35% | 35–40% | 25–30% |
| Muscle gain | 25–30% | 40–45% | 25–30% |
| Maintenance | 25–30% | 40–50% | 20–30% |

Both low-carb and low-fat approaches can work as long as protein floors are met.

---

## Key Accuracy Notes

- **Self-reported intake is systematically underreported** by 12–54% across populations — apps that use verified food databases (Cronometer, MacroFactor) produce more accurate results than crowdsourced ones (MyFitnessPal)
- **Portion size error** accounts for ~49% of total logging error, even when food identification is correct — weigh food when precision matters
- **Formula TDEE estimates can be off by 200–400 kcal/day** for individuals — use weight-trend data over 2–4 weeks to calibrate, or use an adaptive tracking app (MacroFactor, Carbon) that back-calculates actual TDEE from real data

---

## Quick Reference: Sample TDEE for a 19-Year-Old Male, 70 kg, 175 cm

| Activity Level | Estimated TDEE |
|---|---|
| Sedentary (1.2) | ~1,900 kcal |
| Lightly active (1.375) | ~2,175 kcal |
| Moderately active (1.55) | ~2,450 kcal |
| Very active (1.725) | ~2,730 kcal |

Loss target (mod. active, −500): ~1,950 kcal/day
Gain target (mod. active, +300): ~2,750 kcal/day

---

## Related
- [[Bulk and Cut Decision Framework]] — BF%-based decision rule for when to bulk vs. cut
- [[FFMI Natural Muscle Potential]] — natural muscle ceiling at 5'9" reference table
- [[Testosterone Habits Tier List]] — protein, fat, and body composition affect T
- [[Food Health Tier List — Overall]] — whole-food sources to fill calorie targets
- [[Research - Daily Caloric Intake and Tracking Apps]] — full research synthesis + app tier list
