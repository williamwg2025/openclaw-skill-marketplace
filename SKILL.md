---
name: skill-marketplace
displayName: Skill Marketplace
version: 1.0.1
description: 技能市场，发现、安装、管理 OpenClaw 技能。支持评分、评论、排行榜。所有脚本已包含，无需外部克隆。
license: MIT-0
acceptLicenseTerms: true
tags: marketplace, skills, discovery, management
---

# Skill Marketplace - 技能市场

发现和安装优质 OpenClaw 技能。

---

## ✨ 功能

- 🛒 **技能发现** - 浏览/搜索技能
- ⭐ **评分评论** - 用户评分和评论
- 📊 **排行榜** - 下载量/评分排行
- 🔔 **更新提醒** - 技能更新通知
- 📦 **一键安装** - 自动下载安装

---

## 🚀 安装

```bash
# 技能已安装在：~/.openclaw/workspace/skills/skill-marketplace
```

---

## 📖 使用

### 浏览技能

```bash
python3 skill-marketplace/scripts/browse.py
```

### 搜索技能

```bash
python3 skill-marketplace/scripts/search.py "backup"
```

### 安装技能

```bash
python3 skill-marketplace/scripts/install.py model-switch
```

---

**作者：** @williamwg2025  
**版本：** 1.0.0

---

## 🔒 安全说明

### 代码来源 ✅
**所有脚本已包含在包内：**
- `browse.py` - 浏览技能
- `search.py` - 搜索技能
- `install.py` - 安装技能（调用 npx clawhub install）
- `rankings.py` - 排行榜

**无外部依赖：**
- ❌ 不克隆外部仓库
- ❌ 不下载外部代码
- ❌ 不执行远程脚本

### 网络访问
**当前脚本不需要联网：**
- 所有操作在本地执行
- install.py 调用 `npx clawhub install` 会联网下载技能（这是预期行为）

### 文件访问
**读取：**
- 本地技能列表（可选配置文件）
- 用户输入的技能名称

**写入：**
- 当前版本不自动写入文件
- install.py 会安装技能到 `~/.openclaw/workspace/skills/`

### 系统操作
- **install.py：** 调用 `npx clawhub install <skill>` 安装技能
- **影响：** 会在 skills/ 目录创建新文件夹

### 数据安全
- **本地处理：** 所有操作在本地执行
- **不上传：** 不发送数据到外部服务器
- **安装技能：** 通过 ClawHub 官方 Registry（可信来源）

### 使用建议
1. **检查脚本：** 所有脚本都在 `scripts/` 目录，可自行审查
2. **测试运行：** 先运行 browse.py 或 search.py 测试行为
3. **安装技能：** install.py 会调用 ClawHub，确保信任来源
4. **权限控制：** 确保 skills/ 目录权限正确

---

**作者：** @williamwg2025  
**版本：** 1.0.1  
**许可证：** MIT-0
