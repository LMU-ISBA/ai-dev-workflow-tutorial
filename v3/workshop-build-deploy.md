# Workshop: Build & Deploy

**From requirements to a live dashboard using skill-driven development.**

**Format:** 3-hour Zoom workshop

---

## Table of contents

- [Workshop agenda](#workshop-agenda)
- [Section 1: Connect Claude Code to Jira (~10 min)](#section-1-connect-claude-code-to-jira-10-min)
- [Section 2: Brainstorm and plan (~30 min)](#section-2-brainstorm-and-plan-30-min)
  - [2.1 Create v3/CLAUDE.md](#21-create-v3claudemd)
  - [2.2 Create the feature branch](#22-create-the-feature-branch)
  - [2.3 Read the PRD](#23-read-the-prd)
  - [2.4 Brainstorm and plan with one prompt](#24-brainstorm-and-plan-with-one-prompt)
- [Section 3: Create Jira issues (~10 min)](#section-3-create-jira-issues-10-min)
- [Section 4: Build the dashboard (~35 min)](#section-4-build-the-dashboard-35-min)
  - [4.1 Implement the first issue](#41-implement-the-first-issue)
  - [4.2 Commit, push, and update Jira](#42-commit-push-and-update-jira)
  - [4.3 Complete remaining issues](#43-complete-remaining-issues)
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
| 0:15–0:30 | **Live MCP demo** -- everyone watches the Jira connection, then does it themselves |
| 0:30–3:00 | **Build at your own pace** -- work through the guide below; ask questions as you go |

> **Didn't finish the pre-work?** Work through the [pre-work setup guide](pre-work-setup.md) first -- most people finish it in under an hour. You can catch up and still complete the build during the workshop. Ask in the Teams General channel if you get stuck.

---

## What you'll accomplish

By the end of this workshop, you'll have taken a product requirements document through a full development workflow and produced a live analytics dashboard. Specifically, you'll have:

- Connected Claude Code to Jira using the Model Context Protocol (MCP)
- Generated Superpowers artifacts: a design document and an implementation plan
- Created and tracked Jira issues through their full lifecycle
- Built a working Streamlit dashboard with AI-assisted coding
- Committed and pushed code to GitHub with traceability to Jira
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

Each box in this diagram is a distinct stage you'll complete today. The left-to-right flow on the top row moves from planning to execution. The right-to-left flow on the bottom row moves from saving your work to making it publicly available. Together, they form a closed loop: requirements become running software that stakeholders can access.

> **Why skill-driven development?** You could ask Claude "build me a dashboard" directly. But without a clear plan, Claude makes assumptions, and AI can build the wrong thing very fast. Superpowers' skills give the work structure: brainstorming explores what to build, writing-plans turns the design into a bite-sized plan, and executing-plans implements one task at a time. Letting the skills run their process is what makes AI-assisted coding predictable instead of chaotic. In your capstone, this discipline will be the difference between a project that drifts and one that delivers.

---

## Section 1: Connect Claude Code to Jira (~10 min)

### Understanding MCP (Model Context Protocol)

Before you run any commands, it helps to understand what you're setting up and why.

> **What is MCP?** MCP is a plugin system for Claude Code. Just as your phone connects to apps through APIs, Claude Code connects to external services through MCP. Each MCP server gives Claude Code a new capability. Today, you'll add the Atlassian MCP server, which lets Claude Code communicate directly with Jira -- reading your tasks, creating issues, and updating progress, all without leaving the terminal.

Here is what the connection looks like:

```
┌──────────────┐     MCP      ┌──────────────┐
│  Claude Code │ <----------> │    Jira      │
│  (terminal)  │   protocol   │  (cloud)     │
│              │              │              │
│  Can now:    │              │  Your ECOM   │
│  - Read issues│             │  project     │
│  - Create    │              │              │
│    issues    │              │              │
│  - Update    │              │              │
│    status    │              │              │
└──────────────┘              └──────────────┘
```

Without MCP, you'd need to manually switch between Claude Code and the Jira web interface. With MCP, Claude Code handles both coding and project management in a single workflow.

> **Why This Matters:** In professional settings, developers track work in project management tools and maintain traceability between requirements and code. MCP lets you practice this integrated workflow from the start.

### Steps

1. **Exit Claude Code if it's running.** The MCP server must be added before starting a new session. In Claude Code, type:

   ```
   /exit
   ```

   If Claude Code isn't running, skip this step.

2. **Add the Atlassian MCP server.** Run this in Cursor's terminal (not inside Claude Code):

   ```bash
   claude mcp add --transport sse atlassian https://mcp.atlassian.com/v1/sse
   ```

   This command registers the Atlassian server with Claude Code. The `--transport sse` flag tells Claude Code to communicate using Server-Sent Events, which is the protocol Atlassian's server uses. You only need to run this command once -- it persists across sessions.

3. **Start Claude Code.** In Cursor's terminal, run:

   ```bash
   claude
   ```

4. **Set the output style to explanatory.** Inside Claude Code, type:

   ```
   /output-style explanatory
   ```

   By default, Claude Code keeps its responses short. Setting the style to "explanatory" tells Claude to explain what it's doing and why, which helps you learn from its work instead of just receiving code. This is especially useful while you're still learning the workflow.

5. **Verify the server is registered.** Inside Claude Code, type:

   ```
   /mcp
   ```

   You should see `atlassian` in the list of MCP servers. It'll likely show that authentication is required -- this is expected.

6. **Authenticate with Atlassian.** In the `/mcp` output, use the **arrow keys** to select `atlassian`, then press **Enter**.

7. **Complete browser authentication.** A browser window opens. Log in with your Atlassian account (the one you created during the pre-work), authorize Claude Code, and return to the terminal. You may see a "You can close this tab" message in the browser -- this means authentication succeeded.

8. **Test the connection.** In Claude Code, ask:

   ```
   What Jira projects do I have access to?
   ```

   Claude should respond with a list that includes your ECOM project. If you see your project name, the connection is working.

> **Troubleshooting MCP Authentication:** If authentication fails or expires during your session, run `/mcp`, select `atlassian`, and press Enter to re-authenticate. Authentication tokens expire periodically for security reasons -- this is normal behavior, not an error. You may need to re-authenticate once or twice during a long session.

**Checkpoint:** Claude can see your ECOM project and respond to Jira queries.

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

### 2.1 Create v3/CLAUDE.md

> **What is CLAUDE.md?** It's a file Claude Code reads at the start of every session. It's where you put project-specific guidance: code style, workflow conventions, things you want Claude to remember without you having to repeat them every time. For this project, CLAUDE.md tells Claude two things: skip the worktree setup that brainstorming usually does, and stick to the simple, readable code style that matches the rest of the tutorial.

> **Heads up about `/init`:** Claude Code has an `/init` slash command that auto-generates a CLAUDE.md by scanning your codebase. We're not using it. We want a small, focused file rather than a generated one. Don't run `/init` for this project. If you do run it by accident and it overwrites your CLAUDE.md, recover with `git checkout v3/CLAUDE.md`.

1. In Cursor, create a new file at `v3/CLAUDE.md`.

2. Paste in the following content:

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

3. Save the file.

**Checkpoint:** `v3/CLAUDE.md` exists and contains the worktree override.

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

   d. Brainstorming would normally create a git worktree at this point. Because of `v3/CLAUDE.md`, it skips that and hands off directly to writing-plans. You'll see Claude announce `Handing off to writing-plans...`.

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
> When you start Section 4 by saying "Let's implement ECOM-1," the chain extends:
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

## Section 3: Create Jira issues (~10 min)

### Connecting planning to tracking

Now you bridge two worlds: Superpowers (planning) and Jira (tracking). Each task from your implementation plan becomes a Jira issue, giving you visibility into progress and creating traceability between requirements and implementation.

> **Why This Matters:** In professional teams, every piece of work is tracked. When a manager asks "what is the status of the dashboard?" or a stakeholder asks "why was this chart implemented this way?", you can trace the answer through Jira. Each issue links to a requirement (from the spec), a code change (commit), and a result (deployed feature). This traceability is how teams build software without losing track of why changes were made.

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  plan.md     │ --> │  Jira Issues │ --> │  Code        │
│  (writing-   │     │  (ECOM-1,    │     │  (commits    │
│   plans)     │     │   ECOM-2...) │     │   reference  │
│              │     │              │     │   issue keys)│
│  Source of   │     │  Track       │     │              │
│  truth for   │     │  progress    │     │              │
│  what to     │     │  and status  │     │              │
│  build       │     │              │     │              │
└──────────────┘     └──────────────┘     └──────────────┘
```

### 3.1 Create the First Issue

1. In Claude Code, ask Claude to create the first Jira issue based on your tasks:

   ```
   Based on the tasks in the implementation plan at @docs/superpowers/plans/<plan-file>.md, what should be the first Jira issue? Create it in the ECOM project.
   ```

   Replace `<plan-file>` with the actual filename. To find it quickly, run `ls -t docs/superpowers/plans/ | head -1` in your terminal.

   > **How does Claude know to use Jira?** When you mention "Jira" or "ECOM project," Claude recognizes that it needs the Atlassian MCP server and uses it automatically. You don't need to activate MCP manually -- Claude selects the right tool based on your request. This is part of why MCP is powerful: it extends Claude's capabilities transparently.

2. Claude reads the plan, formulates an appropriate Jira issue, uses the Atlassian MCP to create it, and returns the details including the issue key (e.g., ECOM-1).

3. Verify in Jira: open your browser, navigate to your ECOM project backlog, and confirm the issue exists. Click into it and read the description, which should match the corresponding task from your plan.

**Checkpoint:** ECOM-1 is visible in your Jira backlog with a detailed description.

### 3.2 Create Remaining Issues

1. In Claude Code, ask Claude to create issues for the remaining tasks:

   ```
   Create Jira issues in the ECOM project for the remaining tasks in @docs/superpowers/plans/<plan-file>.md
   ```

   Replace `<plan-file>` with the actual filename if needed.

2. Claude creates multiple issues. This may take a minute as it processes each task and communicates with Jira.

3. Verify in Jira: refresh the backlog to see all new issues (ECOM-2, ECOM-3, etc.). Each should have a description derived from the plan tasks.

**Checkpoint:** Multiple issues are visible in the Jira backlog, each with descriptions matching the plan tasks.

> **Pro Tip:** Open a few issues and read their descriptions. Notice how the progression from PRD to brainstorming to writing-plans to Jira creates increasingly specific, actionable items. The PRD said "display Total Sales"; the plan task might say "create KPI scorecards using Streamlit metric components with formatted currency values"; the Jira issue captures this as a trackable work item. This is the refinement process in practice.

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

### 4.1 Implement the first issue

1. In Claude Code, ask which issue to start with. Claude considers dependencies and suggests a logical starting point:

   ```
   Which Jira issue should we implement first?
   ```

   Claude typically recommends starting with the environment setup or app structure issue, since other issues depend on it.

2. In Claude Code, ask Claude to start implementing the first issue:

   ```
   Let's start implementing ECOM-1.
   ```

   Replace `ECOM-1` with whichever issue Claude recommended. Claude will recognize this as an implementation task and auto-invoke `executing-plans`. You'll see `Using executing-plans to...` in the output. The skill reads the plan, picks up the first task, and starts working.

   > **What you'll see during a TDD task:** For tasks flagged as test-driven (typically data-transformation tasks like `compute_total_sales`), executing-plans will: (a) write a failing test in a `tests/` file, (b) run pytest (Python's test runner) and show you the failure, (c) implement the function, (d) run pytest again and show you the pass, (e) commit with a message referencing your Jira issue. For non-TDD tasks (chart rendering, page layout), it'll skip straight to implementation and commit. Watch the test output: seeing red turn green is one of the more satisfying parts of the workshop.

   > **What happens during implementation:** Claude reads the Jira issue description, consults the specification and plan, then writes the code. Watch the output -- you'll see Claude creating files, writing functions, and making decisions. Pay attention to which libraries Claude imports, how it structures the code, and how it handles data loading.

3. In Claude Code, ask Claude to explain what it created:

   ```
   What files did you create? Explain what each one does.
   ```

   Understanding the file structure helps you learn from the AI's work rather than treating it as a black box.

4. Test the dashboard. You can either run these commands yourself in Cursor's terminal, or ask Claude Code to do it for you.

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

5. Open `http://localhost:8501` in your browser. You should see the beginnings of your dashboard. The exact content depends on which issue you implemented first.

6. When done reviewing, press **Ctrl+C** in the terminal to stop the Streamlit server.

**Checkpoint:** The dashboard runs locally at `http://localhost:8501` without errors.

### 4.2 Commit, push, and update Jira

Now you'll save your work using Git and create a traceable link between your code and the Jira issue. This three-step process -- commit, push, update -- is the basic rhythm of professional development.

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
> When you include a Jira issue key (like ECOM-1) in your commit message, you create a traceable link that connects your code change to the requirement that prompted it:
>
> ```
> Jira Issue ECOM-1 --> Commit "ECOM-1: add KPI scorecards" --> GitHub --> Deployed Dashboard
> ```
>
> Anyone can now trace the code back to the requirement that created it. In professional environments, this traceability is how teams maintain accountability, conduct code reviews, and audit changes. Make it a habit to include the Jira key in every commit message.

#### Steps

1. **Commit your changes.** In Claude Code, ask Claude to create a commit with the Jira key in the message. Also ensure the virtual environment directory isn't tracked:

   ```
   Commit my changes for ECOM-1. Make sure venv/ is in .gitignore.
   ```

   Claude will add `venv/` to `.gitignore` (if not already there), stage your changes, and create a commit with a message like "ECOM-1: Set up project structure and dependencies."

   > **Key Concept: .gitignore.** The `.gitignore` file tells Git which files and directories to ignore. Virtual environments (`venv/`), compiled files, and operating system files should never be committed to a repository -- they're large, machine-specific, and can be regenerated. The `.gitignore` file prevents accidental commits of these files.

   > **What is a commit hash?** After committing, Git produces a unique identifier called a **commit hash** -- a string like `05a9ada`. This hash is a fingerprint: no two commits in the history of your repository will ever have the same hash. You'll include this hash in Jira so anyone can find exactly which code change fulfilled a specific requirement.

2. **Push to GitHub.** In Claude Code, upload your local commit to the remote repository:

   ```
   Push my changes to GitHub.
   ```

   If this is your first push on the feature branch, Claude may need to set the upstream tracking branch. It handles this automatically.

3. **Update Jira with evidence.** In Claude Code, close the loop by recording what you did:

   ```
   Update ECOM-1 in Jira: add a comment with implementation summary, commit hash, branch name, and GitHub link. Move to Done.
   ```

   Claude adds a comment to the Jira issue containing the implementation details and changes the status to Done.

4. **Verify in Jira.** Open ECOM-1 in your browser and confirm:
   - Status is "Done"
   - A comment exists with the implementation summary, commit hash, branch name, and a GitHub link

> **If Claude can't access Jira:** Run `/mcp`, select `atlassian`, and press Enter to re-authenticate. Then retry the update command.

**Checkpoint:** Code is on GitHub. ECOM-1 shows "Done" in Jira with a detailed evidence comment.

### 4.3 Complete remaining issues

Now repeat the implementation cycle for each remaining Jira issue. Skip the deployment issue -- that comes in Section 5.

The cycle for each issue is:

```
Ask which issue is next
        |
        v
"Let's implement ECOM-N" --> Claude auto-invokes executing-plans --> Move to In Progress
        |
        v
Test the dashboard (streamlit run app.py)
        |
        v
Commit with Jira key in message
        |
        v
Push to GitHub
        |
        v
Update Jira with evidence --> Move to Done
```

Here is the pattern for each issue. In Claude Code:

```
Let's implement ECOM-2.
```

Claude auto-invokes `executing-plans` and moves the issue to In Progress.

After implementation and testing, in Claude Code:

```
Commit my changes for ECOM-2 and push to GitHub.

Update ECOM-2 in Jira with implementation summary, commit hash, branch name, and GitHub link. Move to Done.
```

Replace `ECOM-2` with the current issue key. Repeat for ECOM-3, ECOM-4, and so on.

> **Skip the deployment issue for now.** You can't deploy until your code is merged to `main`, which happens in the next step. Leave the deployment issue in "To Do" status.

> **Pro Tip:** Watch Claude's output as it implements each issue. You'll see files being created, imports being added, and functions being written. This is a good way to learn how professional code is structured. Pay attention to how Claude names variables, organizes functions, and handles data. You can reuse these patterns in your capstone.

After working through all implementation issues, test the complete dashboard one final time. You can run these yourself or ask Claude Code:

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

**Checkpoint:** All implementation issues are marked "Done" in Jira with evidence comments. Only the deployment issue remains open.

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

   You should be on your feature branch (e.g., `001-sales-dashboard`).

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

### 5.2 Update Jira

Complete the final Jira issue by recording the deployment. In Claude Code:

```
Update the deployment Jira issue: add the live Streamlit URL as a comment. Move to Done.
```

**Checkpoint:** The dashboard is live and accessible at a public URL. The deployment Jira issue is marked "Done" with the URL in a comment.

---

## Section 6: Final verification checklist

Before submitting, walk through every item below. Each category corresponds to a section of this guide.

### MCP and Superpowers

- [ ] Atlassian MCP connected and functional
- [ ] Design document created (`docs/superpowers/specs/<file>.md`)
- [ ] Implementation plan created (`docs/superpowers/plans/<file>.md`)

### Jira

- [ ] Issues created from plan tasks (ECOM-1, ECOM-2, etc.)
- [ ] All issues marked "Done"
- [ ] Each issue has a comment with: implementation summary, commit hash, branch name, GitHub link

### Dashboard

- [ ] Runs locally with KPIs, line chart, and bar charts
- [ ] Deployed and publicly accessible on Streamlit Cloud

### Version control

- [ ] Commits include Jira issue keys in messages
- [ ] Feature branch merged to main
- [ ] All code pushed to GitHub on the main branch

---

## The complete workflow -- what you accomplished

```
PRD [done] -> brainstorming [done] -> writing-plans [done] -> Jira [done] -> Code [done] -> Commit [done] -> Push [done] -> Deploy [done] -> Live! [done]
```

In this workshop, you practiced five professional skills:

1. **Skill-driven development** -- You brainstormed, planned, broke down tasks, then implemented. This discipline works with any technical project, not just this tutorial.

2. **AI-assisted coding** -- You used Claude Code as a tool guided by clear specifications. You saw how context engineering (the `@` symbol, MCP connections, slash commands) makes AI assistance more precise.

3. **Project management with Jira** -- Every piece of work was tracked from creation to completion, with evidence linking requirements to code changes.

4. **Version control with Git and GitHub** -- You created feature branches, committed with meaningful messages, pushed to a remote, and merged completed work.

5. **Deployment** -- You turned a local script into a live application with a shareable URL.

> **For Your Career:** This workflow scales. Whether you're building a data pipeline, a dashboard, or a machine learning model, the pattern is the same: brainstorm, plan, track, build, deploy. You now have hands-on experience with the full cycle. In interviews, you can describe not just what you built but how you built it -- and that process awareness matters to hiring managers.

---

## What to submit

**Due: March 16, 2026 at 11:59 PM** -- Submit the following to Brightspace under the **AI Dev Workflow Tutorial** assignment:

1. **GitHub repository link** -- your public repo URL (e.g., `https://github.com/yourusername/ai-dev-workflow-tutorial`)

2. **Streamlit dashboard link** -- your live deployed URL (e.g., `https://sales-dashboard-yourname.streamlit.app`)

3. **Jira screenshot(s)** -- screenshot of one completed Jira issue showing:
   - Issue status is "Done"
   - Comment with implementation summary, commit hash, branch name, and GitHub link

   If the full issue doesn't fit in one screenshot, submit multiple screenshots named `jira-01.png`, `jira-02.png`, etc.

Make sure your `prd/` and `docs/superpowers/` directories are included in your repository.

---

## Comprehensive troubleshooting

This section covers the most common issues people encounter. For each problem, you'll find three parts: what you see (the symptom), why it happens (the root cause), and how to fix it (the solution).

---

### MCP connection issues

**What you see:** Claude says it can't access Jira, or `/mcp` doesn't show the `atlassian` server.

**Why it happens:** The MCP server either wasn't added correctly, or the authentication token has expired. Authentication tokens are temporary by design -- Atlassian issues short-lived tokens for security, which means they expire during long sessions.

**How to fix it:**

If the server isn't listed in `/mcp`:

1. Exit Claude Code: `/exit`
2. Re-add the server:
   ```bash
   claude mcp add --transport sse atlassian https://mcp.atlassian.com/v1/sse
   ```
3. Restart Claude Code: `claude`
4. Run `/mcp` and authenticate

If the server is listed but authentication has expired:

1. Run `/mcp` inside Claude Code
2. Select `atlassian` with arrow keys and press Enter
3. Complete the browser authentication flow
4. Return to Claude Code and retry your Jira request

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

You'll encounter these in larger projects beyond this tutorial. We didn't formally use them in v3 either because they're more advanced than this workshop needs, or because we explicitly overrode them in CLAUDE.md.

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
| **brainstorming** | A Superpowers skill that asks clarifying questions about a proposed feature and produces a design document |
| **Branch** | A separate line of development in Git, allowing isolated work without affecting the main codebase |
| **Commit** | A saved snapshot of your project at a specific point in time, like a version you can return to |
| **Commit Hash** | A unique identifier (e.g., `05a9ada`) assigned to each commit, serving as its permanent fingerprint |
| **Deploy** | Make software accessible on a server so users can reach it via a URL |
| **executing-plans** | A Superpowers skill that implements tasks from an implementation plan one at a time, with frequent commits |
| **Feature Branch** | A branch created specifically for developing one feature, separate from main |
| **Fork** | Your personal copy of someone else's repository on GitHub, under your own account |
| **Merge** | Combine changes from one branch into another, integrating completed work |
| **MCP** | Model Context Protocol -- a plugin system that lets Claude Code connect to external services like Jira |
| **PRD** | Product Requirements Document -- a written description of what to build and why |
| **Push** | Upload local commits to a remote repository (GitHub), making them visible and backed up |
| **Staging Area** | A holding zone in Git for changes you intend to include in your next commit |
| **Streamlit** | A Python library that transforms Python scripts into interactive web applications |
| **Superpowers** | A Claude Code plugin that gives Claude a library of skills (brainstorming, writing-plans, executing-plans, and more) |
| **Traceability** | The ability to link code changes back to the requirements that prompted them |
| **venv** | Virtual environment -- an isolated Python installation that keeps project dependencies separate |
| **writing-plans** | A Superpowers skill that turns a design document into a bite-sized implementation plan |
| **.gitignore** | A file that tells Git which files and directories to exclude from version control |

---

## What's next

You now have a complete professional workflow you can apply to your capstone project and beyond. The same cycle -- brainstorm, plan, track, build, deploy -- works for any technical project, whether it's a data pipeline, a machine learning model, or another dashboard. The tools and habits transfer.
