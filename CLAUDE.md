# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is an educational tutorial that teaches students an AI-assisted development workflow using:
- **Claude Code** for AI-assisted building
- **spec-kit** (GitHub's tool) for turning requirements into tasks
- **Jira** for task tracking via Atlassian MCP integration
- **GitHub** for version control
- **Streamlit** for dashboard deployment

Students build a sales dashboard for a fictional e-commerce retailer (ShopSmart) as a learning vehicle.

## Key Workflow

The tutorial teaches this development flow:
```
PRD → spec-kit → Jira → Code → Commit → Push → Deploy
```

1. Start with the PRD at `prd/ecommerce-analytics.md`
2. Use spec-kit commands (`/speckit.constitution`, `/speckit.specify`, `/speckit.plan`, `/speckit.tasks`)
3. Create Jira issues from generated tasks
4. Implement with `/speckit.implement`
5. Commit with Jira keys (e.g., `ECOM-1: add sales dashboard`)
6. Push to GitHub
7. Deploy to Streamlit Community Cloud

## Project Structure

- `docs/` - Tutorial documentation (numbered for reading order)
- `prd/` - Product Requirements Document for the dashboard
- `data/sales-data.csv` - Sample e-commerce data (482 orders, 5 categories, 4 regions)
- `.specify/` - spec-kit configuration (created after `specify init`)
- `.claude/commands/` - spec-kit slash commands (created after `specify init`)
- `specs/` - Generated specifications and tasks (created by spec-kit)

## Data Schema

The `data/sales-data.csv` contains:
- `date`, `order_id`, `product`, `category`, `region`, `quantity`, `unit_price`, `total_amount`
- Categories: Electronics, Accessories, Audio, Wearables, Smart Home
- Regions: North, South, East, West

## Dashboard Requirements

The target Streamlit dashboard includes:
- 2 KPI scorecards (Total Sales, Total Orders)
- 1 line chart (sales trend over time)
- 2 bar charts (sales by category, sales by region)

Tech stack: Python 3.11+, Streamlit, Pandas, Plotly

## Conventions

- **Jira project key**: `ECOM`
- **Commit messages**: Include Jira key (e.g., `ECOM-1: description`)
- **Branches**: Feature branches created by spec-kit (e.g., `001-sales-dashboard`)
- **Virtual environment**: Use `venv/` and ensure it's in `.gitignore`

## Atlassian MCP Integration

Claude Code connects to Jira via MCP:
```bash
claude mcp add --transport sse atlassian https://mcp.atlassian.com/v1/sse
```

Authenticate via `/mcp` command, select `atlassian`, then re-authenticate if needed.

## Active Technologies
- Python 3.11+ + Streamlit (dashboard UI), Pandas (data processing), Plotly (interactive charts) (001-sales-dashboard)
- CSV file (`data/sales-data.csv`) - no database required (001-sales-dashboard)

## Recent Changes
- 001-sales-dashboard: Added Python 3.11+ + Streamlit (dashboard UI), Pandas (data processing), Plotly (interactive charts)
