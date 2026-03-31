# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is an educational tutorial repository that teaches a professional AI-assisted development workflow. Students build and deploy a Streamlit e-commerce analytics dashboard by following a spec-driven process: PRD → spec-kit artifacts → Jira issues → code → Git → deploy to Streamlit Cloud.

The repo contains no runnable application itself — it's entirely tutorial documentation plus supporting assets (a PRD and sample dataset).

## Repository Structure

```
prd/ecommerce-analytics.md   # Product Requirements Document students build from
data/sales-data.csv          # Sample dataset (1000 transactions, 12 months of 2024)
v1/                          # Original tutorial: two 100-minute in-person sessions
v2/                          # Current tutorial: async pre-work + 3-hour live workshop
  pre-work-setup.md          # Accounts, tools, repo creation (60-90 min self-paced)
  workshop-build-deploy.md   # Full build-and-deploy workflow (live session)
```

`v2/` is the canonical version. `v1/` is preserved as a reference.

## What Students Build

A Streamlit dashboard (`app.py`) loaded from `data/sales-data.csv` with:
- KPI scorecards: Total Sales, Total Orders
- Sales trend line chart (monthly)
- Bar charts: sales by category, sales by region

The dashboard is deployed to Streamlit Community Cloud for a public URL. Expected totals from the sample data: ~$650K–700K sales, 482 orders.

## Workflow Taught

```
PRD → spec-kit (Claude) → Jira issues → feature branch → Claude Code builds → commit → push → PR → merge → Streamlit deploy
```

Key tools in the workflow:
- **spec-kit** (`gh extension install github/spec-kit`): generates constitution, specification, plan, and task files from a PRD
- **Jira MCP**: Claude Code connects to Jira via `claude mcp add` to create and update issues directly from the terminal
- **Streamlit Community Cloud**: deployment target; connects to GitHub and auto-deploys from `main`

## Editing Guidelines

All content is Markdown. When updating tutorial docs:
- Instructions are UI-sensitive — Atlassian, GitHub, and Streamlit UIs change frequently; include caveats like "the UI may look slightly different" when describing specific steps
- Commit messages in examples should follow the pattern `[ISSUE-KEY] short description` (Jira traceability)
- The v2 pre-work and workshop docs are the primary student-facing materials; v1 docs are secondary

## Active Technologies
- Python 3.11 + streamlit, pandas, plotly (001-analytics-dashboard)
- Static CSV file — `data/sales-data.csv` (no database) (001-analytics-dashboard)

## Recent Changes
- 001-analytics-dashboard: Added Python 3.11 + streamlit, pandas, plotly
