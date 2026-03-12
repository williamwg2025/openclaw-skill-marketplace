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
cd ~/.openclaw/workspace/skills
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

### 查看排行榜

```bash
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

- **本地执行：** 所有脚本在本地运行，不联网
- **权限范围：** 仅需读取 ~/.openclaw/ 目录
- **无外部依赖：** 不克隆外部仓库，所有代码已包含
- **数据安全：** 不上传任何数据到外部服务器

---

**作者：** @williamwg2025  
**版本：** 1.0.1  
**许可证：** MIT-0
