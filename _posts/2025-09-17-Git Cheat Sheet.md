---
layout: post
title: Git Cheat Sheet
description: "Ways to Refer to a Commit · Restore an Old File"
date: 2025-09-17 09:33:00 +0800
type: post
published: true
status: publish
categories: []
tags:
- Git Cheat Sheet

---
---
# 📝 Git Cheat Sheet
As a tech guy, ```git``` is a daily life. The git cheat sheet is a MUST you must master.

## Getting Started
- Start a new repo:  
  ```bash
  git init
````
---
* Clone an existing repo:

  ```bash
  git clone <url>
  ```

## Prepare to Commit

* Add untracked file or unstaged changes:

  ```bash
  git add <file>
  ```
* Add all untracked files and unstaged changes:

  ```bash
  git add .
  ```
* Choose which parts of a file to stage:

  ```bash
  git add -p
  ```
* Move file:

  ```bash
  git mv <old> <new>
  ```
* Delete file:

  ```bash
  git rm <file>
  ```
* Tell Git to forget about a file (without deleting it):

  ```bash
  git rm --cached <file>
  ```
* Unstage one file:

  ```bash
  git reset <file>
  ```
* Unstage everything:

  ```bash
  git reset
  ```
* Check what you added:

  ```bash
  git status
  ```

## Make Commits

* Make a commit (open editor):

  ```bash
  git commit
  ```
* Make a commit with message:

  ```bash
  git commit -m "message"
  ```
* Commit all unstaged changes:

  ```bash
  git commit -am "message"
  ```

## Move Between Branches

* Switch branches:

  ```bash
  git switch <name>
  # or
  git checkout <name>
  ```
* Create a branch:

  ```bash
  git switch -c <name>
  # or
  git checkout -b <name>
  ```
* List branches:

  ```bash
  git branch
  ```
* List branches by most recent:

  ```bash
  git branch --sort=-committerdate
  ```
* Delete a branch:

  ```bash
  git branch -d <name>
  ```
* Force delete a branch:

  ```bash
  git branch -D <name>
  ```

## Diff Staged/Unstaged Changes

* Diff all staged & unstaged changes:

  ```bash
  git diff HEAD
  ```
* Diff just staged changes:

  ```bash
  git diff --staged
  ```
* Diff just unstaged changes:

  ```bash
  git diff
  ```

## Diff Commits

* Show diff between commit & parent:

  ```bash
  git show <commit>
  ```
* Diff two commits:

  ```bash
  git diff <commit1> <commit2>
  ```
* Diff one file since a commit:

  ```bash
  git diff <commit> <file>
  ```
* Show a summary of a diff:

  ```bash
  git diff <commit> --stat
  git show <commit> --stat
  ```

## Ways to Refer to a Commit

* Branch: `main`
* Tag: `v0.1`
* Commit ID: `3e887ab`
* Remote branch: `origin/main`
* Current commit: `HEAD`
* Three commits ago: `HEAD^^^` or `HEAD~3`

## Discard Your Changes

* Delete unstaged changes (one file):

  ```bash
  git checkout <file>
  ```
* Delete all staged & unstaged changes (one file):

  ```bash
  git checkout HEAD <file>
  ```
* Delete all staged & unstaged changes:

  ```bash
  git reset --hard
  ```
* Delete untracked files:

  ```bash
  git clean
  ```
* Stash staged & unstaged changes:

  ```bash
  git stash
  ```

## Edit History

* Undo the most recent commit (keep working dir):

  ```bash
  git reset HEAD^
  ```
* Squash the last 5 commits into one:

  ```bash
  git rebase -i HEAD~6
  ```
* Undo a failed rebase:

  ```bash
  git reflog BRANCHNAME
  ```
* Change a commit message (or add file):

  ```bash
  git commit --amend
  ```
* Hard reset to a specific commit:

  ```bash
  git reset --hard <commit>
  ```

## Code Archaeology

* Look at branch history:

  ```bash
  git log main
  git log --graph main
  git log --oneline
  ```
* Show commits that modified a file:

  ```bash
  git log <file>
  git log --follow <file>
  ```
* Find commits that added/removed text:

  ```bash
  git log -G "banana"
  ```
* Show who last changed each line:

  ```bash
  git blame <file>
  ```

## Combine Diverged Branches

* Rebase:

  ```bash
  git switch banana
  git rebase main
  ```
* Merge:

  ```bash
  git switch main
  git merge banana
  ```
* Squash merge:

  ```bash
  git switch main
  git merge --squash banana
  git commit
  ```
* Fast-forward merge:

  ```bash
  git switch main
  git merge banana
  ```
* Cherry-pick a commit:

  ```bash
  git cherry-pick <commit>
  ```

## Restore an Old File

* Get a version from another commit:

  ```bash
  git checkout <commit> <file>
  # or
  git restore <file> --source <commit>
  ```

## Add a Remote

```bash
git remote add <name> <url>
```

## Push Your Changes

* Push main branch:

  ```bash
  git push origin main
  ```
* Push current branch:

  ```bash
  git push
  ```
* Push a new branch:

  ```bash
  git push -u origin <name>
  ```
* Force push:

  ```bash
  git push --force-with-lease
  ```
* Push tags:

  ```bash
  git push --tags
  ```

## Pull Changes

* Fetch changes (no merge):

  ```bash
  git fetch origin main
  ```
* Fetch + rebase:

  ```bash
  git pull --rebase
  ```
* Fetch + merge:

  ```bash
  git pull origin main
  # or
  git pull
  ```
* Fetch all branches:

  ```bash
  git fetch --all
  ```

## Configure Git

* Set a config option:

  ```bash
  git config user.name "Your Name"
  ```
* Set option globally:

  ```bash
  git config --global ...
  ```
* Add an alias:

  ```bash
  git config alias.st status
  ```
* See all options:

  ```bash
  man git-config
  ```

## Important Files

* Local config: `.git/config`
* Global config: `~/.gitconfig`
* Ignore list: `.gitignore`
---
