<!--
SYNC IMPACT REPORT
==================
Version change: (unversioned template) → 1.0.0
New constitution — initial ratification.

Principles added:
  I.   CSV-First Data Layer
  II.  File-Watch Reactivity
  III. Visualization-Driven Design
  IV.  Unit-Tested Transformations
  V.   Streamlit Cloud First

Sections added:
  - Tech Stack Constraints
  - Development Workflow
  - Governance

Templates reviewed:
  ✅ .specify/templates/plan-template.md  — Constitution Check section aligns; no changes required
  ✅ .specify/templates/spec-template.md  — Requirement/success-criteria sections compatible; no changes required
  ✅ .specify/templates/tasks-template.md — Task phases align with principles; no changes required

Deferred TODOs:
  None — all placeholders resolved.
-->

# E-Commerce Analytics Dashboard Constitution

## Core Principles

### I. CSV-First Data Layer

All data MUST be sourced exclusively from local CSV files. No relational databases,
external APIs, or live data streams are permitted. The canonical dataset is
`data/sales-data.csv` (columns: `date`, `order_id`, `product`, `category`, `region`,
`quantity`, `unit_price`, `total_amount`). Any additional data sources MUST also be
CSV files co-located in the `data/` directory.

**Rationale**: Keeps the project self-contained and eliminates infrastructure
dependencies, enabling participants to run and deploy the dashboard without provisioning
any external services.

### II. File-Watch Reactivity

The dashboard MUST automatically reload when the source CSV file changes on disk.
Manual refresh buttons for data reloading are prohibited. Streamlit's built-in
`@st.cache_data` with `ttl` or file-hash invalidation MUST be used to implement
this behavior without custom polling loops.

**Rationale**: Demonstrates Streamlit's reactive data model as a first-class feature
while keeping the implementation simple and idiomatic.

### III. Visualization-Driven Design

Every user-facing feature MUST produce a visible chart or KPI metric. Backend
transformation logic exists solely to prepare data for display; no raw tables or
debug output MAY be exposed in the final UI. Required visualizations:
- KPI scorecards: Total Sales, Total Orders
- Sales trend line chart (time series)
- Sales by category bar chart (sorted descending)
- Sales by region bar chart (sorted descending)

**Rationale**: The project's sole purpose is data visualization. Any feature that
does not directly contribute to a chart or KPI is out of scope.

### IV. Unit-Tested Transformations

All data transformation functions (filtering, aggregation, derived metrics) MUST
have corresponding unit tests. UI rendering code (Streamlit widget calls) is exempt
from the unit-test requirement. Tests MUST use `pytest` and live in `tests/unit/`.
No integration or contract tests are required for this project.

**Rationale**: Transformations are the only non-trivial logic in a dashboard app
and are the highest-value target for automated testing.

### V. Streamlit Cloud First

All implementation decisions MUST target compatibility with Streamlit Community Cloud
(free tier). This means:
- No Docker, server processes, or system-level dependencies
- Dependencies declared in `requirements.txt` only (no `pyproject.toml` extras
  that Streamlit Cloud does not support without a packages.txt)
- Secrets MUST use `st.secrets` or environment variables — never hardcoded
- The app MUST be deployable from the GitHub repo root with zero manual config
  beyond connecting the repo in Streamlit Cloud

**Rationale**: The deployment target is fixed; optimizing for other environments
introduces unnecessary complexity and diverges from the workshop's learning goals.

## Tech Stack Constraints

| Concern | Requirement |
|---------|-------------|
| Language | Python 3.11+ |
| Package manager | `uv` for local development |
| Web framework | Streamlit (latest stable) |
| Charting | Plotly Express |
| Data manipulation | pandas |
| Testing | pytest (unit tests only) |
| Deployment | Streamlit Community Cloud |

No additional runtime dependencies MAY be introduced without explicit justification
against these constraints. All dependencies MUST be pinned in `requirements.txt`.

## Development Workflow

1. **Spec first**: A `spec.md` MUST exist before any implementation begins.
2. **Plan before code**: A `plan.md` MUST be approved before tasks are generated.
3. **Tasks drive commits**: Each commit SHOULD reference the task ID it closes.
4. **Traceability**: Commit messages MUST include the Jira issue key when one exists
   (e.g., `feat: add KPI scorecards [ECOM-1]`).
5. **Tests before merge**: All unit tests MUST pass before a feature branch is merged
   to `main`.
6. **Deploy on merge**: Streamlit Cloud deploys automatically from `main`; broken
   deploys MUST be fixed before new feature work begins.

## Governance

This constitution supersedes all other practices and conventions for this project.
Any deviation MUST be recorded in the Complexity Tracking table of the relevant
`plan.md` with explicit justification.

**Amendment procedure**: Amendments require (a) a written rationale, (b) a version
bump per the versioning policy below, and (c) an updated Sync Impact Report.

**Versioning policy**:
- MAJOR — backward-incompatible principle removal or redefinition
- MINOR — new principle or section added / materially expanded
- PATCH — clarifications, wording, non-semantic refinements

**Compliance review**: Every `plan.md` Constitution Check gate MUST explicitly
verify each applicable principle before Phase 0 research begins.

**Version**: 1.0.0 | **Ratified**: 2026-03-16 | **Last Amended**: 2026-03-16
