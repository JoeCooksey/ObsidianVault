---
type: source
source_type: distributor
title: "Rigol DHO800 Series Oscilloscope"
author: Rigol / EEVblog / HobbyistScope
date_published: 2026
url: https://hobbyistscope.com/compare/rigol-dho802-vs-rigol-dho814
created: 2026-06-03
updated: 2026-06-03
confidence: medium
tags:
  - source
  - distributor
  - test-equipment
key_claims:
  - "Rigol's current budget line is the 12-bit DHO800 series, succeeding the 8-bit DS1054Z"
  - "DHO802: 12-bit, 2 ch, ~$329 — budget entry to 12-bit territory"
  - "DHO804/DHO814 add 4 channels and/or 100 MHz for a modest premium"
related:
  - "[[Buck Converter BOM (Order-Ready 2026)]]"
  - "[[Consumer Purchase Value Tier List]]"
---
# Rigol DHO800 Series Oscilloscope

Oscilloscope recommendation update for the buck project's bench.

- **Shift since the project page was written:** the old recommendation (DS1054Z, 8-bit, ~$350) is last-gen. Rigol's current budget line is the **12-bit DHO800 series** — touchscreen, USB-C powered, compact.
- **DHO802** — 12-bit, 2 ch, ~70 MHz, **$329** — the budget entry; enough for SW-node and load-transient work on a 100 kHz buck.
- **DHO804 / DHO814** — add channels / 100 MHz bandwidth for ~$110 premium; 4 channels is handy for watching PWM + SW + V_out + gate together.
- **SFRA in firmware** (controller measures its own loop gain) removes the need for a separate ~$1k network analyzer — the scope plus SFRA covers Phase 6 validation.
- DS1054Z still works fine if found cheap used; not discontinued as of June 2026, just superseded.
