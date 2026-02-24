# Session 1: Setup & Foundation

**Understanding and configuring your professional development environment**

Estimated time: 100 minutes

---

## What You Will Set Up

```
Accounts:  GitHub, Atlassian (Jira), Claude Pro
Tools:     Cursor, Git, Python 3.11+, uv, spec-kit, Claude Code
Repo:      Fork and clone the tutorial repository, initialize Claude Code
```

---

## Why This Setup Matters

Every technology company --- from two-person startups to Fortune 500 enterprises --- uses some variation of the workflow you are about to configure. The tools differ slightly from team to team, but the pattern is universal:

```
Requirements  -->  Code  -->  Test  -->  Deploy  -->  Monitor
```

Someone defines what needs to be built. Developers write code to meet those requirements. The code is tracked, reviewed, and deployed so users can access it. This cycle repeats continuously.

You are setting up the exact same pipeline, end to end, in a single session. By the time you finish today, you will have a professional development environment that mirrors what you would find on your first day at a technology company, a consulting firm, or a data science team.

### The MSBA Advantage

Analytics professionals who can **build and deploy** their own work are rare and highly valued. Most business analysts can create a model in a notebook. Far fewer can turn that model into a live dashboard, track the work in a project management system, and push the code to a shared repository. That gap is your opportunity.

### What You Will Be Able to Do After This Session

- Manage code with version control (Git and GitHub)
- Track work using industry-standard project management (Jira)
- Use AI to accelerate building (Claude Code)
- Plan before you build (spec-kit)
- Edit code in a modern, AI-aware editor (Cursor)

### Traditional vs. AI-Assisted Development

| Traditional Approach | AI-Assisted Approach |
|---------------------|---------------------|
| Search Google, copy from Stack Overflow | Ask Claude Code to explain and implement |
| Hours debugging with print statements | AI analyzes errors and suggests fixes |
| Write boilerplate code manually | AI generates scaffolding; you focus on business logic |
| Learn frameworks by reading documentation | AI teaches you as you build |
| Work alone, limited by your own knowledge | AI as a knowledgeable partner available at all times |

The AI-assisted approach does not replace understanding. It accelerates it. You still need to know what you are building and why. The AI handles much of the how.

---

## The Complete Toolchain

The following diagram shows every tool you will install today and how they connect. Refer back to this as you work through each section.

```
+-------------------------------------------------------------+
|               Your Development Toolchain                     |
+-------------------------------------------------------------+
|                                                              |
|  GitHub (code hosting)  <-->  Git (version control)          |
|       ^                           ^                          |
|       |                           |                          |
|  Jira (project mgmt)   <-->  Cursor (code editor)           |
|       ^                           ^                          |
|       |                           |                          |
|  Claude Code (AI assistant)  <-->  spec-kit (planning)       |
|       ^                                                      |
|       |                                                      |
|  Python + Streamlit (your application)                       |
|                                                              |
+-------------------------------------------------------------+
```

- **GitHub** stores your code in the cloud so it is safe, shareable, and versioned.
- **Git** is the version control engine that tracks every change you make.
- **Jira** manages tasks and requirements so you always know what to work on and why.
- **Cursor** is your code editor --- the application where you write and organize files.
- **Claude Code** is an AI assistant that runs in your terminal, reads your project, and helps you build.
- **spec-kit** turns requirements into structured plans before you write a single line of code.
- **Python + Streamlit** is the technology stack for the dashboard you will build in Session 2.

---

## Section 1: Create Accounts (~20 min)

### 1.1 GitHub Account

> **Why GitHub?** GitHub hosts over 100 million developers and is the standard platform for storing and collaborating on code. In your analytics career, you will use it to share analysis code with teammates, collaborate on data pipelines, contribute to open-source projects, and showcase your portfolio. Recruiters and hiring managers actively review GitHub profiles when evaluating candidates.

**Steps:**

1. Go to [github.com](https://github.com) and click **Sign up**.
2. Choose a sign-up method: **Continue with Google**, **Continue with Apple**, or fill out the form manually with your email, a password, and a username.
3. If signing up manually, check your email for a verification code and enter it when prompted.
4. Complete any remaining onboarding prompts.

**Username guidance:** Your GitHub username becomes part of your public profile URL (`github.com/your-username`). Choose something professional --- your name or a clean variation of it. Avoid numbers that look like birth years, inside jokes, or anything you would not put on a resume. Letters, numbers, and single hyphens are the only characters allowed.

> **Checkpoint:** You can log into github.com and see your dashboard.

> **Pro Tip for MSBA Students:** Your GitHub profile becomes a living portfolio. The projects you build in this tutorial, in your capstone, and on your own will all be visible. A clean, active GitHub profile with well-documented projects signals to employers that you can build, not just analyze. Choose your username carefully --- you will use it for years.

---

### 1.2 Atlassian (Jira) Account and Project

> **Why Jira?** Over 65,000 companies use Jira to track work. Whether you become a data analyst at a bank, a consultant at Deloitte, a product manager at a tech company, or launch your own venture, you will almost certainly encounter Jira or a similar tool. Understanding project management software now gives you immediate credibility in professional settings and helps you work effectively on teams from day one.

**Steps:**

1. Go to [atlassian.com](https://www.atlassian.com) and click **Get started**.
2. Sign up with your email, or use **Google**, **Microsoft**, **Apple**, or **Slack**.
3. When asked about your role, select **Student** or **Developer**.
4. When asked what to use, select **Jira Software**.
5. Name your site. This becomes `yourname.atlassian.net` --- the URL where you will access Jira.
6. During onboarding, Jira walks you through creating your first project. Use these settings:

| Question | Answer | Why |
|----------|--------|-----|
| What kind of work do you do? | **Other** | Keeps the setup flexible for analytics projects |
| Select a project template | **Scrum** | Industry-standard agile methodology used by most teams |
| Name your first project | **E-Commerce Analytics** | Descriptive name matching the tutorial's dashboard project |
| What types of work do you need? | **Task** | Simple, clean work item type for this tutorial |
| How do you track work? | **To Do, In Progress, Done** | The simplest effective workflow --- three clear states |

7. After the project is created, verify the project **Key** is `ECOM`. The key is the prefix that appears on every issue (for example, `ECOM-1`, `ECOM-2`). If Jira assigned a different key (such as `ECO` or `ECA`):
   - Click the gear icon or go to **Project settings**.
   - Navigate to **Details**.
   - Change the **Key** field to `ECOM`.
   - Save your changes.

> **Checkpoint:** You can access your ECOM project at `yourname.atlassian.net` and see the Scrum board with To Do, In Progress, and Done columns.

> **Key Concept: Traceability** --- Every piece of code you write in this tutorial will trace back to a Jira issue. When you commit code, you will include the issue key (like `ECOM-1`) in the commit message. This means anyone --- a teammate, a manager, your future self --- can find out *why* code exists, *when* it was added, and *what requirement* it fulfills. This is not academic overhead. This is how professional teams operate, and it is one of the first things interviewers ask about when they evaluate your experience with collaborative workflows.

---

### 1.3 Claude Pro Subscription

> **Why Claude Pro?** Claude Code, the AI command-line assistant you will use throughout this tutorial, requires an active Claude Pro (or Max) subscription. The free tier of Claude does not provide access to Claude Code. Think of Claude Pro as your access pass to having an AI development partner in your terminal.

**Steps:**

1. Go to [claude.ai](https://claude.ai) and sign up using Google or email.
2. Once logged in, go to your profile or settings and select **Upgrade to Pro**.
3. Enter payment information and complete the subscription ($20/month).

**A note about Pro vs. Max:** Most students find Claude Pro sufficient for this tutorial and their coursework. If you hit usage limits during intensive work sessions, Claude Max ($100/month) provides higher limits. You can always upgrade later if needed.

> **Checkpoint:** A Pro badge is visible on claude.ai when you are logged in.

---

## Section 2: Install Tools (~40 min)

### Understanding Your Terminal

Before installing any tools, you need to understand the terminal --- the interface where you will run installation commands, interact with Git, and launch Claude Code.

> **What is a terminal?** A terminal (also called a command line or CLI) is a text-based interface where you type commands instead of clicking buttons. Every professional developer uses a terminal daily. It might feel unfamiliar at first, but by the end of this tutorial, you will be comfortable with the essential commands. You do not need to memorize everything --- Claude Code itself runs in the terminal and can help you with commands when you need it.

**Opening the terminal in Cursor:**

Once Cursor is installed (Section 2.1), you will open the terminal inside it. Go to **Terminal** --> **New Terminal** from the menu bar, or use the keyboard shortcut `` Ctrl+` `` (backtick key, usually below Escape).

```
+-----------------------------------------------------------+
|  Cursor Window                                            |
|-----------------------------------------------------------|
|                                                           |
|  [Your code and files appear here]                        |
|                                                           |
|-----------------------------------------------------------|
|  Terminal                                            - x  |
|  $ _                                                      |
|                                                           |
+-----------------------------------------------------------+
```

You can resize the terminal by dragging the divider between it and the editor area.

**Essential terminal concepts:**

- **The prompt** (`$` on macOS/Linux, `>` on Windows) is the symbol that tells you the terminal is ready for your command. You do not type the prompt character itself --- it is already there.
- **Running commands** follows the pattern: `command [options] [arguments]`. For example, `git --version` runs the `git` command with the `--version` option.
- **`pwd`** (print working directory) shows you where you are in the file system. Think of it as "where am I right now?"
- **`ls`** (list) shows the files and folders in your current directory. On Windows, use `dir` instead.
- **`cd foldername`** (change directory) moves you into a folder. `cd ..` moves you up one level.
- **Tab completion** is your best friend. Start typing a file or folder name, then press Tab --- the terminal will autocomplete it. This saves time and prevents typos.
- **Ctrl+C** stops a running command. If something seems stuck or you made a mistake, press Ctrl+C to cancel.
- **Arrow keys**: Press the up arrow to recall previous commands. This is faster than retyping them.

> **Why open a new terminal after installing tools?** When you install a tool, it updates your system's **PATH** --- the list of directories your computer checks when looking for programs. Terminals that are already open loaded the PATH when they started and do not automatically see updates. Opening a new terminal (Terminal --> New Terminal) loads the fresh PATH with the newly installed tool. This is the most common reason for "command not found" errors after installation.

You will see reminders about this throughout the installation steps. If a tool does not seem to work after installing it, your first step should always be to open a new terminal.

---

### 2.1 Cursor

> **What is Cursor?** Cursor is an AI-powered code editor built on the same foundation as Visual Studio Code (VS Code), the most popular code editor in the world. If you have used VS Code before, Cursor will feel immediately familiar. If you have not, think of it as a sophisticated text editor designed for writing code, with built-in AI capabilities and an integrated terminal. We use Cursor over plain VS Code because it has native Claude Code integration and AI features designed for the kind of workflow you are learning.

**Download and install:**

1. Go to [cursor.com](https://cursor.com).
2. Download the installer for your platform:
   - **macOS:** Download the `.dmg` file. Open it and drag Cursor to your Applications folder.
   - **Windows:** Download the `.exe` file. Run it and follow the installation wizard.
3. Launch Cursor.

**Create your account:**

4. On the sign-up screen, choose **Continue with GitHub** (recommended since you just created a GitHub account), **Continue with Google**, **Continue with Apple**, or sign up with email.
5. Complete verification if prompted.

**Configure initial settings:**

6. On the "Customize Your Experience" screen:
   - How do you plan to use Cursor? --> **With a Team**
   - Which role best describes you? --> **Student**
   - Share Data --> **Off**
   - Click **Continue**
7. If asked to "Claim a free Pro trial," click **Skip for now**. You do not need Cursor Pro for this tutorial.
8. When prompted to connect GitHub, click **Connect**, then **Authorize Cursor** in the browser that opens. Verify accounts and click **Link Account**, then **Continue**.
9. Return to the Cursor desktop app and click **Log In** if prompted. Accept defaults on remaining screens.

> **Checkpoint:** You see the Cursor welcome screen with options: **Open project**, **Clone repo**, and **Connect via SSH**.

---

### 2.2 Git

> **What is Git?** Git is **version control** software --- it tracks every change to your files over time. Instead of ending up with `report_v2_final_REAL.xlsx`, Git maintains a clean history of what changed, when it changed, who changed it, and why. It is the foundation of all modern software development and data engineering. Every company you will work at uses Git or something built on top of it.

```
Without Git:                    With Git:

essay.docx                      essay.docx
essay_v2.docx                   (Git tracks all versions internally)
essay_final.docx
essay_REAL_final.docx           git log shows:
essay_final_v2_FINAL.docx        v1 --> v2 --> v3 --> current
```

With Git, you have one file. The entire history lives inside a hidden `.git` folder. You can go back to any previous version at any time. This is not just convenient --- it is essential when multiple people work on the same codebase, which is the norm in professional settings.

**Check if Git is already installed:**

Open the terminal in Cursor (Terminal --> New Terminal) and run:

```bash
git --version
```

If you see a version number (for example, `git version 2.39.0`), Git is already installed. Skip ahead to **Configure Git** below.

**macOS install:**

1. If Git is not installed, typing `git --version` in the terminal triggers a prompt to install **Command Line Tools for Xcode**. Click **Install** and wait for it to finish (this may take several minutes).
2. Once installation completes, run `git --version` again to confirm.

**Windows install:**

1. Download the installer from [git-scm.com/download/win](https://git-scm.com/download/win) (64-bit recommended).
2. Run the installer. Most defaults are fine, but pay attention to these settings:
   - Select **"Use Git from Git Bash and also from 3rd-party software"** --- this ensures Git works in Cursor's terminal.
   - Select **"Use the OpenSSL library"**
   - Select **"Checkout Windows-style, commit Unix-style line endings"** --- this prevents line ending issues when collaborating with macOS users.
   - Accept other defaults.
3. After installation, **restart Cursor** completely (close and reopen it).

**Configure Git (both platforms):**

Run these two commands in the terminal, replacing the placeholder values with your actual name and email:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

> **Why use your GitHub email?** When you make commits, Git stamps them with the name and email you configure here. If you use the same email as your GitHub account, GitHub can link your commits to your profile. This means your contributions show up on your GitHub activity graph and your profile page --- visible to recruiters and collaborators. Use a mismatched email and your commits will appear as if they came from a stranger.

> **Checkpoint:** `git --version` shows a version number (2.x.x or higher). `git config --list` shows your name and email.

---

### 2.3 Python 3.11+

> **Why Python?** Python is the dominant language in data science and analytics. Pandas, scikit-learn, TensorFlow, Streamlit --- the tools you use and will use in your career are all Python-based. You need Python 3.11 or higher installed so you can run the dashboard application you will build in Session 2.

**Check your current version:**

```bash
python --version
```

or (on macOS, which often requires the `python3` command):

```bash
python3 --version
```

If you see Python 3.11 or higher (for example, `Python 3.12.5`), skip to the next section.

**macOS install:**

1. Go to [python.org/downloads](https://www.python.org/downloads/) and download the latest Python 3.12.x installer.
2. Open the `.pkg` file and follow the installation wizard.
3. On the final screen, click **Install Certificates** if that option appears. This installs SSL certificates Python needs to make secure web requests.
4. Open a **new terminal** (Terminal --> New Terminal).
5. Verify: `python3 --version`

**Windows install:**

1. Go to [python.org/downloads](https://www.python.org/downloads/) and download the latest Python 3.12.x installer.
2. Run the installer. **Critical: Check the box "Add Python to PATH"** at the bottom of the first screen. If you miss this step, Windows will not know where to find Python when you type `python` in the terminal.
3. Click **Install Now** and complete installation.
4. Open a **new terminal** (Terminal --> New Terminal).
5. Verify: `python --version`

> **macOS note --- `python` vs. `python3`:** macOS ships with an older system Python (sometimes Python 2.x) accessible via the `python` command. The installer from python.org places the new version at `python3` to avoid conflicting with the system version. On macOS, always use `python3` unless you have specifically configured otherwise.

> **Checkpoint:** `python3 --version` (macOS) or `python --version` (Windows) shows Python 3.11 or higher.

---

### 2.4 uv

> **What is uv?** uv is a fast Python package manager built by Astral. It replaces the traditional `pip` for installing Python packages and managing project dependencies. spec-kit (which you install next) requires uv. Think of it as a modernized, faster version of pip.

**macOS:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

After installation on either platform, open a **new terminal** (Terminal --> New Terminal) so the PATH updates take effect.

> **Checkpoint:** `uv --version` shows a version number.

---

### 2.5 spec-kit

> **What is spec-kit?** spec-kit is GitHub's toolkit for **spec-driven development** --- the practice of turning requirements into structured plans before writing any code. Instead of jumping straight into coding and hoping for the best, spec-kit guides you through creating a constitution (project principles), a specification (what to build), a plan (how to build it), and tasks (individual work items). This disciplined approach is how experienced engineers avoid building the wrong thing.

**Install:**

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
```

This command tells uv to install the `specify-cli` tool from spec-kit's GitHub repository. It may take a minute to download and install all dependencies.

> **A preview of what is coming:** In Session 2, you will use spec-kit to create a constitution, specification, plan, and tasks for your dashboard --- all before writing a single line of application code. This structured approach might feel like extra work at first, but it dramatically reduces wasted effort and produces better results. AI amplifies both good planning and bad planning --- spec-kit ensures you amplify the good kind.

> **Checkpoint:** `specify --help` displays help information and available commands.

---

### 2.6 Claude Code

> **What is Claude Code?** Unlike the Claude web interface at claude.ai where you chat in a browser, Claude Code runs *directly in your terminal*, inside your project. It can read your files, write code, run commands, execute tests, and connect to external tools like Jira through MCP (Model Context Protocol) servers. Think of it as an AI colleague sitting next to you who can see your entire project, understand its structure, and make changes alongside you. This is fundamentally different from copying code out of a chat window --- Claude Code works within your development environment, just like you do.

Claude Code requires Node.js (a JavaScript runtime) to run. Most developers already have it installed, but let us verify.

**Step 1 --- Verify Node.js is installed:**

```bash
npm --version
```

If you see a version number (for example, `10.2.4`), skip to Step 2.

**If `npm` is not found**, install Node.js first:

1. Go to [nodejs.org](https://nodejs.org) and download the **LTS** (Long Term Support) version. LTS is the stable, recommended version.
2. Run the installer and follow the prompts. Accept all defaults.
3. Open a **new terminal** (Terminal --> New Terminal).
4. Verify: `npm --version`

**Step 2 --- Install Claude Code:**

```bash
npm install -g @anthropic-ai/claude-code
```

The `-g` flag means "install globally" so that the `claude` command is available from any directory, not just this one project.

**Step 3 --- Authenticate:**

1. In the terminal, type `claude` and press Enter.
2. A browser window opens. Log in with your Claude account (the one with the Pro subscription from Section 1.3).
3. Authorize Claude Code to access your account.
4. Return to the terminal. You should see Claude Code's interactive prompt.
5. Type `/exit` to quit for now. You will use Claude Code extensively starting in Section 3.3.

> **If authentication fails:** Run `claude logout`, then run `claude` again. Make sure your browser allows popup windows --- the authentication flow opens a new browser tab. If you are using a browser with aggressive popup blocking, temporarily allow popups for the authentication URL.

> **Checkpoint:** Running `claude` starts an interactive session. Type `/exit` to quit.

---

## Section 3: Fork and Clone the Repository (~15 min)

### Understanding Forks and Clones

Before you do anything, it helps to understand the two-step process you are about to follow and why it works this way.

```
+------------------+     Fork      +------------------+
|  Instructor's    |  ---------->  |   Your Fork      |
|  Repo (GitHub)   |               |   (GitHub)       |
+------------------+               +--------+---------+
                                            | Clone
                                            v
                                   +------------------+
                                   |  Your Computer   |
                                   |  (Local Copy)    |
                                   +------------------+
```

- **Fork** = your personal copy of the repository, hosted on GitHub under your account. You have full control over your fork. Changes you make to your fork do not affect the instructor's original repository.
- **Clone** = downloading your fork from GitHub to your computer so you can work on files locally. This is where you actually edit code.

The flow is: you edit files on your computer (local), then **push** changes up to your fork on GitHub. Your fork is your own space --- you cannot accidentally break the instructor's repository.

> **Why not just clone the instructor's repository directly?** If you cloned the original without forking first, you would not have permission to push your changes back to GitHub. Forking gives you your own copy with full write access.

---

### 3.1 Fork the Repository

1. Go to [github.com/LMU-ISBA/ai-dev-workflow-tutorial](https://github.com/LMU-ISBA/ai-dev-workflow-tutorial).
2. Click the **Fork** button in the upper-right corner of the page.
3. On the "Create a new fork" page, select your GitHub account as the owner.
4. Leave the repository name as `ai-dev-workflow-tutorial`.
5. Click **Create fork** and wait for GitHub to finish.

> **Checkpoint:** The repository is visible at `github.com/[your-username]/ai-dev-workflow-tutorial`. Notice the page now says "forked from LMU-ISBA/ai-dev-workflow-tutorial" near the top.

---

### 3.2 Clone Your Fork

Cloning downloads the repository to your computer so you can work on it locally.

1. On your forked repository page (`github.com/[your-username]/ai-dev-workflow-tutorial`), click the green **Code** button.
2. Make sure the **HTTPS** tab is selected (not SSH or GitHub CLI).
3. Copy the URL. It will look like: `https://github.com/[your-username]/ai-dev-workflow-tutorial.git`
4. In Cursor: **File** --> **New Window** (to start fresh).
5. Click **Clone Repo** on the welcome screen.
6. Paste the URL you copied and press **Enter/Return**.
7. Choose a save location. **Recommended:** Create a `GitHub` folder in your home directory to keep all repositories organized:
   - macOS: `~/GitHub`
   - Windows: `C:\Users\YourName\GitHub`
8. When prompted, click **Open** to open the cloned repository in Cursor.

> **Organizing your repositories:** Keeping all your Git repositories in a single `GitHub` folder (rather than scattering them across Desktop, Documents, and Downloads) is a small habit that pays off as you accumulate projects. It makes finding projects easy and keeps your file system clean.

> **If you cannot see the file explorer sidebar:** Press `Cmd+B` (macOS) or `Ctrl+B` (Windows) to toggle the sidebar. The sidebar shows your project's file and folder structure.

> **Checkpoint:** Tutorial files are visible in Cursor's file explorer (left sidebar). You should see folders like `data/`, `docs/`, `msba/`, and `prd/`, along with a `README.md` file.

---

### 3.3 Initialize Claude Code

With the repository open in Cursor, you will now initialize Claude Code so it understands the project structure and can assist you effectively.

> **Why initialize?** Claude Code works best when it understands your project's context --- what files exist, how they are organized, what the project is about. The `/init` command tells Claude Code to scan the repository and create a `CLAUDE.md` file that captures this understanding. Think of it as introducing Claude to the codebase before asking it to help.

**Steps:**

1. **Free up terminal space** by hiding Cursor's built-in AI panel. This gives the terminal more room. Go to **View** --> **Appearance** --> **Secondary Side Bar** to toggle it off (or click the rightmost icon in the top-right corner of the Cursor window).

2. Open the terminal: **Terminal** --> **New Terminal**.

3. Start Claude Code:

   ```bash
   claude
   ```

4. Once the Claude Code session starts, you will see its interactive prompt. Run the initialization command:

   ```
   /init
   ```

5. Watch as Claude Code reads files, analyzes the project structure, and generates a `CLAUDE.md` file. This takes a moment --- Claude Code is examining the repository's files, directories, configuration, and documentation to build a comprehensive understanding of the project.

6. When it finishes, find `CLAUDE.md` in the file explorer sidebar (left side of Cursor). Click on it to open it. Right-click the file tab and select **Open Preview** to see the rendered markdown.

7. **Read through `CLAUDE.md`.** It describes what the project is about, the repository structure, and conventions for working with it. This file serves as Claude Code's "memory" of your project --- every time you start a new Claude Code session in this repository, it reads `CLAUDE.md` first to re-establish context.

> **What is CLAUDE.md?** It is a markdown file that serves as a project briefing document for Claude Code. It typically contains: what the project does, how the repository is organized, key technical decisions, and any conventions or constraints that Claude should follow. You can edit it to add your own notes or instructions. Claude Code reads it automatically at the start of every session.

> **Checkpoint:** `CLAUDE.md` exists in your repository root, and you have read its contents.

---

## Section 4: Final Verification (~10 min)

Before calling Session 1 complete, run through every item in this checklist. Each verification step confirms that a tool is correctly installed and accessible.

### Accounts

- [ ] Can log into [github.com](https://github.com) and see your dashboard
- [ ] Can access `yourname.atlassian.net` with ECOM project visible (Scrum board with To Do, In Progress, Done)
- [ ] Claude Pro subscription active at [claude.ai](https://claude.ai) (Pro badge visible)

### Tools

Open a terminal in Cursor (Terminal --> New Terminal) and run each command:

```bash
git --version
```
Expected output: `git version 2.x.x` (any 2.x version is fine)

```bash
python3 --version       # macOS
python --version         # Windows
```
Expected output: `Python 3.11.x` or higher (3.12.x, 3.13.x are all fine)

```bash
uv --version
```
Expected output: `uv 0.x.x` or higher

```bash
specify --help
```
Expected output: spec-kit help text showing available commands

```bash
claude --version
```
Expected output: a version number

If any command fails with "command not found," open a new terminal and try again. If it still fails, refer to the Troubleshooting Reference at the end of this document.

### Repository

- [ ] Tutorial repo forked to your GitHub account (`github.com/[your-username]/ai-dev-workflow-tutorial`)
- [ ] Repo cloned locally and open in Cursor
- [ ] Files visible in Cursor's file explorer (you should see `data/`, `docs/`, `msba/`, `prd/`, and `README.md`)
- [ ] `CLAUDE.md` exists in the repository root and you have read it

### Jira

- [ ] ECOM project exists with the key `ECOM`
- [ ] Board has three columns: To Do, In Progress, Done

---

### Understanding What You Have Built

Take a moment to appreciate what you have just configured. You now have a professional development environment that mirrors what you would find at any technology company:

```
+---------------------------------------------------------------+
|                  Your Environment (Complete)                    |
+---------------------------------------------------------------+
|                                                                |
|  Cloud Services:                                               |
|    GitHub ............. Code hosting and collaboration          |
|    Jira ............... Task tracking and project management    |
|    Claude Pro ......... AI assistant subscription               |
|                                                                |
|  Local Tools:                                                  |
|    Cursor ............. AI-powered code editor                  |
|    Git ................ Version control                         |
|    Python 3.11+ ....... Programming language                   |
|    uv ................. Package manager                         |
|    spec-kit ........... Spec-driven planning                   |
|    Claude Code ........ AI terminal assistant                   |
|                                                                |
|  Your Repository:                                              |
|    Fork on GitHub ..... Your remote copy                       |
|    Clone on computer .. Your local working copy                |
|    CLAUDE.md .......... AI context file                        |
|                                                                |
+---------------------------------------------------------------+
```

These tools are connected in a way that creates a complete workflow: GitHub hosts your code, Git tracks changes, Jira tracks tasks, Cursor is where you write code, Claude Code helps you build, and spec-kit ensures you plan before you build. In Session 2, you will see all of these tools work together as you plan, build, and deploy a live dashboard.

---

## Troubleshooting Reference

This section covers the most common issues students encounter during setup. For each problem, you will find what you see (the symptom), why it happens (the cause), and how to fix it (the solution).

---

### 1. "Command not found" after installing a tool

**What you see:**
```
zsh: command not found: uv
bash: git: command not found
'specify' is not recognized as an internal or external command
```

**Why it happens:** Your terminal session loaded the system PATH before the tool was installed. The PATH is a list of directories the terminal searches when you type a command. Installing a tool adds its location to the PATH, but terminals that were already open do not automatically refresh their copy of the PATH.

**How to fix it:**
1. Open a **new terminal** in Cursor: Terminal --> New Terminal. This is the fix 90% of the time.
2. If a new terminal does not help, restart Cursor entirely (close and reopen the application).
3. On macOS, you can also try: `source ~/.zshrc` or `source ~/.bashrc`
4. If the tool is still not found after restarting, the installation may have failed silently. Re-run the install command and watch for error messages.

---

### 2. Git asks for a password on every push or pull

**What you see:** Every time you run `git push` or `git pull`, Git prompts for your username and password. Or you enter your GitHub password and it is rejected.

**Why it happens:** GitHub discontinued password authentication in 2021. If Git is asking for a password, it needs a Personal Access Token (PAT) instead. Additionally, if Git is not caching credentials, it will ask every time.

**How to fix it:**
1. **Set up credential caching** so you only enter credentials once:
   ```bash
   git config --global credential.helper store
   ```
2. The next time Git asks for your password, enter a **Personal Access Token** instead:
   - Go to GitHub --> Settings --> Developer settings --> Personal access tokens --> Tokens (classic)
   - Generate a new token with `repo` permissions
   - Use this token as your password when prompted
3. After entering the token once, it will be saved and Git will not ask again.

---

### 3. Wrong Python version

**What you see:**
```
$ python --version
Python 2.7.18
```
or
```
$ python --version
Python 3.8.10
```

**Why it happens:**
- On macOS, the `python` command often points to an older system Python. The python.org installer places the new version at `python3` to avoid conflicting with the system version.
- On Windows, if "Add Python to PATH" was not checked during installation, the terminal cannot find the new Python installation.

**How to fix it:**
- **macOS:** Use `python3` instead of `python`. If `python3 --version` still shows an old version, you may need to reinstall from python.org and ensure you are running the installer for 3.11+.
- **Windows:** Reinstall Python from [python.org/downloads](https://www.python.org/downloads/). On the very first screen of the installer, check **"Add Python to PATH"** at the bottom. Then open a new terminal.

---

### 4. Claude Code authentication failure

**What you see:** Claude Code starts but cannot authenticate, or the browser window does not open, or you see an authentication error.

**Why it happens:** The authentication flow requires opening a browser window to log into your Claude account. Popup blockers, VPNs, or network restrictions can interfere. Occasionally, cached credentials expire.

**How to fix it:**
1. Run `claude logout` to clear any cached credentials.
2. Run `claude` again to restart the authentication flow.
3. When the browser opens, make sure you log in with the account that has a Pro subscription.
4. If the browser does not open automatically, check for a URL in the terminal output that you can copy and paste into your browser manually.
5. Temporarily disable popup blockers if your browser is blocking the authentication window.

---

### 5. Cloned the wrong repository (instructor's repo instead of your fork)

**What you see:** When you try to push changes later, you get a "Permission denied" error. Or `git remote -v` shows the instructor's repository URL instead of yours.

**Why it happens:** You cloned the original repository at `LMU-ISBA/ai-dev-workflow-tutorial` instead of your fork at `[your-username]/ai-dev-workflow-tutorial`.

**How to fix it:**
1. First, check which remote you have:
   ```bash
   git remote -v
   ```
2. If the URL shows `LMU-ISBA` instead of your username, you have two options:
   - **Option A (fix the remote):** Update the remote URL to point to your fork:
     ```bash
     git remote set-url origin https://github.com/[your-username]/ai-dev-workflow-tutorial.git
     ```
   - **Option B (start fresh):** Delete the local folder, then re-clone from your fork using the correct URL from `github.com/[your-username]/ai-dev-workflow-tutorial`.

---

### 6. npm not found (needed for Claude Code)

**What you see:**
```
npm: command not found
```

**Why it happens:** Node.js is not installed. Claude Code is a Node.js application and requires npm (Node Package Manager), which comes bundled with Node.js.

**How to fix it:**
1. Go to [nodejs.org](https://nodejs.org) and download the **LTS** version.
2. Run the installer and follow the prompts.
3. Open a **new terminal** in Cursor.
4. Verify with `npm --version`.
5. Then install Claude Code: `npm install -g @anthropic-ai/claude-code`

---

### 7. spec-kit / specify command not found

**What you see:**
```
specify: command not found
```

**Why it happens:** Either spec-kit did not install correctly, or the installation directory is not in your PATH.

**How to fix it:**
1. Open a new terminal first (the most common fix).
2. If that does not work, reinstall:
   ```bash
   uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
   ```
3. Watch the output for error messages. If uv itself is not found, install uv first (Section 2.4).
4. After reinstalling, open another new terminal and try `specify --help` again.

---

### General Debugging Approach

When something goes wrong, follow this systematic approach:

1. **Read the error message carefully.** It almost always tells you what went wrong and sometimes suggests a fix.
2. **Open a new terminal.** This fixes the majority of "command not found" issues.
3. **Check the basics:** Are you in the right directory? Is the tool installed? Did you restart after installing?
4. **Ask Claude Code.** Once Claude Code is working, it can diagnose most issues. Describe what you were trying to do and paste the error message.
5. **Search online.** Copy the exact error message into a search engine. Someone has almost certainly encountered it before.
6. **Ask for help.** Post in the class Teams channel with: what you were trying to do, the exact error message (copy and paste, do not paraphrase), and what you have already tried.

---

## What's Next

Session 1 is complete. You have:

- Created accounts on GitHub, Jira, and Claude (the cloud services that power professional workflows)
- Installed six tools: Cursor, Git, Python, uv, spec-kit, and Claude Code (the local tools that make up your development environment)
- Forked and cloned the tutorial repository (your working copy of the project)
- Initialized Claude Code so it understands your project (AI context)

In **Session 2**, you will put everything together:

1. **Connect Claude Code to Jira** via the Atlassian MCP server, so your AI assistant can create and manage issues directly.
2. **Plan with spec-kit** --- create a constitution, specification, plan, and tasks for your dashboard.
3. **Build a Streamlit dashboard** with Claude Code's help, working from the structured plan.
4. **Commit, push, and deploy** your dashboard so it is live and shareable on the internet.

Everything you set up today is the foundation that makes Session 2 possible. The tools are ready. Next time, you build.
