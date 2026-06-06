---
type: concept
title: "Claude Code /loop Command"
status: stable
created: 2026-06-06
updated: 2026-06-06
tags:
  - concept
  - claude-code
  - automation
  - tooling
related:
  - "[[Claude Code Scheduled Tasks]]"
  - "[[Research - Claude Code loop Command]]"
---

# Claude Code /loop Command

`/loop` is a [bundled skill](https://code.claude.com/docs/en/commands) in Claude Code that re-runs a prompt automatically on a schedule **while the session stays open**. It is the quickest way to poll a deployment, babysit a PR, watch a build, or remind yourself to do something later in the session. Requires Claude Code **v2.1.72 or later** (`claude --version`). (Source: [[Source - Claude Code Docs Scheduled Tasks]])

> [!tip] The one-line mental model
> `/loop [interval] [prompt]` — **both arguments are optional**, and what you supply decides the behavior.

## The three forms

| What you provide | Example | What happens |
| :-- | :-- | :-- |
| Interval **and** prompt | `/loop 5m check the deploy` | Prompt runs on a **fixed schedule** |
| Prompt only | `/loop check the deploy` | Prompt runs at an **interval Claude chooses** each iteration (self-paced) |
| Interval only, or nothing | `/loop` | Runs the **built-in maintenance prompt** (or your `loop.md` if one exists) |

(Source: [[Source - Claude Code Docs Scheduled Tasks]], confidence: high)

## 1. Fixed interval

Supply an interval and Claude converts it to a cron expression, schedules the job, and confirms the cadence + job ID.

```text
/loop 5m check if the deployment finished and tell me what happened
```

- The interval can **lead** as a bare token (`30m`) or **trail** as a clause (`every 2 hours`).
- Supported units: `s` seconds, `m` minutes, `h` hours, `d` days.
- Seconds round **up** to the nearest minute (cron is one-minute granular).
- Odd intervals (`7m`, `90m`) round to the nearest clean cron step, and Claude tells you what it picked.
- You can pass another command as the prompt: `/loop 20m /review-pr 1234` re-runs a saved skill each iteration.

## 2. Self-paced (let Claude choose the interval)

Omit the interval and Claude picks a delay **between 1 minute and 1 hour** after each iteration, based on what it observed — short waits while a build is finishing or a PR is active, longer waits when nothing is pending. The chosen delay and the reason are printed at the end of each iteration.

```text
/loop check whether CI passed and address any review comments
```

- Claude may use the [Monitor tool](https://code.claude.com/docs/en/tools-reference#monitor-tool) directly for a dynamic loop — it streams a background script's output instead of polling, which is more token-efficient and responsive.
- Self-paced loops appear in the scheduled-task list like any other and can be listed/cancelled the same way.
- [Jitter](#scheduling-details) does **not** apply, but the 7-day expiry does.
- Claude can **end the loop on its own** by not scheduling the next wakeup once the task is provably complete.

> [!note] Bedrock / Vertex AI / Microsoft Foundry
> A prompt with no interval runs on a fixed **10-minute** schedule instead of being self-paced.

## 3. Bare `/loop` — the maintenance prompt

With no prompt, Claude runs a built-in maintenance prompt at a dynamically chosen interval. Each iteration works through, in order:

1. continue any unfinished work from the conversation
2. tend to the current branch's PR — review comments, failed CI, merge conflicts
3. run cleanup passes (bug hunts, simplification) when nothing else is pending

Claude does **not** start new initiatives outside that scope; irreversible actions (pushing, deleting) only proceed when they continue something the transcript already authorized. Add an interval (`/loop 15m`) to run it on a fixed schedule instead.

## Customize the default with `loop.md`

A `loop.md` file **replaces** the built-in maintenance prompt for bare `/loop`. It is a single default prompt (not a list of tasks) and is ignored whenever you supply a prompt on the command line.

| Path | Scope |
| :-- | :-- |
| `.claude/loop.md` | Project-level. Takes precedence when both exist. |
| `~/.claude/loop.md` | User-level. Applies in any project without its own. |

Plain Markdown, no required structure — write it as if typing the `/loop` prompt directly. Edits take effect on the **next iteration**, so you can refine instructions while a loop runs. Content beyond **25,000 bytes** is truncated.

## Stopping a loop

- Press **`Esc`** while it is waiting for the next iteration — this clears the pending wakeup so it does not fire again.
- `Esc` does **not** affect tasks you scheduled by asking Claude directly (those stay until deleted).
- Fixed-interval loops run until you stop them or **7 days elapse**.
- Self-paced loops also end when Claude decides the task is done.

## Practical patterns

```text
/loop 2m tail the last 20 lines of logs/server.log and summarize any new errors
/loop 5m check how many items are left in the job queue
/loop 10m check if any new GitHub issues have been assigned to me
/loop check whether CI passed and address any review comments   # self-paced
```

- Switch to a cheaper model (`/model haiku`) for reasoning-light monitoring to save cost. (Source: [[Source - Better Stack Claude Code loop Guide]], confidence: medium)
- Minimum interval is **1 minute** (cron granularity).

## Scheduling details

- **7-day expiry**: recurring tasks auto-expire 7 days after creation — they fire one final time, then delete. (Source: [[Source - Claude Code Docs Scheduled Tasks]])
- **Jitter**: recurring tasks fire up to 30 min after the scheduled time (or up to half the interval, for sub-hourly tasks); the offset is deterministic from the task ID.
- **Session-scoped**: tasks only fire while Claude Code is running and idle. A scheduled prompt fires *between* turns, never mid-response. Closing the terminal stops them; starting a fresh conversation clears them; `claude --resume`/`--continue` restores unexpired tasks.
- **No catch-up**: a missed fire runs once when Claude is next idle, not once per missed interval.

> [!gap] A widely-shared third-party guide cites a **3-day** expiry and **10%** jitter. Those figures are **outdated** — the current official docs (v2.1.72+) state 7-day expiry and 30-min jitter. See [[Research - Claude Code loop Command]] for the contradiction.

## When NOT to use `/loop`

`/loop` is for **quick polling during an open session**. For automation that must run unattended, use one of:

- **[[Claude Code Scheduled Tasks|Routines]]** (cloud) — runs on Anthropic infrastructure without your machine
- **Desktop scheduled tasks** — run locally, survive restarts
- **GitHub Actions** — a `schedule` trigger in CI

See [[Claude Code Scheduled Tasks]] for the full comparison, one-shot reminders, and the cron tooling underneath.
