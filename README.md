# Skill Marketplace - 技能市场

发现和安装优质 OpenClaw 技能。

---

## ✨ 功能

### 🎯 智能推荐（v1.1.0 新增）
- **场景推荐** - 根据使用场景推荐技能组合（开发编程、内容创作等）
- **行业推荐** - 根据行业领域推荐（互联网、金融、教育等）
- **身份推荐** - 根据职业身份推荐（开发者、设计师、学生等）
- **基础必装** - 所有用户都应该安装的基础技能
- **排行榜** - Top 100 热门技能排行

### 🔍 技能发现
- 🛒 **浏览技能** - 查看所有可用技能
- 🔎 **搜索技能** - 按名称/标签搜索
- ⭐ **评分评论** - 用户评分和评论
- 📊 **排行榜** - 下载量/评分排行
- 🔔 **更新提醒** - 技能更新通知
- 📦 **一键安装** - 自动下载安装

---

## 🚀 安装

```bash
cd ~/.openclaw/workspace/skills
# 技能已安装在：~/.openclaw/workspace/skills/skill-marketplace
```

---

## 📖 使用

### 🎯 智能推荐（v1.1.0 新增）

```bash
# 根据场景推荐
python3 skill-marketplace/scripts/recommend.py --scenario "开发编程"
# 输出：推荐技能组合 + 安装命令

# 根据行业推荐
python3 skill-marketplace/scripts/recommend.py --industry "互联网"

# 根据身份推荐
python3 skill-marketplace/scripts/recommend.py --role "开发者"

# 查看基础必装技能
python3 skill-marketplace/scripts/recommend.py --basic
# 输出：5 个基础必装技能（auto-backup, model-switch, memory-enhancer 等）

# 查看排行榜 Top 10
python3 skill-marketplace/scripts/recommend.py --top 10
# 输出：评分最高的 10 个技能

# 列出所有可用选项
python3 skill-marketplace/scripts/recommend.py --list-scenarios
python3 skill-marketplace/scripts/recommend.py --list-industries
python3 skill-marketplace/scripts/recommend.py --list-roles
```

### 🔍 技能发现

```bash
# 浏览技能
python3 skill-marketplace/scripts/browse.py

# 搜索技能
python3 skill-marketplace/scripts/search.py "backup"

# 安装技能
python3 skill-marketplace/scripts/install.py model-switch

# 查看排行榜
python3 skill-marketplace/scripts/rankings.py
```

---

## 📁 目录结构

```
skill-marketplace/
├── SKILL.md
├── README.md
├── config/
│   └── marketplace.json
└── scripts/
    ├── browse.py
    ├── search.py
    ├── install.py
    └── rankings.py
```

---

**作者：** @williamwg2025  
**版本：** 1.0.0  
**许可证：** MIT-0

---

## 🔒 安全说明

### 代码来源 ✅
**所有脚本已包含：** browse.py, search.py, install.py, rankings.py
- ❌ 不克隆外部仓库
- ❌ 不下载外部代码

### 网络访问
- **脚本本身不联网**
- **install.py 调用 ClawHub** - 下载技能时联网（预期行为）

### 文件访问
- **读取：** 本地技能列表（可选）
- **写入：** install.py 安装技能到 skills/ 目录

### 系统操作
- **install.py：** 调用 `npx clawhub install <skill>`

### 使用建议
1. 检查 scripts/ 目录脚本
2. 先测试 browse.py 或 search.py
3. 安装技能时确保信任来源

---

**作者：** @williamwg2025  
**版本：** 1.0.1  
**许可证：** MIT-0
