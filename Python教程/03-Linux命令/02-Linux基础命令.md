# 3.2 Linux 基础命令

<div align="center">

**第三章 · Linux 命令 · 第 2 节**

*预计学习时间：1 小时 · 难度：⭐⭐*

</div>

![常用 Linux 命令](assets/ch03-linux-commands.png)

---

## 📖 本节导读

掌握文件和目录的**查看、切换、创建、复制、移动、删除**——日常开发 80% 的终端操作都在这里。

---

## 1. 命令格式

```
command [-options] [parameter]
```

| 部分 | 含义 | 示例 |
|------|------|------|
| command | 命令名 | `ls` |
| -options | 选项（可选） | `-l`、`-a` |
| parameter | 参数（可选） | 文件名、目录名 |

> 🟦 **技巧**：按 `Tab` 自动补全；连按两次 `Tab` 列出所有可选项。

---

## 2. 查看目录

| 命令 | 作用 |
|------|------|
| `ls` | 列出当前目录文件 |
| `ls -l` | 详细信息（权限、大小、时间） |
| `ls -a` | 包含隐藏文件（以 `.` 开头） |
| `tree` | 树状显示目录结构 |
| `pwd` | 显示当前路径 |
| `clear` | 清屏 |

```bash
ls
ls -la
pwd
```

> 📸 **截图位**：`ls -la` 输出文件列表的终端界面

---

## 3. 切换目录 cd

| 命令 | 作用 |
|------|------|
| `cd 目录名` | 进入指定目录 |
| `cd ~` | 回到家目录 |
| `cd ..` | 上一级 |
| `cd -` | 回到上一次目录 |
| `cd` | 等价于 `cd ~` |

### 绝对路径 vs 相对路径

```
绝对路径：从 / 开始     →  /home/python/Desktop
相对路径：从当前目录算   →  ../Downloads
```

```bash
cd ~/Desktop
cd ..
cd -
```

> ⚠️ **避坑**：`cd` 的目标目录必须存在，否则报错。

---

## 4. 创建与删除

| 命令 | 作用 |
|------|------|
| `touch 文件名` | 创建空文件 |
| `mkdir 目录名` | 创建目录 |
| `mkdir -p a/b/c` | 递归创建多级目录 |
| `rm 文件名` | 删除文件 |
| `rm -r 目录名` | 递归删除目录 |
| `rmdir 空目录` | 删除空目录 |

```bash
mkdir my_project
touch my_project/main.py
ls my_project
```

**运行效果：**

```
main.py
```

> 🟥 **危险警告**：`rm -rf` 会永久删除，无法恢复！生产环境慎用。

---

## 5. 复制与移动

| 命令 | 作用 |
|------|------|
| `cp 源 目标` | 复制文件 |
| `cp -r 源目录 目标` | 复制目录 |
| `mv 源 目标` | 移动或重命名 |

```bash
cp main.py main_backup.py
mv main_backup.py backup/main.py
```

---

## 6. 查看文件内容

| 命令 | 作用 |
|------|------|
| `cat 文件名` | 显示全部内容 |
| `more 文件名` | 分页查看 |
| `head -n 5 文件` | 前 5 行 |
| `tail -n 10 文件` | 后 10 行 |
| `tail -f 日志` | 实时跟踪日志（部署常用！） |

---

## 7. 综合练习

请你依次完成：

1. 在家目录创建 `python_learning` 文件夹
2. 在其中创建 `hello.py`
3. 用 `cat` 或编辑器写入 `print("Hello Linux")`
4. 用 `python3 hello.py` 运行

> 📸 **截图位**：完成练习后的目录结构和运行结果

---

## 8. 本节小结

| 类别 | 核心命令 |
|------|---------|
| 查看 | ls, pwd, tree, cat, tail |
| 切换 | cd, cd ~, cd .. |
| 创建 | touch, mkdir |
| 删除 | rm, rm -r |
| 复制移动 | cp, mv |

---

| ← 上一节 | [第三章目录](./README.md) | 下一节 → |
|---------|--------------------------|---------|
| [3.1 入门](./01-操作系统与Linux入门.md) | | [3.3 高级命令](./03-Linux高级命令.md) |

*源码：[`Linux命令/2.Linux基础命令`](https://github.com/Drgonmancer/Leo_code/tree/main/Linux命令/2.Linux基础命令)*
