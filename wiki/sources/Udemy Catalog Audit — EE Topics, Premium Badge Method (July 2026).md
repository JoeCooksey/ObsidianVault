---
type: source
title: "Udemy Catalog Audit — EE Topics, Premium Badge Method (July 2026)"
source_type: primary-observation
author: Joe's Vault (browser audit)
date_published: 2026-07-27
date_accessed: 2026-07-27
url: https://www.udemy.com/topic/power-electronics/
confidence: high
status: complete
created: 2026-07-27
updated: 2026-07-27
tags:
  - source
  - domain/career
  - domain/engineering
  - udemy
  - methodology
key_claims:
  - "The 'Premium' badge on a Udemy course card marks inclusion in the Personal Plan and renders while logged out"
  - "EE hardware coverage is uneven: embedded/PCB/MATLAB are well covered, LTspice is almost entirely excluded"
  - "Marketing copy understates engineering coverage — the catalog contains 376 electrical engineering courses"
related:
  - "[[Udemy Personal Plan EE Coverage Map]]"
  - "[[Udemy Personal Plan]]"
---

# Udemy Catalog Audit — EE Topics, Premium Badge Method (July 2026)

Primary observation, run 2026-07-27. Udemy's marketing copy never names engineering, so the only way to answer "what's actually in the plan for an EE student" is to inspect the catalog directly.

## Method

1. Drive a real browser to `udemy.com/topic/<topic>/` (logged out, US locale). Udemy 403s plain fetch tools.
2. Wait for client-side render, then walk every `a[href*="/course/"]` up to its `course-card_main-content` container.
3. A course is **in the Personal Plan** if its card renders the **"Premium"** badge.
4. Record title, rating, review count, and total hours per card.

## Validation of the method

The badge is rendered client-side and sits *outside* the title wrapper, so a naive selector produces **false negatives on every card**. The method was validated two ways before any result was trusted:

- **Positive control**: the `/topic/python/` page returned Premium on **19 of 19** top courses, matching the six courses Udemy itself labels "Premium" in its own showcase carousel on the [[Udemy — Personal Plan Page and FAQ (July 2026)|Personal Plan page]].
- **Negative discrimination**: within a single page the extractor returns a mix of Premium and non-Premium (e.g. PCB Design returned 15 in-plan of 22), so it is not simply flagging everything.

> [!gap] Verified logged out. Personal Plan membership is regional and the collection rotates, so a subscriber in a different country may see a different set. Re-verify any specific course before committing to it.

## Results — courses returned per topic and in-plan share of the visible top results

| Topic | Total courses | In-plan share of top results |
|---|---|---|
| Electrical Engineering | 376 | high (~15/20) |
| MATLAB | 208 | high (~15/20) |
| Embedded Systems | 126 | high (~14/24) |
| PCB / Circuit Design | 91 | high (~15/22) |
| Control Systems | 95 | moderate (~8/16) |
| FPGA | 63 | **low (6/17)** |
| VLSI | 54 | moderate (7/16) |
| Power Electronics | 54 | moderate (7/17) |
| **LTspice** | **16** | **1/17 — effectively excluded** |
| Python (reference point) | 3,651 | 19/19 |

## The two headline surprises

1. **Engineering is far better covered than the marketing implies.** 376 electrical engineering courses exist and most of the top-rated ones carry the Premium badge, including deep 20–50 hour power-systems courses.
2. **LTspice is a hole.** Of 16 dedicated LTspice courses, exactly one is in the plan — and it is an op-amp circuits course, not an LTspice course. The dedicated LTspice tutorials all rate 3.6–4.5, mostly below the plan's 4.5 curation bar.

Full course-level lists in [[Udemy Personal Plan EE Coverage Map]].
