# Skill Marketplace for OpenClaw

Discover, install, and manage OpenClaw skills from ClawHub.

**Version:** 2.0.0 - Now supports both ClawHub and GitHub installation!

[中文版本](README.md)

---

## ✨ Features

- 🛒 **Browse skills** - View 100+ skills
- 🎯 **Smart recommendations** - By scenario/industry/role
- 🔍 **Enhanced search** - Exact/fuzzy/Chinese keywords
- 📊 **Rankings** - Top 100 skills
- 📦 **One-click install** - Support both ClawHub and GitHub

---

## 🚀 Installation

```bash
cd ~/.openclaw/workspace/skills
# Skill installed at: ~/.openclaw/workspace/skills/skill-marketplace
chmod +x skill-marketplace/scripts/*.py
```

---

## 📦 Install Skills (v2.0.0)

**Two installation methods:**

```bash
# Method 1: From ClawHub (recommended)
python3 skill-marketplace/scripts/install.py auto-backup

# Method 2: From GitHub
python3 skill-marketplace/scripts/install.py auto-backup --from-git

# Method 3: Custom GitHub URL
python3 skill-marketplace/scripts/install.py my-skill --github-url "https://github.com/user/repo.git"

# Force ClawHub
python3 skill-marketplace/scripts/install.py auto-backup --from-clawhub

# Force Git
python3 skill-marketplace/scripts/install.py auto-backup --from-git

# Verify after install
python3 skill-marketplace/scripts/install.py auto-backup --verify

# List installed skills
python3 skill-marketplace/scripts/install.py --list
```

**Auto-selection:**
- Default: Prefer ClawHub (if available)
- Fallback: Switch to Git if ClawHub unavailable
- Use flags to force specific method

---

## 🔒 Security

### Code Source ✅
**All scripts included**
- ❌ No external cloning
- ❌ No downloading external code

### Network Access
- **sync-from-clawhub.py** - Fetch skill list from ClawHub API
- **install.py** - Download skills from GitHub or ClawHub
- **search-enhanced.py** - Local search, no network

### File Access
- **Read:** Skill directory, config files
- **Write:** Install skills to skills/ directory

---

**Author:** @williamwg2025  
**Version:** 2.0.0  
**License:** MIT-0
