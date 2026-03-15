# Git 远程仓库 Github

> 提示：Github网站作为远程代码仓库时的操作和本地代码仓库一样，只是仓库位置不同而已！

---

## 1. 准备阶段

### 获取Git源代码仓库
- Github网站：`https://github.com/`
- 准备自己的文件：`Desktop/Leo/`

### 克隆项目准备
- 准备经理的文件：`Desktop/manager/`
- 准备张三的文件：`Desktop/zhangsan/`

---

## 2. 经理的工作流程

> 立项：克隆远程仓库 → 配置身份信息 → 创建项目 → 推送项目到远程仓库

### 步骤1：克隆远程仓库

```bash
cd Desktop/manager/
git clone https://github.com/qruihua/info.git
```

### 步骤2：克隆远程仓库到本地

克隆成功后查看经理的文件

### 步骤3：配置经理身份信息

```bash
cd Desktop/manager/info/
git config user.name '经理'
git config user.email 'manager@itcast.com'
```

### 步骤4：创建项目（略）

### 步骤5：推送项目到远程仓库

```bash
# 将工作区添加到暂存区
git add .

# 暂存区提交到仓库区
git commit -m '立项'

# 推送到远程仓库
git push
```

---

## 3. 常用Git命令速查

| 命令 | 说明 |
|------|------|
| `git clone <url>` | 克隆远程仓库到本地 |
| `git config user.name <name>` | 配置用户名 |
| `git config user.email <email>` | 配置用户邮箱 |
| `git add .` | 将工作区所有文件添加到暂存区 |
| `git commit -m <message>` | 提交到本地仓库 |
| `git push` | 推送到远程仓库 |
