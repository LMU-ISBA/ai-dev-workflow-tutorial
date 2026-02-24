# Session 2: Build & Deploy

**From specification to live dashboard in one session.**

**Estimated time:** 100 minutes

---

**By the end of this session, you will have:**

- Atlassian MCP connected to Claude Code
- spec-kit artifacts created: constitution, specification, plan, and tasks
- Jira issues created and tracked through completion
- A working Streamlit dashboard built with AI assistance
- Code committed and pushed to GitHub
- A live, publicly accessible dashboard URL

---

## Prerequisites Check

Verify your Session 1 setup before continuing. Run each command in Cursor's terminal:

```bash
git --version
# Expected: git version 2.x.x

python3 --version       # macOS
python --version         # Windows
# Expected: Python 3.11.x or higher

ls data/sales-data.csv
# Expected: data/sales-data.csv (file listed without error)

claude --version
# Expected: version number displayed
```

All four commands should produce output without errors. If any command fails, return to the Session 1 guide and resolve the issue before proceeding.

---

## 1. Connect Claude Code to Jira (~10 min)

**MCP (Model Context Protocol)** is a standard that lets Claude Code connect to external tools and services. It is a plugin system -- once connected, Claude can read from and write to those tools directly. In this section, you will connect Claude Code to Jira so it can create issues, update statuses, and add comments without leaving the terminal.

This integration matters because it creates **traceability** -- the ability to link every code change back to the requirement that prompted it. In your capstone and in professional settings, stakeholders and teammates need to understand not just what was built, but why. Traceability is how you answer that question.

### Steps

1. **Exit Claude Code if running.** If you are currently in a Claude Code session, type `/exit` to quit. The MCP server must be added before starting a new session.

2. **Add the Atlassian MCP server.** Run this command in Cursor's terminal:

   ```bash
   claude mcp add --transport sse atlassian https://mcp.atlassian.com/v1/sse
   ```

   You should see a confirmation message that the server was added to your configuration.

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

   You should see `atlassian` in the list of MCP servers. It will likely show that authentication is required.

6. **Authenticate.** Use the **arrow keys** to select `atlassian`, then press **Enter**. A browser window will open.

7. **Complete browser authentication.** Log in with your Atlassian account (the same one with your ECOM project), authorize Claude Code to access your workspace, and return to the terminal.

8. **Test the connection.** Ask Claude:

   ```
   What Jira projects do I have access to?
   ```

   Claude should respond with a list that includes your ECOM project. You may see output like:

   | Key | Name | Type |
   |-----|------|------|
   | ECOM | E-Commerce Analytics | Software (Team-managed) |

> **If MCP shows "authentication required" later:** This is normal and may happen periodically during your session. Run `/mcp`, select `atlassian` with the arrow keys, and press Enter to re-authenticate. You will not lose any work.

**Checkpoint:** Claude can see your ECOM project and respond to queries about your Jira workspace.

---

## 2. Spec-Kit Workflow (~25 min)

**spec-kit** is GitHub's tool for spec-driven development. It creates a structured plan before any code is written, following a four-step sequence: Constitution, Specification, Plan, and Tasks. This approach prevents building the wrong thing -- which is especially important when working with AI, since AI can build the wrong thing very fast if given vague instructions.

This is the same discipline you will use in your capstone: start with requirements, create a plan, then execute. Good planning saves more time than good coding.

### 2.1 Initialize Spec-Kit

This step creates the configuration files and slash commands that spec-kit needs. Run this command in **Cursor's terminal** (not inside Claude Code):

```bash
specify init . --ai claude
```

- If you see a "directory not empty" warning, type `y` and press Enter. This is expected because you already have files in the repository.
- When asked to choose a script type, use the arrow keys to select:
  - **macOS:** `sh` (POSIX Shell)
  - **Windows:** `ps` (PowerShell)

This creates the slash commands you will use throughout the rest of this section. The commands will not work until this initialization completes successfully.

**Checkpoint:** Verify that both directories exist:

```bash
ls .specify/
ls .claude/commands/
```

You should see files such as `speckit.constitution.md`, `speckit.specify.md`, and others in the `.claude/commands/` directory. These are the detailed prompts that power each slash command.

### 2.2 Create the Constitution

The constitution establishes principles and guidelines that govern the entire project. It ensures Claude makes consistent decisions -- for example, always using a virtual environment, or always preferring readable code over clever code.

1. **Start Claude Code** if not already running:

   ```bash
   claude
   ```

2. **Run the constitution command:**

   ```
   /speckit.constitution

   Create a constitution for our e-commerce analytics project.
   The project will build a Streamlit dashboard for sales data visualization.
   Key principles: simple readable code, user-friendly visualizations, Python best practices, use virtual environment for dependency isolation.
   ```

3. **Approve the file creation.** Claude will ask permission to create or edit files. You have three options:
   - **Yes** -- approve this single edit
   - **Yes, allow all edits during this session** -- approve all future edits without being asked (recommended to speed things up)
   - **No** -- reject the edit

   Select **Yes** or the "allow all" option to continue.

4. **Preview the result.** In Cursor's file explorer (left sidebar), navigate to `.specify/memory/constitution.md` and open it. You should see the principles you specified, organized into a structured document.

**Checkpoint:** `.specify/memory/constitution.md` exists and contains principles about readable code, visualizations, Python best practices, and virtual environment usage.

### 2.3 Create the Specification

The specification refines the PRD (Product Requirements Document) into detailed, actionable requirements. Where the PRD describes what the business needs, the specification describes exactly what to build.

**About the `@` symbol:** When you type `@` followed by a file path in Claude Code, it includes that file's entire content in your message. This is how you give Claude the full context of your PRD without copy-pasting. You can reference multiple files in a single message using multiple `@` references.

1. **Run the specification command:**

   ```
   /speckit.specify @prd/ecommerce-analytics.md
   ```

   This tells Claude to read the PRD and use the spec-kit process to generate a detailed specification from it.

2. **Wait for Claude to finish.** Claude will analyze the PRD, identify requirements, and create a structured specification document. This may take a minute.

3. **Review the output.** In Cursor's file explorer, look inside the `specs/` directory. You should see a feature folder (e.g., `001-sales-dashboard/`) containing `spec.md`. Open it to see the detailed specification Claude generated.

> **Note:** spec-kit may automatically create a feature branch (e.g., `001-sales-dashboard`). A **branch** is a separate line of development that keeps your work isolated from the main codebase. This is expected and is a professional best practice -- you never make changes directly on the `main` branch. You will merge everything back to `main` after implementation is complete.

**Checkpoint:** A specification file exists at `specs/[feature-name]/spec.md`. The exact folder name depends on what spec-kit generates -- it is typically based on the feature name.

### 2.4 Create the Implementation Plan

The plan translates the specification into a technical approach: which technologies to use, how to structure the code, and in what order to build things.

1. **Run the plan command:**

   ```
   /speckit.plan

   Create an implementation plan. Use Python with Streamlit, Pandas for data handling, Plotly for interactive charts. Clean code organization.
   ```

   By specifying the technology stack here, you guide Claude toward the tools you want rather than letting it choose arbitrarily. Giving clear direction on technical decisions while letting the AI handle implementation details produces better results than leaving every choice to the AI.

2. **Review the plan.** Open `specs/[feature-name]/plan.md` in Cursor's file explorer. The plan should cover architecture decisions, component structure, data flow, and technology choices.

**Checkpoint:** `specs/[feature-name]/plan.md` exists and describes a technical approach using Streamlit, Pandas, and Plotly.

### 2.5 Generate Tasks

The final spec-kit step breaks the plan into specific, ordered implementation tasks. Each task becomes a unit of work that maps to a Jira issue.

1. **Run the tasks command:**

   ```
   /speckit.tasks
   ```

2. **Review the generated tasks.** Open `specs/[feature-name]/tasks.md` in Cursor's file explorer. You should see numbered tasks such as:
   - Set up Python virtual environment and install dependencies
   - Create main Streamlit app structure
   - Implement KPI scorecards (Total Sales, Total Orders)
   - Implement sales trend line chart
   - Implement category breakdown bar chart
   - Implement region breakdown bar chart
   - Deploy to Streamlit Community Cloud

   The exact tasks depend on what spec-kit generates, but they should cover the full scope of the specification.

**Checkpoint:** `specs/[feature-name]/tasks.md` exists with clearly defined, ordered implementation steps.

---

## 3. Create Jira Issues (~10 min)

Now convert your spec-kit tasks into tracked Jira issues. Claude uses the Atlassian MCP connection to create issues directly -- no switching between applications or copy-pasting required.

### 3.1 Create the First Issue

1. **Tell Claude to create the first issue.** In Claude Code, run:

   ```
   Based on the tasks in @specs/001-sales-dashboard/tasks.md, what should be the first Jira issue? Create it in the ECOM project.
   ```

   Replace `001-sales-dashboard` with your actual feature folder name if it differs.

2. **Observe what Claude does.** Claude will read the tasks file, determine the first logical issue, and use the Atlassian MCP server to create it in your ECOM project. You will see Claude interacting with the Jira API in real time.

3. **Verify in Jira.** Open your Jira workspace in a browser and navigate to the ECOM project backlog. You should see the new issue (e.g., ECOM-1) with a description that matches the task from spec-kit. Click on it to confirm the description looks correct.

**Checkpoint:** ECOM-1 is visible in your Jira backlog with a detailed description matching the first spec-kit task.

### 3.2 Create Remaining Issues

1. **Ask Claude to create all remaining issues:**

   ```
   Create Jira issues in the ECOM project for the remaining tasks in @specs/001-sales-dashboard/tasks.md
   ```

   Replace the folder name if yours differs.

2. **Wait for Claude to finish.** Depending on the number of tasks, Claude will create several issues (ECOM-2, ECOM-3, etc.). Each one maps to a task from your spec-kit tasks file.

3. **Verify in Jira.** Refresh the ECOM project backlog in your browser. Click on a few issues to confirm they have meaningful descriptions. You should see issues covering environment setup, each dashboard component, and deployment.

**Checkpoint:** Multiple issues (ECOM-1, ECOM-2, etc.) are visible in your Jira backlog, each with descriptions matching spec-kit tasks.

---

## 4. Build the Dashboard (~35 min)

This is where the dashboard comes to life. You will use Claude Code to implement each Jira issue, test the results, and track your progress.

**Streamlit** is a Python library that creates web dashboards directly from Python code -- no HTML, CSS, or JavaScript required. You write Python, and Streamlit turns it into an interactive web page. It is popular in analytics and data science because you can go from raw data to a shareable dashboard quickly.

**Claude Code editing modes:** Press **Shift+Tab** to cycle between modes at any time:

| Mode | Behavior | When to use |
|------|----------|-------------|
| **Normal** | Asks permission before each edit | When you want to review every change |
| **Auto-accept** | Makes edits without asking | Recommended for the build phase |
| **Plan mode** | Explains what it will do, then waits for approval | For complex or risky changes |

Consider switching to **Auto-accept** for the build phase to maintain momentum. You can switch back at any time.

### 4.1 Implement the First Issue

1. **Ask Claude which issue to start with:**

   ```
   Which Jira issue should we implement first?
   ```

   Claude will review your issues and recommend the logical starting point (usually the environment setup or app structure task).

2. **Implement the issue:**

   ```
   /speckit.implement

   Implement ECOM-1 and move it to In Progress in Jira.
   ```

   Replace `ECOM-1` with the issue Claude recommended in step 1.

3. **Review what Claude creates.** Watch the output as Claude generates files, installs dependencies, and structures the application. If you want to understand the code, ask:

   ```
   What files did you create? Explain what each one does.
   ```

4. **Test the dashboard.** Follow Claude's instructions to run the application. The typical process is:

   ```bash
   source venv/bin/activate       # macOS
   # or: venv\Scripts\activate    # Windows
   streamlit run app.py
   ```

   > **If you see `ModuleNotFoundError: streamlit`:** You need to activate the virtual environment first. Run the `source venv/bin/activate` (macOS) or `venv\Scripts\activate` (Windows) command, then try again.

5. **View the dashboard.** Open http://localhost:8501 in your browser. At this stage, you may see the dashboard title and basic structure. Full charts and KPIs come as you implement subsequent issues.

6. **Stop the server** when done reviewing: press **Ctrl+C** in the terminal.

**Checkpoint:** The dashboard runs locally at http://localhost:8501 without errors.

### 4.2 Commit, Push, and Update Jira

After completing each issue, you save your work and record evidence of completion. Here are the Git concepts involved:

- **Commit** = a saved snapshot of your code at a specific point in time. Like saving a version of a document -- you can always return to any previous commit. Each commit gets a unique ID called a **commit hash** (e.g., `05a9ada`), which acts as a fingerprint for that exact version.
- **Push** = upload your commits to GitHub. Until you push, your commits exist only on your local computer. Pushing backs up your work and makes it visible to others.
- **Branch** = a separate line of development. spec-kit created a feature branch (e.g., `001-sales-dashboard`) so your changes stay isolated from `main` until the feature is ready. This is standard professional practice -- you never code directly on the `main` branch.

**Steps:**

1. **Commit your changes:**

   ```
   Commit my changes for ECOM-1. Make sure venv/ is in .gitignore.
   ```

   > **Why .gitignore?** The `.gitignore` file tells Git which files to skip. The `venv/` folder contains installed Python packages that anyone can recreate from `requirements.txt`, so it should never be committed. Claude handles this automatically when you remind it.

   You will see output confirming the commit, including the commit hash and branch name.

2. **Push to GitHub:**

   ```
   Push my changes to GitHub.
   ```

   After pushing, you can view your code on GitHub. Navigate to your repository, click the branch dropdown, and select your feature branch to see the committed files.

3. **Update Jira with completion evidence:**

   ```
   Update ECOM-1 in Jira: add a comment with implementation summary, commit hash, branch name, and GitHub link. Move to Done.
   ```

   This creates a traceable record linking Jira (project management) to GitHub (code). Anyone reviewing the project can follow the trail from requirement to implementation.

4. **Verify in Jira.** Open ECOM-1 in your browser and confirm:
   - Status shows **Done**
   - A comment exists with the implementation summary, commit hash, branch name, and a link to the commit on GitHub

> **If Claude cannot access Jira:** Run `/mcp`, select `atlassian`, and press Enter to re-authenticate.

**Checkpoint:** Code is on GitHub, and ECOM-1 shows "Done" in Jira with a detailed comment containing implementation evidence.

### 4.3 Complete Remaining Issues

Repeat the implement-test-commit cycle for each remaining Jira issue. The pattern is the same each time:

**Step 1 -- Ask which issue is next:**

```
Which Jira issue should we implement next?
```

**Step 2 -- Implement it:**

```
/speckit.implement

Implement ECOM-2 and move it to In Progress in Jira.
```

Replace the issue key with whichever issue Claude recommends.

**Step 3 -- Test the dashboard.** After each implementation, run the dashboard and verify the new feature works. Check that previous features still work correctly.

**Step 4 -- Commit, push, and update Jira:**

```
Commit my changes for ECOM-2 and push to GitHub.

Update ECOM-2 in Jira with implementation summary, commit hash, branch name, and GitHub link. Move to Done.
```

Replace `ECOM-2` with your actual issue key. Repeat this entire cycle for ECOM-3, ECOM-4, and every subsequent implementation issue.

> **Skip the deployment issue for now.** If you have a Jira issue for deployment, leave it open. You cannot deploy until your code is merged to the `main` branch, which happens in the next step.

> **Tip:** Watch Claude's terminal output as it works. You will see files being created, commands being run, and problems being solved in real time. If Claude encounters an error, observe how it diagnoses and fixes the issue. Watching how Claude diagnoses and fixes errors teaches you more than reading about it.

> **Want to see the dashboard yourself while building?** Ask Claude: `How do I run the dashboard in my own browser?` You can run the dashboard at any point to see your progress.

> **Claude suggests next prompts.** After completing an action, Claude may suggest a follow-up prompt at the bottom of the terminal. Press **Tab** to accept it. While learning, writing your own prompts builds understanding of the workflow. As you get comfortable, the suggestions can speed things up.

**Checkpoint:** All implementation issues are marked "Done" in Jira with detailed comments. Only the deployment issue (if one exists) remains open.

### 4.4 Merge to Main

Now that all implementation is complete, combine your feature branch into the main branch.

**Merge** = combining changes from one branch into another. When you merge your feature branch into `main`, all the code you wrote becomes part of the official project. After merging, the `main` branch contains your complete dashboard.

1. **Confirm your current branch:**

   ```
   Which git branch am I on?
   ```

   You should be on your feature branch (e.g., `001-sales-dashboard`), not `main`.

2. **Merge into main:**

   ```
   Merge my current feature branch into main
   ```

   Claude will switch to the `main` branch and merge your feature branch changes into it.

3. **Push main to GitHub:**

   ```
   Push main to GitHub
   ```

   This updates the remote repository with your merged code.

4. **Verify on GitHub.** Navigate to your repository on GitHub. Make sure the branch dropdown shows **main**. You should see all your dashboard files -- `app.py`, `requirements.txt`, the `data/` directory, and any other files Claude created.

**Checkpoint:** The `main` branch on GitHub contains all your dashboard code, including every file from every implemented issue.

---

## 5. Deploy (~15 min)

Make your dashboard publicly accessible on Streamlit Community Cloud. After this step, anyone with the URL can view your dashboard.

> **Prerequisite:** Your code must be merged to `main` (Section 4.4) before deploying. Streamlit Cloud deploys from the `main` branch, so it cannot see code that only exists on a feature branch.

### 5.1 Deploy to Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io) and **sign in with GitHub**.
2. Click **Create app**.
3. Select your repository: `[your-username]/ai-dev-workflow-tutorial`.
4. Set **Branch** to `main`.
5. Set **Main file path** to `app.py` (or wherever your main dashboard file is located -- Claude may have named it differently).
6. Optionally, set a custom **App URL** such as `sales-dashboard-yourname` for a cleaner address.
7. Click **Deploy** and wait 1-2 minutes for the build to complete.

Once deployed, you will receive a public URL like:

```
https://sales-dashboard-yourname.streamlit.app
```

Open the URL in your browser to confirm the dashboard loads correctly with all KPIs, charts, and visualizations.

### 5.2 Update Jira

Complete the deployment issue with the live URL:

```
Update the deployment Jira issue: add the live Streamlit URL as a comment. Move to Done.
```

**Checkpoint:** Dashboard is live at a public URL and the deployment Jira issue is marked "Done" with the URL in the comments.

---

## 6. Final Verification Checklist

Before submitting your work, verify every item in this checklist:

### MCP and Spec-Kit
- [ ] Atlassian MCP connected and functional
- [ ] Constitution created (`.specify/memory/constitution.md`)
- [ ] Specification created (`specs/[feature-name]/spec.md`)
- [ ] Implementation plan created (`specs/[feature-name]/plan.md`)
- [ ] Tasks generated (`specs/[feature-name]/tasks.md`)

### Jira
- [ ] Issues created from spec-kit tasks (ECOM-1, ECOM-2, etc.)
- [ ] All issues marked "Done"
- [ ] Each issue has a comment with implementation summary, commit hash, branch name, and GitHub link

### Dashboard
- [ ] Runs locally with KPIs (Total Sales, Total Orders)
- [ ] Line chart shows sales trend over time
- [ ] Bar charts show sales by category and by region
- [ ] Deployed and publicly accessible on Streamlit Cloud

### Version Control
- [ ] Commits include Jira issue keys in messages
- [ ] Feature branch merged to main
- [ ] All code pushed to GitHub

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

## Quick Troubleshooting Reference

| Problem | Fix |
|---------|-----|
| MCP will not connect to Jira | Re-add the server: `claude mcp add --transport sse atlassian https://mcp.atlassian.com/v1/sse` |
| `/speckit.specify` does nothing | Run `specify init . --ai claude` first, then restart Claude Code with `claude` |
| spec-kit slash commands not found | Confirm `.claude/commands/` directory exists; re-run `specify init . --ai claude` if missing |
| `ModuleNotFoundError: streamlit` | Activate your virtual environment: `source venv/bin/activate` (macOS) or `venv\Scripts\activate` (Windows) |
| Port 8501 already in use | Use an alternate port: `streamlit run app.py --server.port 8502` |
| Dashboard shows no data | Verify the CSV path is correct: `data/sales-data.csv` |
| Cannot push -- permission denied | Run `git remote -v` and confirm the URL includes your GitHub username, not the instructor's |
| Claude says it cannot access Jira | Run `/mcp`, select `atlassian`, press Enter to re-authenticate |
| Dashboard will not deploy | Confirm `requirements.txt` exists on the `main` branch and includes `streamlit` |
| Streamlit Cloud shows "app not found" | Verify the main file path matches your actual file name (e.g., `app.py` vs `dashboard.py`) |

---

## The Complete Workflow

You have now completed the full development lifecycle:

```
PRD --> spec-kit --> Jira --> Code --> Commit --> Push --> Deploy --> Live
```

This is the workflow used by professional development teams. The tools and sequence transfer directly to your capstone project and beyond:

1. **Start with requirements** (PRD) so you know what to build -- in your capstone, this is your project proposal
2. **Plan before building** (spec-kit) so the AI builds the right thing -- this prevents wasted weeks
3. **Track your work** (Jira) so progress is visible and accountable -- your team and advisor can see status at any time
4. **Build with AI assistance** (Claude Code) so you can focus on decisions, not syntax -- you direct the what and why, AI handles the how
5. **Save and share your code** (Git and GitHub) so your work is backed up and collaborative -- no more emailing zip files between teammates
6. **Deploy for your audience** (Streamlit Cloud) so stakeholders can access your work -- a live URL is more impressive than a screenshot in a slide deck

### After Graduation

This workflow does not expire. Whether you join a consulting firm, a data analytics team, a technology company, or start your own venture, the pattern is the same: requirements, planning, tracking, building, deploying. The specific tools may vary (Jira might be Asana, Streamlit might be Tableau), but the discipline and the thinking are identical. Interviewers ask about your process, and now you have one to describe.

---

## What's Next

Continue to [Capstone Project Dev Environment](../../v1/06-capstone-project-dev-environment.md) to set up your capstone project development environment.
