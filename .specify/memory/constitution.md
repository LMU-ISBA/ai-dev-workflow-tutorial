<!--
Sync Impact Report
==================
Version change: (new) → 1.0.0
Modified principles: N/A (initial creation)
Added sections:
  - Core Principles (4 principles)
  - Technical Standards
  - Development Workflow
  - Governance
Removed sections: N/A (initial creation)
Templates requiring updates:
  - .specify/templates/plan-template.md: ✅ No updates needed (uses generic Constitution Check)
  - .specify/templates/spec-template.md: ✅ No updates needed (technology-agnostic)
  - .specify/templates/tasks-template.md: ✅ No updates needed (uses generic structure)
Follow-up TODOs: None
-->

# ShopSmart E-Commerce Analytics Constitution

## Core Principles

### I. Simple, Readable Code

All code in this project MUST be written with clarity as the primary goal. This means:

- Functions MUST be short and focused on a single responsibility
- Variable and function names MUST be descriptive and self-documenting
- Complex logic MUST include inline comments explaining the "why"
- Code MUST follow PEP 8 style guidelines for Python
- Avoid clever one-liners; prefer explicit, readable constructs

**Rationale**: This is an educational project where students learn development practices. Readable code enables learning, debugging, and collaboration.

### II. User-Friendly Interactive Visualizations

All dashboard components MUST prioritize usability and clarity for non-technical stakeholders:

- Charts MUST have clear titles, axis labels, and legends
- Interactive elements (tooltips, hover states) MUST show relevant data
- Color schemes MUST be consistent and accessible
- Layout MUST be intuitive and require no training to navigate
- All monetary values MUST be formatted appropriately ($X,XXX.XX)

**Rationale**: The dashboard serves executives and managers who need immediate, clear insights without technical interpretation.

### III. Python Best Practices

All Python code MUST adhere to established Python conventions and idioms:

- MUST use type hints for function parameters and return values
- MUST use virtual environment (`venv/`) for dependency isolation
- Dependencies MUST be pinned in `requirements.txt`
- MUST handle errors gracefully with informative messages
- MUST use pathlib for file path operations
- Imports MUST be organized (standard library, third-party, local)

**Rationale**: Following Python conventions ensures maintainability, reduces bugs, and prepares students for professional development environments.

### IV. Minimal Viable Solution

Every implementation MUST solve the immediate requirement without over-engineering:

- MUST implement only what is specified in the PRD Phase 1 scope
- MUST NOT add features "for future use" unless explicitly requested
- MUST prefer standard library and established packages (Streamlit, Pandas, Plotly)
- MUST NOT introduce abstractions until a pattern repeats three or more times
- Configuration MUST be straightforward (avoid complex config systems)

**Rationale**: This project teaches focused, iterative development. Over-engineering obscures learning objectives and delays delivery.

## Technical Standards

### Technology Stack

- **Language**: Python 3.11+
- **Framework**: Streamlit for dashboard UI
- **Visualization**: Plotly for interactive charts
- **Data Processing**: Pandas for data manipulation
- **Data Source**: CSV files (no database required for Phase 1)

### Environment Requirements

- Virtual environment MUST be created using `python -m venv venv`
- Virtual environment directory (`venv/`) MUST be excluded via `.gitignore`
- All dependencies MUST be listed in `requirements.txt`
- Application MUST be deployable to Streamlit Community Cloud

### File Structure

```
├── app.py                 # Main Streamlit application
├── data/
│   └── sales-data.csv     # Source data
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore rules
└── README.md             # Project documentation
```

## Development Workflow

### Commit Standards

- Commit messages MUST include Jira issue key (e.g., `ECOM-1: add sales KPI cards`)
- Commits SHOULD be atomic (one logical change per commit)
- Commit messages MUST describe the "what" and optionally the "why"

### Code Quality Gates

Before any code is merged:

1. Application MUST run without errors (`streamlit run app.py`)
2. All data visualizations MUST render correctly
3. KPI calculations MUST match expected values from data source

### Testing Approach

- Manual testing is acceptable for Phase 1 (no automated test requirement)
- Verify dashboard loads within 5 seconds
- Verify all charts render within 2 seconds
- Verify calculations match sample data expectations

## Governance

This constitution serves as the authoritative guide for all development decisions in this project. All team members and AI assistants MUST follow these principles.

### Amendment Process

1. Propose changes via pull request to this file
2. Document rationale for changes
3. Update version number following semantic versioning:
   - MAJOR: Breaking changes to principles or structure
   - MINOR: New principles or substantial expansions
   - PATCH: Clarifications and minor wording updates
4. Update `LAST_AMENDED_DATE` to current date

### Compliance

- All code reviews MUST verify alignment with these principles
- Complexity beyond these standards MUST be explicitly justified
- When in doubt, prefer simplicity over sophistication

**Version**: 1.0.0 | **Ratified**: 2026-01-25 | **Last Amended**: 2026-01-25
