---
type: source
source_type: article
title: "Recurring Tasks in Claude Code: The /loop Skill and Desktop Scheduler"
author: Better Stack Community
date_published: 2026
url: https://betterstack.com/community/guides/ai/claude-code-loop/
confidence: medium
status: stable
created: 2026-06-06
updated: 2026-06-06
tags:
  - source
  - claude-code
related:
  - "[[Claude Code loop Command]]"
  - "[[Research - Claude Code loop Command]]"
---

# Source — Better Stack: Claude Code /loop and Desktop Scheduler

Third-party practical guide to `/loop` and the Desktop scheduler. Useful for concrete workflow examples; **partially stale on specifics**.

## What it contributes (useful)

Concrete, copy-paste workflow examples:

```text
/loop 2m tail the last 20 lines of logs/server.log and summarize any new errors
/loop 5m check how many items are left in the job queue
/loop 10m check if any new GitHub issues have been assigned to me in the anthropic/claude-code repo
```

Best-practice tips:
- Use a cheaper model (`/model haiku`) for reasoning-light monitoring to cut cost.
- "show running cron jobs" to track what is executing.
- `/loop` = in-session delegation; Desktop scheduler = indefinite persistence.
- Minimum interval is 1 minute.

## Contradictions vs official docs (treat as stale)

> [!gap] This source states figures that the official docs contradict.
> - Claims **3-day** auto-expiration → official docs say **7-day**.
> - Claims jitter is **up to 10%** of the period (cap 15 min) → official docs say up to **30 min** (or half the interval, sub-hourly).
>
> The [[Source - Claude Code Docs Scheduled Tasks|official docs]] are the authority; the feature evolved after this article was written. Use this source for *workflow ideas*, not for exact limits.
