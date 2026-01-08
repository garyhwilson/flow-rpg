# Git & GitHub Setup Guide for Autumn Phoenix RPG

This document provides step-by-step instructions for initializing Git, creating a GitHub repository, and pushing your Autumn Phoenix RPG project.

---

## Prerequisites

1. **Git installed** - Check with: `git --version`

   - If not installed: https://git-scm.com/downloads

2. **GitHub account** - Create at https://github.com if needed

3. **Terminal access** - Command line on Mac/Linux, Git Bash on Windows

---

## Step 1: Configure Git (First Time Only)

If you haven't used Git before, configure your identity:

```bash
# Set your name (will appear in commits)
git config --global user.name "Your Name"

# Set your email (should match GitHub account)
git config --global user.email "your.email@example.com"

# Optional: Set default branch name to 'main'
git config --global init.defaultBranch main
```

Verify configuration:

```bash
git config --list
```

---

## Step 2: Initialize Local Git Repository

Navigate to your project directory:

```bash
cd "/Users/garywilson/Downloads/Autumn Phoenix RPG/drafts"
```

Initialize Git:

```bash
# Initialize repository
git init

# Verify .gitignore exists (should already be there)
ls -la .gitignore

# Check status
git status
```

You should see all your files listed as "Untracked files".

---

## Step 3: Create Initial Commit

Add all files to staging:

```bash
# Add all files
git add .

# Check what will be committed
git status
```

You should see files in green under "Changes to be committed".

Create your first commit:

```bash
git commit -m "Initial commit: Complete Autumn Phoenix RPG modular system with publication infrastructure

- Complete core rules (modularized)
- All 10 callings documented
- All 7 core archetypes
- All 4 core species
- Complete equipment system
- Complete spell system (all 4 tiers)
- Publication assembly system with Python script
- YAML manifests for book generation
- Documentation and templates"
```

Verify commit was created:

```bash
git log
```

You should see your commit with timestamp and message.

---

## Step 4: Create GitHub Repository

### Option A: Using GitHub Website

1. Go to https://github.com
2. Click the **+** icon (top right) → **New repository**
3. Fill in details:
   - **Repository name:** `momentum-rpg` (or your preferred name)
   - **Description:** "A narrative-driven TTRPG with flexible casting and unified Momentum economy"
   - **Visibility:**
     - **Private:** Keep it private during development (recommended initially)
     - **Public:** Make it public to share with community
   - **DO NOT** initialize with README, .gitignore, or license (you already have these)
4. Click **Create repository**

GitHub will show you setup instructions - **ignore them** and continue below.

### Option B: Using GitHub CLI (if installed)

```bash
# Create private repo
gh repo create momentum-rpg --private --source=. --remote=origin

# Or create public repo
gh repo create momentum-rpg --public --source=. --remote=origin
```

---

## Step 5: Connect Local Repository to GitHub

Copy the repository URL from GitHub (looks like: `https://github.com/username/momentum-rpg.git`)

Add GitHub as remote:

```bash
# Replace [username] with your GitHub username
git remote add origin https://github.com/[username]/momentum-rpg.git

# Verify remote was added
git remote -v
```

You should see:

```
origin  https://github.com/[username]/momentum-rpg.git (fetch)
origin  https://github.com/[username]/momentum-rpg.git (push)
```

---

## Step 6: Push to GitHub

Push your initial commit:

```bash
# Push to GitHub (first time)
git push -u origin main
```

You may be prompted for GitHub credentials:

- **Username:** Your GitHub username
- **Password:** Use a Personal Access Token (not your account password)
  - Create token at: https://github.com/settings/tokens
  - Select scopes: `repo` (full control of private repositories)
  - Save the token securely - you won't see it again!

After successful push, verify on GitHub:

1. Go to https://github.com/[username]/momentum-rpg
2. You should see all your files!

---

## Step 7: Verify Setup

Check everything is working:

```bash
# Check status
git status
# Should say: "Your branch is up to date with 'origin/main'"

# Check remote
git remote -v
# Should show your GitHub URL

# Check branches
git branch
# Should show: * main
```

Visit your GitHub repository page - you should see:

- ✅ README.md displayed on front page
- ✅ All your directories (drafts/, publications/, scripts/)
- ✅ LICENSE.md and CONTRIBUTING.md
- ✅ Your initial commit in history

---

## Daily Workflow

After setup, your daily workflow becomes:

### Make Changes

```bash
# Edit files (working with Claude)
# Claude creates/edits files as you work together
```

### Review Changes

```bash
# See what changed
git status

# See detailed changes
git diff

# See changes in specific file
git diff path/to/file.md
```

### Commit Changes

```bash
# Add specific files
git add drafts/spells/spell_tiers/cantrips.md

# Or add all changes
git add .

# Commit with descriptive message
git commit -m "Add frost-themed cantrips

- Added Frost Touch cantrip with all 4 attribute variations
- Updated spell quick reference
- Balanced against existing cantrips"
```

### Push to GitHub

```bash
# Push to GitHub
git push

# Or if branch tracking not set
git push origin main
```

---

## Useful Git Commands

### Viewing History

```bash
# See commit history
git log

# See brief history
git log --oneline

# See recent commits
git log -5

# See changes in a commit
git show [commit-hash]
```

### Undoing Changes

```bash
# Discard changes to a file (careful!)
git checkout -- path/to/file.md

# Unstage a file
git reset HEAD path/to/file.md

# Amend last commit (if not pushed yet)
git commit --amend -m "New commit message"
```

### Checking Status

```bash
# Current status
git status

# See what's in staging area
git diff --staged

# See branch info
git branch -vv
```

---

## Working with Branches (Advanced)

For experimental changes:

```bash
# Create new branch
git checkout -b feature/monk-archetype

# Make changes and commit
git add .
git commit -m "Add Monk archetype (WIP)"

# Push branch to GitHub
git push -u origin feature/monk-archetype

# Switch back to main
git checkout main

# Merge branch (when ready)
git merge feature/monk-archetype

# Delete branch
git branch -d feature/monk-archetype
```

---

## Commit Message Best Practices

### Good Commit Messages

```bash
# Specific and clear
git commit -m "Fix Fireball damage calculation in advanced_spells.md"

# Explains why
git commit -m "Reduce Halfling weapon penalty from -2 to -1

The -2 penalty made Halfling fighters non-viable in playtesting.
Reducing to -1 maintains flavor while preserving competitiveness."

# Groups related changes
git commit -m "Rebalance defensive spells

- Increase Mage Armor absorption from 2 to 3
- Reduce Shield cost from -1 to 0 Momentum
- Update quick reference tables"
```

### Poor Commit Messages

```bash
# Too vague
git commit -m "Updates"
git commit -m "Fixed stuff"
git commit -m "Changes"

# Too long for subject line
git commit -m "Updated the spell system to fix several balance issues that came up during playtesting including problems with..."
```

---

## Troubleshooting

### "Repository not found"

- Check remote URL: `git remote -v`
- Verify repository exists on GitHub
- Check spelling of username/repo name

### "Permission denied"

- Generate Personal Access Token on GitHub
- Use token as password (not account password)
- Or set up SSH keys: https://docs.github.com/en/authentication

### "Merge conflict"

- Usually won't happen if working alone
- If it does: edit files to resolve conflicts
- Then: `git add .` and `git commit`

### "Diverged branches"

```bash
# Pull changes from GitHub first
git pull origin main

# Then push your changes
git push origin main
```

---

## GitHub Features to Use

### Issues

Track bugs, features, design questions:

```
Title: Balance - Guard scaling too high
Labels: balance, design-question
Description: [Your detailed description]
```

### Projects

Organize development:

- Create Kanban board
- Track progress
- Organize tasks

### Releases

Mark milestones:

- v0.1.0 - Alpha Playtest
- v0.2.0 - Beta Playtest
- v1.0.0 - First Complete Draft

### Discussions

Community Q&A:

- Ask questions
- Share ideas
- Get feedback

---

## Next Steps After Setup

1. **Verify GitHub page looks good**

   - README displays correctly
   - Files are organized properly

2. **Set repository settings**

   - Add description
   - Add topics/tags (ttrpg, rpg, tabletop, game-design)
   - Configure Issues/Projects if using

3. **Start using Issues**

   - Create issues for design questions
   - Track playtesting feedback
   - Organize TODOs

4. **Continue development**

   - Work with Claude locally
   - Commit regularly
   - Push to GitHub for backup

5. **Consider making public**
   - When ready for playtesters
   - Enable Discussions for community
   - Share on Reddit/Discord/forums

---

## Quick Reference Card

```bash
# DAILY WORKFLOW
git status              # See what changed
git add .              # Stage all changes
git commit -m "msg"    # Commit changes
git push               # Push to GitHub

# CHECKING THINGS
git log                # View history
git diff               # See changes
git branch             # List branches

# UNDOING (CAREFUL!)
git checkout -- file   # Discard changes
git reset HEAD file    # Unstage file
```

---

## Getting Help

- **Git Documentation:** https://git-scm.com/doc
- **GitHub Guides:** https://guides.github.com
- **Git Cheat Sheet:** https://education.github.com/git-cheat-sheet-education.pdf

---

**You're ready to go! Start with Step 1 and work through in order.**

_Questions? Check the troubleshooting section or ask Claude for help with specific Git commands._
