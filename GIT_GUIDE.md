# Git Guide for This Project

A practical guide for working on this project using Git and VS Code.
No prior Git experience needed.

---

## What is Git?

Git is a tool that tracks changes to your code over time.
Think of it like "save history" — you can always go back to any previous version.

- **Git** runs on your computer and tracks your files locally
- **GitHub** is a website where you store and share that history online
- **A repository (repo)** is just a folder that Git is tracking

---

## What is a Fork?

This project belongs to the **ismani-tours** organisation on GitHub.
You cannot push changes directly to it — instead you **fork** it.

A fork is your own personal copy of the project on GitHub.
You make changes in your fork, then propose those changes back via a **Pull Request (PR)**.

---

## Step 1 — Fork the Repo

1. Go to `https://github.com/ismani-tours/tour-web-app`
2. Click the **Fork** button (top-right corner)
3. Select your own GitHub account as the destination
4. You now have your own copy at `https://github.com/YOUR-USERNAME/tour-web-app`

---

## Step 2 — Clone to Your Computer

Cloning downloads the repo to your laptop.

### Using VS Code (recommended)

1. Open VS Code
2. Press `Ctrl + Shift + P` → type `Git: Clone` → press Enter
3. Paste your fork URL: `https://github.com/YOUR-USERNAME/tour-web-app`
4. Choose a folder on your computer (e.g. `Documents\projects`)
5. Click **Open** when VS Code asks

### Using Command Prompt

```
git clone https://github.com/YOUR-USERNAME/tour-web-app
cd tour-web-app
```

---

## Step 3 — Create a Branch

Never work directly on `main`. Create a branch with your name.

### Using VS Code

1. Look at the **bottom-left corner** of VS Code — you will see `main`
2. Click it
3. Click **Create new branch**
4. Type your name as the branch name, e.g. `amina` or `john-dev`
5. Press Enter

### Using Command Prompt

```
git checkout -b your-name
```

You are now working on your own branch. Changes here will not affect `main`.

---

## Step 4 — Set Up and Run the Project

Open the VS Code terminal: `Ctrl + `` ` (backtick key, top-left of keyboard)

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
python run.py
```

Open your browser and go to `http://127.0.0.1:5000`

> If you see an error saying `python` is not recognised, try `py` instead of `python`.

---

## Step 5 — Make Your Changes

Edit files in VS Code as normal.
When you save a file, notice the **Source Control icon** on the left sidebar (looks like a branch) shows a number — that is how many files you have changed.

---

## Step 6 — Stage and Commit

A **commit** is a snapshot of your changes with a message explaining what you did.

### Using VS Code

1. Click the **Source Control icon** on the left sidebar (or press `Ctrl + Shift + G`)
2. You will see a list of changed files under **Changes**
3. Hover over a file and click the **+** button to stage it (or click **+** next to "Changes" to stage all)
4. Type a short message in the box at the top, e.g. `fix login redirect bug`
5. Click the **Commit** button (tick icon) or press `Ctrl + Enter`

### Using Command Prompt

```
git add .
git commit -m "fix login redirect bug"
```

> Write commit messages that describe WHAT you changed, not HOW.
> Good: `fix password not hashing on register`
> Bad: `updated stuff` or `changes`

---

## Step 7 — Push to GitHub

Pushing sends your local commits up to GitHub.

### Using VS Code

1. In the Source Control panel, click the **three-dot menu (...)** at the top
2. Click **Push**
3. If VS Code asks about a remote branch, click **OK / Publish Branch**

### Using Command Prompt

```
git push origin your-branch-name
```

The first time you push a new branch:

```
git push -u origin your-branch-name
```

---

## Step 8 — Open a Pull Request

1. Go to your fork on GitHub: `https://github.com/YOUR-USERNAME/tour-web-app`
2. GitHub will show a yellow banner: **"Compare & pull request"** — click it
3. Make sure the base is `ismani-tours/tour-web-app` → `main`
4. Write a title and description:
   - **What did you change?**
   - **Why did you change it?**
5. Click **Create pull request**

Your changes will be reviewed before being merged.

---

## Daily Workflow (quick reference)

```
1. Pull latest changes before you start
   git pull origin main

2. Work on your branch
   git checkout your-branch-name

3. Save your work
   git add .
   git commit -m "describe what you changed"

4. Push to GitHub
   git push
```

---

## Common Problems

| Problem | Fix |
|---|---|
| `python` not recognised | Use `py` instead of `python` |
| `pip` not recognised | Run `py -m pip install -r requirements.txt` |
| `venv\Scripts\activate` not working | Make sure you are inside the project folder first (`cd tour-web-app`) |
| VS Code says "no git repository" | Open the project folder, not just a file |
| Changes not showing on GitHub | You need to **push** — saving locally is not enough |
| Merge conflict | Ask a teammate or your supervisor before trying to fix it |

---

## VS Code Extensions to Install

These make working with Git much easier:

- **GitLens** — shows who changed each line and full history
- **Git Graph** — visual branch history
- **Python** — syntax highlighting and IntelliSense for Python

To install: press `Ctrl + Shift + X`, search the name, click Install.

---

## Useful Commands Reference

| What you want to do | Command |
|---|---|
| See current status | `git status` |
| See all branches | `git branch` |
| Switch to a branch | `git checkout branch-name` |
| See commit history | `git log --oneline` |
| Pull latest from GitHub | `git pull` |
| See what changed in a file | `git diff` |

---

*If you are stuck, ask a teammate first, then your supervisor.*
