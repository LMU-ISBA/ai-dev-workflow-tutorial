# Workshop: Build & Deploy

**From requirements to a live dashboard using spec-driven development.**

**Format:** 3-hour Zoom workshop

---

## Table of Contents

- [Workshop Agenda](#workshop-agenda)
- [Section 1: Connect Claude Code to Jira (~10 min)](#section-1-connect-claude-code-to-jira-10-min)
- [Section 2: Spec-Kit Workflow (~25 min)](#section-2-spec-kit-workflow-25-min)
  - [2.1 Initialize Spec-Kit](#21-initialize-spec-kit)
  - [2.2 Create the Constitution](#22-create-the-constitution)
  - [2.3 Create the Specification](#23-create-the-specification)
  - [2.4 Create the Implementation Plan](#24-create-the-implementation-plan)
  - [2.5 Generate Tasks](#25-generate-tasks)
- [Section 3: Create Jira Issues (~10 min)](#section-3-create-jira-issues-10-min)
- [Section 4: Build the Dashboard (~35 min)](#section-4-build-the-dashboard-35-min)
  - [4.1 Implement the First Issue](#41-implement-the-first-issue)
  - [4.2 Commit, Push, and Update Jira](#42-commit-push-and-update-jira)
  - [4.3 Complete Remaining Issues](#43-complete-remaining-issues)
  - [4.4 Merge to Main](#44-merge-to-main)
- [Section 5: Deploy (~15 min)](#section-5-deploy-15-min)
- [Section 6: Final Verification Checklist](#section-6-final-verification-checklist)
- [Comprehensive Troubleshooting](#comprehensive-troubleshooting)
- [Glossary](#glossary)

---

## Workshop Agenda

| Time | Activity |
|------|----------|
| 0:00–0:15 | **Setup check + triage** — verify pre-work, troubleshoot stragglers |
| 0:15–0:30 | **Live MCP demo** — everyone watches the Jira connection, then does it themselves |
| 0:30–3:00 | **Build at your own pace** — work through the guide below; ask questions as you go |

> **Did not finish the pre-work?** Work through the [pre-work setup guide](pre-work-setup.md) first — most people finish it in under an hour. You can catch up and still complete the build during the workshop. Ask in the Zoom chat if you get stuck.

---

## What You Will Accomplish

By the end of this workshop, you will have taken a product requirements document through a full development workflow and produced a live analytics dashboard. Specifically, you will have:

- Connected Claude Code to Jira using the Model Context Protocol (MCP)
- Generated spec-kit artifacts: constitution, specification, plan, and tasks
- Created and tracked Jira issues through their full lifecycle
- Built a working Streamlit dashboard with AI-assisted coding
- Committed and pushed code to GitHub with traceability to Jira
- Deployed a live dashboard accessible by anyone with the URL

---

## Prerequisites Check

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

If any command fails, return to the [pre-work setup guide](pre-work-setup.md) and resolve the issue before proceeding. Every tool must be working before you continue.

---

## The Professional Workflow

This is the workflow used at technology companies worldwide. Today you will experience the entire cycle, from specification to deployment.

```
┌─────────┐    ┌──────────┐    ┌─────────┐    ┌────────┐
│   PRD   │ -> │ spec-kit │ -> │  Jira   │ -> │  Code  │
│(written)│    │(Claude)  │    │(tracking)│    │(Claude)│
└─────────┘    └──────────┘    └─────────┘    └────────┘
                                                  │
┌─────────┐    ┌──────────┐    ┌─────────┐    ┌────────┐
│  Live!  │ <- │  Deploy  │ <- │  Push   │ <- │ Commit │
│(public) │    │(Streamlit)│   │(GitHub) │    │(Git)   │
└─────────┘    └──────────┘    └─────────┘    └────────┘
```

Each box in this diagram is a distinct stage you will complete today. The left-to-right flow on the top row moves from planning to execution. The right-to-left flow on the bottom row moves from saving your work to making it publicly available. Together, they form a closed loop: requirements become running software that stakeholders can access.

> **Why spec-driven development?** You could ask Claude "build me a dashboard" directly. But without clear specifications, Claude makes assumptions -- and AI can build the wrong thing very fast. A vague prompt might produce a dashboard with the wrong charts, the wrong data structure, or the wrong layout. Spec-driven development means you specify what you want, plan how to build it, then execute against that plan. Writing specifications before code is what professional teams do. This is the difference between "I built something" and "I solved the right problem." In your capstone, this discipline will be the difference between a project that drifts and one that delivers.

---

## Section 1: Connect Claude Code to Jira (~10 min)

### Understanding MCP (Model Context Protocol)

Before you run any commands, it helps to understand what you are setting up and why.

> **What is MCP?** MCP is a plugin system for Claude Code. Just as your phone connects to apps through APIs, Claude Code connects to external services through MCP. Each MCP server gives Claude Code a new capability. Today, you will add the Atlassian MCP server, which lets Claude Code communicate directly with Jira -- reading your tasks, creating issues, and updating progress, all without leaving the terminal.

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

Without MCP, you would need to manually switch between Claude Code and the Jira web interface. With MCP, Claude Code handles both coding and project management in a single workflow.

> **Why This Matters:** In professional settings, developers track work in project management tools and maintain traceability between requirements and code. MCP lets you practice this integrated workflow from the start.

### Steps

1. **Exit Claude Code if it is running.** The MCP server must be added before starting a new session.

   ```
   /exit
   ```

   If Claude Code is not running, skip this step.

2. **Add the Atlassian MCP server.** Run this in Cursor's terminal (not inside Claude Code):

   ```bash
   claude mcp add --transport sse atlassian https://mcp.atlassian.com/v1/sse
   ```

   This command registers the Atlassian server with Claude Code. The `--transport sse` flag tells Claude Code to communicate using Server-Sent Events, which is the protocol Atlassian's server uses. You only need to run this command once -- it persists across sessions.

3. **Start Claude Code:**

   ```bash
   claude
   ```

4. **Set the output style to explanatory.** Inside Claude Code, run:

   ```
   /output-style explanatory
   ```

   By default, Claude Code keeps its responses short. Setting the style to "explanatory" tells Claude to explain what it is doing and why, which helps you learn from its work instead of just receiving code. This is especially useful while you are still learning the workflow.

5. **Verify the server is registered.** Inside Claude Code, run:

   ```
   /mcp
   ```

   You should see `atlassian` in the list of MCP servers. It will likely show that authentication is required -- this is expected.

6. **Authenticate with Atlassian.** In the `/mcp` output, use the **arrow keys** to select `atlassian`, then press **Enter**.

7. **Complete browser authentication.** A browser window opens. Log in with your Atlassian account (the one you created during the pre-work), authorize Claude Code, and return to the terminal. You may see a "You can close this tab" message in the browser -- this means authentication succeeded.

8. **Test the connection.** Ask Claude a question about your Jira instance:

   ```
   What Jira projects do I have access to?
   ```

   Claude should respond with a list that includes your ECOM project. If you see your project name, the connection is working.

> **Troubleshooting MCP Authentication:** If authentication fails or expires during your session, run `/mcp`, select `atlassian`, and press Enter to re-authenticate. Authentication tokens expire periodically for security reasons -- this is normal behavior, not an error. You may need to re-authenticate once or twice during a long session.

**Checkpoint:** Claude can see your ECOM project and respond to Jira queries.

---

## Section 2: Spec-Kit Workflow (~25 min)

### Understanding Spec-Driven Development

The rest of the tutorial flows from what you create here. Every step that follows -- coding, committing, deploying -- depends on the specifications you write in this section.

> **The Problem with "Just Code It":** When you ask an AI to build something without clear specifications, you get something that might work but probably is not what you wanted. The AI fills in gaps with assumptions, and each assumption is a potential mismatch with your intent. With a complex deliverable like an analytics dashboard, even small mismatches compound: the wrong chart type, unexpected data aggregation, a layout that does not serve the audience.

Spec-kit solves this by creating a structured pipeline that progressively narrows ambiguity:

```
Constitution -> Specification -> Plan -> Tasks -> Implementation
(principles)    (what to build)   (how)   (steps)   (code)
```

Here is what each stage does:

| Stage | Purpose | Analogy |
|-------|---------|---------|
| **Constitution** | Defines project principles and standards | A company's core values |
| **Specification** | Details exactly what to build | An architect's blueprint |
| **Plan** | Describes the technical approach | A construction schedule |
| **Tasks** | Breaks work into actionable items | A contractor's punch list |
| **Implementation** | Writes the actual code | Building the structure |

Each stage narrows the space of possible outcomes. By the time you reach implementation, Claude knows what to build, how to build it, and in what order. The result is more likely to match what you actually wanted.

> **Pro Tip:** This pipeline mirrors how analytics projects work in industry. Before you build a predictive model, you define the business question (constitution), specify the success metrics (specification), choose your methodology (plan), and break the work into phases (tasks). The same discipline applies to software.

### 2.1 Initialize Spec-Kit

Spec-kit needs to set up its configuration files and slash commands before you can use it. This is a one-time initialization step for each project.

Run this in Cursor's terminal (**not** inside Claude Code):

```bash
specify init . --ai claude
```

This command does three things:

- Creates a `.specify/` directory containing spec-kit's configuration
- Creates a `.claude/commands/` directory containing slash commands that Claude Code recognizes (like `/speckit.constitution`, `/speckit.specify`, etc.)
- Sets Claude as the AI backend for spec-kit operations

When prompted:

- **"Directory not empty" warning** -- Type `y` and press Enter. This is expected because your project already has files from the pre-work.
- **Script type** -- Choose `sh` (macOS) or `ps` (Windows). This determines the shell script format for any generated automation scripts.

**Checkpoint:** Both directories exist. Verify with:

```bash
ls .specify/
ls .claude/commands/
```

You should see configuration files in `.specify/` and several `speckit.*` command files in `.claude/commands/`.

### 2.2 Create the Constitution

> **What is a Constitution?** It is your project's "code of conduct." It defines principles that guide every development decision Claude makes. When Claude encounters ambiguity later -- for example, choosing between a simple bar chart and a complex interactive visualization -- it refers back to these principles. A constitution that says "simple, readable code" will produce different results than one that says "maximum visual sophistication."

1. Start Claude Code if it is not already running:

   ```bash
   claude
   ```

2. Run the constitution slash command. Type the following as a single message (the slash command and the instructions together):

   ```
   /speckit.constitution

   We're building an e-commerce analytics project -- a Streamlit dashboard for sales data visualization.
   Ask me one question at a time about this project. Propose numbered options I can choose from. After 3-5 questions, generate the constitution.
   ```

3. Claude will ask you a series of questions about your project's principles and priorities -- things like code style, visualization approach, and development practices. Pick the options that make sense to you. There are no wrong answers here; the point is that you are making deliberate choices about how the project should be built, rather than letting the AI decide for you.

4. After the Q&A, Claude generates a constitution document and asks permission to create the file. You will see a permission prompt.

   > **Key Concept: The Permission Prompt.** Claude Code asks before modifying your files. You have several options:
   > - **Yes** -- approve this one change
   > - **Yes, allow all edits during this session** -- approve all future edits without asking (useful when you trust the workflow)
   > - **No** -- reject the change
   >
   > For this tutorial, either "Yes" or "Yes, allow all" works. If you want to review each change Claude makes (a good learning practice), choose "Yes" each time. If you want to move faster, choose "Yes, allow all."

5. Preview the constitution. In Cursor's file explorer, navigate to `.specify/memory/constitution.md`. Right-click the file and select **Open Preview** to see the formatted version. Read through it -- these principles will shape every decision Claude makes during implementation.

**Checkpoint:** `.specify/memory/constitution.md` exists and contains the principles you specified.

### 2.3 Create the Specification

> **What is a Specification?** The specification turns your PRD (Product Requirements Document) into detailed, actionable requirements. Your PRD says "we want a sales dashboard with KPIs and charts." The specification says exactly what those KPIs are, how the charts should behave, what the data structure looks like, and what constitutes success. The specification eliminates the ambiguity that the PRD intentionally leaves open.

Before running this command, you need to understand an important Claude Code feature.

> **Key Concept: The `@` Symbol (Context Engineering).** When you type `@` followed by a file path in Claude Code, it includes that file's entire content in your message. This is called **context engineering** -- giving AI the right information to produce better results.
>
> For example, `@prd/ecommerce-analytics.md` tells Claude: "read this entire PRD and use it as the basis for your work." Without the `@`, Claude would not know your specific requirements and would have to guess or ask.
>
> The quality of AI output depends on the context you provide. Better context, better results.

1. Run the specification command with the PRD as context:

   ```
   /speckit.specify @prd/ecommerce-analytics.md

   Ask me one question at a time about the requirements. Propose numbered options I can choose from. After 3-5 questions, generate the specification.
   ```

2. Claude reads the PRD and asks you questions about how to interpret the requirements -- things like what KPIs matter most, how interactive the charts should be, and what the data model should look like. Pick the options that fit your vision for the dashboard.

3. After the Q&A, Claude generates a detailed specification. This typically takes 30-60 seconds.

4. Note that spec-kit may automatically create a **feature branch** (e.g., `001-sales-dashboard`).

   > **Key Concept: Feature Branches.** A **branch** in Git is a separate line of development. It is like creating a draft copy of a document: you make all your changes on the draft, and only merge them into the original when you are satisfied.
   >
   > ```
   > main:    A --- B --- C  (stable, untouched)
   >                \
   > feature:        D --- E --- F  (your work in progress)
   > ```
   >
   > Your `main` branch stays clean and stable while you work on the feature branch. This is standard practice in professional development -- it protects the production version of your code from incomplete changes. Spec-kit creates the branch automatically so you do not have to think about it.

5. Preview the specification in Cursor's file explorer.

**Checkpoint:** `specs/[feature-name]/spec.md` exists. The exact folder name depends on what spec-kit generates (commonly something like `001-sales-dashboard`).

### 2.4 Create the Implementation Plan

> **Why Plan Before Coding?** The specification says WHAT to build; the plan says HOW to build it. It defines technology choices, architecture, file organization, and the order of operations. It is the equivalent of a methodology section in a research paper -- before you analyze data, you define your approach and choose your methods. In your capstone, planning before coding will save your team from costly mid-project pivots.

1. Run the plan command:

   ```
   /speckit.plan

   Ask me one question at a time about technology choices and architecture. Propose numbered options I can choose from. After 3-5 questions, generate the plan.
   ```

2. Claude reads the specification and constitution, then asks about your preferences -- things like which charting library to use, how to organize the code, and how to handle data loading. The options will be grounded in what makes sense for this project, so pick what appeals to you.

3. After the Q&A, Claude generates a plan that respects both the requirements and the principles you established.

4. Preview the plan in Cursor's file explorer.

**Checkpoint:** `specs/[feature-name]/plan.md` exists with technical direction including technology choices and architecture.

### 2.5 Generate Tasks

> **From Plan to Tasks:** Breaking work into specific, actionable tasks is a core project management skill. In agile development, each task should be:
> - **Independent** -- completable on its own without waiting for other tasks
> - **Verifiable** -- you can confirm it is done by testing or inspecting the output
> - **Small enough** -- achievable in a single focused work session
>
> This is the same principle behind any well-structured analytics project: break a large deliverable into manageable pieces, then execute them systematically.

1. Run the tasks command:

   ```
   /speckit.tasks

   Ask me one question at a time about how to break this work down. Propose numbered options I can choose from. After 3-5 questions, generate the tasks.
   ```

2. Claude asks about your preferences for task granularity and ordering -- things like how to split up the dashboard components and what to tackle first. This is a lightweight version of sprint planning.

3. Review the output. You should see tasks such as:
   - Set up Python virtual environment and dependencies
   - Create main Streamlit app structure
   - Implement KPI scorecards
   - Implement sales trend line chart
   - Implement category and region bar charts
   - Deploy to Streamlit Cloud

   The exact task names may vary, but the overall scope should cover environment setup, each major dashboard component, and deployment.

4. Preview the tasks file in Cursor's file explorer.

**Checkpoint:** `specs/[feature-name]/tasks.md` exists with numbered implementation steps.

> **Pro Tip:** Take a moment to look at the four documents you just created: constitution, specification, plan, and tasks. Notice how each one builds on the previous. The constitution set principles. The specification used those principles to detail requirements. The plan used the specification to choose an approach. The tasks used the plan to define concrete steps. This step-by-step refinement is what makes AI-assisted coding predictable instead of chaotic.

---

## Section 3: Create Jira Issues (~10 min)

### Connecting Planning to Tracking

Now you bridge two worlds: spec-kit (planning) and Jira (tracking). Each task from your tasks.md becomes a Jira issue, giving you visibility into progress and creating traceability between requirements and implementation.

> **Why This Matters:** In professional teams, every piece of work is tracked. When a manager asks "what is the status of the dashboard?" or a stakeholder asks "why was this chart implemented this way?", you can trace the answer through Jira. Each issue links to a requirement (from the spec), a code change (commit), and a result (deployed feature). This traceability is how teams build software without losing track of why changes were made.

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  tasks.md    │ --> │  Jira Issues │ --> │  Code        │
│  (spec-kit)  │     │  (ECOM-1,    │     │  (commits    │
│              │     │   ECOM-2...) │     │   reference  │
│  Source of   │     │  Track       │     │   issue keys)│
│  truth for   │     │  progress    │     │              │
│  what to     │     │  and status  │     │              │
│  build       │     │              │     │              │
└──────────────┘     └──────────────┘     └──────────────┘
```

### 3.1 Create the First Issue

1. In Claude Code, ask Claude to create the first Jira issue based on your tasks:

   ```
   Based on the tasks in @specs/001-sales-dashboard/tasks.md, what should be the first Jira issue? Create it in the ECOM project.
   ```

   Replace `001-sales-dashboard` with your actual feature folder name if it differs.

   > **How does Claude know to use Jira?** When you mention "Jira" or "ECOM project," Claude recognizes that it needs the Atlassian MCP server and uses it automatically. You do not need to activate MCP manually -- Claude selects the right tool based on your request. This is part of why MCP is powerful: it extends Claude's capabilities transparently.

2. Claude reads the tasks file, formulates an appropriate Jira issue, uses the Atlassian MCP to create it, and returns the details including the issue key (e.g., ECOM-1).

3. Verify in Jira: open your browser, navigate to your ECOM project backlog, and confirm the issue exists. Click into it and read the description -- it should match the corresponding task from spec-kit.

**Checkpoint:** ECOM-1 is visible in your Jira backlog with a detailed description.

### 3.2 Create Remaining Issues

1. Ask Claude to create issues for the remaining tasks:

   ```
   Create Jira issues in the ECOM project for the remaining tasks in @specs/001-sales-dashboard/tasks.md
   ```

   Replace the folder name if yours differs.

2. Claude creates multiple issues. This may take a minute as it processes each task and communicates with Jira.

3. Verify in Jira: refresh the backlog to see all new issues (ECOM-2, ECOM-3, etc.). Each should have a description derived from spec-kit tasks.

**Checkpoint:** Multiple issues are visible in the Jira backlog, each with descriptions matching spec-kit tasks.

> **Pro Tip:** Open a few issues and read their descriptions. Notice how the progression from PRD to spec-kit to Jira creates increasingly specific, actionable items. The PRD said "display Total Sales"; the spec-kit task might say "create KPI scorecards using Streamlit metric components with formatted currency values"; the Jira issue captures this as a trackable work item. This is the refinement process in practice.

---

## Section 4: Build the Dashboard (~35 min)

### Understanding Streamlit

> **What is Streamlit?** Streamlit is a Python library that transforms Python scripts into interactive web applications. Instead of writing HTML, CSS, and JavaScript -- the traditional technologies for building web pages -- you write Python and Streamlit handles the web interface automatically. It is especially popular in data science and business analytics because it lets analysts create dashboards quickly using the language they already know.
>
> For example, this Python code:
> ```python
> import streamlit as st
> st.title("Sales Dashboard")
> st.metric("Total Sales", "$650,000")
> ```
> produces a web page with a title and a formatted metric card. No HTML needed.
>
> Streamlit is not the only option for dashboards (Tableau, Power BI, and Dash are alternatives), but it works well for capstone projects: it uses pure Python, integrates with Pandas and Plotly, and deploys for free. You can use the same data manipulation skills you learned in your coursework.

### Claude Code Editing Modes

Before you start building, understand how Claude Code interacts with your files. Claude Code has three editing modes that control how it handles file changes:

| Mode | Behavior | When to Use |
|------|----------|-------------|
| **Normal** | Asks permission before each edit | When learning and reviewing each change carefully |
| **Auto-accept** | Makes edits without asking | When you trust the workflow and want momentum |
| **Plan mode** | Explains what it will do, waits for approval, then executes | When you want to review the approach before execution |

Press **Shift+Tab** to cycle between modes. The current mode is displayed in the Claude Code interface.

> **Recommendation for this session:** Switch to **Auto-accept** mode for the build phase. You have already defined detailed specifications, and Claude will follow them. Auto-accept lets you maintain momentum through the implementation cycle. If you prefer to review each change (a valid learning choice), stay in Normal mode -- it will just take longer.

### 4.1 Implement the First Issue

1. Ask Claude which issue to start with. Claude considers dependencies and suggests a logical starting point:

   ```
   Which Jira issue should we implement first?
   ```

   Claude typically recommends starting with the environment setup or app structure issue, since other issues depend on it.

2. Implement the issue using the spec-kit implement command:

   ```
   /speckit.implement

   Implement ECOM-1 and move it to In Progress in Jira.
   ```

   Replace `ECOM-1` with whichever issue Claude recommended.

   > **What happens during implementation:** Claude reads the Jira issue description, consults the specification and plan, then writes the code. Watch the output -- you will see Claude creating files, writing functions, and making decisions. Pay attention to which libraries Claude imports, how it structures the code, and how it handles data loading.

3. Ask Claude to explain what it created:

   ```
   What files did you create? Explain what each one does.
   ```

   Understanding the file structure helps you learn from the AI's work rather than treating it as a black box.

4. Test the dashboard. First, activate your Python virtual environment and install dependencies, then run the app:

   ```bash
   source venv/bin/activate       # macOS
   # or: venv\Scripts\activate    # Windows

   streamlit run app.py
   ```

   > **Key Concept: Virtual Environments.** The `source venv/bin/activate` command activates a **virtual environment** -- an isolated Python installation specific to this project. Without it, packages you install might conflict with other Python projects on your machine. The virtual environment ensures that your dashboard's dependencies (Streamlit, Pandas, Plotly) are contained within this project. You will see `(venv)` at the beginning of your terminal prompt when the environment is active.

5. Open `http://localhost:8501` in your browser. You should see the beginnings of your dashboard. The exact content depends on which issue you implemented first.

6. When done reviewing, press **Ctrl+C** in the terminal to stop the Streamlit server.

**Checkpoint:** The dashboard runs locally at `http://localhost:8501` without errors.

### 4.2 Commit, Push, and Update Jira

Now you will save your work using Git and create a traceable link between your code and the Jira issue. This three-step process -- commit, push, update -- is the basic rhythm of professional development.

#### Understanding Git's Workflow

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

- **Working directory** -- the files on your computer as you edit them. Changes here are not yet tracked by Git.
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

1. **Commit your changes.** Ask Claude to create a commit with the Jira key in the message. Also ensure the virtual environment directory is not tracked:

   ```
   Commit my changes for ECOM-1. Make sure venv/ is in .gitignore.
   ```

   Claude will add `venv/` to `.gitignore` (if not already there), stage your changes, and create a commit with a message like "ECOM-1: Set up project structure and dependencies."

   > **Key Concept: .gitignore.** The `.gitignore` file tells Git which files and directories to ignore. Virtual environments (`venv/`), compiled files, and operating system files should never be committed to a repository -- they are large, machine-specific, and can be regenerated. The `.gitignore` file prevents accidental commits of these files.

   > **What is a commit hash?** After committing, Git produces a unique identifier called a **commit hash** -- a string like `05a9ada`. This hash is a fingerprint: no two commits in the history of your repository will ever have the same hash. You will include this hash in Jira so anyone can find exactly which code change fulfilled a specific requirement.

2. **Push to GitHub.** Upload your local commit to the remote repository:

   ```
   Push my changes to GitHub.
   ```

   If this is your first push on the feature branch, Claude may need to set the upstream tracking branch. It handles this automatically.

3. **Update Jira with evidence.** Close the loop by recording what you did in Jira:

   ```
   Update ECOM-1 in Jira: add a comment with implementation summary, commit hash, branch name, and GitHub link. Move to Done.
   ```

   Claude adds a comment to the Jira issue containing the implementation details and changes the status to Done.

4. **Verify in Jira.** Open ECOM-1 in your browser and confirm:
   - Status is "Done"
   - A comment exists with the implementation summary, commit hash, branch name, and a GitHub link

> **If Claude cannot access Jira:** Run `/mcp`, select `atlassian`, and press Enter to re-authenticate. Then retry the update command.

**Checkpoint:** Code is on GitHub. ECOM-1 shows "Done" in Jira with a detailed evidence comment.

### 4.3 Complete Remaining Issues

Now repeat the implementation cycle for each remaining Jira issue. Skip the deployment issue -- that comes in Section 5.

The cycle for each issue is:

```
Ask which issue is next
        |
        v
/speckit.implement with issue key --> Move to In Progress
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

Here is the pattern for each issue:

```
/speckit.implement

Implement ECOM-2 and move it to In Progress in Jira.
```

After implementation and testing:

```
Commit my changes for ECOM-2 and push to GitHub.

Update ECOM-2 in Jira with implementation summary, commit hash, branch name, and GitHub link. Move to Done.
```

Replace `ECOM-2` with the current issue key. Repeat for ECOM-3, ECOM-4, and so on.

> **Skip the deployment issue for now.** You cannot deploy until your code is merged to `main`, which happens in the next step. Leave the deployment issue in "To Do" status.

> **Pro Tip:** Watch Claude's output as it implements each issue. You will see files being created, imports being added, and functions being written. This is a good way to learn how professional code is structured. Pay attention to how Claude names variables, organizes functions, and handles data. You can reuse these patterns in your capstone.

After working through all implementation issues, test the complete dashboard one final time:

```bash
source venv/bin/activate       # macOS, if not already active
streamlit run app.py
```

Open `http://localhost:8501` and verify that all components are present: KPI scorecards, a sales trend line chart, and category/region bar charts. Press **Ctrl+C** to stop the server.

**Checkpoint:** All implementation issues are marked "Done" in Jira with evidence comments. Only the deployment issue remains open.

### 4.4 Merge to Main

Your feature branch contains all the implementation work. Now you will bring those changes into the `main` branch, making them the official version of the code.

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
> This is why feature branches are valuable -- they let you develop freely without risking the stable `main` branch. When you are confident your work is complete, you merge once and know that `main` stays reliable.

1. **Confirm your current branch:**

   ```
   Which git branch am I on?
   ```

   You should be on your feature branch (e.g., `001-sales-dashboard`).

2. **Merge into main:**

   ```
   Merge my current feature branch into main
   ```

   Claude switches to `main`, merges the feature branch, and reports the result.

3. **Push main to GitHub:**

   ```
   Push main to GitHub
   ```

4. **Verify on GitHub:** Open your repository in a browser, select the **main** branch from the branch dropdown, and confirm all dashboard files (app.py, requirements.txt, data directory, etc.) are present.

**Checkpoint:** The `main` branch on GitHub contains all your dashboard code.

---

## Section 5: Deploy (~15 min)

### Why Deployment Matters

> **Why This Matters:** Building something that only runs on your laptop does not deliver value. Deployment makes your work accessible to stakeholders -- a manager, a client, or your capstone advisor can open a URL and see your dashboard without installing Python or cloning a repository. Going from analysis to a shared, accessible output is a skill most graduates lack. Many people can build charts in a Jupyter notebook; far fewer can deploy an interactive dashboard that stakeholders actually use.

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

2. Click **Sign in with GitHub** and authorize Streamlit to access your repositories.

3. Click **Create app** (or **New app**).

4. Configure the deployment:

   | Field | Value |
   |-------|-------|
   | **Repository** | `[your-username]/ai-dev-workflow-tutorial` |
   | **Branch** | `main` |
   | **Main file path** | `app.py` (or wherever your Streamlit entry point is) |

5. Optionally, expand **Advanced settings** and set a custom URL slug, such as `sales-dashboard-yourname`. This determines the first part of your public URL.

6. Click **Deploy** and wait 1-2 minutes. Streamlit Cloud installs your dependencies (from `requirements.txt`), runs your app, and makes it available at a public URL.

7. When deployment completes, you receive a URL like:

   ```
   https://sales-dashboard-yourname.streamlit.app
   ```

   Open this URL and verify that your dashboard looks and functions the same as it did locally.

> **If deployment fails:** The most common cause is a missing or incorrect `requirements.txt`. Check that the file exists in your repository's `main` branch on GitHub and lists all required packages (streamlit, pandas, plotly, etc.). If it is missing, ask Claude to create one, commit, push, and redeploy.

### 5.2 Update Jira

Complete the final Jira issue by recording the deployment:

```
Update the deployment Jira issue: add the live Streamlit URL as a comment. Move to Done.
```

**Checkpoint:** The dashboard is live and accessible at a public URL. The deployment Jira issue is marked "Done" with the URL in a comment.

---

## Section 6: Final Verification Checklist

Before submitting, walk through every item below. Each category corresponds to a section of this guide.

### MCP and Spec-Kit

- [ ] Atlassian MCP connected and functional
- [ ] Constitution created (`.specify/memory/constitution.md`)
- [ ] Specification created (`specs/[feature-name]/spec.md`)
- [ ] Implementation plan created (`specs/[feature-name]/plan.md`)
- [ ] Tasks generated (`specs/[feature-name]/tasks.md`)

### Jira

- [ ] Issues created from spec-kit tasks (ECOM-1, ECOM-2, etc.)
- [ ] All issues marked "Done"
- [ ] Each issue has a comment with: implementation summary, commit hash, branch name, GitHub link

### Dashboard

- [ ] Runs locally with KPIs, line chart, and bar charts
- [ ] Deployed and publicly accessible on Streamlit Cloud

### Version Control

- [ ] Commits include Jira issue keys in messages
- [ ] Feature branch merged to main
- [ ] All code pushed to GitHub on the main branch

---

## The Complete Workflow -- What You Accomplished

```
PRD [done] -> spec-kit [done] -> Jira [done] -> Code [done] -> Commit [done] -> Push [done] -> Deploy [done] -> Live! [done]
```

In this session, you practiced five professional skills:

1. **Spec-driven development** -- You specified, planned, broke down tasks, then implemented. This discipline works with any technical project, not just this tutorial.

2. **AI-assisted coding** -- You used Claude Code as a tool guided by clear specifications. You saw how context engineering (the `@` symbol, MCP connections, slash commands) makes AI assistance more precise.

3. **Project management with Jira** -- Every piece of work was tracked from creation to completion, with evidence linking requirements to code changes.

4. **Version control with Git and GitHub** -- You created feature branches, committed with meaningful messages, pushed to a remote, and merged completed work.

5. **Deployment** -- You turned a local script into a live application with a shareable URL.

> **For Your Career:** This workflow scales. Whether you are building a data pipeline, a dashboard, or a machine learning model, the pattern is the same: specify, plan, track, build, deploy. You now have hands-on experience with the full cycle. In interviews, you can describe not just what you built but how you built it -- and that process awareness matters to hiring managers.

---

## What to Submit

**Due: January 25** -- Submit the following to Brightspace under the **AI Dev Workflow Tutorial** assignment:

1. **GitHub repository link** -- your public repo URL (e.g., `https://github.com/yourusername/ai-dev-workflow-tutorial`)

2. **Streamlit dashboard link** -- your live deployed URL (e.g., `https://sales-dashboard-yourname.streamlit.app`)

3. **Jira screenshot(s)** -- screenshot of one completed Jira issue showing:
   - Issue status is "Done"
   - Comment with implementation summary, commit hash, branch name, and GitHub link

   If the full issue does not fit in one screenshot, submit multiple screenshots named `jira-01.png`, `jira-02.png`, etc.

Make sure your PRD and notes directories are included in your repository.

---

## Comprehensive Troubleshooting

This section covers the most common issues students encounter. For each problem, you will find three parts: what you see (the symptom), why it happens (the root cause), and how to fix it (the solution).

---

### MCP Connection Issues

**What you see:** Claude says it cannot access Jira, or `/mcp` does not show the `atlassian` server.

**Why it happens:** The MCP server either was not added correctly, or the authentication token has expired. Authentication tokens are temporary by design -- Atlassian issues short-lived tokens for security, which means they expire during long sessions.

**How to fix it:**

If the server is not listed in `/mcp`:

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

### Spec-Kit Slash Commands Not Working

**What you see:** Typing `/speckit.constitution` or `/speckit.specify` does nothing, or Claude does not recognize the command.

**Why it happens:** Spec-kit was not initialized in this project, or the initialization did not complete successfully. The slash commands are stored as files in `.claude/commands/`, and Claude Code reads them at startup.

**How to fix it:**

1. Exit Claude Code: `/exit`
2. Run initialization in the terminal:
   ```bash
   specify init . --ai claude
   ```
3. Verify the commands directory exists:
   ```bash
   ls .claude/commands/
   ```
   You should see files like `speckit.constitution.md`, `speckit.specify.md`, etc.
4. Restart Claude Code: `claude`
5. Try the slash command again

If slash commands still do not work, you can use natural language instead. Rather than `/speckit.constitution`, tell Claude directly:

```
Create a spec-kit constitution for this e-commerce analytics project (Streamlit dashboard for sales data). Save it to .specify/memory/constitution.md.
Ask me one question at a time about this project. Propose numbered options I can choose from. After 3-5 questions, generate the constitution.
```

Claude will produce equivalent results without the slash command.

---

### ModuleNotFoundError

**What you see:** Running `streamlit run app.py` produces `ModuleNotFoundError: No module named 'streamlit'` (or 'pandas' or 'plotly').

**Why it happens:** Python cannot find the required package because either (a) the virtual environment is not activated, or (b) the package was never installed. The virtual environment is an isolated Python installation; packages installed inside it are not visible outside it, and vice versa.

**How to fix it:**

1. Check if your virtual environment is active. Look for `(venv)` at the beginning of your terminal prompt.

2. If it is not active, activate it:
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

### Port 8501 Already in Use

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

### Dashboard Shows No Data or Errors on Load

**What you see:** The dashboard loads but shows no charts, displays "NaN" values, or throws a data-related error.

**Why it happens:** The CSV file path in your code does not match the actual file location, or the data file has an unexpected structure. This commonly occurs when the code uses a relative path that resolves differently depending on where you run the command.

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

### Cannot Push -- Permission Denied

**What you see:** `git push` fails with `Permission denied` or `remote: Permission to LMU-ISBA/ai-dev-workflow-tutorial.git denied`.

**Why it happens:** Your local repository is pointed at the original repository rather than your fork. You can pull from the original but cannot push to it -- you can only push to your own fork.

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

### Git Merge Conflicts

**What you see:** When merging the feature branch into main, Git reports "merge conflict" and stops.

**Why it happens:** Both branches modified the same part of the same file, and Git cannot automatically determine which version to keep. This is uncommon in this tutorial (since you are the only developer), but can happen if you made manual changes to `main` during the session.

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

### "Not a Git Repository" Error

**What you see:** Git commands fail with `fatal: not a git repository (or any of the parent directories)`.

**Why it happens:** Your terminal is in a directory that is not inside your project. Git commands only work when you are inside a directory that has been initialized with Git (contains a `.git` folder).

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

3. Verify you are in the right place:
   ```bash
   ls .git
   ```
   You should see Git's internal directory.

---

### Claude Code Rate Limits

**What you see:** Claude Code responds with a rate limit message or becomes slow to respond.

**Why it happens:** Your Claude Pro subscription has a usage cap per time period. Heavy usage during implementation (especially with multiple large file edits) can approach this cap.

**How to fix it:**

1. **Wait a few minutes.** Rate limits typically reset on a rolling window. A 5-10 minute break is usually sufficient.

2. **Work in smaller increments.** Instead of asking Claude to implement an entire feature at once, break requests into smaller pieces:
   ```
   # Instead of: "Implement the entire dashboard"
   # Try: "Create the KPI scorecards section of app.py"
   ```

3. **Use plan mode.** Press Shift+Tab to switch to plan mode. Claude explains what it will do without making changes, using fewer tokens. Review the plan, then ask Claude to execute it.

4. **Upgrade if needed.** If you consistently hit limits, Claude Max ($100/month) provides higher usage caps. Most students find Pro sufficient for the tutorial sessions.

---

### "specify: command not found"

**What you see:** Running `specify init . --ai claude` produces `command not found` or `specify is not recognized`.

**Why it happens:** Spec-kit was not installed, or it was installed but the terminal cannot find it because the PATH has not been updated.

**How to fix it:**

1. Open a **new terminal** (Terminal --> New Terminal). New tools often require a fresh terminal session to be recognized.

2. If it still fails, reinstall spec-kit:
   ```bash
   uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
   ```

3. Open another new terminal and retry: `specify --help`

4. If `uv` itself is not found, return to the [pre-work setup guide](pre-work-setup.md) and install `uv` first.

---

## Glossary

Quick-reference table of key terms used in this document.

| Term | Definition |
|------|------------|
| **Branch** | A separate line of development in Git, allowing isolated work without affecting the main codebase |
| **Commit** | A saved snapshot of your project at a specific point in time, like a version you can return to |
| **Commit Hash** | A unique identifier (e.g., `05a9ada`) assigned to each commit, serving as its permanent fingerprint |
| **Deploy** | Make software accessible on a server so users can reach it via a URL |
| **Feature Branch** | A branch created specifically for developing one feature, separate from main |
| **Fork** | Your personal copy of someone else's repository on GitHub, under your own account |
| **Merge** | Combine changes from one branch into another, integrating completed work |
| **MCP** | Model Context Protocol -- a plugin system that lets Claude Code connect to external services like Jira |
| **PRD** | Product Requirements Document -- a written description of what to build and why |
| **Push** | Upload local commits to a remote repository (GitHub), making them visible and backed up |
| **Staging Area** | A holding zone in Git for changes you intend to include in your next commit |
| **spec-kit** | GitHub's toolkit for spec-driven development, converting requirements into structured plans |
| **Streamlit** | A Python library that transforms Python scripts into interactive web applications |
| **Traceability** | The ability to link code changes back to the requirements that prompted them |
| **venv** | Virtual environment -- an isolated Python installation that keeps project dependencies separate |
| **.gitignore** | A file that tells Git which files and directories to exclude from version control |

---

## What's Next

Continue to [Capstone Project Dev Environment](../../v1/06-capstone-project-dev-environment.md) to set up your capstone project using the same workflow you practiced today.
