#!/usr/bin/env python3
"""
随机抽题（盲选，避免预先知道专题/套路）。

用法
----
    python pick.py                  随机 1 道未做的 Hot 100
    python pick.py 5                随机 5 道未做的 Hot 100
    python pick.py star             仅 ★ 题，未做
    python pick.py --done           已做的 Hot 100（用于复盘）
    python pick.py --any            未做+已做都行（默认是仅未做）
    python pick.py --all            池子改成全部 169 题（含 _labuladong_ext/）
    python pick.py --all --any 3    3 道随机，全池子，全状态
    python pick.py --status         只看进度统计，不抽题

参数可任意组合，比如 `python pick.py --all star --done 3` =
    全池子里随机 3 道已做的 ★ 题。

完成度判定（自动，无状态文件）
- 用 AST 解析题目文件，看 class 里的方法体是不是还只剩 `pass`。
- 你写代码替换掉 `# TODO: ... pass` 后，下次运行就自动认你做完了。
- 想"重做"某题：把方法体清回 `pass`，或者直接 git restore 原模板。

故意只输出"题号 + 题名 + 文件路径"，不打印 HIGH_FREQ.md 里的细分类
（哈希/双指针/DP...）。要做到全盲，去 leetcode.cn 搜题号即可。
"""
import ast
import random
import re
import sys
from pathlib import Path
from typing import List, Optional, Tuple


ROOT = Path(__file__).parent
HF = ROOT / "HIGH_FREQ.md"


# ----- 题库加载 -------------------------------------------------------------
def _slice_section(text: str, header_re: str, end_re: Optional[str]) -> str:
    """截取 markdown 中以 header_re 开头到 end_re（或文末）之前的内容。"""
    if end_re:
        m = re.search(rf"({header_re}.*?)(?={end_re}|\Z)", text, re.DOTALL)
    else:
        m = re.search(rf"({header_re}.*)", text, re.DOTALL)
    return m.group(1) if m else ""


def _parse_problems(section: str) -> List[Tuple[int, str, str, bool]]:
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
    """从 HIGH_FREQ.md 加载题库。include_ext=True 时含 labuladong 扩展。"""
    if not HF.exists():
        raise SystemExit(f"找不到 HIGH_FREQ.md: {HF}")
    text = HF.read_text(encoding="utf-8")
    hot = _slice_section(text, r"##\s+🔥\s*Hot 100", r"##\s+📚")
    items = _parse_problems(hot)
    if include_ext:
        ext = _slice_section(text, r"##\s+📚", None)
        items += _parse_problems(ext)
    # 去重（按题号；扩展区不会和 Hot 100 题号冲突，这里仅保险）
    seen, unique = set(), []
    for it in items:
        if it[0] not in seen:
            seen.add(it[0])
            unique.append(it)
    return unique


# ----- 完成度检测 -----------------------------------------------------------
def is_undone(file_path: Path) -> bool:
    """
    通过 AST 检测：任意一个函数/方法体仍是「单独一个 pass」就视为未做。
    跳过 docstring；考虑所有 class（Solution / LRUCache / Codec 等）。
    """
    if not file_path.exists():
        return True
    try:
        content = file_path.read_text(encoding="utf-8")
        tree = ast.parse(content)
    except (SyntaxError, UnicodeDecodeError):
        return True

    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        body = node.body
        # 跳过 docstring
        if (body
                and isinstance(body[0], ast.Expr)
                and isinstance(body[0].value, ast.Constant)
                and isinstance(body[0].value.value, str)):
            body = body[1:]
        if len(body) == 1 and isinstance(body[0], ast.Pass):
            return True
    return False


# ----- 进度统计 -------------------------------------------------------------
def show_status() -> None:
    def stats(items):
        done = sum(1 for it in items if not is_undone(ROOT / it[2]))
        return done, len(items)

    hot = load_problems(False)
    full = load_problems(True)
    h_done, h_tot = stats(hot)
    f_done, f_tot = stats(full)
    print(f"Hot 100        : {h_done:>3} done / {h_tot - h_done:>3} undone   ({h_done * 100 // max(h_tot, 1)}%)")
    print(f"全部 {f_tot} 题  : {f_done:>3} done / {f_tot - f_done:>3} undone   ({f_done * 100 // max(f_tot, 1)}%)")


# ----- CLI ----------------------------------------------------------------
def parse_args(argv):
    star_only = False
    n = 1
    status = "undone"      # undone | done | any
    include_ext = False
    show_only = False
    for a in argv:
        if a == "star":
            star_only = True
        elif a == "--done":
            status = "done"
        elif a == "--any":
            status = "any"
        elif a == "--undone":
            status = "undone"
        elif a in ("--all", "--ext"):
            include_ext = True
        elif a == "--status":
            show_only = True
        elif a in ("-h", "--help"):
            print(__doc__)
            sys.exit(0)
        else:
            try:
                n = max(1, int(a))
            except ValueError:
                pass
    return star_only, n, status, include_ext, show_only


def main():
    star_only, n, status, include_ext, show_only = parse_args(sys.argv[1:])

    if show_only:
        show_status()
        return

    items = load_problems(include_ext)
    if star_only:
        items = [it for it in items if it[3]]
    if status == "undone":
        items = [it for it in items if is_undone(ROOT / it[2])]
    elif status == "done":
        items = [it for it in items if not is_undone(ROOT / it[2])]

    if not items:
        if status == "undone":
            print("✨ 这个池子里全做完了。试 --done 复盘，--any 随便抽，或 --all 把扩展题也算进来。")
        elif status == "done":
            print("还没有已做的题。先随便抽一道做：python pick.py")
        else:
            print("候选为空。")
        sys.exit(0)

    picks = random.sample(items, min(n, len(items)))
    pool_label = f"全部 {len(load_problems(True))} 题" if include_ext else "Hot 100"
    status_label = {"undone": "未做", "done": "已做", "any": "全状态"}[status]
    star_label = "★ " if star_only else ""
    print(f"——— 从 {pool_label} 的 {star_label}{status_label}（{len(items)} 题候选）抽 {len(picks)} 道 ———")
    for num, name, path, star in picks:
        marker = " ★" if star else ""
        print(f"  #{num}{marker}  {name}")
        print(f"        → {path}")


if __name__ == "__main__":
    main()
