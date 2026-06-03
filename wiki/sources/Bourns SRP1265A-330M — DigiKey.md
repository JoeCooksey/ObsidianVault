---
type: source
source_type: distributor
title: "Bourns SRP1265A-330M — DigiKey"
author: DigiKey / Bourns
date_published: 2026
url: https://www.digikey.com/en/products/detail/bourns-inc/SRP1265A-330M/4876626
created: 2026-06-03
updated: 2026-06-03
confidence: high
tags:
  - source
  - distributor
  - power-electronics
key_claims:
  - "SRP1265A-330M: 33 uH shielded SMD power inductor, I_sat ~11 A, I_rms 8 A, DCR 58 mOhm max"
  - "In stock at DigiKey, Newark, Arrow as of June 2026"
  - "I_sat margin is large vs the 3.45 A peak; DCR of 58 mOhm costs ~0.5 W at 3 A"
related:
  - "[[Buck Converter BOM (Order-Ready 2026)]]"
---
# Bourns SRP1265A-330M — DigiKey

Distributor + datasheet confirmation for the power inductor.

- **Specs:** 33 µH, shielded, carbonyl-powder core; **I_rms 8 A, I_sat ≈ 11 A**, DCR 58 mΩ max; ~13.5 × 12.5 × 6.2 mm SMD.
- **Status (June 2026):** in stock at DigiKey (#4876626), Newark, Arrow.
- **Fit:** I_sat hugely exceeds the design's 3.45 A peak (safe). The 58 mΩ DCR is the one weak spot — ~0.5 W loss at 3 A; a lower-DCR alternative (Würth 7443340330, Coilcraft XAL1010-333) improves efficiency at higher cost.
