---
type: source
title: "Power Electronics and UWBG Faculty Research Scan"
source_file: .raw/articles/power-electronics-uwbg-faculty-scan-2026-05-01.md
author: ChatGPT research (commissioned by Joe)
date: 2026-05-01
status: ingested
tags:
  - power-electronics
  - FURI
  - grad-school
  - WBG
  - GaN
  - faculty
  - ASU
  - magnetics
  - converter-architecture
---

# Power Electronics and UWBG Faculty Research Scan (2026)

## Overview
Research scan of three faculty recommended for Joe's FURI program evaluation. Covers recent papers, lab artifacts, student pipelines, and research directions for each faculty.

## Faculty Covered
| Faculty | Institution | Focus | FURI-viable? |
|---------|-------------|-------|--------------|
| [[Mike Ranjram]] | ASU MAPEL | Converter architecture, MHz magnetics, miniaturization | ✅ Top priority |
| [[Raja Ayyanar]] | ASU EVSTS | EV/PV, grid-control, WBG applications | ✅ Second option |
| [[Yuji Zhao]] | Rice WIDE Lab | GaN/β-Ga₂O₃ device physics, BN interface engineering | ❌ No longer at ASU |

## Key Findings

> [!key-insight] Critical Correction
> Yuji Zhao is at **Rice University**, not ASU. His ASU faculty pages are stale. Any FURI mentorship requires a current ASU faculty member — Zhao is not an option.

### Ranjram (MAPEL) — What Matters for Joe
1. **ML-CEMS paper** is the best entry-point read: variable-gain LLC at fixed frequency; peak flux 231 mT → 66 mT is the headline number; connects magnetics + topology + control in one problem
2. **HPPC** (single-stage ac/dc) is the 2025 flagship; future work = closed-loop control + variable passives → open FURI problem
3. **MAPEL GitHub** (`MHzCoreLossAggregateDataset`) is a data-driven entry point: clone the repo, explore the schema, propose a surrogate model
4. **Fulton Forge posters** (Anderson, Puerta, Novli) confirm active undergrad pipeline — Joe is not the first undergrad to work here

### Ayyanar (EVSTS) — What Matters for Joe
1. Recent visible papers are feeder/DER-control, not hardware — if Joe wants hardware, this is less clean than Ranjram
2. The **EV converter hardware thread** is real (EVSTS "High Frequency Power Converters for EV" project) but less documented
3. Senior professor → larger lab, more bureaucracy, but stronger industry connections (OEMs, utilities)
4. Best use case: if Joe wants EV system-level context + industry pipeline over pure hardware research

### Zhao (WIDE Lab) — What to Know
1. **BN interface engineering** is a reusable design philosophy: thin dielectric interlayer → disproportionate gain in reliability/breakdown
2. Not a FURI option, but Zhao's group is a potential grad school target or collaboration
3. The JUMP 2.0 / CHIMES connection means broad semiconductor center ecosystem access

## Source Links
- [[Mike Ranjram]]
- [[Raja Ayyanar]]
- [[Yuji Zhao]]
- [[FURI Program Complete Guide]]
- [[MS EE Programs Power Electronics Semiconductors]]
- [[FURI to Grad School Roadmap — Joe]]
