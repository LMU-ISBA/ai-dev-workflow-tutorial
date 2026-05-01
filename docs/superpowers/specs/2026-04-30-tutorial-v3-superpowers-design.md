# Tutorial v3: Superpowers replaces spec-kit

**Date:** 2026-04-30
**Status:** Design approved; ready for implementation planning
**Predecessor:** v2 (async pre-work + 3-hour live workshop using spec-kit)

---

## Goal

Create v3 of the AI-Assisted Development Workflow Tutorial, replacing spec-kit with the Superpowers Claude Code plugin. Keep v2's structure, format, and project (e-commerce Streamlit dashboard) intact; change only the planning toolchain in the middle of the workflow.

## Why this version exists

Spec-kit gave v2 a structured pipeline (constitution → spec → plan → tasks), but it required students to memorize and type slash commands (`/speckit.constitution`, `/speckit.specify`, etc.) for each phase. Superpowers offers the same kinds of artifacts through skills that auto-invoke based on the student's prompt, closer to how professional developers work with AI assistants in 2026.

The shift: students stop driving the workflow with explicit commands and start driving it with intent. They prompt Claude with what they want; Claude announces which skill it's using and runs the appropriate process.

## Scope

In scope:
- New `v3/` directory with parallel structure to `v2/` (README, pre-work-setup.md, workshop-build-deploy.md)
- Updated project-root `README.md` promoting v3 to "current"
- A new `v3/CLAUDE.md` that students create early in the workshop
- A `docs/superpowers/specs/` and `docs/superpowers/plans/` directory structure (created by Superpowers skills during the workshop, not pre-populated)

Out of scope:
- Changes to `v1/`, `v2/`, `prd/`, or `data/` (untouched)
- A different project (still the e-commerce dashboard)
- Different external services (still GitHub, Atlassian/Jira, Anthropic, Streamlit Cloud)
- Cursor or Claude Code installation changes (same as v2)

## Decisions log

| Decision | Value | Reasoning |
|----------|-------|-----------|
| Replacement scope | Drop-in swap of spec-kit | Lowest-risk lift; same workflow shape so v2 lessons transfer |
| Slash commands during workflow | None | Skills auto-invoke from natural-language prompts via Superpowers' SessionStart hook |
| Constitution document | Dropped | Superpowers doesn't have an equivalent; principles flow into design doc and CLAUDE.md naturally |
| Git worktrees | No (override default) | Cursor-reopen friction and low transfer value for MSBA audience outweigh the "match the default" benefit |
| Test-driven development | Yes (default) | Real transfer value to data work; Superpowers TDD is pragmatic, not dogmatic |
| `/init` handling | Don't ship CLAUDE.md; have students create it in workshop | Avoids `/init` overwrite risk; makes CLAUDE.md a teachable artifact |
| Design doc location | `docs/superpowers/specs/` (Superpowers default) | Don't fight tooling defaults |
| Plan location | `docs/superpowers/plans/` (Superpowers default) | Same |
| Jira mapping | Each plan task → one Jira issue | Same pattern as v2; only the source file changes |

## Workflow diagram

```
┌─────────┐    ┌──────────────┐    ┌──────────────┐    ┌─────────┐    ┌────────┐
│   PRD   │ -> │ brainstorming│ -> │writing-plans │ -> │  Jira   │ -> │  Code  │
│(written)│    │ (design doc) │    │ (impl plan)  │    │(tracking)│    │(Claude)│
└─────────┘    └──────────────┘    └──────────────┘    └─────────┘    └────────┘
                                                                            │
┌─────────┐    ┌──────────┐    ┌─────────┐    ┌──────────────────────────────┐
│  Live!  │ <- │  Deploy  │ <- │  Push   │ <- │ executing-plans (TDD + commit)│
│(public) │    │(Streamlit)│   │(GitHub) │    │ on a feature branch          │
└─────────┘    └──────────┘    └─────────┘    └──────────────────────────────┘
```

The middle row replaces spec-kit's single box with two Superpowers skills (brainstorming, writing-plans). The bottom row consolidates v2's separate "Code → Commit" boxes into `executing-plans`, which handles task-by-task implementation with TDD cycles and commits as a unified flow.

## File structure

```
ai-dev-workflow-tutorial/
├── README.md                       # update: point to v3 as current; demote v2 to "previous"
├── CLAUDE.md                       # NOT shipped (students create v3/CLAUDE.md during workshop)
├── docs/
│   └── superpowers/
│       ├── specs/
│       │   └── 2026-04-30-tutorial-v3-superpowers-design.md  # this file
│       └── plans/                  # populated when v3 is implemented
├── v1/                             # untouched
├── v2/                             # untouched
└── v3/                             # NEW
    ├── README.md                   # parallels v2/README.md
    ├── pre-work-setup.md           # parallels v2/pre-work-setup.md
    └── workshop-build-deploy.md    # parallels v2/workshop-build-deploy.md
```

`v3/CLAUDE.md` is intentionally absent from the repo. Students create it as an explicit workshop step early in Section 2; this avoids the `/init` overwrite trap and gives students a teachable artifact to author themselves.

## Pre-work changes (v3/pre-work-setup.md)

Inherits v2's structure: accounts → tools → repo setup → verification.

| Section | Change | Rationale |
|---------|--------|-----------|
| Tools table | Remove `spec-kit` row; add `Superpowers` row | Reflects new tooling |
| Account creation | Unchanged | Same external services |
| Tool installs | Unchanged | Same baseline |
| Repo setup | Unchanged | Same project, same data |
| **NEW: Install Superpowers plugin** | Step where students start Claude Code once and run `/plugin install superpowers@claude-plugins-official` inside it | One-time setup; only slash command students type the entire tutorial |
| **NEW: Skills primer** | ~150 words explaining what a Skill is and how Superpowers' SessionStart hook makes auto-invocation work | Without this, the workshop feels like magic |
| Verification block | Add one line: confirm Superpowers loaded by starting Claude Code and looking for the "You have superpowers" message | Catches install failures before workshop |

What gets removed: nothing. Spec-kit was installed during the workshop in v2, not pre-work.

Estimated time: 60-90 min on the student's own (same as v2). The skills primer adds ~5 min of reading; the plugin install is ~30 seconds.

## Workshop changes (v3/workshop-build-deploy.md)

### Section map

| # | Section | Time | Change from v2 |
|---|---------|------|----------------|
| 1 | Connect Claude Code to Jira | 10 min | Unchanged |
| 2 | **Create CLAUDE.md, then Brainstorm + Plan** | 30 min | Rewritten |
| 3 | Create Jira issues from the plan | 10 min | Tweaked (source file changes) |
| 4 | **Execute the plan (TDD)** | 50 min | Expanded |
| 5 | Merge and deploy | 15 min | Unchanged |
| 6 | Final verification | 5 min | Unchanged |

Total guided work: ~120 min in the 2.5-hour build block. ~30 min slack, tighter than v2's ~65 min, but workable. The TDD cycles are the time driver in Section 4.

### Section 2: Create CLAUDE.md, then brainstorm and plan

**2.1 Create the CLAUDE.md file (~3 min)**

Workshop step: students create `v3/CLAUDE.md` and paste the content below. The tutorial explains why each line matters.

```markdown
# Project guidance for Claude

This is an educational tutorial project: an e-commerce Streamlit dashboard
built by MSBA students learning AI-assisted development.

## Workflow conventions
- Work on a feature branch on the main checkout. Do **not** create a git worktree
  for this project, even if the brainstorming skill suggests one.

## Code style
- Python 3.11+; idiomatic pandas; Streamlit components straight from the docs.
- Plain readable code over clever code. Students need to understand it.
```

The tutorial includes a footnote: *"Claude Code has an `/init` command that auto-generates a CLAUDE.md. We're skipping it because we want a small, focused file rather than a generated one. Don't run `/init` for this project."*

**2.2 Create the feature branch (~2 min)**

Standard git: `git checkout -b feature/sales-dashboard`. Same as v2's pre-spec-kit branch creation step.

**2.3 Brainstorm and plan with one prompt (~25 min)**

Single prompt to start the chain:

```
Help me design and plan the e-commerce sales dashboard described in
@prd/ecommerce-analytics.md.
```

What auto-invokes:

1. `using-superpowers` recognizes a creative task → triggers `brainstorming`
2. `brainstorming` asks 3-5 clarifying questions one at a time, then writes a design doc to `docs/superpowers/specs/YYYY-MM-DD-sales-dashboard-design.md`
3. After student approval, brainstorming Phase 5 normally creates a worktree, but `CLAUDE.md` overrides this, so it skips straight to handoff
4. `writing-plans` produces an implementation plan in `docs/superpowers/plans/` with bite-sized tasks; TDD-flagged where it earns its keep (KPI calculations, data filtering, aggregations)

The tutorial includes annotated screenshots of each skill transition. Students see Claude announce "Using brainstorming to..." and "Handing off to writing-plans...". That visibility replaces the explicit slash commands of v2.

### Section 3: Create Jira issues from the plan

Same flow as v2 with a new source file:

```
Based on the implementation plan at @docs/superpowers/plans/<plan-file>.md,
create Jira issues in the ECOM project for each task.
```

Each plan task becomes one Jira issue. The traceability lesson is identical to v2: requirement → plan task → Jira issue → commit → deployed feature.

### Section 4: Execute the plan

Single prompt to start:

```
Let's start implementing ECOM-1.
```

What auto-invokes:

1. `using-superpowers` triggers `executing-plans`
2. For each task, `executing-plans`:
   - Reads the task from the plan
   - For TDD-flagged tasks: invokes `test-driven-development` (write failing test → implement → pass → commit)
   - For non-TDD tasks: implements → commits
   - Each commit message references the Jira issue key
   - Pushes after each task; updates Jira status
3. After the final task, `executing-plans` typically chains into `requesting-code-review` (reviews the diff) and `finishing-a-development-branch` (suggests merge to main)

Students see test failures and successes in real time. For most TDD tasks, a single function gets one or two tests, enough to learn the cycle without bloating the workshop.

### Section 5: Merge and deploy

Three commands: switch to main, merge the feature branch, push. Streamlit Cloud auto-deploys from main as in v2.

### Section 6: Final verification

Same checklist as v2: live URL accessible, all KPIs render, charts respond to filters, Jira issues all closed, every commit traces to an issue.

## Skill handoff sequence (student experience)

```
[student types one prompt]
        │
        ▼
using-superpowers (auto)
        │
        ▼
brainstorming  → asks Qs, writes design doc, gets student approval
        │
        ▼ (Phase 5 handoff, skipping worktree per CLAUDE.md)
writing-plans  → produces plan with TDD-flagged tasks
        │
        ▼ [student creates Jira issues from plan, then prompts Claude to start building]
        ▼
executing-plans → task by task: TDD (where flagged) → implement → commit → push
        │
        ▼ [near final task, automatically:]
        ▼
requesting-code-review → runs review on the diff
finishing-a-development-branch → merges feature branch to main, suggests deploy
```

The tutorial includes a "Skill handoff cheat sheet" sidebar showing this chain so students can orient themselves at any point in the workshop.

## Skills out of scope

Mentioned briefly in an "Other Superpowers skills you'll meet later" appendix; not formally taught:

- `using-git-worktrees` (overridden by CLAUDE.md)
- `dispatching-parallel-agents` (overkill for one project)
- `writing-skills` (meta; for skill authors, not skill consumers)
- `subagent-driven-development` (more advanced than `executing-plans` needs)

## Risks and mitigations

| Risk | Likelihood | Mitigation |
|------|------------|-----------|
| Skill auto-invocation doesn't fire as expected | Medium | Prompt templates in the tutorial use strong intent words ("design", "plan", "implement"); troubleshooting section explains how to nudge with explicit `Skill` tool calls if needed |
| Student runs `/init` despite the footnote, overwriting CLAUDE.md | Low | Recovery line in troubleshooting: `git checkout v3/CLAUDE.md` (works once committed) or recreate from the workshop content |
| TDD cycles overrun the time budget | Medium | Plan tasks pre-flag "test-light" components (chart rendering); workshop guide marks two stretch tasks that can be skipped if running long |
| Superpowers plugin version drift between students | Low | Pre-work pins to `superpowers@claude-plugins-official` (the official channel); troubleshooting section includes update instructions |
| Plan files end up with unexpected names/paths and break the Jira-creation prompt | Low | Tutorial shows a one-liner to find the latest plan file (`ls -t docs/superpowers/plans/`) and use it explicitly with `@` |

## Project-root README updates

Three small edits to the root `README.md`:

1. Update the workflow diagram to match v3's middle row
2. Promote v3 to "current"; demote v2 to "previous"
3. Update the tools table: remove `spec-kit` row, add `Superpowers` row

The "Why this matters," "What you'll build," "Prerequisites," and "Getting help" sections stay verbatim.

## Success criteria

A student completing v3 should:

1. Have the Superpowers plugin installed and a working `using-superpowers` SessionStart hook
2. Have a committed `v3/CLAUDE.md` with the worktree override
3. Have a design doc in `docs/superpowers/specs/` produced by `brainstorming`
4. Have an implementation plan in `docs/superpowers/plans/` produced by `writing-plans`
5. Have one Jira issue per plan task in their ECOM project
6. Have a feature branch with one commit per Jira issue, each commit message referencing its issue key
7. Have a passing test suite covering data-transformation logic
8. Have a live Streamlit dashboard accessible at a public URL, deployed from `main`
9. Be able to articulate the skill handoff chain (brainstorming → writing-plans → executing-plans) in their own words

## Next step

Hand this design to the `writing-plans` skill to produce a detailed implementation plan covering: directory creation, README edits, pre-work doc authoring, workshop doc authoring, screenshot capture for skill-transition visuals, and a verification pass that walks through the full v3 workflow as a student would.
