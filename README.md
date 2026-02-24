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

Building with technology in 2026 looks fundamentally different than it did just two years ago. AI assistants have moved from novelty to necessity. Companies expect new hires to work effectively with AI tools, and those who can are dramatically more productive.

**This is not about becoming a software engineer — it's about being able to build solutions with technology and data.**

Whether you become a business analyst, data scientist, product manager, consultant, or entrepreneur, you will need to:
- Build dashboards and data applications
- Automate workflows and processes
- Create prototypes to test ideas
- Collaborate with technical teams using shared tools

Professionals who use AI assistants effectively:
- Build solutions faster while maintaining quality
- Spend less time on technical details and more on business problems
- Debug issues more efficiently with AI-powered analysis
- Learn new technologies faster with AI as a teaching partner

### Professional Workflows Create Professional Results

Every successful team building technology solutions follows a structured workflow. This isn't bureaucracy — it's how teams coordinate, maintain quality, and move quickly without breaking things.

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

The workflow you learn in this tutorial is used at companies from startups to Fortune 500:
- **GitHub** for version control (used by 100M+ developers and teams)
- **Jira** for task tracking (used by 65K+ companies)
- **Streamlit Community Cloud** for deployment (free hosting for data apps)

### Your Competitive Advantage

By completing this tutorial, you will have skills that set you apart:

1. **AI-Assisted Building**: Using Claude Code as a thinking and implementation partner
2. **Spec-Driven Development**: Turning requirements into working solutions systematically
3. **Full Traceability**: Connecting every deliverable to a business requirement
4. **Industry Tooling**: Hands-on experience with the tools companies actually use

These are not "student skills" — these are professional skills that will set you apart in interviews and on the job, regardless of your specific role.

---

**See what you will build:** [E-Commerce Sales Dashboard](https://sales-dashboard-greg-lontok.streamlit.app/) -- a live, deployed analytics dashboard built using this workflow.

## What You Will Learn

By the end of this tutorial, you will be able to:

- Move from a tracked task to a deployed, shareable solution
- Use Claude Code as a thinking and implementation assistant
- Maintain full traceability: Jira issue → commit → push → deploy
- Apply spec-driven development using GitHub's spec-kit

## Tutorial Versions

This tutorial has two versions. Your instructor will tell you which one to follow.

### Version 2 (Current) -- Two-Format Tutorial

The latest version, available in two formats that cover the same material. Both are designed for two 100-minute sessions.

| Format | Best For | Start Here |
|--------|----------|------------|
| [**Version A: Streamlined Walkthrough**](v2/version-a-walkthrough/) | In-class use, step-by-step follow-along | [Session 1](v2/version-a-walkthrough/session-1-setup.md) |
| [**Version B: Comprehensive Guide**](v2/version-b-reference/) | Self-paced learning, pre-reading, reference | [Session 1](v2/version-b-reference/session-1-setup.md) |

See the [Version 2 README](v2/README.md) for details on the differences between formats.

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
| **Cursor** | AI-powered code editor | Leading AI-native IDE |
| **Claude Code** | AI assistant (CLI) | State-of-the-art AI for building |
| **spec-kit** | Spec-driven development toolkit | Modern requirements-to-solution workflow |

## Quick Start

1. Fork this repository to your GitHub account
2. Follow the Session 1 setup guide for your assigned version:
   - **Version 2A:** [Session 1](v2/version-a-walkthrough/session-1-setup.md)
   - **Version 2B:** [Session 1](v2/version-b-reference/session-1-setup.md)
   - **Version 1:** [Session 1](v1/01-session-1-setup.md)
3. Continue with Session 2 to build and deploy the dashboard

## Naming Conventions

This tutorial uses consistent naming conventions:

| Item | Convention | Example |
|------|------------|---------|
| Jira Project Key | UPPERCASE | `ECOM` |
| Jira Issue | KEY-NUMBER | `ECOM-1` |
| Commit Message | KEY-NUMBER: description | `ECOM-1: add sales dashboard` |

## Getting Help

- **During class**: Ask your instructor
- **Outside class**: Post in the Teams channel
- **Technical issues**: Ask Claude Code for help — it can diagnose and fix most problems

## License

This tutorial is provided for educational purposes.
