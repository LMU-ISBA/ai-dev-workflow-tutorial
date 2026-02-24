# Git Concepts

Git is a **version control system** — software that tracks changes to your files over time. This guide explains the core concepts you need to understand before using Git.

## Why Version Control?

Imagine writing a paper and saving multiple copies:

```
essay.docx
essay_v2.docx
essay_final.docx
essay_final_REAL.docx
essay_final_REAL_v2.docx
```

This approach has problems:
- Hard to know which version is actually current
- No record of what changed between versions
- Difficult to collaborate with others
- Takes up storage space with duplicates

**Git solves these problems** by tracking changes intelligently, storing only what changed, and maintaining a complete history.

## Core Concepts

### Repository (Repo)

A **repository** is a project folder that Git is tracking. It contains:

- Your project files
- A hidden `.git` folder with the complete history

```
my-project/           ← This is a repository
├── .git/             ← Hidden folder with Git data
├── README.md
├── src/
│   └── app.py
└── data/
    └── sales.csv
```

There are two types of repositories:

- **Local repository:** On your computer
- **Remote repository:** On a server (like GitHub)

---

### Commit

A **commit** is a snapshot of your project at a specific moment. Think of it as a "save point" in a video game.

```
┌─────────────────────────────────────────────────────────────┐
│                    Project History                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Commit 1        Commit 2        Commit 3        Commit 4   │
│  "Initial"  →   "Add login" →  "Fix bug"   →  "Add tests"  │
│  Jan 1          Jan 5           Jan 7          Jan 10       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

Each commit has:
- A unique ID (hash): `a1b2c3d4...`
- A message describing the change: `"Add login functionality"`
- A timestamp: when the commit was made
- An author: who made the commit

**Key insight:** You can go back to any previous commit if something goes wrong.

---

### Clone

**Cloning** creates a local copy of a remote repository.

```
┌─────────────────┐                    ┌─────────────────┐
│     GitHub      │     git clone      │  Your Computer  │
│                 │  ───────────────►  │                 │
│  my-project     │                    │  my-project     │
│  (remote)       │                    │  (local copy)   │
└─────────────────┘                    └─────────────────┘
```

After cloning, you have the complete project with all its history.

---

### Fork

A **fork** is your personal copy of someone else's repository on GitHub.

```
┌─────────────────┐                    ┌─────────────────┐
│  Original Repo  │       Fork         │   Your Fork     │
│  owner/project  │  ───────────────►  │  you/project    │
│  (GitHub)       │                    │  (GitHub)       │
└─────────────────┘                    └─────────────────┘
```

**Fork vs Clone:**
- **Fork:** Copy on GitHub (your own remote repository)
- **Clone:** Copy on your computer (local repository)

**Typical workflow:**
1. Fork a repository (creates your copy on GitHub)
2. Clone your fork (downloads to your computer)
3. Make changes locally
4. Commit and push changes to your fork

---

### Staging Area

Before committing, you choose which changes to include. The **staging area** (or "index") holds changes ready to be committed.

```
┌─────────────┐    git add    ┌─────────────┐   git commit   ┌─────────────┐
│  Working    │ ───────────► │   Staging   │ ─────────────► │  Repository │
│  Directory  │              │    Area     │                │   (Commits) │
│             │              │             │                │             │
│ (your files)│              │ (ready to   │                │ (permanent  │
│             │              │  commit)    │                │  history)   │
└─────────────┘              └─────────────┘                └─────────────┘
```

**Why staging?**
- Commit related changes together
- Leave unfinished work out of the commit
- Review changes before making them permanent

---

### Push and Pull

Communication between your local repository and the remote:

```
┌─────────────┐                           ┌─────────────┐
│   Local     │         git push          │   Remote    │
│   Repo      │  ──────────────────────►  │   (GitHub)  │
│             │                           │             │
│             │         git pull          │             │
│             │  ◄──────────────────────  │             │
└─────────────┘                           └─────────────┘
```

- **Push:** Send your local commits to the remote
- **Pull:** Get changes from the remote to your local repository

## The Git Workflow

Here's how all these concepts fit together:

```
┌─────────────────────────────────────────────────────────────┐
│                    Git Workflow for This Tutorial            │
└─────────────────────────────────────────────────────────────┘

1. FORK (on GitHub)
   Original repo → Your fork

2. CLONE (to your computer)
   Your fork → Local copy

3. EDIT (make changes)
   Modify files in your working directory

4. STAGE (prepare changes)
   git add → Staging area

5. COMMIT (save snapshot)
   git commit → Local repository

6. PUSH (upload changes)
   Local → Your fork on GitHub
```

> **Note:** Professional teams often use additional steps like branching and pull requests for code review. You'll learn these in your capstone projects.

## Common Git Commands

| Command | Purpose |
|---------|---------|
| `git clone URL` | Download a repository |
| `git status` | See current state |
| `git add .` | Stage all changes |
| `git commit -m "message"` | Create a commit |
| `git push` | Upload to remote |
| `git pull` | Download from remote |

You don't need to memorize these now — Claude Code will help you with Git commands during the tutorial.

## Connecting to Jira

When you use a Jira issue key in your commit messages, Git and Jira can connect:

```
Jira Issue: ECOM-1 "Create sales dashboard"
                ↓
Commit: "ECOM-1: implement KPI scorecards"
                ↓
Push to GitHub
                ↓
GitHub sees ECOM-1 and links to Jira
                ↓
Jira shows the commits on the issue
```

This **traceability** is valuable because:
- You can see what code relates to what task
- Project managers can track progress
- Anyone can understand why a change was made

## Visual Summary

```
┌─────────────────────────────────────────────────────────────┐
│                         GitHub                              │
│  ┌─────────────────┐              ┌─────────────────┐       │
│  │ Original Repo   │    fork      │   Your Fork     │       │
│  │                 │ ──────────►  │                 │       │
│  └─────────────────┘              └────────┬────────┘       │
│                                            │                │
└────────────────────────────────────────────│────────────────┘
                                             │ clone
                                             ▼
┌─────────────────────────────────────────────────────────────┐
│                      Your Computer                          │
│                                                             │
│  ┌─────────────┐  add   ┌─────────┐ commit ┌─────────────┐  │
│  │  Working    │ ────►  │ Staging │ ─────► │   Local     │  │
│  │  Directory  │        │  Area   │        │   Repo      │  │
│  └─────────────┘        └─────────┘        └──────┬──────┘  │
│        ▲                                          │         │
│        │                                          │ push    │
│        │ edit files                               ▼         │
│        │                              ┌─────────────────┐   │
│        └───────────────────────────── │   Your Fork     │   │
│                                       │   (on GitHub)   │   │
│                                       └─────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

## Key Takeaways

1. **Repository:** A project folder tracked by Git
2. **Commit:** A snapshot of your project at a point in time
3. **Fork:** Your copy of a repository on GitHub
4. **Clone:** Your local copy of a repository
5. **Push/Pull:** Sync between local and remote
6. **Staging Area:** Changes ready to be committed

## Practice Exercise (Optional)

Before starting Session 2, try this exercise to verify your Git setup. Use the tutorial repository you cloned in Session 1.

### Check Repository Status

```bash
git status
```

**What you should see:** A message saying "On branch main" and "nothing to commit, working tree clean" (or similar).

This confirms Git is working correctly and your repository is ready for Session 2.

## Next Steps

Now that you understand Git concepts, continue to [Session 2: Workflow](04-session-2-workflow.md) where you'll put these concepts into practice.
