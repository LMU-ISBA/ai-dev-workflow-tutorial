# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A tutorial teaching an AI-assisted development workflow. Participants fork this repo and use it as the starting point for building a Streamlit sales dashboard. The repo contains **only documentation and sample data** — no application code exists here yet. Students create the application code during the workshop.

## Repository structure

```
v2/                         # Current version (pre-work + 3-hour workshop)
  pre-work-setup.md         # Account creation, tool installation, repo setup
  workshop-build-deploy.md  # Full build+deploy walkthrough (spec-kit → Jira → code → deploy)
v1/                         # Original multi-session version (8 documents)
prd/ecommerce-analytics.md  # The product requirements document students build from
data/sales-data.csv         # Sample dataset (~1,000 transaction records)
```

## The workflow being taught

PRD → spec-kit → Jira issues → Claude Code (build) → Git commit → GitHub push → Streamlit deploy

Key concepts:
- **Traceability**: Commit messages include Jira issue keys (e.g., `ECOM-1`)
- **Spec-driven development**: spec-kit generates constitution → specification → plan → tasks before any code is written
- **Jira MCP integration**: Claude Code connects to Jira via MCP to create and update issues directly

## What students build

A Streamlit dashboard with:
- KPI scorecards (Total Sales, Total Orders)
- Sales trend line chart
- Sales by category bar chart (sorted descending)
- Sales by region bar chart (sorted descending)

Tech stack used during the workshop: **Python 3.11+, uv (package manager), Streamlit, Plotly, pandas**

Reference implementation: https://sales-dashboard-greg-lontok.streamlit.app/

## Data schema (data/sales-data.csv)

Columns: `date`, `order_id`, `product`, `category`, `region`, `quantity`, `unit_price`, `total_amount`

5 categories: Electronics, Accessories, Audio, Wearables, Smart Home
4 regions: North, South, East, West

## Making changes to tutorial content

All content is Markdown. v2 is the canonical version. When updating instructions, check that screenshots/UI descriptions match current tool UIs (Streamlit Cloud, Jira, GitHub, Claude onboarding flows change frequently — the docs note this explicitly).

## Active Technologies
- Python 3.11+ + Streamlit ≥1.32, pandas ≥2.0, Plotly ≥5.18, pytest ≥8.0 (001-ecommerce-dashboard)
- CSV file (`data/sales-data.csv`) — no database (001-ecommerce-dashboard)

## Recent Changes
- 001-ecommerce-dashboard: Added Python 3.11+ + Streamlit ≥1.32, pandas ≥2.0, Plotly ≥5.18, pytest ≥8.0
