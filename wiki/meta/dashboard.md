---
type: meta
title: "Dashboard"
created: 2026-04-18
updated: 2026-04-18
tags:
  - meta
---
# Wiki Dashboard

## Recent Activity
```dataview
TABLE type, status, updated FROM "wiki" SORT updated DESC LIMIT 15
```

## Seed Pages (Need Development)
```dataview
LIST FROM "wiki" WHERE status = "seed" SORT updated ASC
```

## Mature / Evergreen Pages
```dataview
LIST FROM "wiki" WHERE status = "mature" OR status = "evergreen" SORT updated DESC
```

## Entities Missing Sources
```dataview
LIST FROM "wiki/entities" WHERE !sources OR length(sources) = 0
```

## Concepts by Domain
```dataview
TABLE domain, complexity, status FROM "wiki/concepts" SORT domain ASC
```

## Papers by Year
```dataview
TABLE year, authors, key_claim FROM "wiki/papers" SORT year DESC
```
