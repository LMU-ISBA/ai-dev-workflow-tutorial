# Workshop: Build & Deploy

**From requirements to a live dashboard using skill-driven development.**

**Format:** 3-hour Zoom workshop

---

## Table of contents

- [Workshop agenda](#workshop-agenda)
- [Section 1: Set up your task board (~5 min)](#section-1-set-up-your-task-board-5-min)
- [Section 2: Brainstorm and plan (~30 min)](#section-2-brainstorm-and-plan-30-min)
  - [2.1 Create v4/CLAUDE.md](#21-create-v4claudemd)
  - [2.2 Create the feature branch](#22-create-the-feature-branch)
  - [2.3 Read the PRD](#23-read-the-prd)
  - [2.4 Brainstorm and plan with one prompt](#24-brainstorm-and-plan-with-one-prompt)
- [Section 3: Turn your plan into tasks (~10 min)](#section-3-turn-your-plan-into-tasks-10-min)
- [Section 4: Build the dashboard (~35 min)](#section-4-build-the-dashboard-35-min)
  - [4.1 Implement the first milestone](#41-implement-the-first-milestone)
  - [4.2 Commit, push, and update TASKS.md](#42-commit-push-and-update-tasksmd)
  - [4.3 Complete remaining milestones](#43-complete-remaining-milestones)
  - [4.4 Merge to main](#44-merge-to-main)
- [Section 5: Deploy (~15 min)](#section-5-deploy-15-min)
- [Section 6: Final verification checklist](#section-6-final-verification-checklist)
- [Comprehensive troubleshooting](#comprehensive-troubleshooting)
- [Glossary](#glossary)

---

## Workshop agenda

| Time | Activity |
|------|----------|
| 0:00–0:15 | **Setup check + triage** -- verify pre-work, troubleshoot stragglers |
| 0:15–0:30 | **Live walkthrough** -- everyone watches the plan-to-tasks flow, then does it themselves |
| 0:30–3:00 | **Build at your own pace** -- work through the guide below; ask questions as you go |

> **Didn't finish the pre-work?** Work through the [pre-work setup guide](pre-work-setup.md) first -- most people finish it in under an hour. You can catch up and still complete the build during the workshop. Ask in the Teams General channel if you get stuck.

---

## What you'll accomplish

By the end of this workshop, you'll have taken a product requirements document through a full development workflow and produced a live analytics dashboard. Specifically, you'll have:

- Set up an in-repo `TASKS.md` board with a shared Definition of Done
- Generated Superpowers artifacts: a design document and an implementation plan
- Turned your plan into trackable tasks and moved each one from To Do to Done
- Built a working Streamlit dashboard with AI-assisted coding
- Committed and pushed code to GitHub with traceability from each task to its commit
- Deployed a live dashboard accessible by anyone with the URL

---

## Prerequisites check

Before starting, verify your pre-work setup is complete. Run each command in Cursor's terminal:

```bash
git --version
# Expected: git version 2.x.x

python3 --version       # macOS
python --version         # Windows
# Expected: Python 3.11.x or higher

ls data/sales-data.csv
# Expected: data/sales-data.csv (no error)

claude --version
# Expected: version number displayed
```

If any command fails, return to the [pre-work setup guide](pre-work-setup.md) and resolve the issue before proceeding. Make sure everything's working before you continue.

> **Heads up:** Websites and software update their interfaces regularly. A button label, sign-up flow, or menu option described here may look slightly different by the time you go through it. This is normal -- the core steps stay the same even when the UI changes. If something doesn't match exactly, read the screen, figure out the equivalent step, and keep going. That adaptability is itself a professional skill.

---

## The professional workflow

This is the workflow used at technology companies worldwide. Today you'll experience the entire cycle, from specification to deployment.

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

Each box in this diagram is a distinct stage you'll complete today. The left-to-right flow on the top row moves from planning to execution. The right-to-left flow on the bottom row moves from saving your work to making it publicly available. Together, they form a closed loop: requirements become running software that stakeholders can access.

> **Why skill-driven development?** You could ask Claude "build me a dashboard" directly. But without a clear plan, Claude makes assumptions, and AI can build the wrong thing very fast. Superpowers' skills give the work structure: brainstorming explores what to build, writing-plans turns the design into a bite-sized plan, and executing-plans implements one task at a time. Letting the skills run their process is what makes AI-assisted coding predictable instead of chaotic. In your capstone, this discipline will be the difference between a project that drifts and one that delivers.

---

## Section 1: Set up your task board (~5 min)

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
> - **No extra account or connection.** Claude Code can already read and write files in your project, so it updates your task board directly -- no web app to switch to, no login to keep alive.
> - **Versioned with your code.** `TASKS.md` is committed to Git alongside `app.py`. At any point in history, the task board and the code are in sync. Run `git log -- TASKS.md` and you can see exactly how the work evolved -- the same audit trail a tracker like Jira gives you, built into your repo.
> - **Diffable and reviewable.** Changes to tasks show up in your commits and diffs like any other file.
> - **It works offline and travels with the project.** The same file works in Claude Code, Cursor, or any editor.
>
> This is a real, current industry pattern, not a training-wheels version. Teams building with AI coding agents increasingly keep their task lists in the repo so the agent can read and update them directly. (Tools like [Backlog.md](https://github.com/MrLesk/Backlog.md) and [spec-kit](https://github.com/github/spec-kit) formalize the same idea at larger scale -- more on that at the end.)

### Two kinds of "to-do list" (don't mix them up)

As you work, Claude Code shows its own live checklist while it's thinking -- you'll see items get checked off in real time. That's an in-session scratchpad (Claude Code calls it the todo list). **It disappears when the session ends or you run `/clear`.**

`TASKS.md` is different. It's the **durable** record you commit to Git. It survives new sessions, grading, and your own memory a month from now. When this guide says "update your task board," it always means the file -- not Claude's temporary checklist.

### Steps

1. **Start Claude Code** from your project directory in Cursor's terminal:

   ```bash
   claude
   ```

   Confirm `You have superpowers` appears in the banner. If it doesn't, see the troubleshooting section.

2. **Set the output style to explanatory.** Inside Claude Code, type:

   ```
   /output-style explanatory
   ```

   By default, Claude Code keeps its responses short. Setting the style to "explanatory" tells Claude to explain what it's doing and why, which helps you learn from its work instead of just receiving code. This is especially useful while you're still learning the workflow.

3. **Create the task board.** Ask Claude Code to create the file for you:

   ```
   Create a TASKS.md file in the project root with three sections -- "To Do", "In Progress", and "Done" -- all empty for now. Above them, add a "Definition of Done" checklist that applies to every task: acceptance criteria met; app runs locally with `streamlit run app.py`; changes committed with the task ID in the message. Leave a short note at the top explaining that this file tracks all work for the dashboard.
   ```

   Claude creates `TASKS.md`. Open it in Cursor and read it. It should look roughly like this:

   ```markdown
   # Sales Dashboard -- Tasks

   This file tracks all work for the e-commerce sales dashboard.
   Each task moves through To Do -> In Progress -> Done.

   ## Definition of Done (applies to every task)
   - [ ] Acceptance criteria met
   - [ ] App runs locally with `streamlit run app.py`
   - [ ] Changes committed with the task ID in the message

   ## To Do

   ## In Progress

   ## Done
   ```

   > **What is a Definition of Done?** It's a quality checklist that applies to *every* task, no matter what the task is. Individual tasks each get their own **acceptance criteria** (the specific thing that task must do). The Definition of Done is the shared bar underneath all of them -- "before I call anything done, these things are always true." Professional teams agree on a Definition of Done so "done" means the same thing to everyone. You'll fill the To Do section with real tasks in Section 3.

**Checkpoint:** `TASKS.md` exists in your project root with a Definition of Done and empty To Do / In Progress / Done sections.

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

### 2.1 Create v4/CLAUDE.md

> **What is CLAUDE.md?** It's a file Claude Code reads at the start of every session. It's where you put project-specific guidance: code style, workflow conventions, things you want Claude to remember without you having to repeat them every time. For this project, CLAUDE.md tells Claude three things: track work in `TASKS.md`, skip the worktree setup that brainstorming usually does, and stick to the simple, readable code style that matches the rest of the tutorial.

> **Heads up about `/init`:** Claude Code has an `/init` slash command that auto-generates a CLAUDE.md by scanning your codebase. We're not using it. We want a small, focused file rather than a generated one. Don't run `/init` for this project. If you do run it by accident and it overwrites your CLAUDE.md, recover with `git checkout v4/CLAUDE.md`.

1. In Cursor, create a new file at `v4/CLAUDE.md`.

2. Paste in the following content:

   ```markdown
   # Project guidance for Claude

   This is an educational tutorial project: an e-commerce Streamlit dashboard
   built by MSBA students learning AI-assisted development.

   ## Task tracking
   - The implementation plan in docs/superpowers/plans/ holds the detailed build
     steps. TASKS.md in the project root holds the coarser milestones I track
     (TASK-1, TASK-2, ...). One milestone covers several plan steps.
   - Before building, confirm which milestone we're on and which plan steps it
     covers, then work through those steps.
   - When a milestone's steps are done, move it to Done in TASKS.md, check off its
     acceptance criteria, record the commit(s), and use the milestone ID in the
     commit message.

   ## Workflow conventions
   - Work on a feature branch on the main checkout. Do **not** create a git worktree
     for this project, even if the brainstorming skill suggests one.

   ## Code style
   - Python 3.11+; idiomatic pandas; Streamlit components straight from the docs.
   - Plain readable code over clever code. Students need to understand it.
   ```

3. Save the file.

**Checkpoint:** `v4/CLAUDE.md` exists and contains the task-tracking and worktree guidance.

### 2.2 Create the feature branch

In Cursor's terminal:

```bash
git checkout -b feature/sales-dashboard
```

Your `main` branch stays clean and stable while you work on the feature branch. Same pattern professional development teams use.

**Checkpoint:** `git branch --show-current` returns `feature/sales-dashboard`.

### 2.3 Read the PRD

> **What is a PRD?** A PRD (Product Requirements Document) is a written description of what you're building and why. It defines the problem, the intended users, the features, and what success looks like. In professional settings, a PRD is written before any code, and writing one before you start coding will save your team from scope confusion later.

Open the [PRD](../prd/ecommerce-analytics.md) and skim it. You can read it in your browser or open `prd/ecommerce-analytics.md` in Cursor. You don't need to memorize anything; just get a feel for what the dashboard should do, what data you're working with, and what the expected deliverables are.

This matters because brainstorming is about to ask you questions. You'll make better choices if you already know what you're building.

**Checkpoint:** You've skimmed the PRD and have a general sense of the project scope.

### 2.4 Brainstorm and plan with one prompt

This is the moment the workflow shifts from "you driving Claude" to "Claude running a process you observe." You give Claude one prompt; the brainstorming skill activates, asks you questions, writes a design doc, and hands off to writing-plans, which produces an implementation plan. You'll see Claude announce each skill switch in the output.

1. Start Claude Code from your project directory:

   ```bash
   claude
   ```

   Confirm `You have superpowers` appears in the banner. If it doesn't, see the troubleshooting section.

2. Send Claude this prompt:

   ```
   Help me design and plan the e-commerce sales dashboard described in @prd/ecommerce-analytics.md.
   ```

3. Watch what happens:

   a. Claude announces `Using brainstorming to design and plan...` (or similar).

   b. Brainstorming asks you 3-5 clarifying questions, one at a time. Topics include things like which KPIs matter most, how interactive the charts should be, and what edge cases to handle. Pick the options that fit your vision. You can answer with the numbered choices or type your own preference.

   c. After the Q&A, brainstorming writes a design doc to `docs/superpowers/specs/YYYY-MM-DD-sales-dashboard-design.md`. Claude shows you a preview and asks if it looks right. If it does, approve it.

   d. Brainstorming would normally create a git worktree at this point. Because of `v4/CLAUDE.md`, it skips that and hands off directly to writing-plans. You'll see Claude announce `Handing off to writing-plans...`.

   e. writing-plans produces an implementation plan at `docs/superpowers/plans/YYYY-MM-DD-sales-dashboard.md`. The plan contains bite-sized tasks; some are flagged for test-driven development (TDD), typically tasks involving data transformations like KPI calculations and date filtering.

4. Open both files in Cursor and read through them. The design doc captures what to build; the plan captures how to build it, task by task.

> **Why TDD on some tasks?** Test-driven development means writing a small test before writing the function the test exercises. You write a test that says "compute_total_sales should return $1,234,567 for this dataset," run it (it fails because the function doesn't exist yet), write the simplest version of the function that makes the test pass, then move on. The discipline matters because it forces you to think about behavior before implementation. For dashboard rendering, TDD doesn't earn its keep: Streamlit components are hard to test meaningfully. For data transformations, it does. The plan flags which tasks get the TDD treatment.

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
>      v  (Phase 5: skipped worktree per CLAUDE.md)
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

## Section 3: Turn your plan into tasks (~10 min)

### Connecting planning to tracking

You now have an implementation plan from writing-plans. It's a long, detailed list of small engineering steps in the order Claude should build them. That level of detail is exactly what Claude needs to write code, but it's too fine-grained to *track* -- nobody reports status as "step 14 of 37 done."

So you'll create a second, coarser view: a handful of **milestones** in `TASKS.md`. Each milestone groups several plan steps into one deliverable a person would recognize -- "KPI scorecards," "Deploy." This is the difference between an engineer's checklist and the board a manager watches.

> **The two artifacts, and why they don't overlap:**
>
> | | Implementation plan | `TASKS.md` |
> |---|---|---|
> | **Lives in** | `docs/superpowers/plans/` | project root |
> | **Granularity** | Fine -- every engineering step | Coarse -- ~4-8 milestones |
> | **Written/updated by** | Superpowers (`writing-plans`, then `executing-plans` checks steps off as it builds) | You, with Claude's help |
> | **Answers** | "What's the next step to code?" | "What's the status of the dashboard?" |
> | **Audience** | Claude (the builder) | You, your grader, a stakeholder |
>
> The plan is the "how." `TASKS.md` is the "what and where-are-we." Claude builds from the plan; you track from the board. One milestone on the board covers several steps in the plan -- they're two zoom levels of the same work, not two copies of it.

```
Implementation plan (detail)          TASKS.md (milestones)
┌────────────────────────────┐        ┌────────────────────────────┐
│ [x] scaffold app.py         │  ┐     │ TASK-1  Project + data      │
│ [x] add requirements.txt    │  ├───> │         loading             │
│ [x] load + validate CSV     │  ┘     ├────────────────────────────┤
│ [ ] compute_total_sales +   │  ┐     │ TASK-2  KPI scorecards      │
│     test                    │  ├───> │                             │
│ [ ] render KPI metrics      │  ┘     ├────────────────────────────┤
│ [ ] build trend chart       │  ────> │ TASK-3  Sales trend chart   │
│ ...                         │        │ ...                         │
└────────────────────────────┘        └────────────────────────────┘
  Claude works step by step             You track milestone by milestone
```

### 3.1 Create your milestones from the plan

1. In Claude Code, ask Claude to group the plan into a short list of milestones on the board:

   ```
   Read the implementation plan at @docs/superpowers/plans/<plan-file>.md and group its steps into 4-8 milestone tasks in the To Do section of TASKS.md. Number them TASK-1, TASK-2, and so on. For each milestone, add a one-line description, 1-3 acceptance criteria as checkboxes, and a note of which plan steps it covers. Don't copy every plan step -- keep it to milestones. Leave the Definition of Done unchanged.
   ```

   Replace `<plan-file>` with the actual filename. To find it quickly, run `ls -t docs/superpowers/plans/ | head -1` in your terminal.

   > **How does Claude update the board?** `TASKS.md` is just a file in your project, so Claude Code edits it the same way it edits any other file -- no connector, no login, no special tool. You'll see it announce the edit, and you can watch the file change in Cursor. That directness is the whole point of tracking work in the repo.

2. Claude reads the plan and writes the milestones into `TASKS.md`. Open the file in Cursor and read it. The To Do section should now look something like this:

   ```markdown
   ## To Do
   - [ ] **TASK-1 -- Project setup and data loading** (plan steps 1-3)
     - [ ] App runs with `streamlit run app.py` and shows a title
     - [ ] Loads `data/sales-data.csv`; handles a missing file cleanly
   - [ ] **TASK-2 -- KPI scorecards** (plan steps 4-6)
     - [ ] Shows Total Sales and Total Orders as formatted metrics
   - [ ] **TASK-3 -- Sales trend chart** (plan steps 7-9)
     - [ ] Line chart of sales over time renders from the data
   ...
   ```

   The exact milestones depend on your plan. What matters is that you have a short, readable list -- each milestone with its own acceptance criteria and a pointer back to the plan steps it covers.

3. Read your milestones. If two feel like the same deliverable, ask Claude to merge them; if one is doing too much, split it. You're aiming for a list you could read aloud in a status update.

**Checkpoint:** The To Do section of `TASKS.md` lists 4-8 milestones (TASK-1, TASK-2, ...), each with acceptance criteria and a note of the plan steps it covers.

> **Pro Tip:** Notice the zoom levels. The PRD said "display Total Sales." The plan breaks that into steps ("compute total sales with a test," "render a metric component"). The board zooms back out to one milestone: "KPI scorecards." Same work, three altitudes -- requirement, engineering steps, trackable deliverable. Being able to move between them is a real skill.

---

## Section 4: Build the dashboard (~35 min)

### Understanding Streamlit

> **What is Streamlit?** Streamlit is a Python library that transforms Python scripts into interactive web applications. Instead of writing HTML, CSS, and JavaScript -- the traditional technologies for building web pages -- you write Python and Streamlit handles the web interface automatically. It's especially popular in data science and business analytics because it lets analysts create dashboards quickly using the language they already know.
>
> For example, this Python code:
> ```python
> import streamlit as st
> st.title("Sales Dashboard")
> st.metric("Total Sales", "$650,000")
> ```
> produces a web page with a title and a formatted metric card. No HTML needed.
>
> Streamlit isn't the only option for dashboards (Tableau, Power BI, and Dash are alternatives), but it works well for capstone projects: it uses pure Python, integrates with Pandas and Plotly, and deploys for free. You can use the same data manipulation skills you learned in your coursework.

### Claude Code editing modes

Before you start building, understand how Claude Code interacts with your files. Claude Code has three editing modes that control how it handles file changes:

| Mode | Behavior | When to Use |
|------|----------|-------------|
| **Normal** | Asks permission before each edit | When learning and reviewing each change carefully |
| **Auto-accept** | Makes edits without asking | When you trust the workflow and want momentum |
| **Plan mode** | Explains what it will do, waits for approval, then executes | When you want to review the approach before execution |

Press **Shift+Tab** to cycle between modes. The current mode is displayed in the Claude Code interface.

> **Recommendation for this workshop:** Switch to **Auto-accept** mode for the build phase. You've already defined detailed specifications, and Claude will follow them. Auto-accept lets you maintain momentum through the implementation cycle. If you prefer to review each change (a valid learning choice), stay in Normal mode -- it'll just take longer.

### 4.1 Implement the first milestone

Milestones are in plan order, so you'll work top-down: TASK-1 first. Within a milestone, Claude works through the plan steps it covers, one at a time.

1. In Claude Code, start the first milestone and move it to In Progress on your board:

   ```
   Let's work on TASK-1. Move it to the In Progress section of TASKS.md, then implement the plan steps it covers.
   ```

   Claude will recognize this as an implementation task and auto-invoke `executing-plans`. You'll see `Using executing-plans to...` in the output. The skill reads the plan and works through the steps under this milestone, one at a time.

   > **What you'll see during a TDD step:** For plan steps flagged as test-driven (typically data-transformation steps like `compute_total_sales`), executing-plans will: (a) write a failing test in a `tests/` file, (b) run pytest (Python's test runner) and show you the failure, (c) implement the function, (d) run pytest again and show you the pass, (e) commit. For non-TDD steps (chart rendering, page layout), it'll skip straight to implementation and commit. A single milestone may contain several such steps. Watch the test output: seeing red turn green is one of the more satisfying parts of the workshop.

   > **What happens during implementation:** Claude reads the task and its acceptance criteria, consults the specification and plan, then writes the code. Watch the output -- you'll see Claude creating files, writing functions, and making decisions. Pay attention to which libraries Claude imports, how it structures the code, and how it handles data loading.

2. In Claude Code, ask Claude to explain what it created:

   ```
   What files did you create? Explain what each one does.
   ```

   Understanding the file structure helps you learn from the AI's work rather than treating it as a black box.

3. Test the dashboard. You can either run these commands yourself in Cursor's terminal, or ask Claude Code to do it for you.

   **Option A -- run it yourself** in Cursor's terminal:

   ```bash
   source venv/bin/activate       # macOS
   # or: venv\Scripts\activate    # Windows

   streamlit run app.py
   ```

   **Option B -- ask Claude Code:**

   ```
   Activate my virtual environment and run the Streamlit app so I can test it.
   ```

   > **Key Concept: Virtual Environments.** The `source venv/bin/activate` command activates a **virtual environment** -- an isolated Python installation specific to this project. Without it, packages you install might conflict with other Python projects on your machine. The virtual environment ensures that your dashboard's dependencies (Streamlit, Pandas, Plotly) are contained within this project. You'll see `(venv)` at the beginning of your terminal prompt when the environment is active.

4. Open `http://localhost:8501` in your browser. You should see the beginnings of your dashboard. The exact content depends on which milestone you started with.

5. When done reviewing, press **Ctrl+C** in the terminal to stop the Streamlit server.

**Checkpoint:** The dashboard runs locally at `http://localhost:8501` without errors.

### 4.2 Commit, push, and update TASKS.md

Now you'll save your work using Git and create a traceable link between your code and the task it fulfills. This three-step process -- commit, push, update -- is the basic rhythm of professional development.

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

- **Working directory** -- the files on your computer as you edit them. Changes here aren't yet tracked by Git.
- **Staging area** -- a holding zone for changes you intend to include in your next commit. The `git add` command moves changes here. This is like placing items in a box before sealing it.
- **Local repository** -- your project's history of saved snapshots. The `git commit` command creates a new snapshot from everything in the staging area. Each snapshot is permanent and can be revisited.
- **Remote (GitHub)** -- the cloud copy of your repository. The `git push` command uploads your local commits to GitHub, making them visible to others and serving as a backup.

> **Key Concept: Traceability Through Commit Messages.**
> When you include the milestone ID (like TASK-1) in your commit message, you create a traceable link that connects your code change to the milestone that prompted it:
>
> ```
> TASK-1 in TASKS.md --> Commit "TASK-1: add KPI scorecards" --> GitHub --> Deployed Dashboard
> ```
>
> A milestone may span more than one commit (executing-plans commits each plan step as it builds). What matters is that its commits carry the milestone ID and the board records where the work landed. Because `TASKS.md` is versioned too, `git log -- TASKS.md` then shows the full history of how milestones moved from To Do to Done. In professional environments, this traceability is how teams maintain accountability, conduct code reviews, and audit changes.

#### Steps

1. **Commit any outstanding changes.** As it worked through the milestone, executing-plans likely committed each plan step already. This step captures anything still uncommitted -- often just your `TASKS.md` update -- with the milestone ID. In Claude Code:

   ```
   Commit anything outstanding for TASK-1, including the TASKS.md update, with the milestone ID in the message. Make sure venv/ is in .gitignore.
   ```

   Claude will add `venv/` to `.gitignore` (if not already there), stage the remaining changes, and create a commit with a message like "TASK-1: Set up project structure and dependencies." (If nothing's left to commit, Claude will tell you -- that just means the step-by-step commits already covered it.)

   > **Key Concept: .gitignore.** The `.gitignore` file tells Git which files and directories to ignore. Virtual environments (`venv/`), compiled files, and operating system files should never be committed to a repository -- they're large, machine-specific, and can be regenerated. The `.gitignore` file prevents accidental commits of these files.

   > **What is a commit hash?** Each commit gets a unique identifier called a **commit hash** -- a string like `05a9ada`. It's a fingerprint: no two commits in your repository will ever share one. A milestone may produce several commits; you'll record the last one (or the range) next to the milestone in `TASKS.md` so anyone can find the code that fulfilled it.

2. **Push to GitHub.** In Claude Code, upload your local commit to the remote repository:

   ```
   Push my changes to GitHub.
   ```

   If this is your first push on the feature branch, Claude may need to set the upstream tracking branch. It handles this automatically.

3. **Update your task board.** In Claude Code, close the loop by recording what you did:

   ```
   Update TASK-1 in TASKS.md: check off its acceptance criteria and the Definition of Done, record the commit hash, and move it from In Progress to Done.
   ```

   Claude edits `TASKS.md` -- checking the boxes, noting the commit, and moving the milestone into the Done section.

4. **Verify on your board.** Open `TASKS.md` in Cursor and confirm:
   - TASK-1 is now in the Done section
   - Its acceptance criteria and the Definition of Done are checked off
   - The commit hash is recorded next to it

**Checkpoint:** Code is on GitHub. TASK-1 shows in the Done section of `TASKS.md` with its criteria checked and commit recorded.

### 4.3 Complete remaining milestones

Now repeat the cycle for each remaining milestone on your board, in order. If one of your milestones is deployment, skip it for now -- that comes in Section 5.

The cycle for each milestone is:

```
Take the next milestone
        |
        v
"Let's work on TASK-N" --> executing-plans works its plan steps --> Move to In Progress
        |
        v
Test the dashboard (streamlit run app.py)
        |
        v
Make sure the milestone's commits carry the task ID
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

**Option A -- run it yourself** in Cursor's terminal:

```bash
source venv/bin/activate       # macOS, if not already active
streamlit run app.py
```

**Option B -- ask Claude Code:**

```
Activate my virtual environment and run the Streamlit app so I can test the complete dashboard.
```

Open `http://localhost:8501` and verify that all components are present: KPI scorecards, a sales trend line chart, and category/region bar charts. Press **Ctrl+C** to stop the server.

**Checkpoint:** All implementation milestones are in the Done section of `TASKS.md` with their criteria checked and commits recorded. Only a deployment milestone (if you have one) remains in To Do.

### 4.4 Merge to main

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
> This is why feature branches are valuable -- they let you develop freely without risking the stable `main` branch. When you're confident your work is complete, you merge once and know that `main` stays reliable.

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

> **Why This Matters:** Building something that only runs on your laptop doesn't deliver value. Deployment makes your work accessible to stakeholders -- a manager, a client, or your capstone advisor can open a URL and see your dashboard without installing Python or cloning a repository. Going from analysis to a shared, accessible output is a skill most graduates lack. Many people can build charts in a Jupyter notebook; far fewer can deploy an interactive dashboard that stakeholders actually use.

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

> **Prerequisite:** Your code must be merged to `main` (Section 4.4) before deploying. Streamlit Cloud deploys from the `main` branch by default.

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
Add a deployment milestone to TASKS.md if one doesn't exist, record the live Streamlit URL next to it, check off its criteria, and move it to Done. Then commit TASKS.md.
```

**Checkpoint:** The dashboard is live and accessible at a public URL. The deployment milestone is in the Done section of `TASKS.md` with the live URL recorded.

---

## Section 6: Final verification checklist

Before submitting, walk through every item below. Each category corresponds to a section of this guide.

### Superpowers artifacts

- [ ] Design document created (`docs/superpowers/specs/<file>.md`)
- [ ] Implementation plan created (`docs/superpowers/plans/<file>.md`)

### Task board (TASKS.md)

- [ ] Milestones created from the plan (4-8 of them: TASK-1, TASK-2, ...), each with acceptance criteria
- [ ] A Definition of Done applies to every milestone
- [ ] All implementation milestones are in the Done section, criteria checked
- [ ] Each done milestone records its commit hash

### Dashboard

- [ ] Runs locally with KPIs, line chart, and bar charts
- [ ] Deployed and publicly accessible on Streamlit Cloud

### Version control

- [ ] Commits include task IDs (TASK-1, TASK-2, ...) in messages
- [ ] Feature branch merged to main
- [ ] All code pushed to GitHub on the main branch

---

## The complete workflow -- what you accomplished

```
PRD [done] -> brainstorming [done] -> writing-plans [done] -> TASKS.md [done] -> Code [done] -> Commit [done] -> Push [done] -> Deploy [done] -> Live! [done]
```

In this workshop, you practiced five professional skills:

1. **Skill-driven development** -- You brainstormed, planned, broke down tasks, then implemented. This discipline works with any technical project, not just this tutorial.

2. **AI-assisted coding** -- You used Claude Code as a tool guided by clear specifications. You saw how context engineering (the `@` symbol, CLAUDE.md, slash commands) makes AI assistance more precise.

3. **Task tracking in your repo** -- Every piece of work was tracked from To Do to Done in `TASKS.md`, with each task linked to the commit that fulfilled it.

4. **Version control with Git and GitHub** -- You created feature branches, committed with meaningful messages, pushed to a remote, and merged completed work.

5. **Deployment** -- You turned a local script into a live application with a shareable URL.

> **For Your Career:** This workflow scales. Whether you're building a data pipeline, a dashboard, or a machine learning model, the pattern is the same: brainstorm, plan, track, build, deploy. You now have hands-on experience with the full cycle. In interviews, you can describe not just what you built but how you built it -- and that process awareness matters to hiring managers.

---

## What to submit

**Due: Wednesday, July 15, 2026 at 11:59 PM** -- Submit the following to Brightspace under the **AI Dev Workflow Tutorial** assignment:

1. **GitHub repository link** -- your public repo URL (e.g., `https://github.com/yourusername/ai-dev-workflow-tutorial`)

2. **Streamlit dashboard link** -- your live deployed URL (e.g., `https://sales-dashboard-yourname.streamlit.app`)

3. **Your completed `TASKS.md`** -- because the board lives in your repo, there's no screenshot to submit. Just make sure the final `TASKS.md` on your `main` branch shows:
   - Every implementation milestone in the Done section, acceptance criteria checked
   - A commit hash recorded next to each done milestone
   - The Definition of Done checked off

   Your instructor can open `TASKS.md` on GitHub and run `git log -- TASKS.md` to see how the work progressed -- that history is your evidence.

Make sure your `TASKS.md`, `prd/`, and `docs/superpowers/` files are included in your repository.

---

## Comprehensive troubleshooting

This section covers the most common issues people encounter. For each problem, you'll find three parts: what you see (the symptom), why it happens (the root cause), and how to fix it (the solution).

---

### TASKS.md and the code are out of sync

**What you see:** You committed code but the task is still sitting in In Progress (or To Do) in `TASKS.md`, or a task shows as Done but the criteria checkboxes are still empty.

**Why it happens:** Nothing updated the file. Unlike a web tracker with a "move to Done" button, `TASKS.md` only changes when you or Claude edit it. It's easy to implement a task, commit the code, and forget the board.

**How to fix it:**

1. Ask Claude Code to reconcile the board with what's actually built:
   ```
   Compare TASKS.md against the current code and commits. For each task that's actually implemented, check off its criteria, add the commit hash, and move it to Done. Tell me which tasks still have unmet criteria.
   ```
2. Make updating the board part of your rhythm: implement -> test -> **update TASKS.md** -> commit (with the board change in the same commit). If you keep forgetting, add a reminder to `v4/CLAUDE.md` so Claude prompts you every time.

> **Remember the two lists.** Claude Code's live, in-session checklist (the one that ticks off as it works) is *not* `TASKS.md`. It vanishes when the session ends. Only edits to the `TASKS.md` file are saved. If your board looks empty after restarting Claude Code, you were probably looking at the in-session list -- open the actual file in Cursor.

---

### Skill auto-invocation didn't fire

**What you see:** You sent Claude a prompt like "Help me design and plan...", but Claude didn't announce a skill (no `Using brainstorming to...` line) and instead just started writing code or asking generic questions.

**Why it happens:** The Superpowers SessionStart hook didn't load the `using-superpowers` skill, or your prompt didn't match the skill's trigger words strongly enough.

**How to fix it:**

1. Confirm Superpowers is loaded. At the top of your Claude Code session output, look for `You have superpowers`. If it's missing, see the pre-work troubleshooting for "Superpowers plugin not loaded."

2. Strengthen your prompt with explicit intent words. Instead of "let's work on the dashboard," try "Help me design and plan the dashboard." The brainstorming skill triggers on words like *design*, *plan*, *brainstorm*.

3. As a last resort, force the skill manually inside Claude Code:
   ```
   Use the brainstorming skill to design the e-commerce sales dashboard from @prd/ecommerce-analytics.md.
   ```

---

### ModuleNotFoundError

**What you see:** Running `streamlit run app.py` produces `ModuleNotFoundError: No module named 'streamlit'` (or 'pandas' or 'plotly').

**Why it happens:** Python can't find the required package because either (a) the virtual environment isn't activated, or (b) the package was never installed. The virtual environment is an isolated Python installation; packages installed inside it aren't visible outside it, and vice versa.

**How to fix it:**

1. Check if your virtual environment is active. Look for `(venv)` at the beginning of your terminal prompt.

2. If it's not active, activate it:
   ```bash
   source venv/bin/activate       # macOS
   # or: venv\Scripts\activate    # Windows
   ```

3. If the environment is active but the package is still missing, install it:
   ```bash
   pip install streamlit pandas plotly
   ```
   Or, if a `requirements.txt` file exists:
   ```bash
   pip install -r requirements.txt
   ```

4. Retry: `streamlit run app.py`

---

### Port 8501 already in use

**What you see:** Streamlit reports `Port 8501 is already in use` when you try to run the app.

**Why it happens:** A previous Streamlit session is still running in another terminal tab or window. Each Streamlit instance needs its own port, and port 8501 is Streamlit's default.

**How to fix it:**

Option A -- Use a different port:
```bash
streamlit run app.py --server.port 8502
```
Then open `http://localhost:8502` in your browser.

Option B -- Stop the existing process:

On macOS:
```bash
lsof -ti:8501 | xargs kill
```

On Windows:
```bash
netstat -ano | findstr :8501
# Note the PID (last column), then:
taskkill /PID <PID> /F
```

Then retry: `streamlit run app.py`

---

### Dashboard shows no data or errors on load

**What you see:** The dashboard loads but shows no charts, displays "NaN" values, or throws a data-related error.

**Why it happens:** The CSV file path in your code doesn't match the actual file location, or the data file has an unexpected structure. This commonly occurs when the code uses a relative path that resolves differently depending on where you run the command.

**How to fix it:**

1. Verify the data file exists:
   ```bash
   ls data/sales-data.csv
   ```

2. Check the file has content:
   ```bash
   head -5 data/sales-data.csv     # macOS
   # or: Get-Content data/sales-data.csv -First 5    # Windows
   ```
   You should see column headers and data rows.

3. Check what path your code is using. Open `app.py` and look for the line that loads the CSV (usually something like `pd.read_csv(...)`). Ensure the path matches the actual file location.

4. If the path is wrong, ask Claude to fix it:
   ```
   The dashboard cannot find the CSV file. The file is at data/sales-data.csv. Fix the data loading path.
   ```

---

### Can't push -- permission denied

**What you see:** `git push` fails with `Permission denied` or `remote: Permission to LMU-ISBA/ai-dev-workflow-tutorial.git denied`.

**Why it happens:** Your local repository is pointed at the original repository rather than your fork. You can pull from the original but can't push to it -- you can only push to your own fork.

**How to fix it:**

1. Check your remote URL:
   ```bash
   git remote -v
   ```

2. If you see `LMU-ISBA` in the URL (instead of your username), update it:
   ```bash
   git remote set-url origin https://github.com/YOUR-USERNAME/ai-dev-workflow-tutorial.git
   ```
   Replace `YOUR-USERNAME` with your actual GitHub username.

3. Verify the fix:
   ```bash
   git remote -v
   ```
   The URL should now show your username.

4. Retry the push: `git push`

---

### Git merge conflicts

**What you see:** When merging the feature branch into main, Git reports "merge conflict" and stops.

**Why it happens:** Both branches modified the same part of the same file, and Git can't automatically determine which version to keep. This is uncommon in this tutorial (since you're the only developer), but can happen if you made manual changes to `main` during the workshop.

**How to fix it:**

1. Ask Claude for help:
   ```
   I have a merge conflict. Can you help me resolve it?
   ```
   Claude can read the conflicting files and suggest resolutions.

2. Alternatively, if you want to simply take all changes from your feature branch (the most common resolution in this tutorial):
   ```
   Resolve all merge conflicts by accepting the feature branch changes, then complete the merge.
   ```

3. After resolution, commit and push as normal.

---

### "Not a git repository" error

**What you see:** Git commands fail with `fatal: not a git repository (or any of the parent directories)`.

**Why it happens:** Your terminal is in a directory that isn't inside your project. Git commands only work when you're inside a directory that has been initialized with Git (contains a `.git` folder).

**How to fix it:**

1. Check your current directory:
   ```bash
   pwd
   ```

2. Navigate to your project:
   ```bash
   cd ~/GitHub/ai-dev-workflow-tutorial    # macOS
   # or: cd C:\Users\YourName\GitHub\ai-dev-workflow-tutorial    # Windows
   ```
   Adjust the path to wherever you cloned the repository.

3. Verify you're in the right place:
   ```bash
   ls .git
   ```
   You should see Git's internal directory.

---

### Claude Code rate limits

**What you see:** Claude Code responds with a rate limit message or becomes slow to respond.

**Why it happens:** Your Claude Pro subscription has a usage cap per time period. Heavy usage during implementation (especially with multiple large file edits) can approach this cap.

**How to fix it:**

1. **Wait a few minutes.** Rate limits typically reset on a rolling window. A 5-10 minute break is usually sufficient.

2. **Work in smaller increments.** Instead of asking Claude to implement an entire feature at once, break requests into smaller pieces:
   ```
   # Instead of: "Implement the entire dashboard"
   # Try: "Create the KPI scorecards section of app.py"
   ```

3. **Use plan mode.** Press Shift+Tab to switch to plan mode. Claude explains what it'll do without making changes, using fewer tokens. Review the plan, then ask Claude to execute it.

4. **Upgrade if needed.** If you consistently hit limits, Claude Max (from $100/month) provides higher usage caps. Most people find Pro sufficient for the tutorial sessions.

---

## Other Superpowers skills you'll meet later

You'll encounter these in larger projects beyond this tutorial. We didn't formally use them in this workshop either because they're more advanced than it needs, or because we explicitly overrode them in CLAUDE.md.

| Skill | What it does | Why we skipped it here |
|-------|--------------|------------------------|
| `using-git-worktrees` | Creates an isolated working directory per branch so multiple branches can be checked out at the same time | We overrode this in CLAUDE.md to keep the workshop on a single working directory |
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
| **Acceptance Criteria** | The specific, checkable conditions a single task must meet to count as complete |
| **brainstorming** | A Superpowers skill that asks clarifying questions about a proposed feature and produces a design document |
| **Branch** | A separate line of development in Git, allowing isolated work without affecting the main codebase |
| **Commit** | A saved snapshot of your project at a specific point in time, like a version you can return to |
| **Commit Hash** | A unique identifier (e.g., `05a9ada`) assigned to each commit, serving as its permanent fingerprint |
| **Definition of Done** | A shared quality checklist that applies to every task, on top of each task's own acceptance criteria |
| **Deploy** | Make software accessible on a server so users can reach it via a URL |
| **executing-plans** | A Superpowers skill that implements tasks from an implementation plan one at a time, with frequent commits |
| **Feature Branch** | A branch created specifically for developing one feature, separate from main |
| **Fork** | Your personal copy of someone else's repository on GitHub, under your own account |
| **Implementation plan** | The detailed, step-by-step build list `writing-plans` produces in `docs/superpowers/plans/`; Claude builds from it |
| **Merge** | Combine changes from one branch into another, integrating completed work |
| **Milestone** | A coarse, human-facing deliverable on your `TASKS.md` board (TASK-1, TASK-2, ...) that groups several plan steps |
| **PRD** | Product Requirements Document -- a written description of what to build and why |
| **Push** | Upload local commits to a remote repository (GitHub), making them visible and backed up |
| **Staging Area** | A holding zone in Git for changes you intend to include in your next commit |
| **Streamlit** | A Python library that transforms Python scripts into interactive web applications |
| **TASKS.md** | A Markdown file in your repository that tracks every task through To Do, In Progress, and Done |
| **Superpowers** | A Claude Code plugin that gives Claude a library of skills (brainstorming, writing-plans, executing-plans, and more) |
| **Traceability** | The ability to link code changes back to the requirements that prompted them |
| **venv** | Virtual environment -- an isolated Python installation that keeps project dependencies separate |
| **writing-plans** | A Superpowers skill that turns a design document into a bite-sized implementation plan |
| **.gitignore** | A file that tells Git which files and directories to exclude from version control |

---

## What's next

You now have a complete professional workflow you can apply to your capstone project and beyond. The same cycle -- brainstorm, plan, track, build, deploy -- works for any technical project, whether it's a data pipeline, a machine learning model, or another dashboard. The tools and habits transfer.

> **Bring your meetings into the loop.** In the pre-work you connected Claude Code to [Granola](https://www.granola.ai) (see [Section 2.6 of the pre-work](pre-work-setup.md#26-granola-app--connect-it-to-claude-code)). You didn't need it for the dashboard, but it's built for the capstone: record your stakeholder meetings in Granola, then start a Claude Code session and ask things like *"From this week's meeting notes, what did the client ask us to change?"* or *"Draft tasks in TASKS.md from the decisions in yesterday's kickoff."* The same plan-track-build workflow, now starting from what was actually said in the room.
