# Leo_code · main 分支

> 你当前在 **`main` 分支** — 这是源码与学习笔记的主分支。  
> 在线文档由 `gh-pages` 分支自动发布，请勿直接修改 `gh-pages`。

## 快速开始

| 你想做什么 | 去哪里 |
|-----------|--------|
| 在线阅读教程（左侧目录导航） | https://drgonmancer.github.io/Leo_code/ |
| 本地预览文档站 | 见下方「本地预览」 |
| 修改教程内容 | 编辑 `Python教程/` 后推送到 `main` |
| 查看原始笔记与代码 | 浏览下方各章节目录 |

## 本地预览

```powershell
Set-Location "Python教程"
python -m http.server 3000
```

浏览器打开 http://localhost:3000

## main 分支目录

```
main/
├── Python教程/          ← 文档站源码（Docsify，推 main 后自动部署）
├── Python基础语法/      ← 原始笔记与练习代码
├── Python面向对象编程/
├── Linux命令/
├── web服务器/
├── 多任务编程/
├── web前端开发基础/
├── MySQL数据库/
├── Redis数据库/
├── 项目部署/
├── Git/
└── .github/workflows/   ← 推送 main 时自动发布到 gh-pages
```

## 分支说明

| 分支 | 用途 |
|------|------|
| `main` | 源码主分支，在此编辑与提交 |
| `gh-pages` | 由 GitHub Actions 自动生成，承载在线文档，**不要手动修改** |

## 更新在线文档

```powershell
git add Python教程/
git commit -m "更新教程内容"
git push origin main
```

推送后 Actions 会自动将 `Python教程/` 同步到 `gh-pages`，约 1～2 分钟生效。
