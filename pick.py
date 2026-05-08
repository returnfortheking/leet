#!/usr/bin/env python3
"""
随机抽 Hot 100 题（盲选，避免预先知道专题/套路）。

用法
----
    python pick.py            随机 1 道
    python pick.py 3          随机 3 道
    python pick.py star       仅从 ★ 题里抽（默认 1 道）
    python pick.py star 5     仅 ★，5 道

故意只输出"题号 + 题名 + 文件路径"，不打印 HIGH_FREQ.md 里的细分类
（哈希/双指针/DP...），让你打开文件前对解法保持一无所知。

注：路径里的 16 专题目录名（如 01_array_string）是粗粒度的——
跟 LeetCode 上看到题目分类的颗粒度差不多——不算剧透。如果连这层
都想盲，去 leetcode.cn 直接搜题号做，最后回填到我们的模板里。
"""
import random
import re
import sys
from pathlib import Path


HF = Path(__file__).parent / "HIGH_FREQ.md"


def load_hot100():
    """从 HIGH_FREQ.md 解析 Hot 100 区的题目。"""
    if not HF.exists():
        raise SystemExit(f"找不到 HIGH_FREQ.md: {HF}")
    text = HF.read_text(encoding="utf-8")
    # 截取 ## 🔥 Hot 100 与下一个 ## 之间
    m = re.search(r"##\s+🔥\s*Hot 100.*?(?=##\s+📚|\Z)", text, re.DOTALL)
    if not m:
        raise SystemExit("HIGH_FREQ.md 解析失败：找不到 Hot 100 区")
    section = m.group(0)

    items = []
    pat = re.compile(r"- #(\d+)\s+([^→]+?)\s*→\s*\[[^\]]+\]\(([^)]+)\)")
    for line in section.splitlines():
        mm = pat.match(line.strip())
        if not mm:
            continue
        num = int(mm.group(1))
        name = mm.group(2).strip()
        star = "★" in name
        name = name.replace("★", "").strip()
        path = mm.group(3).strip()
        items.append((num, name, path, star))
    return items


def parse_args(argv):
    star_only = False
    n = 1
    for a in argv:
        if a == "star":
            star_only = True
        else:
            try:
                n = max(1, int(a))
            except ValueError:
                pass
    return star_only, n


def main():
    star_only, n = parse_args(sys.argv[1:])
    items = load_hot100()
    if star_only:
        items = [it for it in items if it[3]]
    if not items:
        raise SystemExit("候选为空")
    picks = random.sample(items, min(n, len(items)))

    label = f"{'★ ' if star_only else ''}从 {len(items)} 题中抽 {len(picks)} 道"
    print(f"——— {label} ———")
    for num, name, path, star in picks:
        marker = " ★" if star else ""
        print(f"  #{num}{marker}  {name}")
        print(f"        → {path}")


if __name__ == "__main__":
    main()
