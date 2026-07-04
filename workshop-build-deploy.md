# Part 2: Build & Deploy

**From requirements to a live dashboard using skill-driven development.**

**Format:** Self-paced, about 3 hours

---

## Table of contents

- [How to work through this guide](#how-to-work-through-this-guide)
- [Section 1: Set up your task board from the PRD (~15 min)](#section-1-set-up-your-task-board-from-the-prd-15-min)
- [Section 2: Brainstorm and plan (~30 min)](#section-2-brainstorm-and-plan-30-min)
  - [2.1 Create the feature branch](#21-create-the-feature-branch)
  - [2.2 Brainstorm and plan with one prompt](#22-brainstorm-and-plan-with-one-prompt)
- [Section 3: Confirm the plan covers your milestones (~5 min)](#section-3-confirm-the-plan-covers-your-milestones-5-min)
- [Section 4: Build the dashboard (~35 min)](#section-4-build-the-dashboard-35-min)
  - [4.1 Implement the first milestone](#41-implement-the-first-milestone)
  - [4.2 Commit, push, and update TASKS.md](#42-commit-push-and-update-tasksmd)
  - [4.3 Complete remaining milestones](#43-complete-remaining-milestones)
  - [4.4 Capture project memory with /init](#44-capture-project-memory-with-init)
  - [4.5 Merge to main](#45-merge-to-main)
- [Section 5: Deploy (~15 min)](#section-5-deploy-15-min)
- [Section 6: Final verification checklist](#section-6-final-verification-checklist)
- [Troubleshooting](#troubleshooting)
- [Other Superpowers skills you'll meet later](#other-superpowers-skills-youll-meet-later)
- [Glossary](#glossary)

---

## How to work through this guide

This guide is self-paced. Work through it top to bottom; each section builds on the one before it, so don't skip ahead. Most people finish in about three hours, but there's no clock: do it in one sitting or split it across a few sessions, whatever fits your schedule. (The per-section time labels add up to well under three hours because they only count the hands-on steps; the rest is reading, answering brainstorming's questions, and watching Claude build.) You'll save your progress with Git as you go (Section 4), so you can stop and pick up later without losing anything.

> **Didn't finish the setup yet?** Work through the [setup guide](pre-work-setup.md) first; most people finish it in under an hour. Then come back and complete the build here. Ask in the Teams General channel, or send me a direct message on Teams, if you get stuck.

---

## What you'll accomplish

By the end of this guide, you'll have taken a product requirements document through a full development workflow and produced a live analytics dashboard. Specifically, you'll have:

- Set up an in-repo `TASKS.md` board of milestones drawn from the PRD, with a shared Definition of Done
- Generated Superpowers artifacts: a design document and an implementation plan
- Moved each milestone from To Do to Done as you build
- Built a working Streamlit dashboard with AI-assisted coding
- Generated a `CLAUDE.md` with `/init` so the project carries its own context
- Committed and pushed code to GitHub with traceability from each milestone to its commits
- Deployed a live dashboard accessible by anyone with the URL

---

## Prerequisites check

Before starting, verify your Part 1 setup is complete. Open your cloned `ai-dev-workflow-tutorial` folder in Cursor first (File --> Open Folder); the terminal then opens at the project root, which is where these commands expect to run. Run each command in Cursor's terminal:

```bash
git --version
# Expected: git version 2.x.x

python3 --version       # macOS
python --version         # Windows
# Expected: Python 3.11.x or higher

ls data/sales-data.csv
# Windows cmd: dir data\sales-data.csv
# Expected: data/sales-data.csv (no error)

claude --version
# Expected: version number displayed
```

If any command fails, return to the [setup guide](pre-work-setup.md) and resolve the issue before proceeding. Make sure everything's working before you continue.

> **Heads up:** Websites and software update their interfaces regularly. A button label, sign-up flow, or menu option described here may look slightly different by the time you go through it. That's normal. Focus on the goal of each step rather than the exact clicks: once you know what a step is trying to accomplish, you can usually find the equivalent option even when the UI has moved. Read the screen, work it out, and keep going. Figuring things out on your own like this is itself a professional skill.

---

## The professional workflow

This is the workflow used at technology companies worldwide. You'll experience the entire cycle, from specification to deployment. This tutorial calls the approach *skill-driven development*. A *skill* here is a small, reusable piece of expertise Claude pulls in when it fits the task; instead of jumping straight to code, you let a chain of these skills run the work in order (brainstorm the design, plan the steps, then build), so the project has a clear shape before Claude writes anything.

```
┌─────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌────────┐
│   PRD   │ -> │   TASKS.md   │ -> │ brainstorming│ -> │writing-plans │ -> │  Code  │
│(written)│    │ (milestones) │    │ (design doc) │    │ (impl plan)  │    │(Claude)│
└─────────┘    └──────────────┘    └──────────────┘    └──────────────┘    └────────┘
                                                                              │
┌─────────┐    ┌───────────┐    ┌─────────┐    ┌───────────────────────────────┐
│  Live!  │ <- │  Deploy   │ <- │  Push   │ <- │ executing-plans (TDD + commit)│
│(public) │    │(Streamlit)│    │(GitHub) │    │ on a feature branch           │
└─────────┘    └───────────┘    └─────────┘    └───────────────────────────────┘
```

Each box in this diagram is a distinct stage you'll complete. The left-to-right flow on the top row moves from planning to execution. The right-to-left flow on the bottom row moves from saving your work to making it publicly available. Together, they form a closed loop: requirements become running software that stakeholders can access.

> **Why skill-driven development?** You could ask Claude "build me a dashboard" directly. But without a clear plan, Claude makes assumptions, and AI can build the wrong thing very fast. Superpowers' skills give the work structure: brainstorming explores what to build, writing-plans turns the design into a bite-sized plan, and executing-plans implements one task at a time. Letting the skills run their process is what makes AI-assisted coding predictable instead of chaotic. The same habit will help keep a bigger capstone project from drifting.

---

## Section 1: Set up your task board from the PRD (~15 min)

### Tracking work in a file

Professional teams track every piece of work so they always know what's done, what's in progress, and what's next. Many use a web app like Jira for this. In this tutorial, you'll track work in a single Markdown file that lives in your repository: `TASKS.md`.

Here is the difference:

```
Web-app tracker (e.g. Jira)          File-based tracker (TASKS.md)
┌──────────────┐                     ┌──────────────┐
│  Claude Code │                     │  Claude Code │
│  (terminal)  │                     │  (terminal)  │
└──────┬───────┘                     └──────┬───────┘
       │ needs a connector                 │ just opens a file
       │ + account + login                 │
       v                                    v
┌──────────────┐                     ┌──────────────┐
│  Jira (cloud)│                     │  TASKS.md     │
│  separate    │                     │  in your repo │
│  website     │                     │  next to code │
└──────────────┘                     └──────────────┘
```

> **Why track work in a file?** A Markdown file has real advantages for a project like this one:
> - **No extra account or connection.** Claude Code can already read and write files in your project, so it updates your task board directly, with no web app to switch to and no login to keep alive.
> - **Versioned with your code.** `TASKS.md` is committed to Git alongside `app.py`. At any point in history, the task board and the code are in sync. Run `git log -- TASKS.md` and you can see exactly how the work evolved: the same audit trail a tracker like Jira gives you, built into your repo.
> - **Diffable and reviewable.** Changes to tasks show up in your commits and diffs like any other file.
> - **It works offline and travels with the project.** The same file works in Claude Code, Cursor, or any editor.
>
> This is a real, current industry pattern, not a training-wheels version. Teams building with AI coding agents increasingly keep their task lists in the repo so the agent can read and update them directly. (The open-source tool [Backlog.md](https://github.com/MrLesk/Backlog.md) formalizes the same idea at larger scale.)

### Two kinds of "to-do list" (don't mix them up)

As you work, Claude Code shows its own live checklist while it's thinking; you'll see items get checked off in real time. That's an in-session scratchpad (Claude Code calls it the todo list). **It disappears when the session ends or you run `/clear`.**

`TASKS.md` is different. It's the **durable** record you commit to Git. It survives new sessions, grading, and your own memory a month from now. When this guide says "update your task board," it always means the file, not Claude's temporary checklist.

### Steps

1. **Start Claude Code** from your project directory in Cursor's terminal. To open one, go to **Terminal** --> **New Terminal** in the menu bar (or press `` Ctrl+` ``). Then run:

   ```bash
   claude
   ```

   Superpowers loads automatically for the session (you installed and verified it in Part 1). If you're not sure it's active, ask Claude `Is the Superpowers plugin installed?`

2. **Set the output style to Explanatory.** Inside Claude Code, open the settings menu:

   ```
   /config
   ```

   Navigate with the **arrow keys**: highlight **Output style** and press **Enter**, then highlight **Explanatory**, press **Enter** to confirm, and press **Esc** to close the config menu. (Depending on your terminal, you may also be able to click an option with your mouse, but the arrow keys always work.) By default, Claude Code keeps its responses short; the Explanatory style tells Claude to explain what it's doing and why as it works, which helps you learn from it instead of just receiving code. The choice saves to your project's `.claude/settings.local.json` and persists across sessions, so you only set it once.

   > **Prefer editing the file?** You can set the same thing directly by adding `"outputStyle": "Explanatory"` to `.claude/settings.local.json`.

3. **Read the PRD first.** Your task board should reflect what the project needs to deliver, and that's spelled out in the product requirements document.

   > **What is a PRD?** A PRD (Product Requirements Document) is a written description of what you're building and why. It defines the problem, the users, the features, and what success looks like. It doesn't come out of thin air: someone (usually a product manager or business analyst) interviews the stakeholders, the people who will use the product or are paying for it, to learn what they actually need, then writes those needs down as requirements. In professional settings, the PRD is agreed on before any code is written. (For this tutorial, we've written the PRD for you so you can focus on the build; in your capstone, you'll gather requirements from your own stakeholders.)

   Open the [PRD](prd/ecommerce-analytics.md) and skim it (in your browser, or open `prd/ecommerce-analytics.md` in Cursor). Look at two sections in particular: **Acceptance Criteria** and **Timeline and Milestones**. The PRD already sketches the deliverables your board will track; you're not inventing them from scratch.

4. **Create your task board from the PRD.** Ask Claude Code to draft it:

   ```
   Read @prd/ecommerce-analytics.md. Create a TASKS.md file in the project root with:
   - a short note at the top saying this file tracks all work for the dashboard
   - a "Definition of Done" checklist that applies to every milestone: acceptance criteria met; app runs locally with `streamlit run app.py`; changes committed with the milestone ID in the message
   - a "To Do" section with 4-8 milestones based on the PRD's deliverables and its Milestones table, numbered TASK-1, TASK-2, and so on, each with a one-line description and 1-3 acceptance criteria as checkboxes
   - empty "In Progress" and "Done" sections
   ```

   > **The `@` symbol: pointing Claude at a file.** This is the first time you use it. `@prd/ecommerce-analytics.md` tells Claude Code to pull that exact file into the conversation, so it works from the real contents instead of guessing or making you copy and paste them. You can point at a whole folder the same way (like `@docs/superpowers/plans/`). When you type `@`, Claude Code shows a list of files and folders and autocompletes the path as you go, so you rarely type the whole thing. Pointing the AI at the right file is a small habit with a big payoff. You get better output, because the more precisely you set the context, the more on-target the result. And you get faster, cheaper output: because Claude reads just the file you named, it doesn't burn time and tokens (the chunks of text a model processes) searching your project for the right context, which means quicker replies and more headroom before you hit your plan's usage limits. You'll use `@` throughout the rest of this guide.

   Claude reads the PRD and drafts the board. Open `TASKS.md` in Cursor and read it. It should look roughly like this:

   ```markdown
   # Sales Dashboard: Tasks

   This file tracks all work for the e-commerce sales dashboard.
   Each milestone moves through To Do -> In Progress -> Done.

   ## Definition of Done (applies to every milestone)
   - [ ] Acceptance criteria met
   - [ ] App runs locally with `streamlit run app.py`
   - [ ] Changes committed with the milestone ID in the message

   ## To Do
   - [ ] **TASK-1: Project setup and data loading**
     - [ ] App runs with `streamlit run app.py` and shows a title
     - [ ] Loads `data/sales-data.csv`; handles a missing file cleanly
   - [ ] **TASK-2: KPI scorecards**
     - [ ] Total Sales and Total Orders shown as formatted metrics
   - [ ] **TASK-3: Sales trend chart**
     - [ ] Line chart of sales over time renders from the data
   - [ ] **TASK-4: Category and region breakdowns**
     - [ ] Bar charts for sales by category and by region, sorted by value
   - [ ] **TASK-5: Test and deploy**
     - [ ] Dashboard runs without errors and is deployed to a public URL

   ## In Progress

   ## Done
   ```

   Your milestones may differ a little, and that's fine. Read them against the PRD and adjust anything that doesn't match what you want to build. You're aiming for a short list you could read aloud in a status update: the *what*, not the *how*. (Superpowers works out the *how* in the next section.)

   > **What is a Definition of Done?** It's a quality checklist that applies to *every* milestone, no matter what it is. Each milestone also gets its own **acceptance criteria** (the specific thing that milestone must do). The Definition of Done is the shared bar underneath all of them: "before I call anything done, these things are always true." Professional teams agree on a Definition of Done so "done" means the same thing to everyone.

**Checkpoint:** `TASKS.md` exists in your project root with a Definition of Done and 4-8 milestones (TASK-1, TASK-2, ...) in the To Do section, drafted from the PRD.

---

## Section 2: Brainstorm and plan (~30 min)

### Understanding skill-driven development

The rest of the tutorial flows from what you create here. Every step that follows (coding, committing, deploying) depends on the design and plan you produce in this section.

> **The problem with "just code it":** When you ask an AI to build something without a clear design, you get something that might work but probably isn't what you wanted. The AI fills in gaps with assumptions, and each assumption is a potential mismatch with your intent. With a deliverable like an analytics dashboard, even small mismatches compound: the wrong chart type, unexpected aggregation, a layout that doesn't serve the audience.

Superpowers solves this by chaining three skills:

```
brainstorming -> writing-plans -> executing-plans
(design doc)    (impl plan)      (code, tested, committed)
```

Each skill narrows the space of possible outcomes. By the time executing-plans runs, Claude knows what to build, how to build it, and in what order. The result is more likely to match what you actually wanted.

### 2.1 Create the feature branch

You could type the Git command yourself, but you don't have to. In Claude Code, just ask:

```
Create a new git branch called feature/sales-dashboard and switch to it.
```

Claude runs the command and confirms you're on the new branch.

> **This is the whole idea.** You don't memorize Git commands in this tutorial. When you need one, describe what you want and let Claude Code run it. It'll show you the command it used (here, `git checkout -b feature/sales-dashboard`), so you pick up the vocabulary as you go instead of drilling it up front.

Your `main` branch stays clean and stable while you work on the feature branch. Same pattern professional development teams use.

**Checkpoint:** Ask Claude "which branch am I on?" It should be `feature/sales-dashboard`.

### 2.2 Brainstorm and plan with one prompt

This is the moment the workflow shifts from "you driving Claude" to "Claude running a process you observe." You already know the *what*: the milestones on your board. Now you give Claude one prompt; the brainstorming skill activates, asks you questions, writes a design doc, and hands off to writing-plans, which produces an implementation plan for the *how*. You'll see Claude announce each skill switch in the output.

1. In your Claude Code session (still open from Section 1), send this prompt. It points at the PRD and your milestones, and sets a few ground rules so the plan fits this project:

   ```
   Help me design and plan the e-commerce sales dashboard described in @prd/ecommerce-analytics.md. I'm tracking these milestones in @TASKS.md. Structure the plan so its steps cover each one. Ground rules: work on my current feature branch (do not create a git worktree), set up a Python virtual environment in venv/ for dependencies, and keep the code simple and readable so I can follow it.
   ```

2. Watch what happens:

   a. Claude announces `Using brainstorming to design and plan...` (or similar).

   b. Brainstorming asks you 3-5 clarifying questions, one at a time. Topics include things like which KPIs matter most, how interactive the charts should be, and what edge cases to handle. Pick the options that fit your vision. You can answer with the numbered choices or type your own preference.

   c. After the Q&A, brainstorming writes a design doc to `docs/superpowers/specs/YYYY-MM-DD-sales-dashboard-design.md`. Claude shows you a preview and asks if it looks right. If it does, approve it.

   d. Brainstorming would normally create a git worktree at this point (an isolated copy of your working directory; see the skills table at the end of this guide). Because your prompt told it not to, it skips that and hands off directly to writing-plans. You'll see Claude announce `Handing off to writing-plans...`.

   e. writing-plans produces an implementation plan at `docs/superpowers/plans/YYYY-MM-DD-sales-dashboard.md`. The plan contains bite-sized tasks; some are flagged for test-driven development (TDD), typically tasks involving data transformations like KPI calculations and date filtering.

3. Open both files in Cursor and read through them. The design doc captures what to build; the plan captures how to build it, task by task.

> **Why write this down before any code runs?** The hard part of any project is the thinking: framing the problem, choosing an approach, weighing tradeoffs. That's exactly the part it's tempting to hand to the AI, and exactly the part you learn the most from keeping. Writing the spec and plan first forces your reasoning onto the record, where you and a reviewer can see it, instead of letting it disappear into the tool. The two files you just read are that record.

> **Why TDD on some tasks?** Test-driven development means writing a small test before writing the function the test exercises. You write a test that says "compute_total_sales should return $116,500 for this dataset," run it (it fails because the function doesn't exist yet), write the simplest version of the function that makes the test pass, then move on. The discipline matters because it forces you to think about behavior before implementation. For dashboard rendering, TDD doesn't earn its keep: Streamlit components are hard to test meaningfully. For data transformations, it does. The plan flags which tasks get the TDD treatment.

> **Skill handoff cheat sheet (the chain you just experienced):**
>
> ```
> [you type one prompt]
>      |
>      v
> using-superpowers (auto)
>      |
>      v
> brainstorming  -> asks Qs, writes design doc, gets your approval
>      |
>      v  (Phase 5: skipped worktree per your prompt)
> writing-plans  -> produces plan with TDD-flagged tasks
> ```
>
> When you start Section 4 by saying "Let's implement TASK-1," the chain extends:
>
> ```
> executing-plans -> task by task: TDD (where flagged) -> implement -> commit -> push
>      |
>      v  (after the final task, automatically:)
> requesting-code-review -> reviews the diff
> finishing-a-development-branch -> suggests merging to main
> ```
>
> You'll see Claude announce each handoff. If you ever lose track of where you are in the chain, scroll up and look for the most recent `Using <skill> to...` line.

**Checkpoint:** You have two new files: a design doc in `docs/superpowers/specs/` and an implementation plan in `docs/superpowers/plans/`. Both are committed to your feature branch (Superpowers commits the design doc automatically; the plan commit may be combined with the first implementation task).

---

## Section 3: Confirm the plan covers your milestones (~5 min)

### Two artifacts, two altitudes

You now have two planning documents. Being clear on how they relate matters; this is where students most often get confused.

- **`TASKS.md`** holds your **milestones**: the coarse deliverables you drafted from the PRD in Section 1. This is the *what*, and the board you track status on.
- **The implementation plan** (`docs/superpowers/plans/...`) holds the **detailed steps** Superpowers just produced. This is the *how*, and the checklist Claude builds from.

> **The two artifacts, and why they don't overlap:**
>
> | | `TASKS.md` | Implementation plan |
> |---|---|---|
> | **Lives in** | project root | `docs/superpowers/plans/` |
> | **Granularity** | Coarse (~4-8 milestones) | Fine (every engineering step) |
> | **Comes from** | the PRD, up front (Section 1) | brainstorming + the design doc (Section 2) |
> | **Updated by** | you, with Claude's help | Superpowers (`executing-plans` checks steps off as it builds) |
> | **Answers** | "What's the status of the dashboard?" | "What's the next step to code?" |
> | **Audience** | you, your grader, a stakeholder | Claude (the builder) |
>
> `TASKS.md` is the "what and where-are-we." The plan is the "how." One milestone on your board covers several steps in the plan; they're two zoom levels of the same work, not two copies of it. You track from the board; Claude builds from the plan.

```
TASKS.md (your milestones)              Implementation plan (Claude's steps)
┌────────────────────────────┐          ┌────────────────────────────┐
│ TASK-1 Project + data      │ <──────  │ scaffold app.py             │
│        loading             │ <──────  │ add requirements.txt        │
│                            │ <──────  │ load + validate CSV         │
├────────────────────────────┤          ├────────────────────────────┤
│ TASK-2 KPI scorecards      │ <──────  │ compute_total_sales + test  │
│                            │ <──────  │ render KPI metrics          │
├────────────────────────────┤          ├────────────────────────────┤
│ TASK-3 Sales trend chart   │ <──────  │ build trend chart           │
│ ...                        │          │ ...                         │
└────────────────────────────┘          └────────────────────────────┘
  You set these (from the PRD)            Superpowers wrote these (the how)
```

### 3.1 Check the plan lines up with your board

Because you pointed the planning prompt at your milestones, the plan should already cover them. Do a quick check, and record the mapping so each milestone points back to its plan steps.

1. In Claude Code:

   ```
   Compare the implementation plan in @docs/superpowers/plans/ against the milestones in @TASKS.md. For each milestone, note which plan steps cover it by adding "(plan steps X-Y)" after the milestone title. Then tell me if any milestone has no plan steps behind it, or if the plan does something that isn't on my board.
   ```

2. Claude annotates each milestone and flags any gaps. Your To Do section should end up looking like this:

   ```markdown
   ## To Do
   - [ ] **TASK-1: Project setup and data loading** (plan steps 1-3)
     - [ ] App runs with `streamlit run app.py` and shows a title
     - [ ] Loads `data/sales-data.csv`; handles a missing file cleanly
   - [ ] **TASK-2: KPI scorecards** (plan steps 4-6)
     - [ ] Total Sales and Total Orders shown as formatted metrics
   - [ ] **TASK-3: Sales trend chart** (plan steps 7-9)
     - [ ] Line chart of sales over time renders from the data
   ...
   ```

3. If Claude flags a gap (a milestone with no plan behind it, or plan work that maps to no milestone), decide what to do: adjust a milestone, or ask Claude to extend the plan. It's normal for planning to surface something the PRD implied but didn't spell out.

**Checkpoint:** Every milestone in `TASKS.md` notes the plan steps that cover it, and there are no unexplained gaps between the board and the plan.

> **Pro Tip:** Notice the zoom levels. The PRD said "display Total Sales." The plan breaks that into steps ("compute total sales with a test," "render a metric component"). Your board zooms back out to one milestone: "KPI scorecards." Same work, three altitudes: requirement, engineering steps, trackable deliverable. Being able to move between them is a real skill.

---

## Section 4: Build the dashboard (~35 min)

### Understanding Streamlit

> **What is Streamlit?** Streamlit is a Python library that transforms Python scripts into interactive web applications. Instead of writing HTML, CSS, and JavaScript (the traditional technologies for building web pages), you write Python and Streamlit handles the web interface automatically. It's especially popular in data science and business analytics because it lets analysts create dashboards quickly using the language they already know.
>
> For example, this Python code:
> ```python
> import streamlit as st
> st.title("Sales Dashboard")
> st.metric("Total Sales", "$116,500")
> ```
> produces a web page with a title and a formatted metric card. No HTML needed.
>
> Streamlit isn't the only option for dashboards (Tableau, Power BI, and Dash are alternatives), but it works well for capstone projects: it uses pure Python, integrates with Pandas and Plotly, and deploys for free. You can use the same data manipulation skills you learned in your coursework.

### Claude Code editing modes

Before you start building, understand how Claude Code interacts with your files. Claude Code has three editing modes that control how it handles file changes:

| Mode | Behavior | When to Use |
|------|----------|-------------|
| **Normal** (default) | Asks permission before each edit | When learning and reviewing each change carefully |
| **Accept edits** | Makes edits without asking | When you trust the workflow and want momentum |
| **Plan mode** | Explains what it will do, waits for approval, then executes | When you want to review the approach before execution |

Press **Shift+Tab** to cycle between modes. The current mode (for example, "accept edits on" or "plan mode on") shows at the bottom of the Claude Code interface.

> **Recommendation:** Switch to **Accept edits** mode for the build phase. You've already defined detailed specifications, and Claude will follow them. Accept edits lets you maintain momentum through the implementation cycle. If you prefer to review each change (a valid learning choice), stay in Normal mode; it'll just take longer.

### 4.1 Implement the first milestone

Milestones are in plan order, so you'll work top-down: TASK-1 first. Within a milestone, Claude works through the plan steps it covers, one at a time.

1. In Claude Code, start the first milestone and move it to In Progress on your board:

   ```
   Let's work on TASK-1. Move it to the In Progress section of TASKS.md, then implement the plan steps it covers.
   ```

   Claude will recognize this as an implementation task and auto-invoke `executing-plans`. You'll see `Using executing-plans to...` in the output. The skill reads the plan and works through the steps under this milestone, one at a time.

   > **What you'll see during a TDD step:** For plan steps flagged as test-driven (typically data-transformation steps like `compute_total_sales`), executing-plans will: (a) write a failing test in a `tests/` file, (b) run pytest (Python's test runner) and show you the failure, (c) implement the function, (d) run pytest again and show you the pass, (e) commit. For non-TDD steps (chart rendering, page layout), it'll skip straight to implementation and commit. A single milestone may contain several such steps. Watch the test output: seeing red turn green is one of the more satisfying parts of the build.

   > **What happens during implementation:** Claude reads the task and its acceptance criteria, consults the specification and plan, then writes the code. Watch the output; you'll see Claude creating files, writing functions, and making decisions. Pay attention to which libraries Claude imports, how it structures the code, and how it handles data loading.

2. In Claude Code, ask Claude to explain what it created:

   ```
   What files did you create? Explain what each one does.
   ```

   Understanding the file structure helps you learn from the AI's work rather than treating it as a black box.

3. Test the dashboard. Claude set up the `venv/` virtual environment while implementing TASK-1, so it's ready to use. You can either run these commands yourself in Cursor's terminal, or ask Claude Code to do it for you (Option B; if `venv/` isn't there for any reason, Claude will create it).

   **Option A: run it yourself** in Cursor's terminal:

   ```bash
   source venv/bin/activate       # macOS
   # or: venv\Scripts\activate    # Windows

   streamlit run app.py
   ```

   **Option B: ask Claude Code:**

   ```
   Activate my virtual environment and run the Streamlit app so I can test it.
   ```

   > **Key Concept: Virtual Environments.** The `source venv/bin/activate` command activates a **virtual environment**, an isolated Python installation specific to this project. Without it, packages you install might conflict with other Python projects on your machine. The virtual environment ensures that your dashboard's dependencies (Streamlit, Pandas, Plotly) are contained within this project. You'll see `(venv)` at the beginning of your terminal prompt when the environment is active.

4. Open `http://localhost:8501` in your browser. You should see the beginnings of your dashboard: likely a title and confirmation that the data loaded.

5. When done reviewing, press **Ctrl+C** in the terminal to stop the Streamlit server.

**Checkpoint:** The dashboard runs locally at `http://localhost:8501` without errors.

### 4.2 Commit, push, and update TASKS.md

Now you'll save your work using Git and create a traceable link between your code and the task it fulfills. This three-step process (commit, push, update) is the basic rhythm of professional development.

#### Understanding Git's workflow

Git tracks your code changes through a series of stages. Understanding these stages prevents confusion about where your changes "live" at any point:

```
┌─────────────┐    git add    ┌─────────────┐   git commit   ┌─────────────┐
│  Your edits │ ───────────> │   Staging    │ ─────────────> │  Local repo │
│  (working   │              │    Area      │                │  (history)  │
│   directory) │              │              │                │             │
│             │              │  "Ready to   │                │  "Saved     │
│  Files you  │              │   be saved"  │                │   snapshot" │
│  changed    │              │              │                │             │
└─────────────┘              └─────────────┘                └─────────────┘
                                                                   │
                                                              git push
                                                                   │
                                                                   v
                                                            ┌─────────────┐
                                                            │   GitHub    │
                                                            │  (remote)   │
                                                            │             │
                                                            │  "Backed up │
                                                            │   & shared" │
                                                            └─────────────┘
```

Here is what each stage means:

- **Working directory:** the files on your computer as you edit them. Changes here aren't yet tracked by Git.
- **Staging area:** a holding zone for changes you intend to include in your next commit. The `git add` command moves changes here. This is like placing items in a box before sealing it.
- **Local repository:** your project's history of saved snapshots. The `git commit` command creates a new snapshot from everything in the staging area. Each snapshot is permanent and can be revisited.
- **Remote (GitHub):** the cloud copy of your repository. The `git push` command uploads your local commits to GitHub, making them visible to others and serving as a backup.

> **Key Concept: Traceability Through Commit Messages.**
> When you include the milestone ID (like TASK-1) in your commit message, you create a traceable link that connects your code change to the milestone that prompted it:
>
> ```
> TASK-1 in TASKS.md --> Commit "TASK-1: set up project and data loading" --> GitHub --> Deployed Dashboard
> ```
>
> A milestone may span more than one commit (executing-plans commits each plan step as it builds). What matters is that its commits carry the milestone ID and the board records where the work landed. Because `TASKS.md` is versioned too, `git log -- TASKS.md` then shows the full history of how milestones moved from To Do to Done. In professional environments, this traceability is how teams maintain accountability, conduct code reviews, and audit changes.

#### Steps

1. **Commit any outstanding changes.** As it worked through the milestone, executing-plans likely committed each plan step already. This step captures anything still uncommitted (often just your `TASKS.md` update) with the milestone ID. In Claude Code:

   ```
   Commit anything outstanding for TASK-1, including the TASKS.md update, with the milestone ID in the message. Make sure venv/ is in .gitignore.
   ```

   Claude will add `venv/` to `.gitignore` (if not already there), stage the remaining changes, and create a commit with a message like "TASK-1: Set up project structure and dependencies." (If nothing's left to commit, Claude will tell you; that just means the step-by-step commits already covered it.)

   > **Key Concept: .gitignore.** The `.gitignore` file tells Git which files and directories to ignore. Virtual environments (`venv/`), compiled files, and operating system files should never be committed to a repository; they're large, machine-specific, and can be regenerated. The `.gitignore` file prevents accidental commits of these files.

   > **What is a commit hash?** Each commit gets a unique identifier called a **commit hash**, a string like `05a9ada`. It's a fingerprint: no two commits in your repository will ever share one. A milestone may produce several commits; you'll record the last one (or the range) next to the milestone in `TASKS.md` so anyone can find the code that fulfilled it.

2. **Push to GitHub.** In Claude Code, upload your local commit to the remote repository:

   ```
   Push my changes to GitHub.
   ```

   If this is your first push on the feature branch, Claude may need to set the upstream tracking branch. It handles this automatically.

3. **Update your task board.** In Claude Code, close the loop by recording what you did:

   ```
   Update TASK-1 in TASKS.md: check off its acceptance criteria and the Definition of Done, record the commit hash, and move it from In Progress to Done.
   ```

   Claude edits `TASKS.md`, checking the boxes, noting the commit, and moving the milestone into the Done section.

4. **Verify on your board.** Open `TASKS.md` in Cursor and confirm:
   - TASK-1 is now in the Done section
   - Its acceptance criteria and the Definition of Done are checked off
   - The commit hash is recorded next to it

**Checkpoint:** Code is on GitHub. TASK-1 shows in the Done section of `TASKS.md` with its criteria checked and commit recorded.

### 4.3 Complete remaining milestones

Now repeat the cycle for each remaining milestone on your board, in order. If one of your milestones is deployment, skip it for now; that comes in Section 5.

The cycle for each milestone is:

```
Take the next milestone
        |
        v
"Let's work on TASK-N" --> Move to In Progress --> executing-plans works its plan steps
        |
        v
Test the dashboard (streamlit run app.py)
        |
        v
Make sure the milestone's commits carry the milestone ID
        |
        v
Push to GitHub
        |
        v
Update TASKS.md --> check off criteria --> Move to Done
```

Here is the pattern for each milestone. In Claude Code:

```
Let's work on TASK-2. Move it to In Progress in TASKS.md, then implement the plan steps it covers.
```

Claude auto-invokes `executing-plans` and works through the plan steps under the milestone.

After implementation and testing, in Claude Code:

```
Commit anything outstanding for TASK-2 and push to GitHub.

Then update TASK-2 in TASKS.md: check off its acceptance criteria and the Definition of Done, record the commit hash, and move it to Done.
```

Replace `TASK-2` with the current milestone ID. Repeat for TASK-3, TASK-4, and so on.

> **Skip the deployment milestone for now (if you have one).** You can't deploy until your code is merged to `main`, which happens in the next step. Leave any deployment milestone in the To Do section.

> **Pro Tip:** Watch Claude's output as it works each milestone. You'll see files being created, imports being added, and functions being written. This is a good way to learn how professional code is structured. Pay attention to how Claude names variables, organizes functions, and handles data. You can reuse these patterns in your capstone.

After working through all implementation milestones, test the complete dashboard one final time. You can run these yourself or ask Claude Code:

**Option A: run it yourself** in Cursor's terminal:

```bash
source venv/bin/activate       # macOS, if not already active
streamlit run app.py
```

**Option B: ask Claude Code:**

```
Activate my virtual environment and run the Streamlit app so I can test the complete dashboard.
```

Open `http://localhost:8501` and verify that all components are present: KPI scorecards, a sales trend line chart, and category/region bar charts. Press **Ctrl+C** to stop the server.

**Checkpoint:** All implementation milestones are in the Done section of `TASKS.md` with their criteria checked and commits recorded. Only a deployment milestone (if you have one) remains in To Do.

### 4.4 Capture project memory with /init

Your dashboard is built and working, so now is the moment to give your project a memory. You'll generate a `CLAUDE.md`, a file Claude Code reads at the start of every session, so future sessions (and your capstone) begin with context instead of a blank slate.

> **If Claude offered to merge to main after your last milestone:** hold off. After the final plan step, Superpowers may review the diff and offer to merge (the `finishing-a-development-branch` step). Let it review, but do this `/init` step first so `CLAUDE.md` is part of the merge; then merge in Section 4.5.

> **What is CLAUDE.md, and why now?** `CLAUDE.md` documents your project for the AI: how to run it, where the key files live, the conventions you follow. Claude Code's `/init` command writes one for you by scanning your code. That's why you do it *now* and not at the start: at the start there's nothing to describe; now it can capture your actual project. It also pays off on a team: because `CLAUDE.md` is committed to the repo, every teammate's Claude Code session reads the same file, so everyone (and their AI) follows the same setup, conventions, and structure. That keeps development consistent, and a new teammate gets up to speed from one file instead of asking around.

1. In Claude Code, run:

   ```
   /init
   ```

2. Claude scans your project and writes `CLAUDE.md` to the repo root. Open it in Cursor and read it; it should describe your dashboard: how to run it (`streamlit run app.py`), the main files, and where the data lives. Fix anything that's off, or ask Claude to adjust it.

3. Commit it. In Claude Code:

   ```
   Commit CLAUDE.md with the message "Add project memory (CLAUDE.md)".
   ```

> **For your capstone:** run `/init` once you have a skeleton of the project, then keep `CLAUDE.md` updated as the project grows. Every new Claude Code session then starts already knowing your project.

**Checkpoint:** `CLAUDE.md` exists at the repo root, describes your dashboard, and is committed.

### 4.5 Merge to main

Your feature branch contains all the implementation work. Now you'll bring those changes into the `main` branch, making them the official version of the code.

> **Key Concept: Merging.**
>
> ```
> main:          A --- B --- C ─────────────── D (merge commit)
>                             \               /
> feature:                     E --- F --- G -
> ```
>
> Your feature branch diverged from `main` at point C. You then made commits E, F, and G on the feature branch. Merging creates a new commit (D) on `main` that incorporates all the changes from the feature branch. After the merge, `main` contains everything: the original code plus all your dashboard work.
>
> This is why feature branches are valuable; they let you develop freely without risking the stable `main` branch. When you're confident your work is complete, you merge once and know that `main` stays reliable.

1. **Confirm your current branch.** In Claude Code:

   ```
   Which git branch am I on?
   ```

   You should be on your feature branch (e.g., `feature/sales-dashboard`).

2. **Merge into main.** In Claude Code:

   ```
   Merge my current feature branch into main
   ```

   Claude switches to `main`, merges the feature branch, and reports the result.

3. **Push main to GitHub.** In Claude Code:

   ```
   Push main to GitHub
   ```

4. **Verify on GitHub:** Open your repository in a browser, select the **main** branch from the branch dropdown, and confirm all dashboard files (app.py, requirements.txt, data directory, etc.) are present.

**Checkpoint:** The `main` branch on GitHub contains all your dashboard code.

---

## Section 5: Deploy (~15 min)

### Why deployment matters

> **Why This Matters:** Building something that only runs on your laptop doesn't deliver value. Deployment makes your work accessible to stakeholders: a manager, a client, or your capstone advisor can open a URL and see your dashboard without installing Python or cloning a repository. Going from analysis to a shared, accessible output is a skill most graduates lack. Many people can build charts in a Jupyter notebook; far fewer can deploy an interactive dashboard that stakeholders actually use.

Deployment is the final stage of the professional workflow. It transforms your local project into a publicly accessible application.

```
┌──────────────┐     Streamlit     ┌──────────────┐     Public URL    ┌──────────────┐
│  Your code   │ ──── Cloud ────> │  Cloud server │ ───────────────> │  Stakeholders│
│  on GitHub   │     reads your   │  runs your    │    anyone with   │  view your   │
│  (main branch)│    code         │  app.py       │    the URL       │  dashboard   │
└──────────────┘                  └──────────────┘                   └──────────────┘
```

### 5.1 Deploy to Streamlit Cloud

Streamlit Community Cloud is a free hosting service specifically designed for Streamlit applications. It reads your code directly from GitHub and runs it on their servers.

> **Prerequisite:** Your code must be merged to `main` (Section 4.5) before deploying. Streamlit Cloud deploys from the `main` branch by default.

1. Go to [share.streamlit.io](https://share.streamlit.io) in your browser.

2. Click **Continue to sign-in** on the landing page, then click **Continue with GitHub** and authorize Streamlit to access your repositories.

   > **First-time sign-in:** If this is your first time using Streamlit Cloud, the process involves a few extra steps after clicking "Continue with GitHub":
   > - You'll authorize Streamlit on GitHub (email-only permissions), then **verify your email** by entering a 6-digit code sent to your email address.
   > - After verification, you'll authorize Streamlit a second time with broader GitHub permissions (repository access, webhooks).
   > - Finally, you'll fill out a short account setup form (name, functional area — choose **Student**, development stage, and country). Click **Continue** to finish.
   >
   > On subsequent sign-ins, you'll skip straight to the dashboard.

3. Click **Create app** in the top-right corner, then select **Deploy a public app from GitHub** on the next page.

4. Configure the deployment:

   | Field | Value |
   |-------|-------|
   | **Repository** | `[your-username]/ai-dev-workflow-tutorial` |
   | **Branch** | `main` |
   | **Main file path** | `app.py` (or wherever your Streamlit entry point is) |
   | **App URL** (optional) | A custom slug like `sales-dashboard-yourname` — this determines the first part of your public URL |

5. Click **Deploy** and wait 1-2 minutes. Streamlit Cloud installs your dependencies (from `requirements.txt`), runs your app, and makes it available at a public URL.

6. When deployment completes, you receive a URL like:

   ```
   https://sales-dashboard-yourname.streamlit.app
   ```

   Open this URL and verify that your dashboard looks and functions the same as it did locally.

> **If deployment fails:** The most common cause is a missing or incorrect `requirements.txt`. Check that the file exists in your repository's `main` branch on GitHub and lists all required packages (streamlit, pandas, plotly, etc.). If it's missing, ask Claude to create one, commit, push, and redeploy.

### 5.2 Update your task board

Record the deployment on your board. In Claude Code:

```
Add a deployment milestone to TASKS.md if one doesn't exist, record the live Streamlit URL next to it, check off its criteria, and move it to Done. Then commit TASKS.md and push main to GitHub.
```

You're on `main` now (the merge in Section 4.5 switched you there), so this last update commits straight to `main`. Pushing it makes your finished board visible on GitHub, which is what your instructor checks.

**Checkpoint:** The dashboard is live and accessible at a public URL. The deployment milestone is in the Done section of `TASKS.md` with the live URL recorded, and the update is pushed to GitHub.

---

## Section 6: Final verification checklist

Before submitting, walk through every item below. Each category corresponds to a section of this guide.

### Superpowers artifacts

- [ ] Design document created (`docs/superpowers/specs/<file>.md`)
- [ ] Implementation plan created (`docs/superpowers/plans/<file>.md`)

### Task board (TASKS.md)

- [ ] Milestones created from the PRD (4-8 of them: TASK-1, TASK-2, ...), each with acceptance criteria
- [ ] A Definition of Done applies to every milestone
- [ ] All implementation milestones are in the Done section, criteria checked
- [ ] Each done milestone records its commit hash

### Dashboard

- [ ] Runs locally with KPIs, line chart, and bar charts
- [ ] Deployed and publicly accessible on Streamlit Cloud

### Version control

- [ ] Commits include milestone IDs (TASK-1, TASK-2, ...) in messages
- [ ] `CLAUDE.md` generated with `/init` and committed
- [ ] Feature branch merged to main
- [ ] All code pushed to GitHub on the main branch

---

## The complete workflow: what you accomplished

```
PRD [done] -> TASKS.md [done] -> brainstorming [done] -> writing-plans [done] -> Code [done] -> Commit [done] -> Push [done] -> Deploy [done] -> Live! [done]
```

In this guide, you practiced five professional skills:

1. **Skill-driven development:** You brainstormed, planned, broke down tasks, then implemented. This discipline works with any technical project, not just this tutorial.

2. **AI-assisted coding:** You used Claude Code as a tool guided by clear specifications. You saw how context engineering (the `@` symbol, CLAUDE.md, slash commands) makes AI assistance more precise.

3. **Task tracking in your repo:** Every piece of work was tracked from To Do to Done in `TASKS.md`, with each task linked to the commit that fulfilled it.

4. **Version control with Git and GitHub:** You created feature branches, committed with meaningful messages, pushed to a remote, and merged completed work.

5. **Deployment:** You turned a local script into a live application with a shareable URL.

> **For Your Career:** This workflow scales. Whether you're building a data pipeline, a dashboard, or a machine learning model, the pattern is the same: brainstorm, plan, track, build, deploy. You now have hands-on experience with the full cycle. In interviews, you can describe not just what you built but how you built it, and that process awareness matters to hiring managers.

---

## What to submit

**Due: Wednesday, July 15, 2026 at 11:59 PM.** Submit the following to Brightspace under the **AI Dev Workflow Tutorial** assignment:

1. **GitHub repository link:** your public repo URL (e.g., `https://github.com/yourusername/ai-dev-workflow-tutorial`)

2. **Streamlit dashboard link:** your live deployed URL (e.g., `https://sales-dashboard-yourname.streamlit.app`)

3. **Your completed `TASKS.md`:** because the board lives in your repo, there's no screenshot to submit. Just make sure the final `TASKS.md` on your `main` branch shows:
   - Every implementation milestone in the Done section, acceptance criteria checked
   - A commit hash recorded next to each done milestone
   - The Definition of Done checked off

   Your instructor can open `TASKS.md` on GitHub and run `git log -- TASKS.md` to see how the work progressed; that history is your evidence.

Make sure your `TASKS.md`, `prd/`, and `docs/superpowers/` files are included in your repository.

---

## Troubleshooting

Something will break: a command won't run, the app won't start, a push gets rejected. That's normal, and you already have the best debugging tool installed: Claude Code.

**Ask Claude Code first.** It can see your project, read the error, run commands to investigate, and usually fix the problem for you. Give it the specifics:

- Paste the **exact** error message; don't paraphrase it.
- Say what you were trying to do and what you expected to happen.
- If the first fix doesn't work, paste the new error and let it try again.

For example:

```
I ran `streamlit run app.py` and got this error:
<paste the full error here>
What's wrong and how do I fix it?
```

This handles the large majority of what goes wrong here: wrong file paths, a missing package, a port already in use, a rejected push, a merge conflict. Let Claude diagnose before you go hunting through documentation.

**Three habits that fix things before you even ask:**

- **Read the error.** It usually names the problem, and sometimes the fix.
- **Open a new terminal.** This alone clears most "command not found" errors right after you install a tool.
- **Check where you are.** Run `pwd`; Git and Streamlit commands only work inside your project folder.

**Still stuck?** Post in the Teams General channel, or send me a direct message on Teams, with what you were doing, the exact error, and what you already tried. Someone will help.

---

## Other Superpowers skills you'll meet later

You'll encounter these in larger projects beyond this tutorial. We didn't formally use them here either because they're more advanced than this project needs, or because we explicitly told the skill not to (in the brainstorm prompt).

| Skill | What it does | Why we skipped it here |
|-------|--------------|------------------------|
| `using-git-worktrees` | Creates an isolated working directory per branch so multiple branches can be checked out at the same time | We told brainstorming to skip it (in the prompt) to keep this project on a single working directory |
| `dispatching-parallel-agents` | Splits independent tasks across multiple agents that work in parallel | Overkill for a single-project tutorial |
| `subagent-driven-development` | Executes plans by dispatching a fresh subagent per task, with review checkpoints between | A more advanced execution model than executing-plans; same outcome, more moving parts |
| `writing-skills` | Helps you author your own Superpowers skills | Meta. For skill authors, not skill consumers |
| `systematic-debugging` | Walks through a structured debugging process when something breaks | Triggers automatically if your build hits an unexpected error |

If you want to dig deeper, browse the Superpowers skill library: https://github.com/obra/superpowers-skills

---

## Glossary

Quick-reference table of key terms used in this document.

| Term | Definition |
|------|------------|
| **Acceptance Criteria** | The specific, checkable conditions a single milestone must meet to count as complete |
| **brainstorming** | A Superpowers skill that asks clarifying questions about a proposed feature and produces a design document |
| **Branch** | A separate line of development in Git, allowing isolated work without affecting the main codebase |
| **Commit** | A saved snapshot of your project at a specific point in time, like a version you can return to |
| **Commit Hash** | A unique identifier (e.g., `05a9ada`) assigned to each commit, serving as its permanent fingerprint |
| **Definition of Done** | A shared quality checklist that applies to every milestone, on top of each milestone's own acceptance criteria |
| **Deploy** | Make software accessible on a server so users can reach it via a URL |
| **executing-plans** | A Superpowers skill that implements tasks from an implementation plan one at a time, with frequent commits |
| **Feature Branch** | A branch created specifically for developing one feature, separate from main |
| **Fork** | Your personal copy of someone else's repository on GitHub, under your own account |
| **Implementation plan** | The detailed, step-by-step build list `writing-plans` produces in `docs/superpowers/plans/`; Claude builds from it |
| **Merge** | Combine changes from one branch into another, integrating completed work |
| **Milestone** | A coarse, human-facing deliverable on your `TASKS.md` board (TASK-1, TASK-2, ...) that groups several plan steps |
| **PRD** | Product Requirements Document, a written description of what to build and why |
| **Push** | Upload local commits to a remote repository (GitHub), making them visible and backed up |
| **Staging Area** | A holding zone in Git for changes you intend to include in your next commit |
| **Streamlit** | A Python library that transforms Python scripts into interactive web applications |
| **Superpowers** | A Claude Code plugin that gives Claude a library of skills (brainstorming, writing-plans, executing-plans, and more) |
| **TASKS.md** | A Markdown file in your repository that tracks every milestone through To Do, In Progress, and Done |
| **Traceability** | The ability to link code changes back to the requirements that prompted them |
| **venv** | Virtual environment, an isolated Python installation that keeps project dependencies separate |
| **writing-plans** | A Superpowers skill that turns a design document into a bite-sized implementation plan |
| **.gitignore** | A file that tells Git which files and directories to exclude from version control |

---

## What's next

You now have a complete professional workflow you can apply to your capstone project and beyond. The same cycle (brainstorm, plan, track, build, deploy) works for any technical project, whether it's a data pipeline, a machine learning model, or another dashboard. The tools and habits transfer.

> **Can you explain it without Claude in the room?** Getting the dashboard to run is the easy half. The real test is whether you can walk someone through what you built and why, and defend the decisions, with the AI closed. That's what your capstone will ask of you: in advisor check-ins, stakeholder meetings, and presentations, you speak the reasoning, not just show the result. Practice it now: out loud, explain your spec, your plan, and one tradeoff you made. Any part that comes out fuzzy is the part to go back and understand, because the tools and the process here are yours to account for.

> **Bring your meetings into the loop.** In Part 1 you connected Claude Code to [Granola](https://www.granola.ai) (see [Section 2.6 of the setup guide](pre-work-setup.md#26-granola-app--connect-it-to-claude-code)). You didn't need it for the dashboard, but it's built for the capstone: record your stakeholder meetings in Granola, then start a Claude Code session and ask things like *"From this week's meeting notes, what did the client ask us to change?"* or *"Draft tasks in TASKS.md from the decisions in yesterday's kickoff."* The same plan-track-build workflow, now starting from what was actually said in the room.
