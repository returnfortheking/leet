#!/usr/bin/env python3
"""
随机抽题 + 完成度跟踪。

抽题用法
--------
    python pick.py                  随机 1 道未做 Hot 100（untouched + wip）
    python pick.py 5                5 道
    python pick.py star             仅 ★，未做
    python pick.py star 3           仅 ★，3 道，未做

    python pick.py --untouched      仅"原版模板没动过"
    python pick.py --wip            仅"动过但跑不通"
    python pick.py --done           仅"测试已通过"（用于复盘）
    python pick.py --any            任意状态

    python pick.py --all            池子改为全部 169 题（含 _labuladong_ext/）
    python pick.py --all --done 5   全池子已通过的题里抽 5 道

状态管理
--------
    python pick.py --status         看进度统计
    python pick.py --sync           强制重新跑所有"动过"的文件刷新缓存
    python pick.py mark 1 5 14      手动标 done（即使测试不过）
    python pick.py wip 1 5          手动标 wip
    python pick.py reset 1 5        清除手动标记，恢复自动检测

完成度判定
----------
1. 文件含 `# TODO: 在这里写你的解法` 且方法体仍是 pass → 标记 untouched（不跑测试，秒判）
2. 否则 subprocess 跑 `python <文件>` 15s 超时；
   exit 0 → done；非 0 / 超时 / 异常 → wip
3. 结果缓存到 .pick_state.json（按 mtime 失效；本目录下 .gitignore 已忽略）
4. 手动标记（mark / wip）会盖过自动；reset 后才重新自动跑

故意只输出"题号 + 题名 + 文件路径"，不打印 HIGH_FREQ.md 里的细分类。
"""
import ast
import json
import random
import re
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# 强制 stdout/stderr 用 UTF-8，避免 Windows 默认 GBK 控制台遇到 emoji 崩溃
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except (AttributeError, OSError):
    pass


ROOT = Path(__file__).parent
HF = ROOT / "HIGH_FREQ.md"
CACHE_PATH = ROOT / ".pick_state.json"
TEST_TIMEOUT = 15
TODO_MARKER = "# TODO: 在这里写你的解法"


# ============================================================================
# 题库加载
# ============================================================================
def _slice(text: str, header_re: str, end_re: Optional[str]) -> str:
    if end_re:
        m = re.search(rf"({header_re}.*?)(?={end_re}|\Z)", text, re.DOTALL)
    else:
        m = re.search(rf"({header_re}.*)", text, re.DOTALL)
    return m.group(1) if m else ""


def _parse(section: str) -> List[Tuple[int, str, str, bool]]:
    out = []
    pat = re.compile(r"- #(\d+)\s+([^→]+?)\s*→\s*\[[^\]]+\]\(([^)]+)\)")
    for line in section.splitlines():
        m = pat.match(line.strip())
        if not m:
            continue
        num = int(m.group(1))
        name = m.group(2).strip()
        star = "★" in name
        name = name.replace("★", "").strip()
        path = m.group(3).strip()
        out.append((num, name, path, star))
    return out


def load_problems(include_ext: bool) -> List[Tuple[int, str, str, bool]]:
    if not HF.exists():
        raise SystemExit(f"找不到 HIGH_FREQ.md: {HF}")
    text = HF.read_text(encoding="utf-8")
    items = _parse(_slice(text, r"##\s+🔥\s*Hot 100", r"##\s+📚"))
    if include_ext:
        items += _parse(_slice(text, r"##\s+📚", None))
    seen, unique = set(), []
    for it in items:
        if it[0] not in seen:
            seen.add(it[0])
            unique.append(it)
    return unique


# ============================================================================
# 状态缓存
# ============================================================================
def load_cache() -> dict:
    if not CACHE_PATH.exists():
        return {"version": 1, "files": {}}
    try:
        return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    except Exception:
        return {"version": 1, "files": {}}


def save_cache(cache: dict) -> None:
    CACHE_PATH.write_text(
        json.dumps(cache, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


# ============================================================================
# 完成度自动检测
# ============================================================================
def _has_pass_only_method(content: str) -> bool:
    """Return True if any function/method body is just `pass`."""
    try:
        tree = ast.parse(content)
    except SyntaxError:
        return False  # syntax error 让测试去判
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        body = node.body
        if (body and isinstance(body[0], ast.Expr)
                and isinstance(body[0].value, ast.Constant)
                and isinstance(body[0].value.value, str)):
            body = body[1:]
        if len(body) == 1 and isinstance(body[0], ast.Pass):
            return True
    return False


def _run_test(file_path: Path) -> bool:
    """跑一遍测试，exit 0 = 通过。"""
    try:
        result = subprocess.run(
            [sys.executable, str(file_path)],
            capture_output=True,
            timeout=TEST_TIMEOUT,
            cwd=str(ROOT),
        )
        return result.returncode == 0
    except (subprocess.TimeoutExpired, OSError):
        return False


def detect_status(file_path: Path) -> str:
    """untouched | wip | done"""
    if not file_path.exists():
        return "untouched"
    content = file_path.read_text(encoding="utf-8")
    if TODO_MARKER in content and _has_pass_only_method(content):
        return "untouched"
    return "done" if _run_test(file_path) else "wip"


def get_status(rel_path: str, cache: dict, force: bool = False) -> str:
    """带缓存的状态查询。"""
    file_path = ROOT / rel_path
    files = cache.setdefault("files", {})
    entry = files.get(rel_path)

    if not file_path.exists():
        files.pop(rel_path, None)
        return "untouched"

    # 手动标记永远赢（除非显式 reset 或 force=sync）
    if entry and entry.get("manual") and not force:
        return entry["status"]

    mtime = file_path.stat().st_mtime
    if (not force and entry
            and not entry.get("manual")
            and abs(entry.get("mtime", 0) - mtime) < 0.001):
        return entry["status"]

    status = detect_status(file_path)
    files[rel_path] = {"status": status, "mtime": mtime, "manual": False}
    return status


# ============================================================================
# 命令分发
# ============================================================================
def cmd_show_status(cache: dict) -> None:
    items_hot = load_problems(False)
    items_all = load_problems(True)

    def stats(items):
        out = {"untouched": 0, "wip": 0, "done": 0}
        for it in items:
            out[get_status(it[2], cache)] += 1
        return out

    h = stats(items_hot)
    a = stats(items_all)
    save_cache(cache)

    h_total = sum(h.values())
    a_total = sum(a.values())

    def line(label, total, c):
        return (f"  {label:<10} done {c['done']:>3}  /  "
                f"wip {c['wip']:>3}  /  untouched {c['untouched']:>3}   "
                f"({c['done']*100//max(total,1)}% 通过)")

    print(line(f"Hot 100 ({h_total})", h_total, h))
    print(line(f"全部 ({a_total})", a_total, a))


def cmd_sync(cache: dict) -> None:
    """重新跑所有「动过」的文件（untouched 跳过，因为它们一定 untouched）。"""
    items = load_problems(True)
    refreshed = 0
    for num, name, path, star in items:
        rel = path
        # force 不影响 manual
        before = cache.get("files", {}).get(rel, {})
        if before.get("manual"):
            continue
        get_status(rel, cache, force=True)
        refreshed += 1
        if refreshed % 20 == 0:
            print(f"  ...checked {refreshed}")
    save_cache(cache)
    print(f"sync 完成，重检 {refreshed} 题")
    cmd_show_status(cache)


def cmd_mark(action: str, nums: List[int], cache: dict) -> None:
    """action: 'done' | 'wip' | 'reset'"""
    items = load_problems(True)
    by_num = {it[0]: it[2] for it in items}
    files = cache.setdefault("files", {})
    affected = []
    missed = []
    for num in nums:
        if num not in by_num:
            missed.append(num)
            continue
        rel = by_num[num]
        path = ROOT / rel
        if action == "reset":
            files.pop(rel, None)
        else:
            files[rel] = {
                "status": action,
                "mtime": path.stat().st_mtime if path.exists() else 0.0,
                "manual": True,
            }
        affected.append(num)
    save_cache(cache)
    if affected:
        print(f"[{action}] 标记 {len(affected)} 题: {affected}")
    if missed:
        print(f"  ! 不在题库: {missed}")


def cmd_pick(opts: dict, cache: dict) -> None:
    items = load_problems(opts["include_ext"])
    if opts["star_only"]:
        items = [it for it in items if it[3]]

    statuses = {it[2]: get_status(it[2], cache) for it in items}
    save_cache(cache)

    sf = opts["status"]
    if sf == "undone":
        items = [it for it in items if statuses[it[2]] in ("untouched", "wip")]
    elif sf in ("done", "wip", "untouched"):
        items = [it for it in items if statuses[it[2]] == sf]
    # any: 不过滤

    if not items:
        suggest = {
            "undone": "试 --done 复盘，--any 全状态，或 --all 把扩展加进来",
            "done": "还没有已通过的题。先 python pick.py 抽一道做",
            "wip": "没有进行中的题。试 --untouched 抽全新的",
            "untouched": "全部都摸过了 🎉",
            "any": "空池",
        }[sf]
        print(f"候选为空。{suggest}")
        return

    n = opts["n"]
    picks = random.sample(items, min(n, len(items)))
    pool_label = f"全部 {len(load_problems(True))} 题" if opts["include_ext"] else "Hot 100"
    sf_label = {"undone": "未做", "done": "已通过", "wip": "进行中",
                "untouched": "全新", "any": "全状态"}[sf]
    star_label = "★ " if opts["star_only"] else ""

    print(f"——— 从 {pool_label} 的 {star_label}{sf_label}（{len(items)} 题候选）抽 {len(picks)} 道 ———")
    for num, name, path, star in picks:
        s = statuses[path]
        icon = {"untouched": "⚪", "wip": "🚧", "done": "✅"}[s]
        marker = " ★" if star else ""
        print(f"  {icon} #{num}{marker}  {name}")
        print(f"        → {path}")


# ============================================================================
# CLI 解析
# ============================================================================
def parse_args(argv: List[str]) -> dict:
    if argv and argv[0] in ("mark", "wip", "reset"):
        action = argv[0]
        nums = []
        for a in argv[1:]:
            try:
                nums.append(int(a))
            except ValueError:
                pass
        return {"cmd": action, "nums": nums}

    star_only = False
    n = 1
    status = "undone"
    include_ext = False
    show_only = False
    sync = False
    for a in argv:
        if a == "star":
            star_only = True
        elif a == "--done":
            status = "done"
        elif a == "--wip":
            status = "wip"
        elif a == "--untouched":
            status = "untouched"
        elif a == "--any":
            status = "any"
        elif a == "--undone":
            status = "undone"
        elif a in ("--all", "--ext"):
            include_ext = True
        elif a == "--status":
            show_only = True
        elif a == "--sync":
            sync = True
        elif a in ("-h", "--help"):
            print(__doc__)
            sys.exit(0)
        else:
            try:
                n = max(1, int(a))
            except ValueError:
                pass
    return {
        "cmd": "pick",
        "star_only": star_only,
        "n": n,
        "status": status,
        "include_ext": include_ext,
        "show_only": show_only,
        "sync": sync,
    }


def main():
    cache = load_cache()
    opts = parse_args(sys.argv[1:])

    if opts["cmd"] in ("done_alias", "mark"):
        cmd_mark("done", opts["nums"], cache)
    elif opts["cmd"] == "wip":
        cmd_mark("wip", opts["nums"], cache)
    elif opts["cmd"] == "reset":
        cmd_mark("reset", opts["nums"], cache)
    elif opts["cmd"] == "pick":
        if opts["sync"]:
            cmd_sync(cache)
            return
        if opts["show_only"]:
            cmd_show_status(cache)
            return
        cmd_pick(opts, cache)


if __name__ == "__main__":
    main()
