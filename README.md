# AI-Assisted Development Workflow Tutorial

A hands-on tutorial for establishing a complete, end-to-end, AI-assisted workflow for building technology solutions using Cursor, Claude Code, GitHub, and Jira.

```
┌─────────┐    ┌──────────┐    ┌─────────┐    ┌────────┐
│   PRD   │ →  │ spec-kit │ →  │  Jira   │ →  │  Code  │
└─────────┘    └──────────┘    └─────────┘    └────────┘
                                                  ↓
┌─────────┐    ┌──────────┐    ┌─────────┐    ┌────────┐
│  Live!  │ ←  │  Deploy  │ ←  │  Push   │ ←  │ Commit │
└─────────┘    └──────────┘    └─────────┘    └────────┘
```

## Why This Matters

### The Industry Has Changed

Building with technology in 2026 looks different than it did two years ago. AI assistants have become standard tools. Companies expect new hires to work effectively with them, and those who can get more done.

**This is not about becoming a software engineer -- it is about being able to build solutions with technology and data.**

Whatever role you end up in -- business analyst, data scientist, product manager, consultant, or founder -- you will need to:
- Build dashboards and data applications
- Automate workflows and processes
- Create prototypes to test ideas
- Collaborate with technical teams using shared tools

### Professional Workflows Create Professional Results

Every team building technology solutions follows a structured workflow. This is how teams coordinate, maintain quality, and move quickly without breaking things.

```
┌─────────────────────────────────────────────────────────────┐
│                    Why Workflows Matter                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Without Workflow:              With Workflow:              │
│  ─────────────────              ───────────────             │
│  • "Who changed this?"          • Full audit trail          │
│  • "Is this the latest?"        • Single source of truth    │
│  • "What broke it?"             • Easy to trace and fix     │
│  • "What are we building?"      • Clear requirements        │
│  • Chaos at scale               • Scales to any team size   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

The workflow you learn in this tutorial is used across the industry:
- **GitHub** for version control (used by 100M+ developers and teams)
- **Jira** for task tracking (used by 65K+ companies)
- **Streamlit Community Cloud** for deployment (free hosting for data apps)

### Your Competitive Advantage

By completing this tutorial, you will have:

1. **AI-Assisted Building**: Experience using Claude Code as a development partner
2. **Spec-Driven Development**: A systematic process for turning requirements into working solutions
3. **Full Traceability**: The habit of connecting every deliverable to a business requirement
4. **Industry Tooling**: Hands-on experience with the tools companies actually use

These are professional skills that apply in interviews and on the job, regardless of your specific role.

---

**See what you will build:** [E-Commerce Sales Dashboard](https://sales-dashboard-greg-lontok.streamlit.app/) -- a live, deployed analytics dashboard built using this workflow.

## What You Will Learn

By the end of this tutorial, you will be able to:

- Move from a tracked task to a deployed, shareable solution
- Use Claude Code as a thinking and implementation assistant
- Maintain full traceability: Jira issue → commit → push → deploy
- Apply spec-driven development using GitHub's spec-kit

## Tutorial Versions

This tutorial has two versions. Version 2 is current; Version 1 is the original.

### Version 2 (Current)

The latest version, designed as async pre-work + a 3-hour live workshop. Explains the "why" behind every step, with concept foundations, troubleshooting, and career context.

| Guide | Content | Start Here |
|-------|---------|------------|
| Pre-Work: Setup | Accounts, tools, repo setup (async, 60–90 min) | [pre-work-setup.md](v2/pre-work-setup.md) |
| Workshop: Build & Deploy | Spec-kit, Jira, build, deploy (live, ~3 hours) | [workshop-build-deploy.md](v2/workshop-build-deploy.md) |

### Version 1 (Original) -- Multi-Document Tutorial

The original tutorial, organized as a series of focused documents. Designed for two 100-minute sessions.

| Order | Document | Description |
|:-----:|----------|-------------|
| 1 | [Overview](v1/00-overview.md) | Tutorial objectives and what you'll build |
| 2 | [Session 1: Setup](v1/01-session-1-setup.md) | Account creation and tool installation |
| — | [Terminal Basics](v1/02-terminal-basics.md) | *Reference:* Read if unfamiliar with command line |
| — | [Git Concepts](v1/03-git-concepts.md) | *Reference:* Read if unfamiliar with version control |
| 3 | [Session 2: Workflow](v1/04-session-2-workflow.md) | Complete development workflow |

**Reference Materials:**

| Document | Description |
|----------|-------------|
| [Troubleshooting](v1/05-troubleshooting.md) | Common issues and solutions |
| [Capstone Project Dev Environment](v1/06-capstone-project-dev-environment.md) | Setting up your capstone project |
| [FAQ](v1/07-faq.md) | Frequently asked questions |
| [Glossary](v1/08-glossary.md) | Key terms and definitions |

## Project Materials

| Resource | Description |
|----------|-------------|
| [E-Commerce PRD](prd/ecommerce-analytics.md) | Product requirements document |
| [Sales Data](data/sales-data.csv) | Sample dataset for the dashboard |

## Prerequisites

No prior experience with Git, Jira, or AI tools is required. You should have:

- A computer running macOS or Windows
- Basic Python knowledge
- Familiarity with VS Code (Cursor is VS Code-based)

## Tools You Will Use

| Tool | Purpose | Industry Context |
|------|---------|------------------|
| **GitHub** | Version control and collaboration | Used by 100M+ professionals worldwide |
| **Jira** | Project and task management | Used by 65,000+ companies |
| **Cursor** | AI-powered code editor | VS Code-based editor with AI integration |
| **Claude Code** | AI assistant (CLI) | Terminal-based AI for building and debugging |
| **spec-kit** | Spec-driven development toolkit | Requirements-to-solution workflow |

## Quick Start

1. Fork this repository to your GitHub account
2. Follow the setup guide for your assigned version:
   - **Version 2:** [Pre-Work: Setup](v2/pre-work-setup.md)
   - **Version 1:** [Session 1](v1/01-session-1-setup.md)
3. Continue with the workshop/Session 2 to build and deploy the dashboard

## Naming Conventions

This tutorial uses consistent naming conventions:

| Item | Convention | Example |
|------|------------|---------|
| Jira Project Key | UPPERCASE | `ECOM` |
| Jira Issue | KEY-NUMBER | `ECOM-1` |
| Commit Message | KEY-NUMBER: description | `ECOM-1: add sales dashboard` |

## Getting Help

If you get stuck, try to solve it yourself first. Google the error message, use AI tools to help diagnose the issue, or ask Claude Code directly -- it can troubleshoot most problems. If none of that works:

- **During class**: Ask your instructor
- **Outside class**: Post in the Teams channel

## License

This tutorial is provided for educational purposes.
