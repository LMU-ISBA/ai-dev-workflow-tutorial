<!--
SYNC IMPACT REPORT
==================
Version change: N/A → 1.0.0 (initial ratification)
Modified principles: N/A (new document)
Added sections:
  - Core Principles (I–V)
  - Tech Stack Constraints
  - Development Workflow
  - Governance
Removed sections: N/A
Templates reviewed:
  - .specify/templates/plan-template.md ✅ aligned (Constitution Check gate present)
  - .specify/templates/spec-template.md ✅ aligned (spec-driven workflow compatible)
  - .specify/templates/tasks-template.md ✅ aligned (phase/story structure compatible)
Follow-up TODOs: None — all placeholders resolved.
-->

# E-Commerce Analytics Dashboard Constitution

## Core Principles

### I. Executive Clarity

The dashboard is designed exclusively for executive stakeholders. Every chart, KPI,
and label MUST communicate a clear business insight at a glance — no raw data tables,
no unexplained jargon, and no visualizations requiring domain expertise to interpret.
If a senior leader cannot derive a meaningful conclusion within seconds, the output
fails this principle.

### II. Data Accuracy (NON-NEGOTIABLE)

All KPIs and chart values MUST exactly reflect the underlying CSV data. Approximations,
undisclosed rounding, and silent data omissions are strictly forbidden. Every
aggregation MUST be reproducible directly from the source file. When in doubt,
show the exact figure.

### III. Spec-Driven Development

Every feature, change, or bug fix MUST begin with a written spec that is approved
before any code is authored. No implementation starts without a corresponding spec
artifact in `specs/`. Specs MUST reference the PRD for traceability.

### IV. Minimal Dependencies

The project MUST use only the libraries necessary for the task at hand. Adding a new
dependency requires explicit justification documented in the relevant spec. Prefer
Python stdlib and already-present packages over introducing new ones. A lower
dependency count is a quality signal — fewer is better.

### V. Static CSV Data Source

The sole data source is a single static CSV file bundled with the repository. The app
MUST NOT connect to databases, external APIs, or any dynamic data source. No real
customer data is permitted in the repo; only sample or synthetic data is allowed.

## Tech Stack Constraints

- **Runtime**: Python 3.x; Streamlit is the sole UI framework
- **Data layer**: `pandas` for all data manipulation; `plotly` permitted for charting
- **Serialization**: No pickled model files — data flows directly from CSV at runtime
- **Dependency management**: `requirements.txt` with pinned versions per app directory
- **New libraries**: MUST be justified in the relevant spec before being added to
  `requirements.txt`

## Development Workflow

All work follows this sequence without exception:

```
PRD → spec (written & approved) → implementation → commit → PR → merge → deploy
```

- A spec MUST exist and be approved before any code is written (Principle III)
- Commit messages MUST follow the pattern `[ISSUE-KEY] short description` for
  Jira traceability
- PRs MUST be reviewed against the spec's acceptance criteria before merge
- The dashboard MUST be locally runnable by loading `data/sales-data.csv` with
  no additional configuration

## Governance

This constitution supersedes all other practices and conventions in this repository.
Amendments MUST be documented with a version bump, a clear rationale, and an updated
`LAST_AMENDED_DATE`. Version bumps follow semantic versioning:

- **MAJOR**: A principle is removed or fundamentally redefined
- **MINOR**: A new principle or section is added or materially expanded
- **PATCH**: Clarifications, wording fixes, or non-semantic refinements

All implementation plans MUST include a Constitution Check gate before Phase 0
research (see `.specify/templates/plan-template.md`). Complexity violations MUST
be logged in the Complexity Tracking table of `plan.md`.

This file (`.specify/memory/constitution.md`) is the authoritative governance
reference for all agents and human reviewers on this project.

**Version**: 1.0.0 | **Ratified**: 2026-03-30 | **Last Amended**: 2026-03-30
