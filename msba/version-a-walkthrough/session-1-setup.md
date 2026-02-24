# Session 1: Setup & Foundation

**Get your development environment ready in one session.**

Estimated time: 100 minutes

```
What you will set up
--------------------
Accounts:  GitHub, Atlassian (Jira), Claude Pro
Tools:     Cursor, Git, Python 3.11+, uv, spec-kit, Claude Code
Repo:      Fork and clone the tutorial repository, initialize Claude Code
```

By the end of this session you will have every account created, every tool installed and verified, and the tutorial repository open in your editor with Claude Code initialized. Nothing from Session 2 onward depends on anything other than completing these steps.

---

## 1. Create Accounts (~20 min)

### 1.1 GitHub Account

GitHub is the industry-standard platform for hosting code and collaborating with version control. Your work throughout this tutorial will live in a GitHub repository.

1. Go to [github.com](https://github.com) and click **Sign up**.
2. Choose a sign-up method: **Continue with Google**, **Continue with Apple**, or fill out the form manually with your email, a password, and a username.
   - Passwords must be at least 15 characters, or at least 8 characters with a number and a lowercase letter.
3. **Username tip:** Pick something professional -- this is publicly visible. Usernames can contain letters, numbers, and single hyphens. They cannot begin or end with a hyphen.
4. Select your **Country/Region** when prompted.
5. If signing up manually, check your email for a verification code and enter it when prompted.

> **Checkpoint:** You can log into github.com and see your dashboard.

---

### 1.2 Atlassian (Jira) Account and Project

Jira is the most widely used project management tool in technology teams. It tracks tasks, bugs, and features using boards and workflows. During signup, you will also create the project used throughout this tutorial.

1. Go to [atlassian.com](https://www.atlassian.com) and click **Get started**.
2. Sign up with your email, or use **Google**, **Microsoft**, **Apple**, or **Slack**.
3. When asked about your role, select **Student** or **Developer**.
4. When asked what you want to use, select **Jira Software**.
5. Name your site -- this becomes your workspace URL (e.g., `yourname.atlassian.net`).
6. Jira walks you through creating your first project during onboarding. Use these exact settings:

| Question | Answer |
|----------|--------|
| What kind of work do you do? | **Other** |
| Select a project template | **Scrum** |
| Name your first project | **E-Commerce Analytics** |
| What types of work do you need? | **Task** |
| How do you track work? | **To Do, In Progress, Done** |

7. After the project is created, verify the project **Key** is `ECOM`. The key appears next to the project name in the sidebar and is used as a prefix for all issue IDs (e.g., ECOM-1, ECOM-2).
8. If the key is different (e.g., `ECO`), change it: go to **Project settings** (gear icon in the project sidebar) --> **Details** --> update the **Key** field to `ECOM` --> save.

> **Checkpoint:** You can access your ECOM project at `yourname.atlassian.net` and see the Scrum board.

---

### 1.3 Claude Pro Subscription

Claude Pro gives you access to Claude Code, the AI coding assistant you will use throughout this tutorial. Claude Code runs in your terminal and can read your codebase, write code, run commands, and interact with external tools.

1. Go to [claude.ai](https://claude.ai) and sign up using Google or email.
2. Once logged in, go to your profile or settings and select **Upgrade to Pro**.
3. Enter your payment information and complete the subscription ($20/month).

**Note:** If you encounter usage limits during the tutorial, you can upgrade to Claude Max ($100/month) for higher limits. Most students find Pro sufficient for the sessions covered here.

> **Checkpoint:** A Pro badge is visible on claude.ai when you are logged in.

---

## 2. Install Tools (~40 min)

This section installs six tools. Each subsection follows the same pattern: install, then verify with a checkpoint command. If a verification command fails, check the inline troubleshooting note before moving on.

### 2.1 Cursor

Cursor is an AI-powered code editor built on VS Code. If you have used VS Code before, Cursor will feel familiar -- it has the same layout, keyboard shortcuts, and extension support. You will use Cursor as your primary editor for the entire tutorial.

**Download and install:**

1. Go to [cursor.com](https://cursor.com).
2. Download the installer for your platform (macOS: `.dmg`, Windows: `.exe`).
3. macOS: Open the `.dmg` file and drag Cursor to your Applications folder. Windows: Run the `.exe` installer and follow the wizard.
4. Launch Cursor. On macOS, if prompted about opening an app from the internet, click **Open**.

**Create your Cursor account:**

5. On the sign-up screen, choose **Continue with GitHub** (recommended since you already created a GitHub account), **Continue with Google**, **Continue with Apple**, or enter your email.
6. Complete email verification if prompted.

**Configure initial settings:**

7. On the "Customize Your Experience" screen:
   - How do you plan to use Cursor? --> **With a Team**
   - Which role best describes you? --> **Student**
   - Share Data --> **Off**
   - Click **Continue**
8. If asked to "Claim a free Pro trial," click **Skip for now**. You do not need Cursor Pro for this tutorial.
9. When prompted to connect GitHub:
   - Click **Connect** next to GitHub.
   - A GitHub authorization page opens in your browser. Click **Authorize Cursor** to allow access to your repositories.
   - On the "Link GitHub Account" screen, verify both accounts and click **Link Account**.
   - Click **Continue**.
10. Return to the Cursor desktop app and click **Log In** if prompted.
11. On the "Preferences" screen, accept the defaults and click **Continue**. Continue through any remaining onboarding screens.

> **Checkpoint:** You see the Cursor welcome screen with three options: **Open project**, **Clone repo**, and **Connect via SSH**.

---

### Opening the Terminal in Cursor

You will run all remaining installation commands in the terminal built into Cursor. The **terminal** is a text-based interface where you type commands and see their output -- it is how developers install tools, run programs, and interact with version control.

**Open the terminal now:**

- Go to **Terminal** --> **New Terminal** from the menu bar.
- Keyboard shortcut: `` Ctrl+` `` (backtick key, usually above Tab) on both macOS and Windows.

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

You can resize the terminal by dragging the divider between it and the editor area. All commands in the remaining sections are typed here and executed by pressing **Enter/Return**.

**Key concept -- PATH and new terminals:** When you install a new tool, your system updates a list of directories called the **PATH** that tells the terminal where to find programs. An already-open terminal session loaded the old PATH when it started, so it will not see newly installed tools. The fix throughout this guide is always the same: open a **new terminal** (Terminal --> New Terminal). This is the single most common source of "command not found" errors.

---

### 2.2 Git

Git is the **version control system** that tracks every change to your code. It lets you save snapshots of your work (called **commits**), create parallel lines of development (called **branches**), and collaborate with others. You will use Git commands throughout Session 2.

**Check if Git is already installed:**

```bash
git --version
```

If you see a version number (e.g., `git version 2.39.0`), Git is already installed. Skip to **Configure Git** below.

**macOS install:**

1. Typing `git --version` in the terminal automatically triggers a prompt to install **Command Line Tools**. Click **Install** and wait for it to finish (this can take a few minutes).
2. Once complete, run `git --version` again to confirm.

If the automatic prompt does not appear, download the installer manually from [git-scm.com/download/mac](https://git-scm.com/download/mac).

**Windows install:**

1. Download the installer from [git-scm.com/download/win](https://git-scm.com/download/win) (64-bit recommended).
2. Run the installer. Important settings to select during installation:
   - "Use Git from Git Bash and also from 3rd-party software"
   - "Use the OpenSSL library"
   - "Checkout Windows-style, commit Unix-style line endings"
   - Accept defaults for all other options.
3. After installation completes, restart Cursor entirely (close and reopen).
4. Open a new terminal and verify: `git --version`

**Configure Git (both platforms):**

Tell Git who you are. This information is attached to every commit you make.

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Use the **same email** you used when creating your GitHub account. This links your commits to your GitHub profile.

> **If you see "command not found" after installing:** Open a new terminal (**Terminal** --> **New Terminal**). See the PATH explanation above.

> **Checkpoint:** `git --version` shows a version number. `git config --list` shows your name and email.

---

### 2.3 Python 3.11+

Python is the programming language used for spec-kit and the Streamlit dashboard you will build in Session 2.

**Check your current version:**

```bash
python --version
```

or

```bash
python3 --version
```

If you see Python 3.11 or higher (e.g., `Python 3.12.5`), you are set. Skip to the next section.

**macOS install:**

1. Go to [python.org/downloads](https://www.python.org/downloads/) and download the latest Python 3.12.x installer.
2. Open the downloaded `.pkg` file and follow the installation wizard.
3. On the final screen, click **Install Certificates** if that option appears. This installs SSL certificates that Python needs to make HTTPS requests.
4. Open a **new terminal** (Terminal --> New Terminal).
5. Verify: `python3 --version`

**Windows install:**

1. Go to [python.org/downloads](https://www.python.org/downloads/) and download the latest Python 3.12.x installer.
2. Run the installer. **Critical: Check the box "Add Python to PATH"** at the bottom of the first screen. Missing this step is the most common Python installation issue on Windows.
3. Click **Install Now** and complete installation.
4. Open a **new terminal** (Terminal --> New Terminal).
5. Verify: `python --version`

> **If `python` shows an old version on macOS:** Use `python3` instead. macOS ships with a legacy system Python (2.7 or an older 3.x); the python.org installer places the new version at `python3` to avoid overwriting the system copy.

> **Checkpoint:** `python3 --version` (macOS) or `python --version` (Windows) shows Python 3.11 or higher.

---

### 2.4 uv

**uv** is a fast Python package and project manager. It is required to install spec-kit in the next step.

**macOS:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

After installation on either platform, open a **new terminal** (Terminal --> New Terminal).

**Verify:**

```bash
uv --version
```

> **Checkpoint:** `uv --version` shows a version number (e.g., `uv 0.5.x`).

---

### 2.5 spec-kit

**spec-kit** is GitHub's toolkit for spec-driven development. It helps you generate structured specifications from product requirements, which Claude Code can then use to build software.

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
```

This command downloads and installs spec-kit as a globally available tool.

**Verify:**

```bash
specify --help
```

You should see a help message listing available commands and options.

> **Checkpoint:** `specify --help` displays help information and available commands.

---

### 2.6 Claude Code

Claude Code is the AI command-line assistant you will use throughout the tutorial. Unlike the Claude web interface at claude.ai, Claude Code runs directly in your terminal, can read and write files in your project, execute shell commands, and integrate with external tools like Jira.

**Step 1 -- Install Claude Code:**

**macOS:**

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows (PowerShell):**

```powershell
irm https://claude.ai/install.ps1 | iex
```

After installation, open a **new terminal** (Terminal --> New Terminal).

**Step 2 -- Authenticate:**

1. Run `claude` in the terminal.
2. You will be prompted to log in. A browser window opens automatically. Log in with your Claude account (the one with the Pro subscription).
3. Authorize Claude Code to access your account.
4. Return to the terminal. You should see the Claude Code interactive prompt.

> **If authentication fails:** Run `claude logout`, then run `claude` again. Make sure your browser allows the popup window. Some browsers block popups by default.

> **Checkpoint:** Running `claude` starts an interactive session. Type `/exit` to quit.

---

## 3. Fork and Clone the Repository (~15 min)

This section introduces two Git concepts you will use immediately:

- **Fork:** A copy of someone else's repository under your own GitHub account. You have full control over your fork -- you can modify it, push to it, and experiment freely without affecting the original.
- **Clone:** A download of a repository from GitHub to your local machine. Cloning creates a folder on your computer with all the project files and their full Git history.

### 3.1 Fork the Repository

1. Go to [github.com/LMU-ISBA/ai-dev-workflow-tutorial](https://github.com/LMU-ISBA/ai-dev-workflow-tutorial).
2. Click the **Fork** button in the upper right corner of the page.
3. Select your GitHub account as the destination.
4. Wait for the fork to complete. GitHub redirects you to your new copy.

> **Checkpoint:** The repository is visible at `github.com/[your-username]/ai-dev-workflow-tutorial`. The page header should show your username, not `LMU-ISBA`.

---

### 3.2 Clone Your Fork

1. On your forked repository page (not the original), click the green **Code** button.
2. Make sure **HTTPS** is selected (not SSH or GitHub CLI).
3. Copy the URL. It should look like `https://github.com/[your-username]/ai-dev-workflow-tutorial.git` -- confirm your username is in the URL, not `LMU-ISBA`.
4. In Cursor: **File** --> **New Window**.
5. In the new window, click **Clone Repo**.
6. Paste the URL you copied and press **Enter/Return**.
7. Choose a save location. **Recommended:** Create a `GitHub` folder in your home directory to keep all repositories organized:
   - macOS: `~/GitHub`
   - Windows: `C:\Users\YourName\GitHub`
8. When prompted "Would you like to open the cloned repository?", click **Open**.

> **If you cannot see the file explorer sidebar:** Press `Cmd+B` (macOS) or `Ctrl+B` (Windows) to toggle the sidebar, or go to **View** --> **Appearance** --> **Primary Side Bar**.

> **Checkpoint:** Tutorial files (including folders like `data/`, `docs/`, `msba/`, `prd/`, and a `README.md`) are visible in Cursor's file explorer on the left.

---

### 3.3 Initialize Claude Code

With the repository open in Cursor, you will now initialize Claude Code so it understands the project structure and purpose. This generates a `CLAUDE.md` file that acts as a project guide for Claude Code.

1. **Free up terminal space** by hiding Cursor's built-in AI panel: go to **View** --> **Appearance** --> **Secondary Side Bar** (or click the rightmost icon in the top-right corner of the Cursor window). This gives more room for Claude Code's output.
2. Open the terminal (**Terminal** --> **New Terminal**).
3. Start Claude Code:

   ```bash
   claude
   ```

4. Once the Claude Code interactive session starts, type the following command and press Enter:

   ```
   /init
   ```

5. **Watch what happens.** Claude Code reads files across the repository, analyzes the project structure, and determines what the codebase is about. This is a preview of how Claude Code operates -- it builds context by reading your code before it helps you write or modify anything.
6. When Claude Code finishes, it will have created a `CLAUDE.md` file in the root of the repository.
7. Open `CLAUDE.md` in the file explorer by clicking on it. To see the formatted version, right-click the file tab at the top of the editor and select **Open Preview**.
8. **Read through `CLAUDE.md`.** It describes what the project is about, the structure of the codebase, and conventions for working with it. This is your first look at the tutorial repository -- you will learn more about each part in Session 2.
9. Type `/exit` in the Claude Code session to quit when you are done.

> **Checkpoint:** `CLAUDE.md` exists in the root of your repository, and you have read its contents.

---

## 4. Final Verification Checklist

Run through every item below before calling Session 1 complete.

### Accounts

- [ ] Can log into github.com and see your dashboard
- [ ] Can access `yourname.atlassian.net` with the ECOM project visible
- [ ] Claude Pro subscription is active at claude.ai (Pro badge visible)

### Tools

Run each command in the Cursor terminal and confirm the output:

```bash
git --version
# Expected: git version 2.x.x

python3 --version   # macOS
python --version     # Windows
# Expected: Python 3.11.x or higher

uv --version
# Expected: uv 0.x.x or higher

specify --help
# Expected: spec-kit help output with available commands

claude --version
# Expected: version number displayed
```

### Repository

- [ ] Tutorial repo forked to your GitHub account
- [ ] Repo cloned locally and open in Cursor
- [ ] Files visible in Cursor's file explorer (data/, docs/, msba/, prd/, README.md)
- [ ] `CLAUDE.md` file exists in the repository root and you have read it

### Jira

- [ ] ECOM project exists with key `ECOM`
- [ ] Board shows columns: To Do, In Progress, Done

---

## Quick Troubleshooting Reference

| Problem | Fix |
|---------|-----|
| "Command not found" after installing a tool | Open a new terminal (**Terminal** --> **New Terminal**) or restart Cursor entirely. New installs update your PATH, but an already-open terminal loaded the old PATH when it started. |
| Git asks for username/password on every operation | Run `git config --global credential.helper store`, then enter your credentials once on the next Git command. They will be saved for future use. |
| `python` shows old version on macOS | Use `python3` instead. macOS includes a legacy system Python; the python.org installer places the new version at `python3`. |
| `python` not found on Windows after installing | Reinstall Python and make sure to check **"Add Python to PATH"** on the first screen of the installer. |
| Claude Code authentication fails | Run `claude logout`, then `claude` again. Ensure your browser allows popup windows. |
| Cloned the original repo instead of your fork | Run `git remote -v` in the terminal. If the URL shows `LMU-ISBA` instead of your username, delete the local folder and re-clone using the URL from your fork (`github.com/[your-username]/ai-dev-workflow-tutorial`). |
| Cursor cannot find the cloned repository | Make sure you clicked **Open** when prompted after cloning. If you missed it, go to **File** --> **Open Folder** and navigate to the directory where you saved the clone. |
| `uv tool install` fails with a network error | Check your internet connection and try again. If you are behind a corporate firewall or VPN, try disconnecting temporarily. |

---

## What's Next

Session 1 is complete. All accounts are created, all tools are installed and verified, and your repository is ready.

Next session: **Session 2** -- connect Claude Code to Jira, use spec-kit to generate a specification and plan, build a Streamlit dashboard with AI assistance, and deploy it live.
