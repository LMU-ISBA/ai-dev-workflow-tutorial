# AI-Assisted Development Workflow Tutorial

This tutorial teaches you a professional development workflow by having you build and deploy a real project: an e-commerce sales dashboard.

You'll work through it in two parts:

| Part | What you do | Time |
|------|-------------|------|
| [Pre-work](pre-work-setup.md) | Set up accounts, install tools, get your repo ready | 55–85 min on your own, before the workshop |
| [Workshop](workshop-build-deploy.md) | Plan with [Superpowers](https://github.com/obra/superpowers), track work in `TASKS.md`, build with Claude Code, deploy live | ~3 hours, live on Zoom |

## Why this matters

Building with technology in 2026 looks different than it did two years ago. AI assistants have moved from experimental to essential, and companies are looking for people who can work with them effectively.

This isn't about becoming a software engineer. It's about being able to build solutions with technology and data -- dashboards, automated workflows, prototypes -- regardless of your specific role. Whether you end up in analytics, consulting, product management, or something else, these skills transfer.

| Traditional approach | AI-assisted approach |
|---------------------|---------------------|
| Search Google, copy from Stack Overflow | Ask Claude Code to explain and implement |
| Hours debugging with print statements | AI analyzes errors and suggests fixes |
| Write boilerplate code manually | AI generates scaffolding; you focus on business logic |
| Learn frameworks by reading documentation | AI teaches you as you build |
| Work alone, limited by your own knowledge | AI as a second perspective when you get stuck |

You're learning this now, at the start of your career. That puts you ahead of many experienced professionals who are still adapting.

## What you'll build

A Streamlit dashboard with KPI scorecards, a sales trend chart, and breakdowns by category and region.

```
┌─────────────────────────────────────────────────────────────┐
│                E-Commerce Sales Dashboard                    │
├────────────────────────────┬────────────────────────────────┤
│       Total Sales          │       Total Orders             │
│       $1,234,567           │       8,432                    │
├────────────────────────────┴────────────────────────────────┤
│                   Sales Trend (Line Chart)                   │
│    $                                                         │
│    │      ╱╲        ╱╲                                       │
│    │     ╱  ╲      ╱  ╲      ╱                              │
│    │    ╱    ╲    ╱    ╲    ╱                               │
│    │   ╱      ╲  ╱      ╲  ╱                                │
│    │  ╱        ╲╱        ╲╱                                 │
│    └──────────────────────────────────────────── time       │
├────────────────────────────┬────────────────────────────────┤
│    Sales by Category       │    Sales by Region             │
│    (Bar Chart)             │    (Bar Chart)                 │
└────────────────────────────┴────────────────────────────────┘
```

See the finished version: https://sales-dashboard-greg-lontok.streamlit.app/

The dashboard itself is straightforward. The point is the workflow you use to build it.

## The workflow

Every technology company uses a variation of this workflow. You'll experience the entire cycle:

```
┌─────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────┐    ┌────────┐
│   PRD   │ -> │ brainstorming│ -> │writing-plans │ -> │ TASKS.md │ -> │  Code  │
│(written)│    │ (design doc) │    │ (impl plan)  │    │(tracking)│    │(Claude)│
└─────────┘    └──────────────┘    └──────────────┘    └──────────┘    └────────┘
                                                                            │
┌─────────┐    ┌──────────┐    ┌─────────┐    ┌──────────────────────────────┐
│  Live!  │ <- │  Deploy  │ <- │  Push   │ <- │ executing-plans (TDD + commit)│
│(public) │    │(Streamlit)│   │(GitHub) │    │ on a feature branch          │
└─────────┘    └──────────┘    └─────────┘    └──────────────────────────────┘
```

1. **PRD** -- Start with a written specification of what to build
2. **brainstorming** -- A Superpowers skill that asks clarifying questions and produces a design document
3. **writing-plans** -- A Superpowers skill that turns the design into a bite-sized implementation plan
4. **TASKS.md** -- Turn the plan into trackable tasks in a Markdown file in your repo
5. **Code** -- Build the feature with Claude Code
6. **Commit** -- Save your changes with a meaningful message linked to the task ID
7. **Push** -- Upload your code to GitHub
8. **Deploy** -- Make your dashboard publicly accessible

## Key concepts

**Traceability.** Every piece of code traces back to a requirement. When you commit, you include the task ID (like TASK-1) in the message, and because `TASKS.md` is versioned in the repo, `git log` shows the whole chain from requirement to code to deployed feature.

**Skill-driven development.** Instead of jumping straight to code, you let Claude's Superpowers skills run a structured process: brainstorming explores what to build, writing-plans turns that into a bite-sized plan, then executing-plans implements task by task. This prevents the most common failure mode: building the wrong thing fast.

**AI as a partner.** Claude Code isn't just a code generator. It helps you understand requirements, plan your approach, write code, debug issues, and learn concepts as you work. You provide direction and judgment; it provides speed and technical knowledge.

## What you need

- Basic Python knowledge (if you've used pandas or written a few scripts, you're fine)
- A computer running macOS or Windows
- No prior experience with Git or AI coding tools

## Where to start

Open [pre-work-setup.md](pre-work-setup.md) and work through it before the workshop.
