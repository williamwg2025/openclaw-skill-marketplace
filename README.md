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
