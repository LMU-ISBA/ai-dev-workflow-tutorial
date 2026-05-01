# Tutorial v3 implementation plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create v3 of the AI-Assisted Development Workflow Tutorial, replacing spec-kit with the Superpowers Claude Code plugin while preserving v2's structure, format, and project (e-commerce dashboard).

**Architecture:** Documentation-only project. Bootstrap `v3/` by copying `v2/`'s three files, then apply targeted edits to each. Update the project-root `README.md` to point to v3. No code changes; spec lives at `docs/superpowers/specs/2026-04-30-tutorial-v3-superpowers-design.md`.

**Tech Stack:** Markdown only. Git for version control. Each task ends in a focused commit. Each prose-bearing task ends with a humanizer pass before commit (per the user's global rule that document content must be humanized).

**Working directory:** main checkout (worktrees explicitly not used per spec).

**Verification model adapted for docs:** Steps don't follow TDD because there's no code under test. Each task instead has a "verify against spec" step that checks the changes against `docs/superpowers/specs/2026-04-30-tutorial-v3-superpowers-design.md` before committing.

---

## Reference inventory

The spec-kit references in v2 (gathered via `grep` before writing this plan) live at these locations and must all be replaced or removed in v3. Tasks below cite specific lines.

**v2/README.md:** lines 10, 63, 74, 85
**v2/pre-work-setup.md:** lines 20, 35, 70, 102, 115, 369, 389-403, 575, 617, 628, 646, 756-772, 794, 798, 803
**v2/workshop-build-deploy.md:** lines 13, 15-16, 50, 89, 101, 191-391 (Section 2 entirely), 399-449 (Section 3 partial), 493-650 (Section 4 partial), 804-867, 904-929, 1128-1143, 1166, 1176
**README.md (project root):** lines 7, 47

---

## Task 1: Bootstrap v3/ by copying v2/

**Files:**
- Create: `v3/README.md` (copy of `v2/README.md`)
- Create: `v3/pre-work-setup.md` (copy of `v2/pre-work-setup.md`)
- Create: `v3/workshop-build-deploy.md` (copy of `v2/workshop-build-deploy.md`)

- [ ] **Step 1: Confirm v3/ does not yet exist**

Run: `ls v3/ 2>/dev/null || echo "v3/ does not exist"`
Expected: `v3/ does not exist`

- [ ] **Step 2: Copy the three v2 files into v3/**

Run:
```bash
mkdir -p v3
cp v2/README.md v3/README.md
cp v2/pre-work-setup.md v3/pre-work-setup.md
cp v2/workshop-build-deploy.md v3/workshop-build-deploy.md
```

- [ ] **Step 3: Verify line counts match**

Run: `wc -l v3/README.md v3/pre-work-setup.md v3/workshop-build-deploy.md`
Expected: 97, 809, 1176 lines respectively (matching v2).

- [ ] **Step 4: Commit**

```bash
git add v3/
git commit -m "Bootstrap v3/ from v2/ (verbatim copy before edits)"
```

---

## Task 2: Update v3/README.md (workflow + tooling references)

**Files:**
- Modify: `v3/README.md` (lines 10, 63, 74, 85)

- [ ] **Step 1: Replace the workshop link description (line 10)**

Find:
```
| [Workshop](workshop-build-deploy.md) | Plan with [spec-kit](https://github.com/github/spec-kit), build with Claude Code, deploy live | ~3 hours, live on Zoom |
```

Replace with:
```
| [Workshop](workshop-build-deploy.md) | Plan with [Superpowers](https://github.com/obra/superpowers), build with Claude Code, deploy live | ~3 hours, live on Zoom |
```

- [ ] **Step 2: Replace the workflow diagram (lines 62-71)**

Find the spec-kit ASCII diagram and replace with the v3 diagram from the spec (`docs/superpowers/specs/2026-04-30-tutorial-v3-superpowers-design.md` "Workflow diagram" section). Keep the same boxed-ASCII style; show: `PRD → brainstorming → writing-plans → Jira → Code` on the top row and `Live! ← Deploy ← Push ← executing-plans` on the bottom row.

- [ ] **Step 3: Replace bullet 2 in the workflow numbered list (line 74)**

Find: `2. **spec-kit** -- Refine requirements into a constitution, specification, plan, and tasks`

Replace with two bullets:
```
2. **brainstorming** -- A Superpowers skill that asks clarifying questions and produces a design document
3. **writing-plans** -- A Superpowers skill that turns the design into a bite-sized implementation plan
```

Renumber the remaining bullets accordingly (Jira becomes 4, Code 5, Commit 6, Push 7, Deploy 8).

- [ ] **Step 4: Update the "Spec-driven development" key concept (line 85)**

Find the paragraph beginning `**Spec-driven development.**` and replace with:
```
**Skill-driven development.** Instead of jumping straight to code, you let Claude's Superpowers skills run a structured process: brainstorming explores what to build, writing-plans turns that into a bite-sized plan, then executing-plans implements task by task. This prevents the most common failure mode: building the wrong thing fast.
```

- [ ] **Step 5: Run humanizer pass on the file**

Re-read v3/README.md from start to finish. Watch for em-dash overuse, AI vocabulary words, copula avoidance, and any content brought in from the spec that wasn't humanized. Apply edits inline.

- [ ] **Step 6: Verify against spec**

Open `docs/superpowers/specs/2026-04-30-tutorial-v3-superpowers-design.md`. Confirm `v3/README.md` matches the "Workflow diagram" and the spirit of the "Why this version exists" section. Confirm no spec-kit references remain in `v3/README.md`.

Run: `grep -i "spec-kit\|speckit\|specify init" v3/README.md`
Expected: no output.

- [ ] **Step 7: Commit**

```bash
git add v3/README.md
git commit -m "Update v3/README.md workflow diagram and tooling references for Superpowers"
```

---

## Task 3: Update v3/pre-work-setup.md TOC, intro, and tools list

**Files:**
- Modify: `v3/pre-work-setup.md` (lines 20, 35, 70, 102, 115)

- [ ] **Step 1: Update the table of contents entry for Section 2.5 (line 20)**

Find: `  - [2.5 spec-kit](#25-spec-kit)`
Replace with: `  - [2.5 Superpowers plugin](#25-superpowers-plugin)`

- [ ] **Step 2: Update the tools list (line 35)**

Find: `Tools:     Cursor, Git, Python 3.11+, uv, spec-kit, Claude Code`
Replace with: `Tools:     Cursor, Git, Python 3.11+, Claude Code, Superpowers plugin`

(uv was a dependency of spec-kit. With spec-kit gone, uv is no longer needed for the tutorial. Drop it.)

- [ ] **Step 3: Update the "Plan before you build" bullet (line 70)**

Find: `- Plan before you build (spec-kit)`
Replace with: `- Plan before you build (Superpowers' brainstorming and writing-plans skills)`

- [ ] **Step 4: Update the tools diagram (line 102)**

Find: `|  Claude Code (AI assistant)  <-->  spec-kit (planning)       |`
Replace with: `|  Claude Code (AI assistant)  <-->  Superpowers (planning skills) |`

- [ ] **Step 5: Update the tool description bullet (line 115)**

Find: `- **spec-kit** turns requirements into structured plans before you start coding.`
Replace with: `- **Superpowers** is a Claude Code plugin whose skills (brainstorming, writing-plans, executing-plans) turn requirements into bite-sized implementation tasks before you start coding.`

- [ ] **Step 6: Run humanizer pass on the modified passages**

Re-read each edited section. Apply humanizer rules. Pay attention to em-dash overuse and AI vocabulary words ("crucial", "key", "leverage", "robust"). Edit inline.

- [ ] **Step 7: Verify against spec**

Confirm the changes match the "Pre-work changes" section of the spec ("Tools table", "Account creation: unchanged", etc.).

- [ ] **Step 8: Commit**

```bash
git add v3/pre-work-setup.md
git commit -m "Update v3/pre-work-setup.md TOC, intro, and tools references for Superpowers"
```

---

## Task 4: Replace v3/pre-work-setup.md Section 2.4 (uv install) and 2.5 (spec-kit) with the Superpowers install section

**Files:**
- Modify: `v3/pre-work-setup.md` (lines ~360-410, covering the uv intro through end of section 2.5 spec-kit content)

- [ ] **Step 1: Remove the uv-spec-kit dependency callout (around line 369)**

Find the callout that begins with `> **What is uv?**` and ends with the sentence about spec-kit requiring uv. Since uv is no longer needed (uv was only there to install spec-kit), remove the entire 2.4 uv section. Renumber subsequent subsections accordingly.

(Note: if uv is still useful for the project for other reasons — e.g., fast pip-replacement for pandas/streamlit — keep it but rewrite the rationale to drop the spec-kit dependency framing. Default: remove unless v2 used uv elsewhere. Verify with `grep -n 'uv ' v3/pre-work-setup.md` before removing.)

- [ ] **Step 2: Replace section 2.5 (spec-kit) in its entirety**

The new section 2.5 is "Superpowers plugin" and reads approximately as follows. Paste this verbatim:

```markdown
### 2.5 Superpowers plugin

> **What is Superpowers?** [Superpowers](https://github.com/obra/superpowers) is a Claude Code plugin that gives Claude a library of skills — small pieces of expertise Claude can apply when your prompt matches one of them. Three skills you'll use today: `brainstorming` (asks clarifying questions and produces a design document), `writing-plans` (turns a design into a bite-sized implementation plan), and `executing-plans` (implements the plan task by task with frequent commits). The skills auto-invoke based on what you ask Claude to do, so you don't have to memorize commands.

#### Skills primer

Skills are markdown files that ship with the Superpowers plugin. Each one teaches Claude how to handle a specific type of task. When you ask Claude to design something, the brainstorming skill activates. When you ask Claude to implement a plan, the executing-plans skill activates. You'll see Claude announce which skill it's using, like "Using brainstorming to..." — that visibility is the whole reason this works as a teaching tool.

You'll only ever type one slash command for the entire tutorial: the install command below. Everything else flows from natural-language prompts.

#### Install the plugin

1. Start Claude Code from any directory:

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
```

- [ ] **Step 3: Run humanizer pass on the new section**

Re-read the section. Watch for em-dash overuse (the "What is" callout has one — keep at most one), AI vocabulary words, and the "rule of three" (the three-skill list is content, not pattern, so it stays). Edit inline.

- [ ] **Step 4: Verify against spec**

Confirm the section matches the spec's "NEW: Install Superpowers plugin" and "NEW: Skills primer" rows in the pre-work changes table. Confirm only one slash command is present (the install).

Run: `grep -c '^/' v3/pre-work-setup.md` to estimate slash command lines (rough check; some may be inline).

- [ ] **Step 5: Commit**

```bash
git add v3/pre-work-setup.md
git commit -m "Replace v3 pre-work section 2.5 with Superpowers plugin install"
```

---

## Task 5: Update v3/pre-work-setup.md verification block

**Files:**
- Modify: `v3/pre-work-setup.md` (lines 575, 617, 628)

- [ ] **Step 1: Replace the spec-kit verification command (line 575)**

Find:
```
Expected output: spec-kit help text showing available commands
```
And the command above it (`specify --help` or similar).

Replace the command with starting Claude Code and the expected output with:
```
Expected output: "You have superpowers" appears in the session start banner
```

(The actual command students run is `claude` from inside the project directory; they then visually confirm the banner.)

- [ ] **Step 2: Update the tools diagram in the verification section (line ~617)**

Find: `|    spec-kit ........... Spec-driven planning                   |`
Replace with: `|    Superpowers ........ Skill-driven planning                  |`

- [ ] **Step 3: Update the wrap-up summary paragraph (line 628)**

Find the sentence: `These tools are connected in a way that creates a complete workflow: GitHub hosts your code, Git tracks changes, Jira tracks tasks, Cursor is where you write code, Claude Code helps you build, and spec-kit ensures you plan before you build.`

Replace with: `These tools are connected in a way that creates a complete workflow: GitHub hosts your code, Git tracks changes, Jira tracks tasks, Cursor is where you write code, Claude Code helps you build, and Superpowers' skills help Claude plan before you build.`

- [ ] **Step 4: Run humanizer pass**

Re-read the verification section. Apply edits inline.

- [ ] **Step 5: Verify against spec**

Run: `grep -ni "spec-kit\|specify --help\|specify init" v3/pre-work-setup.md`
Expected: no remaining matches in the verification section (lines 500-650). Some references may still exist in summary or troubleshooting sections covered by Tasks 6-7.

- [ ] **Step 6: Commit**

```bash
git add v3/pre-work-setup.md
git commit -m "Update v3 pre-work verification block for Superpowers"
```

---

## Task 6: Update v3/pre-work-setup.md troubleshooting section

**Files:**
- Modify: `v3/pre-work-setup.md` (lines 646, 756-772)

- [ ] **Step 1: Remove troubleshooting item 7 (spec-kit / specify command not found)**

Find the section beginning `### 7. spec-kit / specify command not found` and ending before the next `###` heading. Delete it entirely. Renumber subsequent items (8 becomes 7, etc.).

- [ ] **Step 2: Add a new troubleshooting item: Superpowers plugin not loaded**

Insert before the renumbered item 7 (which was 8):

```markdown
### 7. Superpowers plugin not loaded

**What you see:** Starting Claude Code does not show `You have superpowers` in the banner, and prompts that should auto-invoke skills (like "Help me design...") don't trigger any skill announcements.

**Why it happens:** Either the plugin install didn't complete, the SessionStart hook isn't firing, or you're using an older Claude Code version that doesn't support plugins.

**How to fix:**
1. Confirm Claude Code version: run `claude --version` in your terminal. You need a version that supports plugins (anything from late 2025 onward).
2. List installed plugins: inside Claude Code, run `/plugin list`. You should see `superpowers` listed.
3. If the plugin is missing, reinstall it: `/plugin install superpowers@claude-plugins-official`
4. Exit Claude Code (`/exit`) and start a fresh session. The hook only fires on session start.
5. If `You have superpowers` still doesn't appear, check `/plugin list` again. If the plugin shows but the hook doesn't fire, there's likely a version mismatch — update Claude Code with `claude update`.
```

- [ ] **Step 3: Update line 646 if it references spec-kit in another troubleshooting context**

Run: `grep -n "spec-kit\|specify" v3/pre-work-setup.md`
Address any remaining hits with edits or removals as appropriate.

- [ ] **Step 4: Run humanizer pass**

Re-read the new troubleshooting section. Apply edits inline.

- [ ] **Step 5: Verify against spec**

Run: `grep -i "spec-kit\|speckit\|specify init\|specify-cli" v3/pre-work-setup.md`
Expected: no output.

- [ ] **Step 6: Commit**

```bash
git add v3/pre-work-setup.md
git commit -m "Replace spec-kit troubleshooting with Superpowers troubleshooting in v3 pre-work"
```

---

## Task 7: Update v3/pre-work-setup.md final summary

**Files:**
- Modify: `v3/pre-work-setup.md` (lines 794, 798, 803)

- [ ] **Step 1: Update the "you installed" summary line (line 794)**

Find: `Installed six tools: Cursor, Git, Python, uv, spec-kit, and Claude Code`
Replace with: `Installed five tools: Cursor, Git, Python, Claude Code, and the Superpowers plugin`

(Adjusted count after dropping uv per Task 4. If uv was kept, adjust to "six tools: Cursor, Git, Python, uv, Claude Code, and the Superpowers plugin".)

- [ ] **Step 2: Update the capstone-transfer paragraph (line 798)**

Find: `...Claude Code for accelerating development, and spec-kit for turning requirements into structured plans.`
Replace with: `...and Claude Code with Superpowers for turning requirements into bite-sized plans you can implement.`

- [ ] **Step 3: Update the "what's next" preview (line 803)**

Find: `2. **Plan with spec-kit** -- create a constitution, specification, plan, and tasks for your dashboard.`
Replace with: `2. **Plan with Superpowers** -- let the brainstorming skill produce a design document, then writing-plans turn it into a bite-sized implementation plan.`

- [ ] **Step 4: Run humanizer pass on the summary section**

Re-read the section. Apply edits inline.

- [ ] **Step 5: Verify**

Run: `grep -i "spec-kit\|speckit\|specify" v3/pre-work-setup.md`
Expected: no output.

- [ ] **Step 6: Commit**

```bash
git add v3/pre-work-setup.md
git commit -m "Update v3 pre-work summary and what's-next for Superpowers"
```

---

## Task 8: Update v3/workshop-build-deploy.md TOC, agenda, accomplishments

**Files:**
- Modify: `v3/workshop-build-deploy.md` (lines 13, 15-16, 50, 89, 101)

- [ ] **Step 1: Update the table of contents Section 2 entries (lines 13, 15-16)**

Find:
```
- [Section 2: Spec-Kit workflow (~25 min)](#section-2-spec-kit-workflow-25-min)
  - [2.1 Read the PRD](#21-read-the-prd)
  - [2.2 Initialize Spec-Kit](#22-initialize-spec-kit)
  - [2.3 Create the constitution](#23-create-the-constitution)
  - [2.4 Create the specification](#24-create-the-specification)
  - [2.5 Create the implementation plan](#25-create-the-implementation-plan)
  - [2.6 Generate tasks](#26-generate-tasks)
```

Replace with:
```
- [Section 2: Brainstorm and plan (~30 min)](#section-2-brainstorm-and-plan-30-min)
  - [2.1 Create v3/CLAUDE.md](#21-create-v3claudemd)
  - [2.2 Create the feature branch](#22-create-the-feature-branch)
  - [2.3 Read the PRD](#23-read-the-prd)
  - [2.4 Brainstorm and plan with one prompt](#24-brainstorm-and-plan-with-one-prompt)
```

- [ ] **Step 2: Update the accomplishments list (line 50)**

Find: `- Generated spec-kit artifacts: constitution, specification, plan, and tasks`
Replace with: `- Generated Superpowers artifacts: a design document and an implementation plan`

- [ ] **Step 3: Update the workflow diagram (lines 87-97)**

Replace the spec-kit ASCII diagram with the v3 diagram (same as Task 2 Step 2).

- [ ] **Step 4: Update the "Why spec-driven development?" callout (line 101)**

Find the callout starting with `> **Why spec-driven development?**`. Replace its body to keep the lesson but update terminology:

```markdown
> **Why skill-driven development?** You could ask Claude "build me a dashboard" directly. But without a clear plan, Claude makes assumptions, and AI can build the wrong thing very fast. Superpowers' skills give the work structure: brainstorming explores what to build, writing-plans turns the design into a bite-sized plan, and executing-plans implements one task at a time. Letting the skills run their process is what makes AI-assisted coding predictable instead of chaotic. In your capstone, this discipline will be the difference between a project that drifts and one that delivers.
```

- [ ] **Step 5: Run humanizer pass on the agenda and intro**

Re-read lines 1-150 of the file. Apply edits inline.

- [ ] **Step 6: Verify**

Run: `grep -i "spec-kit\|speckit" v3/workshop-build-deploy.md | head -20`
Expected: matches still exist below line 150 (Section 2-6); they'll be addressed in subsequent tasks.

- [ ] **Step 7: Commit**

```bash
git add v3/workshop-build-deploy.md
git commit -m "Update v3 workshop TOC, agenda, and intro for Superpowers"
```

---

## Task 9: Replace v3/workshop-build-deploy.md Section 2 entirely

**Files:**
- Modify: `v3/workshop-build-deploy.md` (replace lines 191-391, currently the spec-kit Section 2)

- [ ] **Step 1: Identify the section boundaries**

Run: `grep -n "^## Section" v3/workshop-build-deploy.md`
Expected: a list of section headings with line numbers. Confirm Section 2 starts around line 191 and Section 3 starts around line 395.

- [ ] **Step 2: Replace Section 2 with the v3 version**

Delete lines from `## Section 2: Spec-Kit workflow (~25 min)` through (but NOT including) `## Section 3: Create Jira issues (~10 min)`.

Insert this content in its place:

```markdown
## Section 2: Brainstorm and plan (~30 min)

### Understanding skill-driven development

The rest of the tutorial flows from what you create here. Every step that follows — coding, committing, deploying — depends on the design and plan you produce in this section.

> **The problem with "just code it":** When you ask an AI to build something without a clear design, you get something that might work but probably isn't what you wanted. The AI fills in gaps with assumptions, and each assumption is a potential mismatch with your intent. With a deliverable like an analytics dashboard, even small mismatches compound: the wrong chart type, unexpected aggregation, a layout that doesn't serve the audience.

Superpowers solves this by chaining three skills:

```
brainstorming -> writing-plans -> executing-plans
(design doc)    (impl plan)      (code, tested, committed)
```

Each skill narrows the space of possible outcomes. By the time executing-plans runs, Claude knows what to build, how to build it, and in what order. The result is more likely to match what you actually wanted.

### 2.1 Create v3/CLAUDE.md

> **What is CLAUDE.md?** It's a file Claude Code reads at the start of every session. It's where you put project-specific guidance — code style, workflow conventions, things you want Claude to remember without you having to repeat them every time. For this project, CLAUDE.md tells Claude two things: skip the worktree setup that brainstorming usually does, and stick to the simple, readable code style that matches the rest of the tutorial.

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

Your `main` branch stays clean and stable while you work on the feature branch. Same pattern as professional development teams use.

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

> **Why TDD on some tasks?** Test-driven development means writing a small test before writing the function the test exercises. You write a test that says "compute_total_sales should return $1,234,567 for this dataset," run it (it fails because the function doesn't exist yet), write the simplest version of the function that makes the test pass, then move on. The discipline matters because it forces you to think about behavior before implementation. For dashboard rendering, TDD doesn't earn its keep — Streamlit components are hard to test meaningfully. For data transformations, it does. The plan flags which tasks get the TDD treatment.

**Checkpoint:** You have two new files: a design doc in `docs/superpowers/specs/` and an implementation plan in `docs/superpowers/plans/`. Both are committed to your feature branch (Superpowers commits the design doc automatically; the plan commit may be combined with the first implementation task).
```

- [ ] **Step 3: Run humanizer pass on the new Section 2**

Re-read the entire new Section 2. Apply edits inline. Pay special attention to em-dashes — there should be very few in such a long passage.

- [ ] **Step 4: Verify against spec**

Confirm the section matches the spec's "Section 2 — Create CLAUDE.md, then Brainstorm + Plan" subsection. Confirm:
- 2.1 has the CLAUDE.md content matching the spec exactly
- 2.4 has the single-prompt example matching the spec
- The skill chain explanation is present

Run: `grep -i "spec-kit\|speckit" v3/workshop-build-deploy.md | head -10`
Expected: remaining matches only in Sections 3-6 (will be addressed in subsequent tasks).

- [ ] **Step 5: Commit**

```bash
git add v3/workshop-build-deploy.md
git commit -m "Replace v3 workshop Section 2 with brainstorm-and-plan flow"
```

---

## Task 10: Update v3/workshop-build-deploy.md Section 3 (Jira issues)

**Files:**
- Modify: `v3/workshop-build-deploy.md` (lines 399-449)

- [ ] **Step 1: Update the Section 3 intro paragraph (line 399)**

Find: `Now you bridge two worlds: spec-kit (planning) and Jira (tracking). Each task from your tasks.md becomes a Jira issue...`

Replace with: `Now you bridge two worlds: Superpowers (planning) and Jira (tracking). Each task from your implementation plan becomes a Jira issue, giving you visibility into progress and creating traceability between requirements and implementation.`

- [ ] **Step 2: Update the mental-model diagram (lines 403-413)**

Find the boxed ASCII showing `tasks.md (spec-kit) -> Jira Issues -> Code`. Replace the leftmost box with `plan.md (writing-plans)`. Keep the same structure.

- [ ] **Step 3: Update the prompt template for the first issue (line 420)**

Find:
```
Based on the tasks in @specs/001-sales-dashboard/tasks.md, what should be the first Jira issue? Create it in the ECOM project.
```

Replace with:
```
Based on the tasks in the implementation plan at @docs/superpowers/plans/<plan-file>.md, what should be the first Jira issue? Create it in the ECOM project.
```

Add a note immediately below: `Replace <plan-file> with the actual filename. To find it quickly, run \`ls -t docs/superpowers/plans/ | head -1\` in your terminal.`

- [ ] **Step 4: Update the prompt template for remaining issues (line 438)**

Find:
```
Create Jira issues in the ECOM project for the remaining tasks in @specs/001-sales-dashboard/tasks.md
```

Replace with:
```
Create Jira issues in the ECOM project for the remaining tasks in @docs/superpowers/plans/<plan-file>.md
```

- [ ] **Step 5: Update the Pro Tip at the bottom of the section (line 449)**

Find the sentence in the Pro Tip: `Notice how the progression from PRD to spec-kit to Jira creates increasingly specific, actionable items.`

Replace with: `Notice how the progression from PRD to brainstorming to writing-plans to Jira creates increasingly specific, actionable items.`

Update the example chain in the same Pro Tip: replace `the spec-kit task might say` with `the plan task might say`.

- [ ] **Step 6: Update other "spec-kit" references in this section**

Run: `grep -n "spec-kit\|specs/001" v3/workshop-build-deploy.md | awk -F: '$2 < 470'`
Address any remaining hits with appropriate edits.

- [ ] **Step 7: Run humanizer pass**

Re-read Section 3. Apply edits inline.

- [ ] **Step 8: Verify against spec**

Confirm Section 3 matches the spec's "Section 3 — Create Jira issues from the plan" subsection. Confirm prompt templates use `@docs/superpowers/plans/<plan-file>.md`.

- [ ] **Step 9: Commit**

```bash
git add v3/workshop-build-deploy.md
git commit -m "Update v3 workshop Section 3 to use writing-plans output as Jira source"
```

---

## Task 11: Update v3/workshop-build-deploy.md Section 4 (Build)

**Files:**
- Modify: `v3/workshop-build-deploy.md` (lines 493-650)

- [ ] **Step 1: Update the Section 4 intro to set up auto-invocation**

Find the prose around lines 480-495 that introduces how students will build the issue. Replace any text that mentions `/speckit.implement` with the auto-invocation prompt approach.

- [ ] **Step 2: Replace the spec-kit implement command (line 493-496)**

Find:
```
2. In Claude Code, implement the issue using the spec-kit implement command:

   ```
   /speckit.implement
   ```
```

Replace with:
```
2. In Claude Code, ask Claude to start implementing the first issue:

   ```
   Let's start implementing ECOM-1.
   ```

   Claude will recognize this as an implementation task and auto-invoke `executing-plans`. You'll see `Using executing-plans to...` in the output. The skill reads the plan, picks up the first task, and starts working.
```

- [ ] **Step 3: Add a TDD walkthrough callout right after the prompt example**

Insert this callout:

```markdown
> **What you'll see during a TDD task:** For tasks flagged as test-driven (typically data-transformation tasks like `compute_total_sales`), executing-plans will: (a) write a failing test in a `tests/` file, (b) run pytest and show you the failure, (c) implement the function, (d) run pytest again and show you the pass, (e) commit with a message referencing your Jira issue. For non-TDD tasks (chart rendering, page layout), it'll skip straight to implementation and commit. Watch the test output — seeing red turn green is one of the more satisfying parts of the workshop.
```

- [ ] **Step 4: Update the implement-cycle diagram (line 632)**

Find the ASCII diagram showing `/speckit.implement with issue key --> Move to In Progress`. Replace the trigger with the natural-language prompt: `"Let's implement ECOM-N" --> Claude auto-invokes executing-plans --> Move to In Progress`.

- [ ] **Step 5: Find and remove other speckit command references in Section 4**

Run: `grep -n "speckit\|/speck" v3/workshop-build-deploy.md`
Address each hit. Most should be replaced with natural-language prompts that match the auto-invocation pattern.

- [ ] **Step 6: Run humanizer pass**

Re-read Section 4. Apply edits inline.

- [ ] **Step 7: Verify against spec**

Confirm Section 4 matches the spec's "Section 4 — Execute the plan" subsection. Confirm:
- Single-prompt-to-start example is present
- TDD walkthrough explains what students will see
- No `/speckit.implement` references remain

- [ ] **Step 8: Commit**

```bash
git add v3/workshop-build-deploy.md
git commit -m "Update v3 workshop Section 4 to use executing-plans auto-invocation with TDD"
```

---

## Task 12: Update v3/workshop-build-deploy.md Section 5 (Deploy) and Section 6 (Final verification)

**Files:**
- Modify: `v3/workshop-build-deploy.md` (lines covering Section 5 deployment and Section 6 verification, including 804-867)

- [ ] **Step 1: Audit Section 5 for spec-kit references**

Run: `grep -n "spec-kit\|.specify\|specs/001" v3/workshop-build-deploy.md | awk -F: '$2 > 700 && $2 < 870'`
Most of Section 5 should not need changes (deploy mechanics are unchanged from v2). Address any remaining hits.

- [ ] **Step 2: Update the Section 6 verification checklist (lines 804-814)**

Find the checklist heading `### MCP and Spec-Kit` and rename to `### MCP and Superpowers`.

Find checklist items that reference spec-kit artifacts:
- `- [ ] Constitution created (\`.specify/memory/constitution.md\`)`
- `- [ ] Issues created from spec-kit tasks (ECOM-1, ECOM-2, etc.)`

Replace with:
- `- [ ] Design document created (\`docs/superpowers/specs/<file>.md\`)`
- `- [ ] Implementation plan created (\`docs/superpowers/plans/<file>.md\`)`
- `- [ ] Issues created from plan tasks (ECOM-1, ECOM-2, etc.)`

(Also remove any other items that referenced spec-kit-specific artifacts like `.specify/` files.)

- [ ] **Step 3: Update the final workflow summary diagram (line 834)**

Find the line: `PRD [done] -> spec-kit [done] -> Jira [done] -> Code [done]...`
Replace with: `PRD [done] -> brainstorming [done] -> writing-plans [done] -> Jira [done] -> Code [done]...`

- [ ] **Step 4: Update the "include in repository" instruction (line 867)**

Find: `Make sure your \`prd/\`, \`specs/\`, and \`.specify/\` directories are included in your repository.`
Replace with: `Make sure your \`prd/\` and \`docs/superpowers/\` directories are included in your repository.`

- [ ] **Step 5: Run humanizer pass**

Re-read Sections 5 and 6. Apply edits inline.

- [ ] **Step 6: Verify**

Run: `grep -i "spec-kit\|.specify\|specify-cli" v3/workshop-build-deploy.md | awk -F: '$2 > 700 && $2 < 900'`
Expected: no output.

- [ ] **Step 7: Commit**

```bash
git add v3/workshop-build-deploy.md
git commit -m "Update v3 workshop Sections 5 and 6 for Superpowers artifacts"
```

---

## Task 13: Update v3/workshop-build-deploy.md troubleshooting and glossary

**Files:**
- Modify: `v3/workshop-build-deploy.md` (lines 904-929, 1128-1143, 1166)

- [ ] **Step 1: Remove the "Spec-Kit slash commands not working" troubleshooting (lines 904-929)**

Find the section starting `### Spec-Kit slash commands not working` and ending before the next `###` heading. Delete it entirely.

- [ ] **Step 2: Add a new troubleshooting item: Skill auto-invocation didn't fire**

Insert in roughly the same position (alphabetical or workflow order — match the surrounding pattern):

```markdown
### Skill auto-invocation didn't fire

**What you see:** You sent Claude a prompt like "Help me design and plan...", but Claude didn't announce a skill (no `Using brainstorming to...` line) and instead just started writing code or asking generic questions.

**Why it happens:** The Superpowers SessionStart hook didn't load the `using-superpowers` skill, or your prompt didn't match the skill's trigger words strongly enough.

**How to fix:**
1. Confirm Superpowers is loaded: at the top of your Claude Code session output, look for `You have superpowers`. If it's missing, see the pre-work troubleshooting for "Superpowers plugin not loaded."
2. Strengthen your prompt with explicit intent words. Instead of "let's work on the dashboard," try "Help me design and plan the dashboard." The brainstorming skill triggers on words like *design*, *plan*, *brainstorm*.
3. As a last resort, force the skill manually inside Claude Code:
   ```
   Use the brainstorming skill to design the e-commerce sales dashboard from @prd/ecommerce-analytics.md.
   ```
```

- [ ] **Step 3: Remove the "specify: command not found" troubleshooting (lines 1128-1143)**

Find and delete the entire section.

- [ ] **Step 4: Update the glossary (line 1166)**

Find:
```
| **spec-kit** | GitHub's toolkit for spec-driven development, converting requirements into structured plans |
```

Replace with three entries (in alphabetical order with existing entries):
```
| **brainstorming** | A Superpowers skill that asks clarifying questions about a proposed feature and produces a design document |
| **executing-plans** | A Superpowers skill that implements tasks from an implementation plan one at a time, with frequent commits |
| **Superpowers** | A Claude Code plugin that gives Claude a library of skills (brainstorming, writing-plans, executing-plans, and more) |
| **writing-plans** | A Superpowers skill that turns a design document into a bite-sized implementation plan |
```

(The existing glossary entries should already be alphabetical — slot the new ones in correctly.)

- [ ] **Step 5: Update the "for your career" closing paragraph (line 1176)**

Find: `The same cycle -- specify, plan, track, build, deploy -- works for any technical project...`
Replace with: `The same cycle — brainstorm, plan, track, build, deploy — works for any technical project...`

- [ ] **Step 6: Run humanizer pass**

Re-read the troubleshooting and glossary sections. Apply edits inline. Especially watch the new troubleshooting entry for em-dash overuse.

- [ ] **Step 7: Verify**

Run: `grep -i "spec-kit\|speckit\|specify" v3/workshop-build-deploy.md`
Expected: no output.

- [ ] **Step 8: Commit**

```bash
git add v3/workshop-build-deploy.md
git commit -m "Update v3 workshop troubleshooting and glossary for Superpowers"
```

---

## Task 14: Add the skill handoff cheat sheet and "Other Superpowers skills" appendix

**Files:**
- Modify: `v3/workshop-build-deploy.md` (insert two new sections)

- [ ] **Step 1: Add the skill handoff cheat sheet sidebar in Section 2**

Insert this sidebar at the end of Section 2.4 (just before the **Checkpoint** line):

```markdown
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
```

- [ ] **Step 2: Add the "Other Superpowers skills" appendix at the end of the document**

Insert before the glossary, as a new top-level section:

```markdown
## Other Superpowers skills you'll meet later

You'll encounter these in larger projects beyond this tutorial. We didn't formally use them in v3 either because they're more advanced than this workshop needs, or because we explicitly overrode them in CLAUDE.md.

| Skill | What it does | Why we skipped it here |
|-------|--------------|------------------------|
| `using-git-worktrees` | Creates an isolated working directory per branch so multiple branches can be checked out simultaneously | We overrode this in CLAUDE.md to keep the workshop on a single working directory |
| `dispatching-parallel-agents` | Splits independent tasks across multiple agents that work in parallel | Overkill for a single-project tutorial |
| `subagent-driven-development` | Executes plans by dispatching a fresh subagent per task, with review checkpoints between | A more advanced execution model than executing-plans; same outcome, more moving parts |
| `writing-skills` | Helps you author your own Superpowers skills | Meta — for skill authors, not skill consumers |
| `systematic-debugging` | Walks through a structured debugging process when something breaks | Triggers automatically if your build hits an unexpected error |

If you want to dig deeper, browse the Superpowers skill library: https://github.com/obra/superpowers-skills
```

- [ ] **Step 3: Run humanizer pass on both new sections**

Apply humanizer rules. Watch the cheat sheet sidebar especially — block diagrams with arrows are content, not patterns, but the prose around them should be plain.

- [ ] **Step 4: Verify against spec**

Confirm both insertions match the spec's "Skill handoff sequence" and "Skills out of scope" subsections.

- [ ] **Step 5: Commit**

```bash
git add v3/workshop-build-deploy.md
git commit -m "Add skill handoff cheat sheet and other-skills appendix to v3 workshop"
```

---

## Task 15: Update root README.md (project-level)

**Files:**
- Modify: `README.md` (lines 7, 47, plus version pointers)

- [ ] **Step 1: Update the workflow diagram (line 7)**

Replace the spec-kit ASCII diagram with the v3 diagram (same as Task 2 Step 2 / Task 8 Step 3).

- [ ] **Step 2: Update the tools table (line 47)**

Find the row:
```
| [spec-kit](https://github.com/github/spec-kit) | Turns requirements into a structured plan |
```

Replace with:
```
| [Superpowers](https://github.com/obra/superpowers) | A Claude Code plugin whose skills turn requirements into bite-sized plans |
```

- [ ] **Step 3: Promote v3 to "current" and demote v2 to "previous"**

Find the section headers in README.md that say "Version 2 (current)" and "Version 1 (original)". Update so that:
- "Version 3 (current)" appears first, with a description and links to `v3/pre-work-setup.md` and `v3/workshop-build-deploy.md`
- "Version 2 (previous)" appears next, with its existing links
- "Version 1 (original)" stays at the bottom

The Version 3 description should mirror Version 2's structure. Suggested text:
```markdown
### Version 3 (current)

Async pre-work + a 3-hour live workshop, using the Superpowers Claude Code plugin for skill-driven planning instead of spec-kit.

1. Start with [Pre-work: Setup](v3/pre-work-setup.md) — accounts, tools, repo setup (60-90 min on your own)
2. Then [Workshop: Build & Deploy](v3/workshop-build-deploy.md) — design, plan, build, and deploy the dashboard (~3 hours, live)
```

- [ ] **Step 4: Run humanizer pass on the modified passages**

Apply humanizer rules. Pay attention to em-dash overuse.

- [ ] **Step 5: Verify**

Run: `grep -i "spec-kit" README.md`
Expected: no output.

Run: `grep -i "Superpowers" README.md`
Expected: at least the tools table row and the v3 description.

- [ ] **Step 6: Commit**

```bash
git add README.md
git commit -m "Promote v3 to current in root README.md and update tooling references"
```

---

## Task 16: End-to-end verification (no commit)

This task confirms the v3 docs are coherent and accurate before declaring the project done.

- [ ] **Step 1: Confirm all spec-kit references are gone from v3/**

Run: `grep -ri "spec-kit\|speckit\|specify init\|.specify\|specify-cli" v3/`
Expected: no output.

- [ ] **Step 2: Confirm all spec-kit references are gone from root README.md**

Run: `grep -i "spec-kit" README.md`
Expected: no output.

- [ ] **Step 3: Read v3/README.md end to end**

Verify:
- The workflow diagram matches the spec
- The "what you'll build" section is intact
- The version pointers are clear

- [ ] **Step 4: Read v3/pre-work-setup.md end to end as a student would**

Verify:
- Account creation steps still make sense
- Tool installation completes with verification commands
- Section 2.5 (Superpowers plugin) install works mentally — could you actually do it from this doc?
- Verification block at the end actually verifies the new state

- [ ] **Step 5: Read v3/workshop-build-deploy.md end to end as a student would**

Verify:
- Section 1 (MCP setup) is unchanged from v2 and still works
- Section 2 (Brainstorm + Plan) flow makes sense end-to-end:
  - 2.1: students can create CLAUDE.md
  - 2.2: students can create a feature branch
  - 2.3: students read the PRD
  - 2.4: a single prompt produces both a design doc and an implementation plan
- Section 3 (Jira issues) prompt templates point at `docs/superpowers/plans/<plan-file>.md`
- Section 4 (Execute) auto-invocation prompt is plausible; the TDD callout sets expectations correctly
- Section 5 (Deploy) and 6 (Verification) tie everything together
- Troubleshooting covers the new failure modes (plugin not loaded, skill not auto-invoked)
- Glossary has Superpowers entries

- [ ] **Step 6: Smoke test the brainstorming prompt (manual or skipped)**

Optional but recommended: in a fresh Claude Code session inside this repo, with Superpowers installed, send the prompt from Section 2.4 (`Help me design and plan the e-commerce sales dashboard described in @prd/ecommerce-analytics.md.`) and confirm:
- Claude announces brainstorming
- Brainstorming asks clarifying questions
- After approval, brainstorming hands off to writing-plans (without setting up a worktree, because of CLAUDE.md)
- writing-plans produces a plan with TDD-flagged tasks for data transformations

If this smoke test fails because the override in CLAUDE.md isn't honored, the spec needs revisiting — escalate to the user before continuing.

- [ ] **Step 7: Confirm the design doc lives in docs/superpowers/specs/**

Run: `ls docs/superpowers/specs/`
Expected: `2026-04-30-tutorial-v3-superpowers-design.md`

- [ ] **Step 8: Confirm the plan lives in docs/superpowers/plans/**

Run: `ls docs/superpowers/plans/`
Expected: `2026-04-30-tutorial-v3-superpowers.md` (this file).

- [ ] **Step 9: Report verification results to the user**

Summarize what was verified, what (if anything) couldn't be verified automatically, and any issues found. No commit for this task.

---

## Self-review checklist (run before declaring the plan ready)

The writing-plans skill calls for a self-review pass. Performed inline before this plan is committed:

**1. Spec coverage:** Every requirement in the spec is covered by a task above:
- Spec "File structure" → Task 1 (creates v3/ from v2/), Task 14 (handoff cheat sheet placement implies docs/superpowers/), Task 15 (root README updates)
- Spec "Pre-work changes" → Tasks 3-7
- Spec "Workshop changes" Section 1 → no edits needed (unchanged from v2; carried by Task 1's bootstrap copy)
- Spec "Workshop changes" Section 2 → Task 9
- Spec "Workshop changes" Section 3 → Task 10
- Spec "Workshop changes" Section 4 → Task 11
- Spec "Workshop changes" Section 5 → Task 12
- Spec "Workshop changes" Section 6 → Task 12
- Spec "Skill handoff sequence" → Task 14
- Spec "Skills out of scope" → Task 14
- Spec "Risks and mitigations" → mitigations expressed as troubleshooting entries (Tasks 6, 13)
- Spec "Project-root README updates" → Task 15
- Spec "Success criteria" → Task 16 verification

**2. Placeholder scan:** No "TBD", "implement later", or "similar to Task N" patterns. The few `<plan-file>` and `YYYY-MM-DD` placeholders that remain are intentional (students fill them in or Superpowers generates them).

**3. Type/identifier consistency:** Skill names appear consistently (`brainstorming`, `writing-plans`, `executing-plans`, `using-superpowers`, `requesting-code-review`, `finishing-a-development-branch`, `using-git-worktrees`). File paths consistent (`docs/superpowers/specs/`, `docs/superpowers/plans/`, `v3/CLAUDE.md`).

---

## Execution handoff

Plan complete and saved to `docs/superpowers/plans/2026-04-30-tutorial-v3-superpowers.md`. Two execution options:

**1. Subagent-driven (recommended)** — I dispatch a fresh subagent per task, review between tasks, fast iteration. Each subagent gets just the task it needs to execute, plus the spec for context.

**2. Inline execution** — Execute tasks in this session using executing-plans, batch execution with checkpoints for your review.

Which approach?
