#!/usr/bin/env python3
"""
Skill Marketplace - Enhanced Installer
增强安装器 - 支持 Git 和 ClawHub 两种安装方式

功能：
- 从 ClawHub 安装技能
- 从 GitHub 安装技能
- 自动检测最佳安装方式
- 依赖检查
- 安装后验证

Usage:
  python3 install.py <skill-name>
  python3 install.py <skill-name> --from-git
  python3 install.py <skill-name> --from-clawhub
  python3 install.py <skill-name> --github-url <url>
"""

import subprocess
import sys
import argparse
from pathlib import Path

SKILLS_DIR = Path.home() / ".openclaw" / "workspace" / "skills"

class Colors:
    BLUE = '\033[0;34m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    CYAN = '\033[0;36m'
    RED = '\033[0;31m'
    NC = '\033[0m'
    BOLD = '\033[1m'

def log_info(msg): print(f"{Colors.BLUE}[INFO]{Colors.NC} {msg}")
def log_success(msg): print(f"{Colors.GREEN}[✓]{Colors.NC} {msg}")
def log_warning(msg): print(f"{Colors.YELLOW}[⚠]{Colors.NC} {msg}")
def log_error(msg): print(f"{Colors.RED}[✗]{Colors.NC} {msg}")

def check_clawhub_installed() -> bool:
    """检查 ClawHub CLI 是否已安装"""
    try:
        result = subprocess.run(
            ['npx', 'clawhub', '--version'],
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.returncode == 0
    except Exception:
        return False

def check_git_installed() -> bool:
    """检查 Git 是否已安装"""
    try:
        result = subprocess.run(
            ['git', '--version'],
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.returncode == 0
    except Exception:
        return False

def install_from_clawhub(skill_name: str) -> bool:
    """从 ClawHub 安装"""
    log_info(f"从 ClawHub 安装技能：{skill_name}")
    
    try:
        result = subprocess.run(
            ['npx', 'clawhub', 'install', skill_name],
            cwd=str(SKILLS_DIR),
            timeout=120
        )
        
        if result.returncode == 0:
            log_success(f"已从 ClawHub 安装：{skill_name}")
            return True
        else:
            log_error(f"ClawHub 安装失败，退出码：{result.returncode}")
            return False
    except subprocess.TimeoutExpired:
        log_error("安装超时（超过 2 分钟）")
        return False
    except FileNotFoundError:
        log_error("未找到 npx 命令")
        return False
    except Exception as e:
        log_error(f"安装失败：{e}")
        return False

def install_from_github(skill_name: str, github_url: str = None) -> bool:
    """从 GitHub 安装"""
    
    # 如果没有提供 URL，尝试构建标准 URL
    if not github_url:
        if skill_name.startswith('openclaw-'):
            github_url = f"https://github.com/williamwg2025/{skill_name}.git"
        else:
            github_url = f"https://github.com/williamwg2025/openclaw-{skill_name}.git"
    
    log_info(f"从 GitHub 安装技能：{skill_name}")
    log_info(f"仓库地址：{github_url}")
    
    # 检查是否已存在
    target_dir = SKILLS_DIR / skill_name
    if target_dir.exists():
        log_warning(f"技能已存在：{target_dir}")
        response = input("是否覆盖？(y/N): ")
        if response.lower() != 'y':
            log_info("取消安装")
            return False
        else:
            import shutil
            shutil.rmtree(target_dir)
            log_info(f"已删除旧版本：{skill_name}")
    
    try:
        # Git clone
        result = subprocess.run(
            ['git', 'clone', github_url, str(target_dir)],
            timeout=120
        )
        
        if result.returncode != 0:
            log_error(f"Git clone 失败，退出码：{result.returncode}")
            return False
        
        log_success(f"已从 GitHub 克隆：{skill_name}")
        
        # 添加执行权限
        scripts_dir = target_dir / 'scripts'
        if scripts_dir.exists():
            for script in scripts_dir.glob('*.py'):
                script.chmod(0o755)
            log_info(f"已添加脚本执行权限")
        
        log_success(f"技能安装成功：{skill_name}")
        return True
        
    except subprocess.TimeoutExpired:
        log_error("Git clone 超时（超过 2 分钟）")
        return False
    except FileNotFoundError:
        log_error("未找到 git 命令")
        return False
    except Exception as e:
        log_error(f"安装失败：{e}")
        return False

def verify_installation(skill_name: str) -> bool:
    """验证安装"""
    target_dir = SKILLS_DIR / skill_name
    
    if not target_dir.exists():
        log_error(f"技能目录不存在：{target_dir}")
        return False
    
    # 检查 SKILL.md
    skill_md = target_dir / 'SKILL.md'
    if not skill_md.exists():
        log_warning(f"缺少 SKILL.md 文件")
        return False
    
    # 检查 scripts 目录
    scripts_dir = target_dir / 'scripts'
    if scripts_dir.exists():
        py_scripts = list(scripts_dir.glob('*.py'))
        if py_scripts:
            log_success(f"找到 {len(py_scripts)} 个脚本文件")
        else:
            log_warning("scripts 目录为空")
    else:
        log_warning("缺少 scripts 目录")
    
    log_success(f"安装验证通过：{skill_name}")
    return True

def get_github_url(skill_name: str) -> str:
    """获取 GitHub URL"""
    # 标准命名：openclaw-{skill-name}
    if skill_name.startswith('openclaw-'):
        return f"https://github.com/williamwg2025/{skill_name}.git"
    else:
        return f"https://github.com/williamwg2025/openclaw-{skill_name}.git"

def main():
    parser = argparse.ArgumentParser(description='技能安装器 - 支持 Git 和 ClawHub')
    parser.add_argument('skill', type=str, nargs='?', help='技能名称')
    parser.add_argument('--from-git', action='store_true', help='强制从 GitHub 安装')
    parser.add_argument('--from-clawhub', action='store_true', help='强制从 ClawHub 安装')
    parser.add_argument('--github-url', type=str, help='自定义 GitHub 仓库 URL')
    parser.add_argument('--verify', action='store_true', help='安装后验证')
    parser.add_argument('--list', action='store_true', help='列出已安装技能')
    
    args = parser.parse_args()
    
    # 列出已安装技能
    if args.list:
        if not SKILLS_DIR.exists():
            log_warning("技能目录不存在")
            return 0
        
        installed = []
        for item in SKILLS_DIR.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                skill_md = item / 'SKILL.md'
                if skill_md.exists():
                    installed.append(item.name)
        
        if installed:
            print(f"\n{Colors.BOLD}{Colors.CYAN}已安装的技能：{Colors.NC}\n")
            for skill in sorted(installed):
                print(f"  ✅ {skill}")
            print(f"\n共 {len(installed)} 个技能\n")
        else:
            log_warning("暂无技能")
        return 0
    
    skill_name = args.skill
    
    # 检查前置条件
    clawhub_ready = check_clawhub_installed()
    git_ready = check_git_installed()
    
    if not clawhub_ready and not git_ready:
        log_error("ClawHub CLI 和 Git 都未安装")
        print(f"\n{Colors.CYAN}请安装以下工具之一：{Colors.NC}")
        print(f"  1. Node.js + npm (用于 ClawHub CLI)")
        print(f"     https://nodejs.org/")
        print(f"  2. Git")
        print(f"     https://git-scm.com/")
        print()
        return 1
    
    # 确定安装方式
    if args.from_clawhub:
        install_method = 'clawhub'
    elif args.from_git or args.github_url:
        install_method = 'git'
    else:
        # 自动选择：优先 ClawHub，其次 Git
        if clawhub_ready:
            install_method = 'clawhub'
        else:
            install_method = 'git'
    
    log_info(f"使用安装方式：{install_method}")
    
    # 执行安装
    success = False
    
    if install_method == 'clawhub':
        success = install_from_clawhub(skill_name)
    else:
        github_url = args.github_url or get_github_url(skill_name)
        success = install_from_github(skill_name, github_url)
    
    # 验证安装
    if success and args.verify:
        verify_installation(skill_name)
    elif success:
        # 默认验证
        verify_installation(skill_name)
    
    # 显示下一步
    if success:
        print(f"\n{Colors.CYAN}下一步：{Colors.NC}")
        print(f"  1. 查看技能文档：cat {SKILLS_DIR}/{skill_name}/README.md")
        print(f"  2. 运行技能脚本：python3 {skill_name}/scripts/*.py")
        print(f"  3. 查看帮助：python3 {skill_name}/scripts/*.py --help")
        print()
    
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())
