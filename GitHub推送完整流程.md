# 仓库 GitHub 推送完整流程

> 本文档描述如何将 `docs/rule` 内容推送到 **TashanGKD/tashan-docs-rule** 仓库，供任何人完整复现。

---

## 目标仓库

- **组织**：TashanGKD  
- **仓库**：https://github.com/TashanGKD/tashan-docs-rule  
- **内容**：`docs/rule` 目录下的规则、目标、要求体系文档及子目录

---

## 前置条件

| 要求 | 说明 |
|------|------|
| Git | 已安装 [Git for Windows](https://git-scm.com/download/win) |
| GitHub CLI (`gh`) | 已安装 [GitHub CLI](https://cli.github.com/) |
| 组织权限 | 在 TashanGKD 组织下拥有创建仓库及 Push 权限（首次创建时）或 Push 权限（后续更新时） |

---

## 一、一次性配置：登录 GitHub

打开终端（PowerShell 或 CMD），执行：

```powershell
gh auth login
```

按提示操作：
1. 选择 **GitHub.com**
2. 协议选择 **HTTPS**
3. 认证方式选择 **Login with a web browser**
4. 复制终端显示的设备码
5. 在浏览器中打开 `https://github.com/login/device`，输入设备码并授权

登录成功后，终端会显示类似 `Logged in as xxx`。此后无需重复登录。

---

## 二、首次推送：创建仓库并上传

### 2.1 准备上传目录

在任意盘符（如 `D:\`）创建目录并复制 `docs/rule` 内容：

```powershell
# 假设项目路径为 T:\TashanAgent4S_2026\0310_huaxiang，请按实际路径修改
$projectRoot = "T:\TashanAgent4S_2026\0310_huaxiang"
$uploadDir = "D:\github-upload"

New-Item -ItemType Directory -Path $uploadDir -Force
Copy-Item -Path "$projectRoot\docs\rule\*" -Destination $uploadDir -Recurse -Force
```

### 2.2 初始化 Git 并提交

```powershell
cd D:\github-upload

git init
git add .
git commit -m "Initial commit: docs/rule 规则与目标体系文档"
git branch -M main
```

### 2.3 创建组织仓库并推送

使用 GitHub CLI 在 TashanGKD 下创建仓库并推送：

```powershell
gh repo create TashanGKD/tashan-docs-rule --public --source=. --remote=origin --push
```

成功后会输出仓库地址：`https://github.com/TashanGKD/tashan-docs-rule`。

---

## 三、后续更新：推送到已有仓库

当本地 `docs/rule` 有修改，需要同步到 GitHub 时：

### 3.1 同步文件到上传目录

```powershell
$projectRoot = "T:\TashanAgent4S_2026\0310_huaxiang"
$uploadDir = "D:\github-upload"

# 清空上传目录后重新复制（避免删除过的文件残留）
Remove-Item -Path "$uploadDir\*" -Recurse -Force -ErrorAction SilentlyContinue
Copy-Item -Path "$projectRoot\docs\rule\*" -Destination $uploadDir -Recurse -Force
```

### 3.2 提交并推送

```powershell
cd D:\github-upload

git add .
git status   # 可选：查看本次变更
git commit -m "更新: 简要描述本次修改内容"
git push
```

---

## 四、从零复现（他人首次操作）

若他人从未克隆过该仓库，需从零完成整套流程时：

### 4.1 安装与登录

1. 安装 [Git](https://git-scm.com/download/win) 和 [GitHub CLI](https://cli.github.com/)
2. 执行 `gh auth login` 完成登录（需在 TashanGKD 组织内拥有权限）

### 4.2 克隆仓库

```powershell
cd D:\   # 或任意工作目录
git clone https://github.com/TashanGKD/tashan-docs-rule.git
cd tashan-docs-rule
```

克隆后可直接在 `tashan-docs-rule` 目录内修改文件，然后：

```powershell
git add .
git commit -m "更新说明"
git push
```

### 4.3 若需从本地项目目录推送（非克隆）

若本地有完整的 `0310_huaxiang` 项目，希望将 `docs/rule` 推送到该仓库，则：

1. 按 **二、首次推送** 的 2.1、2.2 准备并提交
2. 在 2.3 之前，先添加远程仓库（若仓库已存在）：

```powershell
git remote add origin https://github.com/TashanGKD/tashan-docs-rule.git
git branch -M main
git push -u origin main
```

若仓库尚未创建，仍使用：

```powershell
gh repo create TashanGKD/tashan-docs-rule --public --source=. --remote=origin --push
```

---

## 五、常用命令速查

| 操作 | 命令 |
|------|------|
| 查看状态 | `git status` |
| 查看远程 | `git remote -v` |
| 拉取最新 | `git pull` |
| 推送 | `git push` |
| 查看提交历史 | `git log --oneline` |

---

## 六、故障排查

| 现象 | 可能原因 | 处理 |
|------|----------|------|
| `gh: command not found` | 未安装或未加入 PATH | 安装 [GitHub CLI](https://cli.github.com/) 并重启终端 |
| `You are not logged in` | 未登录 | 执行 `gh auth login` |
| `Permission denied` / `403` | 无组织仓库权限 | 联系 TashanGKD 管理员添加协作权限 |
| `remote origin already exists` | 远程已存在 | 用 `git remote set-url origin https://github.com/TashanGKD/tashan-docs-rule.git` 更新 |

---

*最后更新：2026-03-12*
