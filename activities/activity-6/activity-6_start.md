## Expected outputs
You've done a lot of work. In a real project, this work would be done as a series of commits on a feature branch.

## Step 6 – Light Git intro, commit simulation, and reflection

This step gives a gentle version-control primer. First, you’ll see what “good” commits could look like. If you’re running from a downloaded ZIP (no Git history), this is just a glimpse of what’s possible. If you’re in a Codespace on `main` (as instructed earlier), you’ll also see real tracked changes in VS Code’s Source Control view.

### 1) Preview a clean commit log
Run this in a new code cell to print an example history you might have created by following TDD with good messages:

```python
print("### My Commit Log")
commits = [
    "feat: Add initial failing test for lunch loyalty",
    "fix: Implement lunch loyalty rule",
    "feat: Add evening loyalty test",
    "fix: Handle time-of-day logic",
    "refactor: Simplify function and add docstring",
    "fix: Add busy heatwave override",
]
for c in commits:
    print("-", c)
```

If you’re running from a ZIP without Git, this is illustrative only. In a Codespace, you can compare this to your real changes.

### 2) See your pending changes in VS Code (Codespace)
- Open the **Source Control** view (VS Code left sidebar icon).  
- Confirm you’re on `main` of your fork and notice the **Changes** list—Git is already tracking your edits in the Codespace.  
- Click files to review diffs; stage individual files if you want to practice selective staging.

### 3) Make a single commit in the UI
If you want to bundle everything into one commit:
- In Source Control, enter a concise message (e.g., “docs: add venv setup and mlflow commands”).  
- Optionally, use your LLM/Copilot to draft a good message, then edit for accuracy.  
- Click **Commit**. (Skip pushing unless instructed.)

### 4) Try the same flow in the terminal
Open a terminal in your Codespace:
- Check your branch: `git branch` (stay on `main` of your fork for this exercise).
- See pending changes and diffs: `git status`, `git diff`.
- Stage everything: `git add -A`
- Commit with a clear message: `git commit -m "docs: add venv setup and mlflow commands"`
- Do **not** push unless told.

### 5) Think about branching (for real projects)
- Today you’re on `main` and committing locally. You could push to `main` here, but in real teams you create feature branches for changes (e.g., `feature/mlflow-docs`) and open a PR for review before merging.
- Branch basics you’ll use elsewhere:
  - Create/switch: `git switch -c feature/something`
  - Push branch: `git push -u origin feature/something`
  - Open a PR for review, then merge into `main` after checks pass.

### 6) Wrap-up and next steps
Create a Markdown cell to close this exercise and look ahead:

```markdown
### Wrap-up
- How did TDD (red → green → refactor) and small commits reinforce each other in this workshop?
- Which TDD habit will you keep using first when you start a new feature?
- After this intro to Git, what’s one small Git habit you’ll practice next time (UI or CLI)?

### Going further
- Move on to Activity 7 to bridge these habits into a small ML pipeline (see `activities/activity-7/activity-7__start.md`), using the same TDD + defensive + observability mindset.
```
