
# 🧠 Git & GitHub Cheatsheet – One Shot Edition

---

## Section 0: Shell Commands
```bash
pwd          # Print working directory  
ls -la       # List files with details  
cd ..        # Move to parent directory  
mkdir <dir>  # Create a new directory  
touch <file> # Create a new file  
rm <file>    # Remove file  
```

---

## Section 1: Git Internals
- `.git/` folder contains: `HEAD`, `index`, `objects/`, `refs/`
- Git is a **content-addressable filesystem** (everything is a hash)

---

## Section 1.1: Git Low-Level Commands
```bash
git hash-object <file>         # Create blob object  
git cat-file -p <hash>         # Print object content  
git update-index --add <file>  # Stage file manually  
git write-tree                 # Save current index to tree  
git commit-tree <tree_hash> -m "msg" -p <parent_commit>  
```

---

## Section 2: Working Tree
- **Working Directory**: Your actual files  
- **Index/Stage**: Snapshot to be committed  
- **HEAD**: Pointer to the last commit

---

## Section 3: Git Operations
```bash
git init                 # Initialize repo  
git status               # Show current state  
git add <file>           # Stage file  
git commit -m "msg"      # Commit staged changes  
git diff                 # Show unstaged changes  
git log                  # Show commit history  
git stash                # Save current changes  
git stash pop            # Apply stashed changes  
git revert <commit>      # Undo a commit safely  
git reset --hard HEAD~1  # Delete latest commit  
```

---

## Section 4: Git Branches
```bash
git branch               # List branches  
git branch <name>        # Create branch  
git checkout <branch>    # Switch branch  
git switch -c <branch>   # Create & switch  
git branch -d <branch>   # Delete
```

---

## Section 4.1: GitHub Workaround
- Push branch: `git push origin <branch>`
- Handle conflicts with rename/rebase if needed

---

## Section 5: Merge & Merge Conflicts
```bash
git merge <branch>       # Merge into current branch
```
- Resolve conflicts manually, then:
```bash
git add <file>  
git commit               # Finish merge
```

---

## Section 6: Remote Repositories
```bash
git remote -v  
git remote add origin <url>  
git push origin <branch>  
git fetch  
git pull  
```

---

## Section 7: GitHub Operations
- `git clone <url>`  
- `git remote add origin <url>`  
- Push, Pull, PRs, etc.

---

## Section 8: Pull Requests
- Create branch  
- Push and open PR  
- Review, discuss, and merge via GitHub

---

## Section 9: Forking & Tagging
```bash
git tag <tagname>  
git tag -a <tagname> -m "msg"  
git push origin <tagname>  
```

---

## Section 10: Rebasing
```bash
git rebase <branch>  
git rebase --continue  
git rebase --abort  
```

---

## Section 11: .gitignore
Examples:
```
*.log  
node_modules/  
.env
```

---

## Section 12: Git Log (Use Cases)
```bash
git log  
git log --oneline  
git log --graph --decorate  
git log -S <string>  
```

---

## Section 13: Git in DevOps
- Git for CI/CD, code reviews, feature branches, PR strategies

---

## Section 14: GitHub Pages
- Host static sites from `gh-pages` branch
- Enable from GitHub repo settings

---

## Section 15: Git Hooks
Located in `.git/hooks`  
Common hooks:
- `pre-commit`
- `post-merge`

---

## 📂 Resources
- **PPT Slides**: [Download Link](#)
- **Cheatsheet PDF**: [Download Link](#)

---

