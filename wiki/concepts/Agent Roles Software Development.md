---
type: concept
title: "Agent Roles — Software Development"
status: developing
created: 2026-05-25
updated: 2026-05-25
tags:
  - AI
  - agents
  - roles
  - software-development
---

# Agent Roles — Software Development

Detailed definitions of each specialized agent in a [[Multi-Agent Development Team]]. Each role maps to a real software company function.

---

## 1. Product Manager Agent

**Role**: Translates a vague user prompt into a precise, testable specification.

**System prompt ingredients**:
- "Never code — your output is documentation only"
- "If the prompt is ambiguous, ask one clarifying question before writing"
- "Scope creep is a bug — mark everything out-of-scope explicitly"

**Inputs**: Raw user prompt (natural language)
**Outputs**: `prd.md` containing:
- Problem statement (2–3 sentences)
- User stories (`As a [user], I want [feature] so that [value]`)
- Acceptance criteria (testable `Given/When/Then`)
- Out-of-scope items
- Tech constraints (language, framework, environment)

**Model**: Opus 4.7 — ambiguity resolution requires best judgment.

---

## 2. Architect Agent

**Role**: Translates the PRD into a technical blueprint that engineers can implement without guessing.

**System prompt ingredients**:
- "Read the PRD fully before writing anything"
- "Prefer simple, boring technology. Don't over-engineer."
- "Define all API contracts and data models explicitly"

**Inputs**: `prd.md`
**Outputs**: `architecture.md` containing:
- System diagram (ASCII or Mermaid)
- Component list with responsibilities
- File/folder structure
- API contracts (endpoint, method, request/response schema)
- Data models
- Tech stack decisions with rationale

**Model**: Opus 4.7 — structural mistakes compound into expensive rewrites.

---

## 3. Project Manager Agent (optional)

**Role**: Decomposes the architecture into discrete, parallelizable implementation tasks.

**When to include**: When the project has 5+ components or multiple engineer agents working in parallel.

**Inputs**: `architecture.md`
**Outputs**: `tasks.md` — ordered task list with:
- Task ID
- Description
- Dependencies (which task IDs must complete first)
- Assigned agent (engineer-1, engineer-2, etc.)
- Estimated complexity (S/M/L)

**Model**: Sonnet 4.6 — task decomposition is structured, doesn't need top-tier reasoning.

---

## 4. Engineer Agent

**Role**: Implements the code. The "worker" in the pipeline — given clear inputs, this agent runs fast and cheap.

**System prompt ingredients**:
- "Implement exactly what is specified. Do not invent features."
- "Write no TODOs, no placeholder comments"
- "All code goes in /src/ following the file structure in architecture.md"
- "Import and use real libraries. Do not stub."

**Inputs**: `architecture.md` (or assigned task from `tasks.md`)
**Outputs**: Working code in `/src/` — fully implemented, no stubs.

**Tools required**: Filesystem MCP (read/write), Code Execution MCP (to verify code runs)

**Multiple engineer agents**: For large projects, spawn one engineer per module/service. Each reads the shared architecture spec but works in a separate directory.

**Model**: Sonnet 4.6 — cost-optimized for iterative implementation.

---

## 5. QA / Tester Agent

**Role**: Verifies the code against the PRD's acceptance criteria. Finds bugs before the reviewer.

**System prompt ingredients**:
- "Test every acceptance criterion in the PRD"
- "Write tests first (as specs), then verify the implementation passes them"
- "Report all failures clearly with expected vs. actual behavior"

**Inputs**: `prd.md` (for acceptance criteria), `/src/` (code to test)
**Outputs**:
- Test files in `/tests/`
- Coverage report
- Bug report (failed criteria) in `/artifacts/bugs.md`

**Tools required**: Code Execution MCP (run tests), Playwright MCP (UI testing)

**Model**: Sonnet 4.6 — test generation is formulaic.

---

## 6. Reviewer Agent

**Role**: Final quality gate before the project ships. Looks for correctness, security, performance, and maintainability issues the engineer and tester might have missed.

**System prompt ingredients**:
- "You are a staff engineer doing a final review. Be thorough but not pedantic."
- "Flag: security vulnerabilities, performance antipatterns, missing error handling, dead code"
- "Apply inline fixes for small issues. File larger issues in /artifacts/review.md."
- "Write the final commit message and PR description"

**Inputs**: All `/src/`, `/tests/`, `prd.md`
**Outputs**: `/artifacts/review.md` + inline fixes + PR created via GitHub MCP

**Model**: Opus 4.7 — final quality gate needs highest accuracy.

---

## Agent Isolation Rule

Each agent should see **only what it needs**:
- PM agent: user prompt only
- Architect: PRD only
- Engineer: architecture spec (+ their task if PM agent is used)
- QA: PRD + code
- Reviewer: code + tests + PRD

Never pass the entire conversation history to every agent — this degrades reasoning quality, increases cost, and blurs role boundaries.

## Related

- [[Multi-Agent Development Team]] — the team structure
- [[Agent Orchestration Frameworks]] — frameworks to run these roles
- [[Research - Full Agent Stack Team Guide]] — full code examples
