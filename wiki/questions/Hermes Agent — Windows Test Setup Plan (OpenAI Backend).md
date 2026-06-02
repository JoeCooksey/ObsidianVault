---
type: guide
title: "Hermes Agent — Windows Test Setup Plan (OpenAI Backend)"
created: 2026-06-02
updated: 2026-06-02
tags:
  - guide
  - ai
  - agents
  - hermes
  - setup
status: developing
related:
  - "[[Hermes Agent]]"
  - "[[Research - Hermes Agent (What It's For, Setup, POCs)]]"
  - "[[Nous Research]]"
  - "[[Persistent Agent Memory]]"
  - "[[Self-Improving Agent Loop]]"
sources:
  - "[[Hermes Agent — Official Site and GitHub]]"
---

# Hermes Agent — Windows Test Setup Plan (OpenAI Backend)

A step-by-step runbook to **kick the tires on [[Hermes Agent]] on this Windows desktop**, using **OpenAI / Codex (GPT-5.x) as the model backend**. This is a *test* install to see it work — not the always-on production setup. For real value, the agent should later move to an always-on host (see [[Research - Hermes Agent (What It's For, Setup, POCs)]] — Hetzner VPS + Telegram is Nous's own reference pattern for Joe's exact LLM-Wiki use case).

> [!warning] Test scope, by design
> Running on the desktop means **no overnight briefings and it dies on reboot** — the compounding value of Hermes (skills + session memory over weeks) only shows up on an always-on box. Use this install to learn the tool and validate the OpenAI backend, then graduate to a VPS.

## Prerequisites

- [ ] **OpenAI API key** with billing enabled (`OPENAI_API_KEY`). Codex = OpenAI's models, so this is the standard OpenAI provider path. Pick a GPT-5.x model id once installed.
- [ ] Windows 11 (this machine). The official Windows installer **bundles Python 3.11, Node.js, ripgrep, ffmpeg, and a portable Git Bash**, so you do *not* need to pre-install those. (Source: [[Hermes Agent — Official Site and GitHub]])
- [ ] ~15–20 min and a terminal you can read script output in.
- [ ] (Optional, for the Telegram test) a phone with Telegram + a bot token from `@BotFather`.

## Step 1 — Verify the install command against the live repo (do not skip)

The install is a **piped remote script**. Before running it:

1. Open the repo in a browser: `https://github.com/NousResearch/hermes-agent`
2. Confirm the current install command and version (the one below is a **2026-06 snapshot**; treat the exact URL/version as needing confirmation).
3. **Read `scripts/install.ps1`** in the repo before piping it to your shell.

> [!gap] Version/stars/command are a 2026-06 capture (v0.15.2, ~177k stars, MIT). Re-verify on the live repo — this is the one step where a stale snapshot bites you.

## Step 2 — Install (Windows PowerShell)

```powershell
# Windows (PowerShell) — bundles Python 3.11, Node.js, ripgrep, ffmpeg, portable Git Bash
iex (irm https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.ps1)
```

"One command to install, one to start." Docs: `hermes-agent.nousresearch.com/docs/`. After it finishes, confirm the CLI is on PATH:

```powershell
hermes --version
```

If `hermes` isn't found, open a new terminal (PATH refresh) or check the installer's reported install dir.

## Step 3 — Point Hermes at the OpenAI / Codex backend

Hermes is **model-agnostic with no lock-in** — you swap backends with `hermes model`, no code changes. Supported providers include OpenAI directly. (Source: [[Hermes Agent — Official Site and GitHub]])

1. Set the API key for the session (or store it where Hermes expects — check `hermes --help` / docs for the config path):

   ```powershell
   $env:OPENAI_API_KEY = "sk-..."   # session-scoped; for persistence use the config file
   ```

2. Select the OpenAI provider + a GPT-5.x model:

   ```powershell
   hermes model            # interactive picker: choose OpenAI provider, then the GPT-5.x model
   ```

> [!gap] Exact subcommand flags (non-interactive `hermes model set <provider> <id>`, env var names beyond `OPENAI_API_KEY`, and config file location) are **not confirmed in the captured sources** — confirm in `hermes-agent.nousresearch.com/docs/` rather than trusting a guessed flag.

**Model choice for a test:** start with a mid-tier GPT-5.x for cost while you poke at it; reserve the top model for hard synthesis once you know it works. (Your vault flags "best model" advice as volatile — benchmark on your real workload before committing — see [[Hermes Agent]] gap note.)

## Step 4 — First run (CLI gateway)

```powershell
hermes            # or the start command the installer prints
```

Give it a simple, verifiable goal to confirm the loop + tools work end-to-end, e.g.:

- "Search the web for today's top EE news headline and summarize it in 3 bullets."
- "What files are in C:\Users\joe43\Documents\Joe_Vault\wiki and how many?"

You're checking three things: (1) it decomposes the goal, (2) it selects tools (web/search/filesystem) and executes, (3) it returns a coherent result. This validates the OpenAI backend is wired correctly.

## Step 5 — (Optional) Telegram gateway test

Telegram is the **first-class UX** and the easiest gateway to stand up:

1. In Telegram, message `@BotFather` → `/newbot` → copy the bot token.
2. Configure the token in Hermes (check docs for the gateway config — likely `hermes gateway` / a config entry).
3. Start the gateway and message your bot. Now you can drive the agent from your phone while the desktop runs it.

> [!gap] Exact Telegram gateway config keys/commands not in captured sources — see docs.

## Step 6 — (Optional) Let it see this vault — read-only first

The real payoff is wiring Hermes into this LLM-Wiki. For a **test**, keep it read-only and safe:

- Point it at `C:\Users\joe43\Documents\Joe_Vault\wiki` and ask it to **read and summarize**, *not* write, until you trust it.
- Hermes's own [[Persistent Agent Memory]] (`MEMORY.md`/`USER.md` + FTS5 session search) layers *on top of* the wiki — they complement, they don't replace your existing notes.
- **Do not** let a test instance auto-commit/push to the vault git repo yet. Save the ingest-and-commit loop for the always-on VPS phase, with explicit approval gates.

## Verification checklist

- [ ] `hermes --version` returns a version
- [ ] `hermes model` shows OpenAI selected with a GPT-5.x id
- [ ] A simple goal completes end-to-end with tool use
- [ ] (If tried) Telegram bot responds
- [ ] No secrets written into the vault git repo

## Security hygiene

- Read `install.ps1` before running it (Step 1).
- Keep `OPENAI_API_KEY` and any bot token in env/Hermes config — **never** in a file inside the vault repo that gets committed.
- On a test desktop, prefer the **local execution backend**; reserve Docker sandboxing for when it runs unattended on a public host. (Backends: local, Docker, SSH, Singularity, Modal, Daytona.)

## When to graduate off the desktop

Move to the always-on setup once the test proves out. Target architecture (from [[Research - Hermes Agent (What It's For, Setup, POCs)]]):

- **Host:** small VPS (Hetzner ~€4/mo) — matches Nous's official Joe-pattern user story.
- **Gateway:** Telegram.
- **Memory:** clone the vault repo on the VPS; Hermes ingests → commits → you `git pull` on the desktop.
- **Backend:** Docker (hardened sandbox for unattended runs).
- **Scheduler:** natural-language cron for `/autoresearch`-style briefings + scheduled ingestion.
- **Keep Claude Code** for desk-bound deep coding — they're complements ([[Hermes Agent vs Claude Code vs OpenClaw]]).

## Open items to confirm in live docs

- Non-interactive `hermes model` syntax + config file location.
- Telegram gateway config keys.
- Where Hermes stores `OPENAI_API_KEY` persistently.
- Current install URL + version (re-verify the 2026-06 snapshot).
