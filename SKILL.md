---
name: openclaw-skill-marketplace
displayName: OpenClaw Skill Marketplace - 技能市场
version: 2.0.0
description: |
  OpenClaw 技能市场 - 从 ClawHub 同步 100+ 技能，智能推荐最适合你的技能组合。
  支持场景推荐（开发/创作/办公）、行业推荐（互联网/金融/教育）、身份推荐（开发者/设计师/学生）。
  增强搜索：精确搜索、模糊搜索、中文关键词映射（如"备份"搜到"backup"）。
  增强安装：支持从 ClawHub 和 GitHub 两种方式安装技能。
  浏览、搜索、一键安装、评分评论、排行榜 Top100。
  关键词：openclaw, marketplace, skills, recommendation, clawhub, discovery, search, chinese, install, git
license: MIT-0
acceptLicenseTerms: true
tags:
  - openclaw
  - marketplace
  - skills
  - discovery
  - management
  - recommendation
  - ai
  - clawhub
  - sync
  - installer
  - search
  - chinese-keywords
  - enhanced-search
  - git-install
---

# Skill Marketplace - 技能市场

发现和安装优质 OpenClaw 技能。

---

## ✨ 功能

- 🛒 **技能发现** - 浏览/搜索技能
- ⭐ **评分评论** - 用户评分和评论
- 📊 **排行榜** - 下载量/评分排行
- 🔔 **更新提醒** - 技能更新通知
- 📦 **一键安装** - 支持 ClawHub 和 GitHub 两种方式
- 🎯 **智能推荐** - 场景/行业/身份推荐
- 🔍 **增强搜索** - 精确/模糊/中文关键词

---

## 🚀 安装

```bash
# 技能已安装在：~/.openclaw/workspace/skills/skill-marketplace
```

---

## 📖 使用

### 📦 安装技能（v2.0.0 新增）

**支持两种安装方式：**

```bash
# 方式 1：从 ClawHub 安装（推荐）
python3 skill-marketplace/scripts/install.py auto-backup

# 方式 2：从 GitHub 安装
python3 skill-marketplace/scripts/install.py auto-backup --from-git

# 方式 3：指定 GitHub URL
python3 skill-marketplace/scripts/install.py my-skill --github-url "https://github.com/user/repo.git"

# 强制使用 ClawHub
python3 skill-marketplace/scripts/install.py auto-backup --from-clawhub

# 强制使用 Git
python3 skill-marketplace/scripts/install.py auto-backup --from-git

# 安装后验证
python3 skill-marketplace/scripts/install.py auto-backup --verify

# 列出已安装技能
python3 skill-marketplace/scripts/install.py --list
```

**自动选择策略：**
- 默认优先使用 ClawHub（如果已安装）
- 如果 ClawHub 不可用，自动切换到 Git
- 可通过参数强制指定安装方式

**安装流程：**
```
1. 检查 ClawHub CLI 和 Git 是否安装
2. 自动选择最佳安装方式
3. 下载技能文件
4. 添加执行权限
5. 验证安装
6. 显示下一步指引
```

---

### 🔄 从 ClawHub 同步技能（v1.2.0）

```bash
# 同步 ClawHub 所有技能（默认 100 个）
python3 skill-marketplace/scripts/sync-from-clawhub.py

# 同步更多技能
python3 skill-marketplace/scripts/sync-from-clawhub.py --limit 500
```

---

### 🎯 智能推荐（v1.1.0）

```bash
# 根据场景推荐
python3 skill-marketplace/scripts/recommend.py --scenario "开发编程"

# 根据行业推荐
python3 skill-marketplace/scripts/recommend.py --industry "互联网"

# 根据身份推荐
python3 skill-marketplace/scripts/recommend.py --role "开发者"

# 查看基础必装技能
python3 skill-marketplace/scripts/recommend.py --basic

# 查看排行榜 Top 10
python3 skill-marketplace/scripts/recommend.py --top 10
```

---

### 🔍 增强搜索（v1.3.0）

```bash
# 智能搜索
python3 skill-marketplace/scripts/search-enhanced.py "backup"

# 精确搜索
python3 skill-marketplace/scripts/search-enhanced.py "openclaw-auto-backup" --exact

# 模糊搜索（支持中文）
python3 skill-marketplace/scripts/search-enhanced.py "备份" --fuzzy

# 在 ClawHub 中搜索
python3 skill-marketplace/scripts/search-enhanced.py "backup" --from-clawhub
```

---

## 🔒 安全说明

### 代码来源 ✅
**所有脚本已包含在包内**
- ❌ 不克隆外部仓库（技能本身）
- ❌ 不下载外部代码

### 网络访问
- **sync-from-clawhub.py** - 从 ClawHub API 获取技能列表
- **install.py** - 从 GitHub 或 ClawHub 下载技能
- **search-enhanced.py** - 本地搜索，不联网

### 文件访问
- **读取：** 技能目录、配置文件
- **写入：** 安装技能到 skills/ 目录

### 数据安全
- **本地处理** - 搜索和推荐在本地执行
- **不上传** - 不发送用户数据到外部

---

**作者：** @williamwg2025  
**版本：** 2.0.0  
**许可证：** MIT-0
