# Git 分支管理

Git 分支管理是 Git 强大功能之一，能够让多个开发人员并行工作，开发新功能、修复 bug 或进行实验，而不会影响主代码库。

几乎每一种版本控制系统都以某种形式支持分支，一个分支代表一条独立的开发线。使用分支意味着你可以从开发主线上分离开来，然后在不影响主线的同时继续工作。

---

## 创建分支

**创建新分支并切换到该分支：**

```bash
git checkout -b <branchname>
```

例如：

```bash
git checkout -b feature-xyz
```

**切换分支命令：**

```bash
git checkout <branchname>
```

例如：

```bash
git checkout main
```

> 💡 当你切换分支的时候，Git 会用该分支的最后提交的快照替换你的工作目录的内容，所以多个分支不需要多个目录。

---

## 查看分支

| 命令 | 说明 |
|------|------|
| `git branch` | 查看本地分支 |
| `git branch -r` | 查看远程分支 |
| `git branch -a` | 查看所有本地和远程分支 |

---

## 合并分支

将其他分支合并到当前分支：

```bash
git merge <branchname>
```

例如，切换到 main 分支并合并 feature-xyz 分支：

```bash
git checkout main
git merge feature-xyz
```

### 解决合并冲突

当合并过程中出现冲突时，Git 会标记冲突文件，你需要手动解决冲突。

1. 打开冲突文件，按照标记解决冲突
2. 标记冲突解决完成：`git add <conflict-file>`
3. 提交合并结果：`git commit`

---

## 删除分支

| 命令 | 说明 |
|------|------|
| `git branch -d <branchname>` | 删除本地分支 |
| `git branch -D <branchname>` | 强制删除未合并的分支 |
| `git push origin --delete <branchname>` | 删除远程分支 |

---

## Git 命令手册

| 命令 | 说明 | 用法示例 |
|------|------|----------|
| `git branch` | 列出、创建或删除分支。它不切换分支，只是用于管理分支的存在。 | `git branch`：列出所有分支<br>`git branch new-branch`：创建新分支<br>`git branch -d old-branch`：删除分支 |
| `git checkout` | 切换到指定的分支或恢复工作目录中的文件。也可以用来检出特定的提交。 | `git checkout branch-name`：切换分支<br>`git checkout file.txt`：恢复文件到工作区<br>`git checkout <commit-hash>`：检出特定提交 |
| `git switch` | 专门用于切换分支，相比 git checkout 更加简洁和直观，主要用于分支操作。 | `git switch branch-name`：切换到指定分支<br>`git switch -c new-branch`：创建并切换到新分支 |
| `git merge` | 合并指定分支的更改到当前分支。 | `git merge branch-name`：将指定分支的更改合并到当前分支 |
| `git mergetool` | 启动合并工具，以解决合并冲突。 | `git mergetool`：使用默认合并工具解决冲突<br>`git mergetool --tool=<tool-name>`：指定合并工具 |
| `git log` | 显示提交历史记录。 | `git log`：显示提交历史<br>`git log --oneline`：以简洁模式显示提交历史 |
| `git stash` | 保存当前工作目录中的未提交更改，并将其恢复到干净的工作区。 | `git stash`：保存当前更改<br>`git stash pop`：恢复最近保存的更改<br>`git stash list`：列出所有保存的更改 |
| `git tag` | 创建、列出或删除标签。标签用于标记特定的提交。 | `git tag`：列出所有标签<br>`git tag v1.0`：创建一个新标签<br>`git tag -d v1.0`：删除标签 |
| `git worktree` | 允许在一个仓库中检查多个工作区，适用于同时处理多个分支。 | `git worktree add <path> branch-name`：在指定路径添加新的工作区并切换到指定分支<br>`git worktree remove <path>`：删除工作区 |