# Part 1: Setup & Foundation

**Get your tools set up before you start building (Part 1 of 2)**

Estimated time: 70–100 minutes, at your own pace. Do this part first; Part 2 (Build & Deploy) picks up where it leaves off.

---

## Table of contents

- [Section 1: Create accounts (~25 min)](#section-1-create-accounts-25-min)
  - [1.1 GitHub account](#11-github-account)
  - [1.2 Claude Pro subscription](#12-claude-pro-subscription)
  - [1.3 Granola account and student plan](#13-granola-account-and-student-plan)
  - [1.4 Wispr Flow account and student plan](#14-wispr-flow-account-and-student-plan)
- [Section 2: Install tools (~50 min)](#section-2-install-tools-50-min)
  - [2.1 Cursor](#21-cursor)
  - [2.2 Git](#22-git)
  - [2.3 Python 3.11+](#23-python-311)
  - [2.4 Claude Code](#24-claude-code)
  - [2.5 Superpowers plugin](#25-superpowers-plugin)
  - [2.6 Granola app + connect it to Claude Code](#26-granola-app--connect-it-to-claude-code)
- [Section 3: Fork and clone the repository (~15 min)](#section-3-fork-and-clone-the-repository-15-min)
  - [3.1 Fork the repository](#31-fork-the-repository)
  - [3.2 Clone your fork](#32-clone-your-fork)
- [Section 4: Final verification (~10 min)](#section-4-final-verification-10-min)
- [Troubleshooting reference](#troubleshooting-reference)

---

## What you'll set up

```
Accounts:  GitHub, Claude Pro, Granola, Wispr Flow
Tools:     Cursor, Git, Python 3.11+, Claude Code, Superpowers plugin, Granola app
Repo:      Fork and clone the tutorial repository
Tracking:  A TASKS.md file in your repo (no extra account needed)
Meetings:  Granola connected to Claude Code (for your capstone)
Dictation: Wispr Flow, speak your prompts to Claude Code instead of typing
```

**See the finished product:** Before you start, look at what you'll build in Part 2: [E-Commerce Sales Dashboard](https://sales-dashboard-greg-lontok.streamlit.app/). This is a live, deployed dashboard built using the workflow you're about to learn. By the end, you'll have built and deployed your own version. (If the app shows a "Zzzz" sleeping page, click the button to wake it up, which takes about 30 seconds.)

> **If you get stuck:** Try to solve the problem yourself first. Google the error message, use AI tools to help diagnose the issue, or if you've already got Claude Code set up, just ask it, since it can troubleshoot most installation and configuration problems. If none of that works, post in the Teams General channel and someone will help.

> **Heads up:** Websites and software update their interfaces regularly. A button label, sign-up flow, or menu option described here may look slightly different by the time you go through it. That's normal. Focus on the goal of each step rather than the exact clicks: once you know what a step is trying to accomplish, you can usually find the equivalent option even when the UI has moved. Read the screen, work it out, and keep going. Figuring things out on your own like this is itself a professional skill.

---

## Why this setup matters

Setting up your own development environment is a skill most people skip. They wait for someone else to do it for them. When you can configure a toolchain yourself, debug installation problems, and get everything running from scratch, teammates and managers notice. It tells them you can own a problem from start to finish.

A well-configured environment also saves you time. Every technology company uses some variation of the workflow you're about to configure. The tools differ slightly from team to team, but the pattern is the same:

```
Requirements  -->  Code  -->  Test  -->  Deploy  -->  Monitor
```

Someone defines what needs to be built. Developers write code to meet those requirements. The code is tracked, reviewed, and deployed so users can access it. This cycle repeats continuously.

You're setting up that same pipeline, end to end. When you finish, you'll have a development environment that looks like what you'd find on your first day at a technology job. This is also the environment you'll use for your capstone project, so getting it right now saves you time later.

### Your competitive advantage

Most analysts can build a model in a notebook. Fewer can turn that model into a live dashboard and deploy it. That gap is your opportunity, in your capstone and in job interviews.

### What you'll be able to do after Part 1

- Manage code with version control (Git and GitHub)
- Track work in a version-controlled task file (TASKS.md) that lives alongside your code
- Use AI to accelerate building (Claude Code)
- Plan before you build (Superpowers' brainstorming and writing-plans skills)
- Edit code in a modern, AI-aware editor (Cursor)
- Bring meeting notes into your AI workflow (Granola connected to Claude Code) for your capstone stakeholder meetings

AI-assisted development doesn't replace understanding. It accelerates it. You still need to know what you're building and why. The AI handles much of the how.

---

## The complete toolchain

The following diagram shows every tool you'll install and how they connect. Refer back to this as you work through each section.

```
+-------------------------------------------------------------+
|               Your Development Toolchain                     |
+-------------------------------------------------------------+
|                                                              |
|  GitHub (code hosting)  <-->  Git (version control)          |
|       ^                           ^                          |
|       |                           |                          |
| TASKS.md (task tracking) <-->  Cursor (code editor)          |
|       ^                           ^                          |
|       |                           |                          |
| Claude Code (coding agent) <--> Superpowers (planning skills) |
|       ^              ^                                        |
|       |              |                                        |
| Python + Streamlit   Granola (meeting notes, via MCP)        |
|  (your application)                                          |
|                                                              |
+-------------------------------------------------------------+
```

- **GitHub** stores your code in the cloud so it's safe, shareable, and versioned.
- **Git** is the version control engine that tracks every change you make.
- **TASKS.md** is a plain-text task board that lives in your repository. It tracks what to build and what's done, and because it's just a file, Claude Code can read and update it directly, with no separate account or web app to switch to. The board holds your milestones (the major deliverables, with IDs like TASK-1), and the plan you write in Part 2 breaks each milestone into the smaller build tasks Claude Code works through.
- **Cursor** is your code editor, where you write and organize files.
- **Claude Code** is an AI coding agent that runs in your terminal, reads your project, and helps you build.
- **Superpowers** is a Claude Code plugin whose skills (brainstorming, writing-plans, executing-plans) turn requirements into bite-sized implementation tasks before you start coding.
- **Python + Streamlit** is the technology stack for the dashboard you'll build in Part 2.
- **Granola** is an AI notepad for meetings. Connected to Claude Code through MCP, it lets Claude read your meeting notes. You set it up now but use it in your capstone, not for the dashboard.
- **Wispr Flow** lets you dictate instead of type. You speak, and it enters clean text into any app, including the terminal where you prompt Claude Code, so giving Claude a lot of context takes seconds.

---

## Section 1: Create accounts (~25 min)

### 1.1 GitHub account

> **Why GitHub?** GitHub hosts over 100 million developers and is the standard platform for storing and collaborating on code. In your career, you'll use it to share code, collaborate on projects, and build a public portfolio. Recruiters check GitHub profiles.

**Steps:**

1. Go to [github.com](https://github.com) and click **Sign up**.
2. Choose a sign-up method: **Continue with Google**, **Continue with Apple**, or fill out the form manually with your email, a password, a username, and your country/region.
3. If signing up manually, check your email for a verification code and enter it when prompted. You may be asked to sign in again with your new credentials after verifying.
4. Complete any onboarding prompts if they appear (you may go directly to the dashboard).

**Username guidance:** Your GitHub username becomes part of your public profile URL (`github.com/your-username`). Choose something professional, like your name or a clean variation of it. Avoid numbers that look like birth years, inside jokes, or anything you wouldn't put on a resume. Letters, numbers, and single hyphens are the only characters allowed.

> **Checkpoint:** You can log into github.com and see your dashboard.

> **Pro Tip:** Your GitHub profile is a portfolio. The projects you build (in this tutorial, in your capstone, on your own) are all visible. A GitHub profile with well-documented projects shows employers you can build, not just analyze. Choose your username carefully. You'll use it for years.

---

### 1.2 Claude Pro subscription

> **Why Claude Pro?** Claude Code, the AI coding agent you'll use throughout this tutorial, requires an active Claude Pro (or Max) subscription. The free tier of Claude doesn't provide access to Claude Code. You need Pro to use the terminal-based AI assistant in this tutorial.

**Steps:**

1. Go to [claude.ai](https://claude.ai) and sign up using Google or email.
2. On the pricing page, click **Try Claude** under the **Pro** plan.
3. Enter payment information and complete the subscription ($17/month with annual billing, or $20/month billed monthly).

**A note about Pro vs. Max:** Most students find Claude Pro sufficient for this tutorial and their coursework. You only need the Pro subscription for one month to complete this tutorial. If you hit usage limits during intensive work sessions, Claude Max (from $100/month) provides higher limits. You can always upgrade later if needed. You can cancel your subscription after completing the tutorial, but it's highly recommended that you resubscribe when you start your capstone project; Claude Code is just as useful there. You can also apply what you learn here to other classes or your job if you're working.

**If the subscription cost is a concern,** message me on Teams. I don't want that to be a blocker for anyone.

> **Checkpoint:** When you're logged in to claude.ai, a Pro badge appears next to your name in the bottom-left corner.

---

### 1.3 Granola account and student plan

> **Why Granola?** Granola is an AI notepad for meetings. It listens while you talk, then turns the conversation into clean, searchable notes, so you can pay attention instead of scrambling to type. You won't need it to build the dashboard in this tutorial. You set it up now because it pays off in your **capstone**: when you meet with stakeholders, Granola captures what was said, and later (in Section 2.6) you'll connect it to Claude Code so you can pull those meeting notes straight into a build session: "what did the client ask for in Tuesday's meeting?" answered from your actual notes, not your memory.

**Steps:**

1. Go to [granola.ai/students](https://www.granola.ai/students) and click **Apply**. Sign up with your **school email** and follow the prompts to verify you're a current student.
2. The student plan gives you **12 months of Granola Business free**. It's available to enrolled students at accredited universities in the **US, UK, and Canada**.

> **Not eligible for the student plan?** No problem. Granola's free **Basic** plan works with everything in this tutorial; the only limit is that Claude Code can query your notes from the **last 30 days** rather than your whole history. Sign up at [granola.ai](https://www.granola.ai) without the student application.

> **Checkpoint:** You can sign in to your Granola account (student application submitted or approved).

---

### 1.4 Wispr Flow account and student plan

> **Why Wispr Flow?** Wispr Flow is a voice dictation app that turns your speech into text in any application, including Cursor's terminal where Claude Code runs. It advertises around 4x faster than typing and cleans up filler and false starts as you talk. Here's why it earns a spot in this setup: what you get out of an AI agent depends on how much context you put in. In Part 2, the Superpowers `brainstorming` skill interviews you with clarifying questions, and the richer your answers, the better the design and plan it produces. Speaking a few paragraphs of context is far easier than typing them, so dictation is the fastest way to give Claude the detailed direction it works best with.

**Steps:**

1. Go to [wisprflow.ai/students](https://wisprflow.ai/students) and click **Start Today for free** to create your account.
2. Download the app for your platform (macOS or Windows) and install it.
3. Sign in with your **school (.edu) email** to auto-activate the student offer. No .edu address? Use the form on that page to verify with a student ID, enrollment confirmation, or similar.

The student offer is **3 months free**, then $6/month billed annually (50% off the standard price). You can cancel anytime.

> **Checkpoint:** Wispr Flow is installed, and you can dictate a sentence into any text field and watch it appear as text. (Finish the app's onboarding first; it sets the key you hold to talk.)

---

## Section 2: Install tools (~50 min)

### Understanding your terminal

Before installing any tools, you need to understand the terminal, the interface where you'll run installation commands, interact with Git, and launch Claude Code.

> **What is a terminal?** A terminal (also called a command line or CLI) is a text-based interface where you type commands instead of clicking buttons. Professional developers use a terminal daily. It might feel unfamiliar at first, but by the end of this tutorial, you'll be comfortable with the essential commands. You don't need to memorize everything; Claude Code itself runs in the terminal and can help you with commands when you need it.

**Opening the terminal in Cursor:**

Once Cursor is installed (Section 2.1), you'll open the terminal inside it. Go to **Terminal** --> **New Terminal** from the menu bar, or use the keyboard shortcut `` Ctrl+` `` (backtick key, usually below Escape).

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

- **The prompt** (`$` on macOS/Linux, `>` on Windows) is the symbol that tells you the terminal is ready for your command. You don't type the prompt character itself; it's already there.
- **Running commands** follows the pattern: `command [options] [arguments]`. For example, `git --version` runs the `git` command with the `--version` option.
- **`pwd`** (print working directory) shows you where you are in the file system. Think of it as "where am I right now?"
- **`ls`** (list) shows the files and folders in your current directory. On Windows, use `dir` instead.
- **`cd foldername`** (change directory) moves you into a folder. `cd ..` moves you up one level.
- **Tab completion** is your best friend. Start typing a file or folder name, then press Tab. The terminal will autocomplete it. This saves time and prevents typos.
- **Ctrl+C** stops a running command. If something seems stuck or you made a mistake, press Ctrl+C to cancel.
- **Arrow keys**: Press the up arrow to recall previous commands. This is faster than retyping them.

> **Why open a new terminal after installing tools?** When you install a tool, it updates your system's **PATH**, the list of directories your computer checks when looking for programs. Terminals that are already open loaded the PATH when they started and don't automatically see updates. Opening a new terminal (Terminal --> New Terminal) loads the fresh PATH with the newly installed tool. This is the most common reason for "command not found" errors after installation.

You'll see reminders about this throughout the installation steps. If a tool doesn't seem to work after installing it, your first step should always be to open a new terminal.

---

### 2.1 Cursor

> **What is Cursor?** Cursor is an AI-powered code editor built on Visual Studio Code (VS Code). If you've used VS Code before, Cursor will feel familiar. If you haven't, it's a text editor designed for writing code, with built-in AI capabilities and an integrated terminal. We use Cursor over plain VS Code because it has native Claude Code integration and AI features designed for this workflow.

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
7. If offered a free Pro trial (you may see something like a "7-day free Pro trial"), click **Skip for now**. You don't need Cursor Pro for this tutorial.
8. When prompted to connect GitHub, click **Connect**, then **Authorize Cursor** in the browser that opens. Verify accounts and click **Link Account**, then **Continue**.
9. Return to the Cursor desktop app and click **Log In** if prompted. Accept defaults on remaining screens.

> **Checkpoint:** You see the Cursor welcome screen with options: **Open project**, **Clone repo**, and **Connect via SSH**.

---

### 2.2 Git

> **What is Git?** Git is **version control** software; it tracks every change to your files over time. Instead of ending up with `report_v2_final_REAL.xlsx`, Git maintains a clean history of what changed, when, who changed it, and why. It's standard in software development and data engineering. Every company you'll work at uses Git or something built on top of it.

```
Without Git:                    With Git:

essay.docx                      essay.docx
essay_v2.docx                   (Git tracks all versions internally)
essay_final.docx
essay_REAL_final.docx           git log shows:
essay_final_v2_FINAL.docx        v1 --> v2 --> v3 --> current
```

With Git, you have one file. The entire history lives inside a hidden `.git` folder. You can go back to any previous version at any time. This becomes essential when multiple people work on the same codebase, which is the norm in professional settings.

**Check if Git is already installed:**

Open the terminal in Cursor (Terminal --> New Terminal) and run:

```bash
git --version
```

If you see a version number (for example, `git version 2.39.0`), Git is already installed. Skip ahead to **Configure Git** below.

**macOS install:**

1. If Git isn't installed, typing `git --version` in the terminal triggers a prompt to install **Command Line Tools for Xcode**. Click **Install** and wait for it to finish (this may take several minutes).
2. Once installation completes, run `git --version` again to confirm.

**Windows install:**

1. Download the installer from [git-scm.com/download/win](https://git-scm.com/download/win) (64-bit recommended).
2. Run the installer. Most defaults are fine, but pay attention to these settings:
   - Select **"Git from the command line and also from 3rd-party software"** (the recommended option) so Git works in Cursor's terminal. Don't pick "Use Git from Git Bash only," which would hide Git from Cursor.
   - Select **"Use the OpenSSL library"**
   - Select **"Checkout Windows-style, commit Unix-style line endings"** to prevent line ending issues when collaborating with macOS users.
   - Accept other defaults.
3. After installation, **restart Cursor** completely (close and reopen it).

**Configure Git (both platforms):**

Run these two commands in the terminal, replacing the placeholder values with your actual name and email:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

> **Why use your GitHub email?** When you make commits, Git stamps them with the name and email you configure here. If you use the same email as your GitHub account, GitHub can link your commits to your profile. This means your contributions show up on your GitHub activity graph and your profile page, visible to recruiters and collaborators. Use a mismatched email and your commits will appear as if they came from a stranger.

> **Checkpoint:** `git --version` shows a version number (2.x.x or higher). `git config --list` shows your name and email.

---

### 2.3 Python 3.11+

> **Why Python?** Python is the dominant language in data science, analytics, and AI. Pandas, scikit-learn, TensorFlow, Streamlit: the tools you use in your coursework and will use in your career are all Python-based. You need Python 3.11 or higher installed so you can run the dashboard application you'll build in Part 2.

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

1. Go to [python.org/downloads](https://www.python.org/downloads/) and download the latest Python 3 installer (the big button at the top of the page).
2. Open the `.pkg` file and follow the installation wizard.
3. On the final screen, click **Install Certificates** if that option appears. This installs SSL certificates Python needs to make secure web requests.
4. Open a **new terminal** (Terminal --> New Terminal).
5. Verify: `python3 --version`

**Windows install:**

1. Go to [python.org/downloads](https://www.python.org/downloads/) and download the latest Python 3 installer (the big button at the top of the page). You may also see a "Python install manager" option; ignore it and use the standard installer.
2. Run the installer. **Critical: Check the box "Add Python to PATH"** at the bottom of the first screen. If you miss this step, Windows won't know where to find Python when you type `python` in the terminal.
3. Click **Install Now** and complete installation.
4. Open a **new terminal** (Terminal --> New Terminal).
5. Verify: `python --version`

> **macOS note: `python` vs. `python3`.** On current versions of macOS, the plain `python` command usually doesn't exist at all ("command not found"). The installer from python.org installs the new version as `python3`. On macOS, always use `python3` unless you've specifically configured otherwise.

> **Checkpoint:** `python3 --version` (macOS) or `python --version` (Windows) shows Python 3.11 or higher.

---

### 2.4 Claude Code

> **What is Claude Code?** Unlike the Claude web interface at claude.ai where you chat in a browser, Claude Code runs *directly in your terminal*, inside your project. It can read your files, write code, run commands, execute tests, and even update your project's task list as it works. It's an AI agent that can see your entire project and make changes alongside you. This is different from copying code out of a chat window; Claude Code works inside your development environment.

**Step 1: Install Claude Code**

Claude Code has a native installer that handles everything automatically, including background updates.

**macOS:**

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows (PowerShell):**

```powershell
irm https://claude.ai/install.ps1 | iex
```

After installation, open a **new terminal** (Terminal --> New Terminal) so the PATH updates take effect.

**Step 2: Authenticate**

1. In the terminal, type `claude` and press Enter.
2. You'll be prompted to log in. A browser window opens. Log in with your Claude account (the one with the Pro subscription from Section 1.2).
3. Authorize Claude Code to access your account.
4. Return to the terminal. You should see Claude Code's interactive prompt.
5. Type `/exit` to quit for now. You'll come back to Claude Code in Section 2.5 and use it throughout Part 2.

> **If authentication fails:** Run `claude auth logout` in the terminal (or type `/logout` inside Claude Code), then run `claude` again. Make sure your browser allows popup windows. The authentication flow opens a new browser tab. If you're using a browser with aggressive popup blocking, temporarily allow popups for the authentication URL.

> **Checkpoint:** Running `claude` starts an interactive session. Type `/exit` to quit.

---

### 2.5 Superpowers plugin

> **What is Superpowers?** [Superpowers](https://github.com/obra/superpowers) is a Claude Code plugin that gives Claude a library of skills. A skill is a small piece of expertise Claude pulls in when your prompt matches it. Three skills you'll use in Part 2: `brainstorming` (asks clarifying questions and produces a design document), `writing-plans` (turns a design into a bite-sized implementation plan), and `executing-plans` (works through the plan task by task with frequent commits). The skills auto-invoke based on what you ask Claude to do, so you don't have to memorize commands.

#### Skills primer

Skills are markdown files that ship with the Superpowers plugin. Each one teaches Claude how to handle a specific type of task. When you ask Claude to design something, the brainstorming skill activates. When you ask Claude to implement a plan, the executing-plans skill activates. Claude reads each skill's description at session start and matches your prompt against those descriptions to decide which skill to load. Claude announces which skill it's using, like "Using brainstorming to..." That visibility is the whole reason this works as a teaching tool.

Here's the flow you'll see in Part 2: you never call a skill by name; your plain-English prompt triggers the chain:

```
You type a plain-English prompt
("Help me design and plan the dashboard")
              |
              v
     using-superpowers          <- loaded at session start;
     reads your intent             matches your words to a skill
              |
              v
  brainstorming ──► writing-plans ──► executing-plans
  (clarifies and     (turns it into     (builds it task by
   writes a          a step-by-step      task, testing and
   design doc)       plan)               committing)
              |
              v
  Claude announces each step: "Using <skill> to ..."
  (that line is your cue a skill kicked in)
```

The install command below is the only time you'll type a slash command to use Superpowers. The skills themselves never need one; they activate from natural-language prompts. (You'll still type a few unrelated slash commands elsewhere in the tutorial, like `/exit` and `/init`.)

#### Install the plugin

1. Open your terminal in Cursor (Terminal --> New Terminal) and run `claude` from any directory:

   ```bash
   claude
   ```

2. Inside Claude Code, run:

   ```
   /plugin install superpowers@claude-plugins-official
   ```

3. Wait for the install to complete (~30 seconds). Claude Code will confirm `Superpowers installed`.

4. Exit Claude Code (`/exit`) and start it again. The Superpowers plugin loads on each new session via a SessionStart hook.

5. When Claude Code starts, look for the line `You have superpowers` near the top of the session output. That line confirms the plugin loaded and the `using-superpowers` skill is active.

> **Checkpoint:** Starting Claude Code shows `You have superpowers` in the session output.

---

### 2.6 Granola app + connect it to Claude Code

This is the payoff of the Granola account you made in Section 1.3. You'll install the app and then give Claude Code the ability to read your meeting notes. Again: you don't use this to build the dashboard; it's here so it's ready for your capstone.

> **What is MCP?** MCP (Model Context Protocol) is how Claude Code connects to outside services. Think of it as a port you can plug tools into: once you plug in Granola, Claude Code can search and read your meeting notes without you copying and pasting anything. (Notice the contrast with how this tutorial tracks tasks: your `TASKS.md` board is just a file Claude Code already reads, so it needs no MCP. Meeting notes live in Granola's cloud, so MCP is how Claude reaches them. Use a plain file when you can; use MCP when the data lives somewhere else.)

Here's how your words in a meeting end up readable by Claude Code:

```
┌──────────────┐   Granola listens,    ┌──────────────┐
│ Your meeting │──  transcribes,    ──> │ Granola app  │
│  (you talk)  │    cleans up           │  (desktop)   │
└──────────────┘                        └──────┬───────┘
                                               │ syncs your notes up
                                               v
                                        ┌──────────────┐
                                        │ Granola cloud│
                                        │ (your notes) │
                                        └──────┬───────┘
                                               │ MCP server
                                               │ (you authorize once,
                                               │  in the browser)
                                               v
                                        ┌──────────────┐
                                        │  Claude Code │  <- "Summarize my
                                        │  (terminal)  │      last meeting"
                                        └──────────────┘
```

The top half (record -> transcribe -> sync) happens in the Granola app. The bottom half (cloud -> MCP -> Claude Code) is the connection you set up below, once.

**Install the app:**

1. Download the Granola desktop app from [granola.ai](https://www.granola.ai) and install it.
2. Open Granola and sign in with the account you created in Section 1.3. If you're unsure which email that account uses, check under **Settings** in Granola after signing in; you'll need the same email when you authorize Claude Code below.
3. *(Optional but useful)* Record one short test note (even a few minutes of a lecture or a chat with a classmate) so you have something for Claude Code to find later.

**Connect it to Claude Code:**

4. In **Cursor's terminal** (not inside Claude Code), register the Granola MCP server. You can run this from any directory; it only needs to be done once:

   ```bash
   claude mcp add --transport http granola https://mcp.granola.ai/mcp
   ```

5. Start Claude Code:

   ```bash
   claude
   ```

6. Inside Claude Code, open the MCP menu:

   ```
   /mcp
   ```

   You'll see `granola` listed, likely showing that authentication is required.

7. Select `granola` with the **arrow keys**, press **Enter**, and choose **Authenticate**. A browser window opens; sign in to Granola with the **same email** as your account, authorize the connection, and return to the terminal.

8. Test it. In Claude Code, ask:

   ```
   Which Granola account am I signed in with?
   ```

   Claude uses Granola's `get_account_info` tool and replies with your email and workspace. This works even if you have no notes yet, which makes it a clean way to confirm the connection. If you recorded a test note in step 3, try: `Summarize my most recent meeting.`

> **If it can't reach your notes:** Run `/mcp`, select `granola`, and re-authenticate. If you see "Unauthorized: user has not created a Granola account yet," you signed in with a different email than your Granola account; check the account email in Granola's **Settings** and reconnect with that one.

> **How you'll use this in your capstone:** After a stakeholder meeting, open a Claude Code session in your capstone repo and ask things like *"From my meeting notes this week, list what the client asked us to change,"* or *"Draft tasks in TASKS.md based on the decisions in yesterday's kickoff."* Your meeting record flows straight into the plan-and-build workflow you're learning here.

> **Checkpoint:** `/mcp` shows `granola` as authenticated, and asking "Which Granola account am I signed in with?" returns your email.

---

## Section 3: Fork and clone the repository (~15 min)

### Understanding forks and clones

Before you do anything, it helps to understand the two-step process you're about to follow and why it works this way.

```
+------------------+     Fork      +------------------+
|  Original        |  ---------->  |   Your Fork      |
|  Repo (GitHub)   |               |   (GitHub)       |
+------------------+               +--------+---------+
                                            | Clone
                                            v
                                   +------------------+
                                   |  Your Computer   |
                                   |  (Local Copy)    |
                                   +------------------+
```

- **Fork** = your personal copy of the repository, hosted on GitHub under your account. You have full control over your fork. Changes you make to your fork don't affect the original repository.
- **Clone** = downloading your fork from GitHub to your computer so you can work on files locally. This is where you actually edit code.

The flow is: you edit files on your computer (local), then **push** changes up to your fork on GitHub. Your fork is your own space. You can't accidentally break the original repository.

> **Why not just clone the original repository directly?** If you cloned the original without forking first, you wouldn't have permission to push your changes back to GitHub. Forking gives you your own copy with full write access.

---

### 3.1 Fork the repository

1. Go to [github.com/LMU-ISBA/ai-dev-workflow-tutorial](https://github.com/LMU-ISBA/ai-dev-workflow-tutorial).
2. Click the **Fork** button in the upper-right corner of the page.
3. On the "Create a new fork" page, select your GitHub account as the owner.
4. Leave the repository name as `ai-dev-workflow-tutorial`.
5. Click **Create fork** and wait for GitHub to finish.

> **Checkpoint:** The repository is visible at `github.com/[your-username]/ai-dev-workflow-tutorial`. Notice the page now says "forked from LMU-ISBA/ai-dev-workflow-tutorial" near the top.

---

### 3.2 Clone your fork

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

> **If you can't see the file explorer sidebar:** Press `Cmd+B` (macOS) or `Ctrl+B` (Windows) to toggle the sidebar. The sidebar shows your project's file and folder structure.

> **Checkpoint:** Tutorial files are visible in Cursor's file explorer (left sidebar). You should see folders like `data/`, `prd/`, `docs/`, and the versioned tutorial folders `v1/` through `v4/` (you're following `v4/`), along with a `README.md` file.

---

## Section 4: Final verification (~10 min)

Before calling Part 1 complete, run through every item in this checklist. Each verification step confirms that a tool is correctly installed and accessible.

### Accounts

- [ ] Can log into [github.com](https://github.com) and see your dashboard
- [ ] Claude Pro subscription active at [claude.ai](https://claude.ai) (Pro badge visible)
- [ ] Can sign in to Granola (student plan applied, or the free Basic plan)
- [ ] Wispr Flow installed and dictating (student offer activated with your school email)

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
claude --version
```
Expected output: a version number

### Superpowers plugin

Start a Claude Code session:
```bash
claude
```
Expected output: the session banner shows `You have superpowers` near the top, which means the Superpowers plugin loaded. Type `/exit` to close the session.

If any command fails with "command not found," open a new terminal and try again. If it still fails, refer to the Troubleshooting Reference at the end of this document.

### Granola (Claude Code connection)

Start a Claude Code session, run `/mcp`, and confirm `granola` is listed and authenticated. Then ask:
```
Which Granola account am I signed in with?
```
Expected: Claude returns your Granola email and workspace. Type `/exit` to close the session.

- [ ] `granola` shows as authenticated in `/mcp`
- [ ] "Which Granola account am I signed in with?" returns your email

### Repository

- [ ] Tutorial repo forked to your GitHub account (`github.com/[your-username]/ai-dev-workflow-tutorial`)
- [ ] Repo cloned locally and open in Cursor
- [ ] Files visible in Cursor's file explorer (you should see `data/`, `prd/`, the `v1/` through `v4/` tutorial folders, and `README.md`)

---

### Understanding what you've built

Here's what you've just configured:

```
+---------------------------------------------------------------+
|                  Your Environment (Complete)                    |
+---------------------------------------------------------------+
|                                                                |
|  Cloud Services:                                               |
|    GitHub ............. Code hosting and collaboration          |
|    Claude Pro ......... AI assistant subscription               |
|    Granola ............ Meeting notes (linked to Claude Code)    |
|                                                                |
|  Local Tools:                                                  |
|    Cursor ............. AI-powered code editor                  |
|    Git ................ Version control                         |
|    Python 3.11+ ....... Programming language                   |
|    Claude Code ........ AI coding agent                         |
|    Superpowers ........ Skill-driven planning (Claude plugin)   |
|    Granola app ........ AI notepad for meetings                  |
|    Wispr Flow ......... Voice dictation for AI prompts           |
|    TASKS.md ........... In-repo task board (created in Part 2)  |
|                                                                |
|  Your Repository:                                              |
|    Fork on GitHub ..... Your remote copy                       |
|    Clone on computer .. Your local working copy                |
|                                                                |
+---------------------------------------------------------------+
```

These tools connect into one workflow: GitHub hosts your code, Git tracks changes, a `TASKS.md` file tracks your work, Cursor is where you write it, the Superpowers plugin's skills help Claude plan, and Claude Code builds alongside you. In Part 2, you'll see them work together as you plan, build, and deploy a live dashboard.

> **Before you start Part 2:** If anything above isn't working, post in the Teams General channel now. It's much easier to sort out setup problems before you start building than in the middle of it.

---

## Troubleshooting reference

This section covers the most common issues people encounter during setup. For each problem, you'll find what you see (the symptom), why it happens (the cause), and how to fix it (the solution).

---

### 1. "Command not found" after installing a tool

**What you see:**
```
zsh: command not found: claude
bash: git: command not found
'python' is not recognized as an internal or external command
```

**Why it happens:** Your terminal session loaded the system PATH before the tool was installed. The PATH is a list of directories the terminal searches when you type a command. Installing a tool adds its location to the PATH, but terminals that were already open don't automatically refresh their copy of the PATH.

**How to fix it:**
1. Open a **new terminal** in Cursor: Terminal --> New Terminal. This is the fix 90% of the time.
2. If a new terminal doesn't help, restart Cursor entirely (close and reopen the application).
3. On macOS, you can also try: `source ~/.zshrc` or `source ~/.bashrc`
4. If the tool is still not found after restarting, the installation may have failed silently. Re-run the install command and watch for error messages.

---

### 2. Git asks for a password on every push or pull

**What you see:** Every time you run `git push` or `git pull`, Git prompts for your username and password. Or you enter your GitHub password and it's rejected.

**Why it happens:** GitHub discontinued password authentication in 2021. If Git is asking for a password, it needs a Personal Access Token (PAT) instead. Additionally, if Git isn't caching credentials, it'll ask every time.

**How to fix it:**
1. **Set up credential caching** so you only enter credentials once:
   ```bash
   git config --global credential.helper store
   ```
2. The next time Git asks for your password, enter a **Personal Access Token** instead:
   - Go to GitHub --> Settings --> Developer settings --> Personal access tokens --> Tokens (classic)
   - Generate a new token with `repo` permissions
   - Use this token as your password when prompted
3. After entering the token once, it'll be saved and Git won't ask again.

---

### 3. Wrong Python version

**What you see:**
```
$ python --version
zsh: command not found: python
```
or
```
$ python --version
Python 3.8.10
```

**Why it happens:**
- On macOS, the plain `python` command usually doesn't exist (or, on older setups, points to an outdated Python). The python.org installer places the new version at `python3` to avoid conflicting with anything on the system.
- On Windows, if "Add Python to PATH" wasn't checked during installation, the terminal can't find the new Python installation.

**How to fix it:**
- **macOS:** Use `python3` instead of `python`. If `python3 --version` still shows an old version, you may need to reinstall from python.org and ensure you're running the installer for 3.11+.
- **Windows:** Reinstall Python from [python.org/downloads](https://www.python.org/downloads/). On the very first screen of the installer, check **"Add Python to PATH"** at the bottom. Then open a new terminal.

---

### 4. Claude Code authentication failure

**What you see:** Claude Code starts but can't authenticate, or the browser window doesn't open, or you see an authentication error.

**Why it happens:** The authentication flow requires opening a browser window to log into your Claude account. Popup blockers, VPNs, or network restrictions can interfere. Occasionally, cached credentials expire.

**How to fix it:**
1. Run `claude auth logout` in the terminal (or `/logout` inside Claude Code) to clear any cached credentials.
2. Run `claude` again to restart the authentication flow.
3. When the browser opens, make sure you log in with the account that has a Pro subscription.
4. If the browser doesn't open automatically, check for a URL in the terminal output that you can copy and paste into your browser manually.
5. Temporarily disable popup blockers if your browser is blocking the authentication window.

---

### 5. Cloned the wrong repository (original repo instead of your fork)

**What you see:** When you try to push changes later, you get a "Permission denied" error. Or `git remote -v` shows the original repository URL instead of yours.

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

### 6. Claude Code install fails or `claude` not found

**What you see:**
```
claude: command not found
```
or the install script produces an error.

**Why it happens:** The installer couldn't complete (network issue, permissions), or the terminal hasn't loaded the updated PATH after installation.

**How to fix it:**
1. Open a **new terminal** in Cursor (Terminal --> New Terminal). This is the fix most of the time.
2. If that doesn't work, try running the installer again:
   - **macOS:** `curl -fsSL https://claude.ai/install.sh | bash`
   - **Windows (PowerShell):** `irm https://claude.ai/install.ps1 | iex`
3. If you're behind a corporate firewall or VPN, try disconnecting temporarily and re-running the installer.
4. After reinstalling, open another new terminal and try `claude --version`.

---

### 7. Superpowers plugin not loaded

**What you see:** Starting Claude Code does not show `You have superpowers` in the banner, and prompts that should auto-invoke skills (like "Help me design...") don't trigger any skill announcements.

**Why it happens:** The plugin install didn't finish, or it was installed mid-session so the SessionStart hook hasn't run yet. The hook only fires when a session starts.

**How to fix it:**
1. List installed plugins. Inside Claude Code, run `/plugin list`. You should see `superpowers`.
2. If it's missing, reinstall it: `/plugin install superpowers@claude-plugins-official`
3. Exit with `/exit` and start a fresh session. Look for `You have superpowers` in the new session's banner.

---

### General debugging approach

When something goes wrong, follow this systematic approach:

1. **Read the error message carefully.** It almost always tells you what went wrong and sometimes suggests a fix.
2. **Open a new terminal.** This fixes the majority of "command not found" issues.
3. **Check the basics:** Are you in the right directory? Is the tool installed? Did you restart after installing?
4. **Ask Claude Code.** Once Claude Code is working, it can diagnose most issues. Describe what you were trying to do and paste the error message.
5. **Search online.** Copy the exact error message into a search engine. Someone has almost certainly encountered it before.
6. **Ask for help.** Post in the Teams General channel with: what you were trying to do, the exact error message (copy and paste, don't paraphrase), and what you've already tried.

---

## What's next

Part 1 is complete. You've:

- Created accounts on GitHub, Claude, Granola, and Wispr Flow
- Installed the tools that make up your development environment: Cursor, Git, Python, Claude Code, the Superpowers plugin, the Granola app, and Wispr Flow
- Connected Claude Code to your Granola meeting notes for your capstone
- Forked and cloned the tutorial repository (your working copy of the project)

Every tool you just set up transfers directly to your capstone project: Git and GitHub for team collaboration, an in-repo `TASKS.md` for tracking deliverables, Claude Code with the Superpowers plugin for turning requirements into bite-sized plans, and Granola for capturing stakeholder meetings as notes Claude Code can read. You'll use this same environment for your capstone and beyond.

**With setup done, you're ready for Part 2.** In the build guide, you'll put everything together:

1. **Set up your `TASKS.md` board** so you (and Claude Code) can track every task from *To Do* to *Done*, all inside your repository.
2. **Plan with Superpowers** by letting the brainstorming skill produce a design document, then having writing-plans turn it into a bite-sized implementation plan.
3. **Build a Streamlit dashboard** with Claude Code's help, working from the structured plan.
4. **Commit, push, and deploy** your dashboard so it's live and shareable on the internet.

The tools are ready. Next, you build.

Continue to [**Part 2: Build & Deploy**](workshop-build-deploy.md).
