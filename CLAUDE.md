# Joe's Vault — LLM Wiki

Mode: D (Personal / Second Brain) + E (Research) + F (Books)
Purpose: Personal second brain connecting ideas across engineering, math, books, and deep research topics.
Owner: Joe
Created: 2026-04-18

## Structure

```
vault/
├── .raw/                   # Source documents — NEVER modify
│   ├── articles/
│   ├── transcripts/
│   ├── data/
│   └── assets/
│
├── wiki/                   # LLM-maintained knowledge base
│   ├── index.md            # Master catalog — update on every ingest
│   ├── log.md              # Append-only operation log — new entries at TOP
│   ├── hot.md              # ~500-word recent context cache
│   ├── overview.md         # Executive summary of the whole wiki
│   ├── sources/            # One summary page per ingested source
│   ├── entities/           # People, orgs, products
│   │   └── _index.md
│   ├── concepts/           # Ideas, patterns, frameworks
│   │   └── _index.md
│   ├── domains/            # Top-level subject areas
│   │   ├── _index.md
│   │   ├── Engineering.md
│   │   ├── Mathematics.md
│   │   ├── Books.md
│   │   ├── Research.md
│   │   └── Theology.md
│   ├── papers/             # Research paper summaries
│   │   └── _index.md
│   ├── comparisons/        # Side-by-side analyses
│   ├── questions/          # Filed answers to queries
│   └── meta/               # Dashboards, lint reports
│       └── dashboard.md
│
├── _templates/             # Templater templates
├── _attachments/           # Images and PDFs
├── WIKI.md                 # Full schema reference
└── CLAUDE.md               # This file
```

## Conventions

- All notes use YAML frontmatter: type, status, created, updated, tags (minimum)
- Wikilinks use [[Note Name]] format — filenames are unique, no paths needed
- `.raw/` contains source documents — never modify them
- `wiki/index.md` is the master catalog — update on every ingest
- `wiki/log.md` is append-only — new entries go at the TOP, never edit past entries
- Atomic notes — one concept per page, split if covering two things
- Update, don't duplicate — if a page exists, update it

## Cross-Context Reading Order

When reading the wiki from another project:
1. `wiki/hot.md` first (~500 tokens, recent context)
2. `wiki/index.md` second (~1000 tokens, full catalog)
3. `wiki/<domain>/_index.md` for focused domain lookups
4. Individual pages only when needed (100-300 tokens each)

## Operations

- **Ingest**: drop source in `.raw/`, say "ingest [filename]"
- **Query**: ask any question — Claude reads index first, then drills in
- **Lint**: say "lint the wiki" to run a health check
- **Batch ingest**: say "ingest all of these" for multiple sources
