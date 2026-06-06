---
type: concept
title: "Claude Code Scheduled Tasks"
status: stable
created: 2026-06-06
updated: 2026-06-06
tags:
  - concept
  - claude-code
  - automation
  - tooling
related:
  - "[[Claude Code loop Command]]"
  - "[[Research - Claude Code loop Command]]"
---

# Claude Code Scheduled Tasks

The scheduling system in Claude Code lets Claude re-run prompts on an interval, fire one-time reminders, and manage recurring jobs — all session-scoped. [[Claude Code loop Command|/loop]] is the convenience wrapper over this system; underneath, Claude uses the `Cron*` tools directly. Requires **v2.1.72+**. (Source: [[Source - Claude Code Docs Scheduled Tasks]])

## Three ways to schedule (compare)

|                       | Cloud (Routines)   | Desktop            | `/loop` (session)            |
| :-------------------- | :----------------- | :----------------- | :--------------------------- |
| Runs on               | Anthropic cloud    | Your machine       | Your machine                 |
| Machine must be on    | No                 | Yes                | Yes                          |
| Open session required | No                 | No                 | **Yes**                      |
| Survives restart      | Yes                | Yes                | Restored on `--resume` if unexpired |
| Local file access     | No (fresh clone)   | Yes                | Yes                          |
| MCP servers           | Per-task           | Config + connectors| Inherits from session        |
| Permission prompts    | None (autonomous)  | Configurable       | Inherits from session        |
| Minimum interval      | **1 hour**         | 1 minute           | 1 minute                     |

**Rule of thumb:** cloud for reliable unattended work, Desktop for local files/tools, `/loop` for quick in-session polling. (Source: [[Source - Claude Code Docs Scheduled Tasks]], confidence: high)

## One-time reminders

For one-shot tasks, describe it in natural language — no `/loop` needed. Claude schedules a single-fire task that deletes itself after running.

```text
remind me at 3pm to push the release branch
in 45 minutes, check whether the integration tests passed
```

## The cron tools underneath

Ask Claude in plain language ("what scheduled tasks do I have?", "cancel the deploy check job") or it uses these directly:

| Tool | Purpose |
| :-- | :-- |
| `CronCreate` | Schedule a task — 5-field cron expression, prompt, recur-or-once |
| `CronList` | List all tasks with IDs, schedules, prompts |
| `CronDelete` | Cancel a task by its 8-character ID |

A session can hold up to **50** scheduled tasks at once.

### Cron expression reference

5 fields: `minute hour day-of-month month day-of-week`. Supports `*`, single values, steps (`*/15`), ranges (`1-5`), lists (`1,15,30`).

| Example | Meaning |
| :-- | :-- |
| `*/5 * * * *` | Every 5 minutes |
| `0 * * * *` | Every hour on the hour |
| `0 9 * * *` | Every day at 9am local |
| `0 9 * * 1-5` | Weekdays at 9am local |
| `30 14 15 3 *` | March 15 at 2:30pm local |

- Day-of-week: `0` or `7` = Sunday … `6` = Saturday.
- Extended syntax (`L`, `W`, `?`, `MON`, `JAN`) is **not** supported.
- When both day-of-month and day-of-week are set, a date matches if **either** matches (vixie-cron semantics).
- All times are **local timezone**, not UTC.

## How tasks run

- Scheduler checks every second; due tasks enqueue at low priority and fire **between turns**, never mid-response. If Claude is busy, the prompt waits for the current turn to end.
- **Jitter** (avoids API stampedes): recurring tasks fire up to 30 min late (or half the interval if sub-hourly); one-shots at `:00`/`:30` fire up to 90 s early. Offset is deterministic from task ID — pick a minute like `:03` to dodge one-shot jitter.
- **7-day expiry**: recurring tasks fire one last time at 7 days, then self-delete. Recreate before expiry, or use Routines/Desktop for durability.

## Disable entirely

Set `CLAUDE_CODE_DISABLE_CRON=1` to turn off the scheduler — cron tools and `/loop` become unavailable and scheduled tasks stop firing.

## Limitations

- Fires only while Claude Code is running and idle; closing the terminal stops everything.
- No catch-up for missed fires.
- A fresh conversation clears all session-scoped tasks; `--resume`/`--continue` restores unexpired ones (background Bash/monitor tasks are never restored).

For durable automation see Routines (cloud / API / GitHub events), GitHub Actions (`schedule` trigger), or Desktop scheduled tasks.
