---
type: synthesis
title: "Research: Claude Code /loop Command"
created: 2026-06-06
updated: 2026-06-06
status: stable
tags:
  - research
  - claude-code
  - automation
related:
  - "[[Claude Code loop Command]]"
  - "[[Claude Code Scheduled Tasks]]"
sources:
  - "[[Source - Claude Code Docs Scheduled Tasks]]"
  - "[[Source - Better Stack Claude Code loop Guide]]"
---

# Research: Claude Code /loop Command

## Overview

`/loop` is a bundled Claude Code skill (v2.1.72+) that re-runs a prompt on a schedule while a session stays open — for polling deployments, babysitting PRs, watching builds, or in-session reminders. Both the interval and the prompt are optional; what you supply selects fixed-interval, self-paced, or maintenance-prompt behavior. It is the session-scoped tier of a three-way scheduling system (Cloud Routines / Desktop / `/loop`).

## Key Findings

- **One syntax, three behaviors** (Source: [[Source - Claude Code Docs Scheduled Tasks]]):
  - `/loop 5m check the deploy` → fixed cron schedule
  - `/loop check the deploy` → self-paced, Claude picks 1 min–1 hr each iteration
  - `/loop` → built-in maintenance prompt (or your `loop.md`)
- **Interval syntax** is forgiving: lead (`30m`) or trail (`every 2 hours`); units `s`/`m`/`h`/`d`; seconds round up; odd values snap to clean cron steps.
- **Self-paced mode is the standout** — Claude reasons about the right cadence (short while active, long while quiet), prints its reasoning, can switch to the **Monitor tool** to stream instead of poll, and **can end the loop itself** when the task is provably done.
- **`loop.md` customizes bare `/loop`** — `.claude/loop.md` (project) over `~/.claude/loop.md` (user); edits apply next iteration; 25 KB cap.
- **Stop with `Esc`** (clears the pending wakeup); fixed loops otherwise run until 7-day expiry.
- **Session-scoped**: fires only while Claude Code is idle, between turns; cleared by a fresh conversation; restored by `--resume`/`--continue` if unexpired; no catch-up for missed fires.
- **For unattended automation, don't use `/loop`** — use Routines (cloud), Desktop tasks, or GitHub Actions (Source: [[Source - Claude Code Docs Scheduled Tasks]]).

## Key Concepts

- [[Claude Code loop Command]]: the usage guide — three forms, syntax, self-pacing, `loop.md`, stopping, patterns.
- [[Claude Code Scheduled Tasks]]: the broader system — Cloud/Desktop/loop comparison, one-shot reminders, `Cron*` tools, cron reference, jitter/expiry.

## Contradictions

- **Expiry**: [[Source - Better Stack Claude Code loop Guide]] says recurring tasks expire after **3 days**; [[Source - Claude Code Docs Scheduled Tasks]] says **7 days**. The official docs are current and authoritative; the third-party figure is stale.
- **Jitter**: Better Stack says **up to 10%** of the period (15-min cap); the docs say **up to 30 min** (or half the interval for sub-hourly tasks). Trust the docs.

## Open Questions

- Exact behavior of the Monitor tool when a self-paced loop chooses it over re-prompting (referenced but not detailed here).
- Interaction between `loop.md` precedence and a prompt passed on the command line in edge cases (docs say CLI prompt always wins, but multi-task scheduling alongside `loop.md` is only lightly documented).

## Sources

- [[Source - Claude Code Docs Scheduled Tasks]]: Anthropic official docs — primary, high confidence.
- [[Source - Better Stack Claude Code loop Guide]]: Better Stack Community — workflow examples, medium confidence, stale on limits.
