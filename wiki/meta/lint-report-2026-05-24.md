---
type: meta
title: "Lint Report 2026-05-24"
created: 2026-05-24
updated: 2026-05-24
tags:
  - meta
  - lint
status: complete
---
# Wiki Lint Report — 2026-05-24

Full health check of the Obsidian wiki vault. 8 checks run across all pages under `wiki/`.

---

## Summary

| Check | Status | Issue Count |
|---|---|---|
| Dead wikilinks | FAIL | 12 dead link targets (across 14 occurrences) |
| Orphan pages | WARN | 4 pages with no inbound wikilinks |
| Misfiled pages | FAIL | 21 research synthesis pages in wrong folder |
| Frontmatter gaps | WARN | 4 pages missing required frontmatter fields |
| Empty sections | WARN | 3 pages with unpopulated placeholder sections |
| Stale index entries | WARN | 2 index entries point to misfiled pages |
| Missing entity pages | FAIL | 2 entity pages referenced but never created |
| Index coverage | PASS | All actively-used pages are cataloged |

---

## 1. Dead Wikilinks

### 1a. 7 Habits Source Page — 9 dead concept links

File: `wiki/sources/The 7 Habits of Highly Effective People - Stephen Covey.md`

All 9 links appear in the frontmatter `related:` block and inline in body text. None of these concept pages exist as files anywhere in `wiki/`:

| Dead Link | Referenced In |
|---|---|
| `[[Circle of Concern vs Circle of Influence]]` | frontmatter + Habit 1 section |
| `[[Maturity Continuum]]` | frontmatter + Core Thesis |
| `[[P/PC Balance]]` | frontmatter + Core Thesis |
| `[[Character Ethic vs Personality Ethic]]` | frontmatter + Part 1 section |
| `[[Time Management Matrix]]` | frontmatter + Habit 3 section |
| `[[Emotional Bank Account]]` | frontmatter + bridge concept section |
| `[[Abundance Mentality]]` | frontmatter + Habit 4 section |
| `[[Empathic Listening]]` | frontmatter + Habit 5 section |
| `[[Win-Win Paradigm]]` | frontmatter + Habit 4 section |

**Fix**: Create 9 concept stub pages in `wiki/concepts/` — each is a rich, standalone concept with cross-domain connections (Character Ethic connects to [[Deep Work]], [[Deliberate Practice]]; Time Management Matrix connects to [[Deep Work Task Taxonomy]]; Abundance Mentality connects to [[Generosity-First Networking]]; Empathic Listening connects to [[Emotional Agility]]).

### 1b. Isaacson Biographies — 1 dead concept link in 3 files

Files:
- `wiki/sources/Leonardo da Vinci - Walter Isaacson.md`
- `wiki/sources/Elon Musk - Walter Isaacson.md`
- `wiki/sources/Steve Jobs - Walter Isaacson.md`

Dead link: `[[Entrepreneurship and Innovation]]` — appears in frontmatter `related:` of all three Isaacson biographies. No concept page exists for this topic.

**Fix**: Create `wiki/concepts/Entrepreneurship and Innovation.md` synthesizing the innovation principles from all three biographies (Reality Distortion Field, The Algorithm, sfumato as comfort with ambiguity, product-before-profit).

---

## 2. Missing Entity Pages

Two entities are referenced throughout the wiki but have no entity page in `wiki/entities/`:

| Missing Entity | Referenced In |
|---|---|
| `[[Stephen Covey]]` | `wiki/index.md`, `wiki/domains/Books.md`, `wiki/sources/The 7 Habits of Highly Effective People - Stephen Covey.md` |
| `[[Walter Isaacson]]` | `wiki/index.md`, `wiki/entities/Elon Musk.md`, `wiki/entities/Leonardo da Vinci.md`, `wiki/entities/Steve Jobs.md`, and the three Isaacson source files |

**Fix**: Create `wiki/entities/Stephen Covey.md` and `wiki/entities/Walter Isaacson.md`. Both are already described in `wiki/index.md`; the pages just need to be created.

---

## 3. Misfiled Pages — 21 Research Syntheses in Sources Instead of Questions

Per `CLAUDE.md`, research syntheses should live in `wiki/questions/`. Twenty-one "Research - ..." synthesis files are incorrectly stored in `wiki/sources/`:

```
wiki/sources/Research - Math and Physics Foundations for EE.md
wiki/sources/Research - College Dating Guide for Young Men.md
wiki/sources/Research - Hobbies for Young Men.md
wiki/sources/Research - Peptide Tier List.md
wiki/sources/Research - Zero Cost Computer Skills.md
wiki/sources/Research - Power Electronics UWBG Faculty Scan 2026.md
wiki/sources/Research - Book Recommendations Master List.md
wiki/sources/Research - Sleep Habits Tier List.md
wiki/sources/Research - Top Learning Podcasts.md
wiki/sources/Research - Human Hormones and Optimization.md
wiki/sources/Research - Comfort Zone Daily Habits.md
wiki/sources/Research - 90 Day Project Ideas.md
wiki/sources/Research - ASU Scholarships for California EE Students.md
wiki/sources/Research - Top Apartment Health Products.md
wiki/sources/Research - Stackable EE Scholarships ASU Second Year.md
wiki/sources/Research - Diet Cheat Day Recovery.md
wiki/sources/Research - Top Topics to Research.md
wiki/sources/Research - Purchases That Genuinely Benefit Your Life.md
wiki/sources/Research - Summer 2026 Activities Tier List.md
wiki/sources/Research - Probiotic Foods Complete Guide.md
wiki/sources/Research - Trending GitHub Repositories May 2026.md
```

The correct 21 `Research - ...` syntheses are already correctly filed in `wiki/questions/` (confirmed present). These 21 in `sources/` are either duplicates or should be moved.

**Action**: Verify whether these are duplicates of the questions/ versions or different content. If duplicates, delete from sources/. If unique, move to questions/.

**Impact**: Obsidian wikilinks resolve by filename regardless of folder (since filenames are unique), so wikilink resolution is not currently broken — but the misfiling creates confusion and violates vault schema.

---

## 4. Frontmatter Gaps

### 4a. Missing `title:` field

File: `wiki/sources/Roblox AI Development Guide 2025.md`

This file has `type:`, `status:`, `created:`, `updated:`, and `tags:` but is **missing `title:`**. Per the CLAUDE.md minimum frontmatter spec, `title:` is required.

**Fix**: Add `title: "Roblox AI Development Guide 2025"` to the frontmatter.

### 4b. `name:` instead of `title:` (inconsistency)

Three ASU faculty entity pages use `name:` instead of `title:`, inconsistent with all other entity pages:

| File | Issue |
|---|---|
| `wiki/entities/Mike Ranjram.md` | Has `name: Mike Ranjram` — should be `title: "Mike Ranjram"` |
| `wiki/entities/Raja Ayyanar.md` | Has `name: Raja Ayyanar` — should be `title: "Raja Ayyanar"` |
| `wiki/entities/Yuji Zhao.md` | Has `name: Yuji Zhao` — should be `title: "Yuji Zhao"` |

**Fix**: Add `title:` field to each of these three files (can keep `name:` as an additional field or remove it).

---

## 5. Empty Sections / Stale Placeholder Pages

### 5a. `wiki/domains/Mathematics.md` — All sections are empty placeholders

Every content section reads "*(populated as sources are ingested)*". The wiki now has substantial mathematics content (Laplace Transform, Circuit Theory, MIT 18.06, Calculus/DiffEQ/Mechanics/EM concept pages) that should be cross-referenced here.

**Fix**: Update `wiki/domains/Mathematics.md` with links to the 6+ math-related concept pages that now exist.

### 5b. `wiki/papers/_index.md` — Empty

All sections say "*(populated as papers are ingested)*". The wiki has 6 research papers ingested (4 LLM papers, 2 WBG papers, 2 PMC health papers) that are not reflected in this index.

**Fix**: Populate `wiki/papers/_index.md` with the ingested papers: Survey - Low-bit LLMs 2024, Edge LLM Inference Benchmark 2026, Framework Comparison Apple Silicon 2025, Bitnet.cpp Edge Inference 2025, IEEE Spectrum SiC vs GaN 2024, MDPI WBG Comparative Review 2024, PMC Creatine Meta-analysis 2024, PMC Caffeine Theanine Review 2022.

### 5c. `wiki/overview.md` — Stale (last updated 2026-04-18)

The overview has never been updated since vault creation. It does not reflect the wiki's actual content (200+ pages across 15 domains). `updated:` field is 36 days stale.

**Fix**: Regenerate wiki/overview.md to reflect current scope and cross-domain connection map.

---

## 6. Orphan Pages

Pages that have no inbound wikilinks from other wiki pages (verified by searching for `[[PageName]]` references):

| Page | Notes |
|---|---|
| `wiki/papers/_index.md` | Never linked from any content page; only exists as structural scaffold |
| `wiki/domains/Mathematics.md` | Not linked from any concept page despite math concepts existing |
| `wiki/sources/Roblox AI Development Guide 2025.md` | Source record not linked from the Roblox concept pages |
| `wiki/overview.md` | Never referenced by any page; structural orphan |

**Fix**: Add inbound links to these pages from relevant index/domain/concept pages.

---

## 7. Stale Index Entries

Two entries in `wiki/index.md` reference files that are not in the expected location:

| Index Entry | Expected Location | Actual Location |
|---|---|---|
| `[[Research - Hobbies for Young Men]]` | `wiki/questions/` | `wiki/sources/` (misfiled) |
| `[[Research - College Dating Guide for Young Men]]` | `wiki/questions/` | `wiki/sources/` (misfiled) |

Since Obsidian resolves links by filename regardless of folder, these links resolve correctly — but they are structurally incorrect per the vault schema.

---

## 8. Index Coverage — PASS

All 200+ actively-used pages are cataloged in `wiki/index.md`. The index is comprehensive and well-organized. No meaningful pages were found to be missing from the index. The index accurately represents the vault's content.

---

## Priority Action Plan

### P1 — Fix now (broken links)
1. Create 9 missing concept pages for 7 Habits concepts (Circle of Concern vs Circle of Influence, Maturity Continuum, P/PC Balance, Character Ethic vs Personality Ethic, Time Management Matrix, Emotional Bank Account, Abundance Mentality, Empathic Listening, Win-Win Paradigm)
2. Create `wiki/entities/Stephen Covey.md`
3. Create `wiki/entities/Walter Isaacson.md`
4. Create `wiki/concepts/Entrepreneurship and Innovation.md`

### P2 — Fix soon (structural issues)
5. Resolve the 21 misfiled Research synthesis pages (confirm duplicates vs. unique content, then move or delete)
6. Add `title:` to `Roblox AI Development Guide 2025.md`
7. Add `title:` field to Mike Ranjram, Raja Ayyanar, Yuji Zhao entity pages

### P3 — Fix when convenient (stale/empty)
8. Update `wiki/domains/Mathematics.md` with actual math concept links
9. Populate `wiki/papers/_index.md` with ingested papers
10. Regenerate `wiki/overview.md` to reflect current vault state

---

## Open Questions
```dataview
LIST FROM "wiki/questions" WHERE contains(tags, "open-question") SORT created DESC
```

*Note: This Dataview query will return results in Obsidian if pages have been tagged with `open-question`. Currently no pages use this tag — add `tags: [open-question]` to questions that remain unresolved.*
