# Terminal Basics

The terminal (also called command line or CLI) is a text-based interface for interacting with your computer. Instead of clicking buttons and icons, you type commands. This guide covers the essential commands you need for this tutorial.

## Opening the Terminal

### In Cursor (Recommended)

Cursor has a built-in terminal that you will use throughout this tutorial:

1. Open Cursor
2. Go to **Terminal** → **New Terminal** from the menu bar
3. Or press `` Ctrl+` `` (backtick key, usually below Escape)

The terminal appears at the bottom of the Cursor window.

### Standalone Terminal (Alternative)

**macOS:**
- Open **Finder** → **Applications** → **Utilities** → **Terminal**
- Or press `Cmd+Space`, type "Terminal", press Enter

**Windows:**
- Press `Win+X`, select **Windows Terminal** or **PowerShell**
- Or press `Win+R`, type "cmd", press Enter

## Understanding the Prompt

When you open a terminal, you see a **prompt** — text indicating the terminal is ready for your command:

**macOS/Linux:**
```
username@computer ~ %
```

**Windows:**
```
C:\Users\username>
```

The `~` or path shows your current location in the file system.

## Essential Commands

### Seeing Where You Are: `pwd`

**Print Working Directory** — shows your current location.

```bash
pwd
```

**Example output (macOS):**
```
/Users/alex/projects
```

**Example output (Windows):**
```
C:\Users\alex\projects
```

**Checkpoint:** Run `pwd` now. You should see a path on your computer.

---

### Listing Files: `ls` (macOS) / `dir` (Windows)

Shows files and folders in the current directory.

**macOS/Linux:**
```bash
ls
```

**Windows:**
```cmd
dir
```

**Example output:**
```
Documents    Downloads    Desktop    projects
```

**Tip:** On macOS, `ls -la` shows hidden files and more details.

**Checkpoint:** Run `ls` (macOS) or `dir` (Windows). You should see files and folders.

---

### Changing Directories: `cd`

**Change Directory** — moves you to a different folder.

```bash
cd foldername
```

**Examples:**
```bash
# Go into a folder called "projects"
cd projects

# Go up one level (to parent folder)
cd ..

# Go to your home directory
cd ~

# Go to a specific path (macOS)
cd /Users/alex/Documents

# Go to a specific path (Windows)
cd C:\Users\alex\Documents
```

**Important:** If a folder name has spaces, wrap it in quotes:
```bash
cd "My Documents"
```

**Checkpoint:** Try `cd ..` then `pwd` to see you moved up one level. Then `cd -` to go back (macOS) or navigate back manually (Windows).

---

### Creating Directories: `mkdir`

**Make Directory** — creates a new folder.

```bash
mkdir foldername
```

**Example:**
```bash
mkdir my-project
```

**Checkpoint:** Create a test folder with `mkdir test-folder`, then `ls` to see it.

---

### Clearing the Screen: `clear` (macOS) / `cls` (Windows)

Clears all text from the terminal for a fresh view.

**macOS/Linux:**
```bash
clear
```

**Windows:**
```cmd
cls
```

**Tip:** You can also press `Ctrl+L` on most terminals.

---

## Running Programs

To run a program, type its name:

```bash
# Check Python version
python --version

# Check Git version
git --version

# Run Claude Code
claude
```

Some programs take **arguments** (additional information):

```bash
# Clone a repository (git is the program, clone is the command, URL is the argument)
git clone https://github.com/user/repo.git
```

## Command Structure

Most commands follow this pattern:

```
command [options] [arguments]
```

**Examples:**
```bash
# command only
pwd

# command with argument
cd projects

# command with option and argument
ls -la Documents

# command with multiple arguments
cp file1.txt file2.txt
```

**Options** (also called flags) modify how a command works:
- Usually start with `-` (single letter) or `--` (full word)
- Example: `ls -l` (long format) or `git --version`

## Paths: Absolute vs Relative

### Absolute Paths

Start from the root of your file system. They work from anywhere.

**macOS/Linux:**
```
/Users/alex/projects/my-app
```

**Windows:**
```
C:\Users\alex\projects\my-app
```

### Windows Path Notes

Windows paths use backslashes (`\`) while macOS/Linux use forward slashes (`/`).

**In PowerShell, forward slashes usually work too:**
```powershell
cd C:/Users/alex/projects    # Works in PowerShell
cd C:\Users\alex\projects    # Also works
```

**Common Windows paths:**
| Location | Path |
|----------|------|
| Home folder | `C:\Users\YourName` |
| Desktop | `C:\Users\YourName\Desktop` |
| Documents | `C:\Users\YourName\Documents` |
| GitHub folder | `C:\Users\YourName\GitHub` |

### Relative Paths

Start from your current location.

```bash
# If you're in /Users/alex
cd projects          # Goes to /Users/alex/projects

# Special relative paths
.     # Current directory
..    # Parent directory
~     # Home directory (macOS/Linux)
```

**Example:**
```bash
pwd
# /Users/alex/projects

cd ../Documents
pwd
# /Users/alex/Documents
```

## Tab Completion

Press `Tab` to auto-complete file and folder names:

```bash
cd Doc[TAB]
# Completes to: cd Documents/
```

If multiple matches exist, press `Tab` twice to see options.

**This saves time and prevents typos!**

### Tab Completion with Git

Tab completion also works with Git commands:

```bash
git sta[TAB]
# Completes to: git status
```

**Tip:** Use Tab completion for Git commands to save time and prevent typos.

## Command History

- Press `↑` (up arrow) to see previous commands
- Press `↓` (down arrow) to go forward
- Type `history` to see all recent commands (macOS/Linux)

## Stopping a Command

If a command is running and you want to stop it:

- Press `Ctrl+C` to cancel/interrupt
- Press `Ctrl+D` to exit (close the terminal session)

## Common Mistakes and Fixes

### "Command not found"

```
zsh: command not found: pythno
```

**Cause:** Typo in command name, or the program isn't installed.

**Fix:** Check spelling, or install the missing program.

---

### "No such file or directory"

```
cd: no such file or directory: projcts
```

**Cause:** The folder doesn't exist, or you misspelled it.

**Fix:** Use `ls` to see what folders exist, check spelling.

---

### "Permission denied"

```
permission denied: ./script.sh
```

**Cause:** You don't have permission to run this file.

**Fix:** On macOS/Linux, use `chmod +x script.sh` first.

---

### Spaces in names

```
cd My Documents
# Error: too many arguments
```

**Cause:** Terminal thinks "My" and "Documents" are separate arguments.

**Fix:** Use quotes: `cd "My Documents"`

## Quick Reference

| Task | macOS/Linux | Windows |
|------|-------------|---------|
| See current directory | `pwd` | `cd` (no arguments) |
| List files | `ls` | `dir` |
| Change directory | `cd folder` | `cd folder` |
| Go up one level | `cd ..` | `cd ..` |
| Go to home | `cd ~` | `cd %USERPROFILE%` |
| Create folder | `mkdir name` | `mkdir name` |
| Clear screen | `clear` | `cls` |
| Cancel command | `Ctrl+C` | `Ctrl+C` |

## Practice Exercises

Before continuing, try these exercises:

1. **Navigate:** Open the terminal in Cursor, run `pwd` to see where you are
2. **List:** Run `ls` (macOS) or `dir` (Windows) to see files
3. **Move:** Use `cd` to go to your Desktop, then `pwd` to confirm
4. **Create:** Make a folder called `test-folder` with `mkdir`
5. **Return:** Use `cd ..` to go back up

**Checkpoint:** If you can complete these five exercises, you have the terminal skills needed for this tutorial.

## Next Steps

Now that you understand terminal basics, continue to [Git Concepts](03-git-concepts.md).
