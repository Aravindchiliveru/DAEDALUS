# DAEDALUS Question Engine v0.2

## Purpose

The Question Engine is the first true research subsystem of DAEDALUS.

Its job is to capture, refine, rank, and track engineering questions before they become projects or products.

## Why Questions First

A weak question creates weak research.

A strong question:

- narrows uncertainty,
- exposes assumptions,
- suggests experiments,
- reveals required expertise,
- and prevents premature product building.

## Core Object: Research Question

A research question represents an uncertainty worth investigating.

### Required fields

- Title
- Question text
- Domain
- Category
- Why it matters
- Current belief
- Known facts
- Unknowns
- Related physics
- Related technologies
- Suggested experiment
- Status
- Review date

### Scoring dimensions

All scores use a 0 to 10 scale.

- Scientific importance
- Engineering impact
- Commercial relevance
- Feasibility
- Novelty
- Capability creation potential
- Urgency

## Lifecycle

```text
Observed
↓
Open
↓
Under Investigation
↓
Experiment Proposed
↓
Experiment Running
↓
Partially Answered
↓
Resolved
↓
Reopened
```

Questions are allowed to reopen because science and technology change.

## API v0.2

Planned endpoints:

```text
GET /questions
POST /questions
GET /questions/{id}
GET /questions/high-priority
```

## v0.2 Success Criteria

DAEDALUS should allow us to:

1. Capture a research question.
2. Rank it objectively.
3. See why it matters.
4. Identify what is known and unknown.
5. Propose the smallest useful experiment.
6. Preserve it for future review.

## Non-goals for v0.2

- No AI question refinement yet.
- No Neo4j.
- No vector search.
- No patent ingestion.
- No paper ingestion.

Those come only after the core question object is stable.
