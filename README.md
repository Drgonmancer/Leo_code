# Python 全栈入门教程

<div align="center">

# 🐍 Python 全栈入门教程

**8 大篇章 · 配图讲解 · 边学边练**

> 💡 **推荐阅读方式**：使用左侧目录导航的在线文档站（类似 [DataWhale 动手学大模型](https://datawhalechina.github.io/llm-universe/)）

</div>

## 🌐 在线文档站（左侧目录 + 点击跳转）

本教程已配置 **Docsify** 文档站，左侧为完整目录，点击即可跳转到对应章节。

### 本地启动

在 `Python教程` 目录下执行：

```powershell
# 方式一：Python（推荐，PowerShell）
Set-Location "d:\code\python\Python_project\Leo_Python_NoteBook\Python教程"
python -m http.server 3000
```

```bash
# 方式二：Git Bash / macOS / Linux
cd Python教程
python -m http.server 3000

# 方式三：npx
npx serve . -p 3000
```

浏览器打开：**http://localhost:3000**

你将看到：
- **左侧**：完整章节目录（可折叠、可搜索）
- **右侧**：章节正文内容
- **顶部**：八大篇章快速导航
- **底部**：上一节 / 下一节翻页

### 部署到 GitHub Pages

推送 `main` 分支后，GitHub Actions 会自动将 `Python教程/` 发布到 `gh-pages` 分支。

**首次需手动开启**（只需一次）：

1. 打开 https://github.com/Drgonmancer/Leo_code/settings/pages
2. **Build and deployment** → **Source** 选 **Deploy from a branch**
3. **Branch** 选 `gh-pages`，目录选 `/ (root)`
4. 点击 **Save**

访问地址：https://drgonmancer.github.io/Leo_code/

---

---

## 📚 全书目录（已确认）

| 篇章 | 主题 | 入口 |
|:----:|------|------|
| **第一章** | Python 基础语法 | [进入 →](./C1/01-变量和数据类型.md) |
| **第二章** | Python 面向对象编程 | [进入 →](./C2/README.md) |
| **第三章** | Linux 命令 | [进入 →](./C3/README.md) |
| **第四章** | Web 服务器 | [进入 →](./C4/README.md) |
| **第五章** | 多任务编程 | [进入 →](./C5/README.md) |
| **第六章** | Web 前端开发基础 | [进入 →](./C6/README.md) |
| **第七章** | MySQL 数据库 | [进入 →](./C7/README.md) |
| **第八章** | Redis 数据库 | [进入 →](./C8/README.md) |

```mermaid
flowchart LR
    C1[第一章<br/>Python基础] --> C2[第二章<br/>面向对象]
    C2 --> C3[第三章<br/>Linux命令]
    C3 --> C4[第四章<br/>Web服务器]
    C4 --> C5[第五章<br/>多任务编程]
    C5 --> C6[第六章<br/>前端基础]
    C6 --> C7[第七章<br/>MySQL]
    C7 --> C8[第八章<br/>Redis]

    style C1 fill:#4CAF50,color:#fff
    style C8 fill:#F44336,color:#fff
```

---

## 第一章 · Python 基础语法

![Python基础](./assets/ch01-python-basics.png)

👉 [进入第一章目录](./C1/README.md)（共 16 节）

## 第二章 · Python 面向对象编程

![面向对象](./assets/ch02-oop.png)

👉 [进入第二章目录](./C2/README.md)（共 8 节）

## 第三章 · Linux 命令

![Linux命令](./assets/ch03-linux-commands.png)

| 节 | 标题 |
|:--:|------|
| 3.1 | [操作系统与 Linux 入门](./C3/01-操作系统与Linux入门.md) |
| 3.2 | [Linux 基础命令](./C3/02-Linux基础命令.md) |
| 3.3～3.7 | [更多章节](./C3/README.md) |

## 第四章 · Web 服务器

![Web服务器](./assets/ch04-web-server.png)

| 节 | 标题 |
|:--:|------|
| 4.1～4.3 | [全部章节](./C4/README.md) |

## 第五章 · 多任务编程

![多任务编程](./assets/ch05-multitasking.png)

| 节 | 标题 |
|:--:|------|
| 5.1～5.5 | [全部章节](./C5/README.md) |

## 第六章 · Web 前端开发基础

![Web前端](./assets/ch06-web-frontend.png)

| 节 | 标题 |
|:--:|------|
| 6.1～6.4 | [全部章节](./C6/README.md) |

## 第七章 · MySQL 数据库

![MySQL](./assets/ch07-mysql.png)

| 节 | 标题 |
|:--:|------|
| 7.1～7.7 | [全部章节](./C7/README.md) |

## 第八章 · Redis 数据库

![Redis](./assets/ch08-redis.png)

| 节 | 标题 |
|:--:|------|
| 8.1～8.4 | [全部章节](./C8/README.md) |

---

*源码仓库：[`Leo_code`](https://github.com/Drgonmancer/Leo_code)*
