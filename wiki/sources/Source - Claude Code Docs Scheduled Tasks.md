---
type: source
source_type: documentation
title: "Claude Code Docs — Run Prompts on a Schedule"
author: Anthropic
date_published: 2026
url: https://code.claude.com/docs/en/scheduled-tasks
confidence: high
status: stable
created: 2026-06-06
updated: 2026-06-06
tags:
  - source
  - claude-code
  - documentation
related:
  - "[[Claude Code loop Command]]"
  - "[[Claude Code Scheduled Tasks]]"
---

# Source — Claude Code Docs: Run Prompts on a Schedule

Official Anthropic documentation for `/loop` and the Claude Code scheduling system. **Primary, authoritative source.** Current as of the v2.1.72+ scheduled-tasks feature.

## What it contributes

The complete, current specification of `/loop` and scheduled tasks:

- **The three `/loop` forms** — interval+prompt (fixed), prompt-only (self-paced 1 min–1 hr), bare `/loop` (built-in maintenance prompt or `loop.md`).
- **Interval syntax** — leading bare token or trailing clause; units `s`/`m`/`h`/`d`; seconds round up; odd intervals round to clean cron steps.
- **Self-paced mode** — Claude picks each delay and prints the reason; may use the Monitor tool to stream instead of poll; can end the loop itself.
- **`loop.md`** — `.claude/loop.md` (project) > `~/.claude/loop.md` (user); replaces the maintenance prompt; 25 KB cap; live edits.
- **Stopping** — `Esc` clears the pending wakeup.
- **Scheduling internals** — 7-day expiry, jitter (30 min recurring / 90 s one-shot), local timezone, between-turn firing, no catch-up, 50-task cap, 8-char IDs.
- **Cron tools** — `CronCreate` / `CronList` / `CronDelete`; standard 5-field expressions (no `L`/`W`/`?`/name-alias extensions).
- **Comparison table** — Cloud (Routines) vs Desktop vs `/loop`.
- **Disable flag** — `CLAUDE_CODE_DISABLE_CRON=1`.
- **Platform caveats** — Bedrock / Vertex AI / Microsoft Foundry change no-interval and no-prompt behavior.

## Key claims (high confidence)

- `/loop` requires Claude Code v2.1.72+.
- Recurring tasks expire 7 days after creation.
- Self-paced delays range 1 minute to 1 hour.
- A session can hold up to 50 scheduled tasks.
- Scheduled prompts fire between turns, never mid-response.
