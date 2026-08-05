#!/usr/bin/env python3
"""
复健重测：从已通过的题里分层抽样，剥掉解法重做一遍，计时判定遗忘程度。

流程（你只需要 4 个命令）
------------------------
    python retest.py start          开一轮重测（默认 T2+T3 各专题抽样，共 12 题）
    python retest.py next           出下一题 → 生成干净副本并开始计时
    python retest.py check          跑当前题的测试；通过则记录用时并自动出下一题
    python retest.py report         全部做完后生成 RETEST_REPORT.md（专题级诊断）

辅助命令
--------
    python retest.py start 8 --tiers T2,T3,T4    自定义题数和档位
    python retest.py skip           当前题卡死放弃（记为 ❌，出下一题）
    python retest.py status         看本轮进度
    python retest.py abort          废弃本轮（删除 _retest/ 会话）

规则
----
- 只从 PROGRESS.md 里标 [x]（历史已通过）的题里抽；每个专题目录最多 2 题。
- 干净副本 = 原文件剥掉 Solution 方法体 + 文档串里的「思路/复杂度/复盘要点」段，
  题目描述和测试用例原样保留。做题就在副本文件里写，别看原文件。
- 计时从 `next` 生成副本那一刻开始，到 `check` 通过为止；中途跑 `check` 失败不停表。
- 判定线 = 该题所属档位的估时上限（T1=3 / T2=5 / T3=10 / T4=20 / T5=35 分钟）：
  ≤1× 达标 ✅ ｜ ≤2× 生疏 ⚠️ ｜ >2× 或放弃 遗忘 ❌
"""
import ast
import json
import re
import shutil
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except (AttributeError, OSError):
    pass

import pick  # 复用题库加载（HIGH_FREQ.md → 题号/题名/路径）

ROOT = Path(__file__).parent
PROGRESS = ROOT / "PROGRESS.md"
SESSION_DIR = ROOT / "_retest"
SESSION_FILE = SESSION_DIR / "session.json"
REPORT_FILE = ROOT / "RETEST_REPORT.md"
TEST_TIMEOUT = 20

TIER_BUDGET_MIN = {"T1": 3, "T2": 5, "T3": 10, "T4": 20, "T5": 35}
SPOILER_HEADERS = ("思路", "复杂度", "复盘要点")


# ============================================================================
# 题库：PROGRESS.md 的档位 + 完成状态
# ============================================================================
def load_tiers() -> dict:
    """{题号: (tier, done_bool)}"""
    text = PROGRESS.read_text(encoding="utf-8")
    out = {}
    tier = None
    for line in text.splitlines():
        m = re.match(r"##\s+(T\d)\b", line.strip())
        if m:
            tier = m.group(1)
            continue
        m = re.match(r"- \[(x| )\] (\d{3,4})\s", line.strip())
        if m and tier:
            out[int(m.group(2))] = (tier, m.group(1) == "x")
    return out


def build_pool(tiers_wanted: list) -> list:
    """[(num, name, rel_path, tier, topic)] 仅历史已通过的题。"""
    tiers = load_tiers()
    pool = []
    for num, name, rel, _star in pick.load_problems(include_ext=False):
        tier, done = tiers.get(num, (None, False))
        if done and tier in tiers_wanted:
            topic = rel.split("/")[0].split("\\")[0]
            pool.append((num, name, rel, tier, topic))
    return pool


def stratified_sample(pool: list, n: int, per_topic: int = 2) -> list:
    """按专题轮转抽样，每专题最多 per_topic 道。"""
    import random
    by_topic = {}
    for item in pool:
        by_topic.setdefault(item[4], []).append(item)
    for items in by_topic.values():
        random.shuffle(items)
    picked, round_i = [], 0
    while len(picked) < n and round_i < per_topic:
        for topic in sorted(by_topic):
            if len(picked) >= n:
                break
            if round_i < len(by_topic[topic]):
                picked.append(by_topic[topic][round_i])
        round_i += 1
    random.shuffle(picked)
    return picked


# ============================================================================
# 剥离解法：方法体 → pass，文档串剧透段删除
# ============================================================================
def strip_solution(src_path: Path) -> str:
    src = src_path.read_text(encoding="utf-8")
    lines = src.splitlines()
    tree = ast.parse(src)

    edits = []  # (start_idx, end_idx_inclusive, replacement_lines)

    # 1) Solution* 类的每个方法体 → TODO + pass
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and node.name.startswith("Solution"):
            for fn in node.body:
                if not isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    continue
                first, last = fn.body[0], fn.body[-1]
                indent = " " * first.col_offset
                edits.append((
                    first.lineno - 1,
                    last.end_lineno - 1,
                    [f"{indent}# TODO: 在这里写你的解法",
                     f"{indent}pass"],
                ))

    # 2) 模块文档串：从「思路/复杂度/复盘要点」起截断（保留题目描述/约束/示例）
    if (tree.body and isinstance(tree.body[0], ast.Expr)
            and isinstance(tree.body[0].value, ast.Constant)
            and isinstance(tree.body[0].value.value, str)):
        doc = tree.body[0]
        for i in range(doc.lineno - 1, doc.end_lineno - 1):
            if lines[i].strip() in SPOILER_HEADERS:
                # 删到文档串结束引号那一行之前
                edits.append((i, doc.end_lineno - 2, []))
                break

    for start, end, repl in sorted(edits, key=lambda e: -e[0]):
        lines[start:end + 1] = repl
    return "\n".join(lines) + "\n"


# ============================================================================
# 会话状态
# ============================================================================
def load_session() -> dict:
    if not SESSION_FILE.exists():
        raise SystemExit("没有进行中的重测会话。先跑: python retest.py start")
    return json.loads(SESSION_FILE.read_text(encoding="utf-8"))


def save_session(s: dict) -> None:
    SESSION_DIR.mkdir(exist_ok=True)
    SESSION_FILE.write_text(
        json.dumps(s, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def current_problem(s: dict):
    for p in s["problems"]:
        if p["status"] == "active":
            return p
    return None


def verdict_of(p: dict) -> str:
    if p["status"] == "skipped":
        return "❌ 放弃"
    budget = TIER_BUDGET_MIN[p["tier"]]
    m = p["elapsed_min"]
    if m <= budget:
        return "✅ 达标"
    if m <= 2 * budget:
        return "⚠️ 生疏"
    return "❌ 遗忘"


# ============================================================================
# 命令
# ============================================================================
def cmd_start(n: int, tiers: list, force: bool) -> None:
    if SESSION_FILE.exists() and not force:
        s = json.loads(SESSION_FILE.read_text(encoding="utf-8"))
        undone = [p for p in s["problems"] if p["status"] in ("pending", "active")]
        if undone:
            raise SystemExit(
                f"已有进行中的会话（剩 {len(undone)} 题）。继续: python retest.py next / check；"
                f"废弃重开: python retest.py abort")
    if SESSION_DIR.exists():
        shutil.rmtree(SESSION_DIR)
    pool = build_pool(tiers)
    if not pool:
        raise SystemExit(f"档位 {tiers} 里没有已通过的题可抽。")
    picked = stratified_sample(pool, n)
    session = {
        "created": datetime.now().isoformat(timespec="seconds"),
        "tiers": tiers,
        "problems": [
            {"num": num, "name": name, "path": rel, "tier": tier, "topic": topic,
             "status": "pending", "start": None, "elapsed_min": None, "fails": 0}
            for num, name, rel, tier, topic in picked
        ],
    }
    save_session(session)
    print(f"重测会话已建：{len(picked)} 题（{'+'.join(tiers)}，跨 "
          f"{len(set(p[4] for p in picked))} 个专题）")
    print("题目顺序保密，做一题见一题。开始: python retest.py next")


def cmd_next() -> None:
    s = load_session()
    if current_problem(s):
        p = current_problem(s)
        print(f"当前题 #{p['num']} 还没过测试（python retest.py check），"
              f"卡死可 skip。文件: {p['file']}")
        return
    pending = [p for p in s["problems"] if p["status"] == "pending"]
    if not pending:
        print("全部做完 🎉  生成诊断: python retest.py report")
        return
    p = pending[0]
    src = ROOT / p["path"]
    stripped = strip_solution(src)
    seq = len([x for x in s["problems"] if x["status"] not in ("pending",)]) + 1
    dest = SESSION_DIR / f"{seq:02d}_{src.name}"
    dest.write_text(stripped, encoding="utf-8")
    helpers = src.parent / "_helpers.py"
    if helpers.exists():
        shutil.copy2(helpers, SESSION_DIR / "_helpers.py")
    p["status"] = "active"
    p["start"] = time.time()
    p["file"] = str(dest.relative_to(ROOT))
    save_session(s)
    budget = TIER_BUDGET_MIN[p["tier"]]
    done_ct = len([x for x in s["problems"] if x["status"] in ("passed", "skipped")])
    print(f"—— 第 {done_ct + 1}/{len(s['problems'])} 题 ——")
    print(f"  #{p['num']} {p['name']}   [{p['tier']}，达标线 {budget} 分钟]")
    print(f"  → {p['file']}")
    print(f"  ⏱ 计时已开始。写完跑: python retest.py check")


def cmd_check() -> None:
    s = load_session()
    p = current_problem(s)
    if not p:
        print("没有进行中的题。下一题: python retest.py next")
        return
    try:
        r = subprocess.run([sys.executable, str(ROOT / p["file"])],
                           capture_output=True, timeout=TEST_TIMEOUT,
                           cwd=str(SESSION_DIR))
        ok = r.returncode == 0
        tail = (r.stdout or b"").decode("utf-8", errors="replace").strip().splitlines()
    except subprocess.TimeoutExpired:
        ok, tail = False, ["(运行超时——可能死循环)"]
    elapsed = (time.time() - p["start"]) / 60
    if ok:
        p["status"] = "passed"
        p["elapsed_min"] = round(elapsed, 1)
        save_session(s)
        print(f"✅ 通过  用时 {p['elapsed_min']} 分钟 → {verdict_of(p)}"
              f"（达标线 {TIER_BUDGET_MIN[p['tier']]} 分钟）")
        cmd_next()
    else:
        p["fails"] += 1
        save_session(s)
        print(f"未通过（第 {p['fails']} 次尝试，已用 {elapsed:.1f} 分钟，计时继续）")
        for line in tail[-6:]:
            print(f"  {line}")


def cmd_skip() -> None:
    s = load_session()
    p = current_problem(s)
    if not p:
        print("没有进行中的题。")
        return
    p["status"] = "skipped"
    p["elapsed_min"] = round((time.time() - p["start"]) / 60, 1)
    save_session(s)
    print(f"已放弃 #{p['num']}（{p['elapsed_min']} 分钟）→ 计入 ❌")
    cmd_next()


def cmd_status() -> None:
    s = load_session()
    done = [p for p in s["problems"] if p["status"] in ("passed", "skipped")]
    print(f"进度 {len(done)}/{len(s['problems'])}  （会话建于 {s['created']}）")
    for p in done:
        print(f"  #{p['num']:>4} {p['name']:<14} {p['tier']}  "
              f"{p['elapsed_min']}min  {verdict_of(p)}")
    p = current_problem(s)
    if p:
        print(f"  ▶ 进行中: #{p['num']} {p['name']}（{p['file']}）")


def cmd_report() -> None:
    s = load_session()
    done = [p for p in s["problems"] if p["status"] in ("passed", "skipped")]
    if not done:
        raise SystemExit("还没做题，没法出报告。")
    lines = [
        f"# 复健重测报告（{datetime.now().date()}）",
        "",
        f"> 会话建于 {s['created']}，档位 {'+'.join(s['tiers'])}，"
        f"完成 {len(done)}/{len(s['problems'])} 题。",
        f"> 判定线=档位估时上限：≤1× ✅达标 / ≤2× ⚠️生疏 / >2×或放弃 ❌遗忘",
        "",
        "## 逐题结果",
        "",
        "| 题 | 专题 | 档 | 达标线 | 用时 | 判定 | 失败次数 |",
        "|---|---|---|---|---|---|---|",
    ]
    for p in done:
        lines.append(
            f"| #{p['num']} {p['name']} | {p['topic']} | {p['tier']} "
            f"| {TIER_BUDGET_MIN[p['tier']]}min | {p['elapsed_min']}min "
            f"| {verdict_of(p)} | {p['fails']} |")
    lines += ["", "## 专题诊断", "",
              "| 专题 | 题数 | ✅ | ⚠️ | ❌ | 结论 |", "|---|---|---|---|---|---|"]
    by_topic = {}
    for p in done:
        by_topic.setdefault(p["topic"], []).append(p)
    weak = []
    for topic in sorted(by_topic):
        ps = by_topic[topic]
        vs = [verdict_of(p) for p in ps]
        ok = sum(1 for x in vs if x.startswith("✅"))
        meh = sum(1 for x in vs if x.startswith("⚠"))
        bad = sum(1 for x in vs if x.startswith("❌"))
        if bad:
            concl, is_weak = "重刷该专题 + 精读 NOTES.md", True
        elif meh:
            concl, is_weak = "再抽 2 题巩固", True
        else:
            concl, is_weak = "状态在线", False
        if is_weak:
            weak.append(topic)
        lines.append(f"| {topic} | {len(ps)} | {ok} | {meh} | {bad} | {concl} |")
    lines += ["", "## 修补清单", ""]
    if weak:
        for t in weak:
            lines.append(f"- [ ] {t}：重做本轮失手题 → `{t}/NOTES.md` → "
                         f"`python pick.py --done` 同专题再抽 1-2 题验证")
        lines.append("- [ ] 过一遍 `_review/pitfalls.md` 与 `_review/LOGIC_TRAPS.md` 中相关专题条目")
    else:
        lines.append("- 全部达标：跳过修补，直接进入 T4 高频缺口"
                     "（0146 LRU / 0056 / 0207 / 0208 / 0300 / 0394 / 1143 / 0239）")
    REPORT_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"报告已写入 {REPORT_FILE.name}")
    print("\n".join(lines[lines.index("## 专题诊断"):]))


def cmd_abort() -> None:
    if SESSION_DIR.exists():
        shutil.rmtree(SESSION_DIR)
        print("会话已废弃（_retest/ 已删除）。")
    else:
        print("没有会话可废弃。")


def main():
    argv = sys.argv[1:]
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return
    cmd = argv[0]
    if cmd == "start":
        n = 12
        tiers = ["T2", "T3"]
        force = "--force" in argv
        for i, a in enumerate(argv[1:], 1):
            if a.isdigit():
                n = int(a)
            elif a == "--tiers" and i + 1 <= len(argv) - 1:
                tiers = [t.strip().upper() for t in argv[i + 1].split(",")]
        cmd_start(n, tiers, force)
    elif cmd == "next":
        cmd_next()
    elif cmd == "check":
        cmd_check()
    elif cmd == "skip":
        cmd_skip()
    elif cmd == "status":
        cmd_status()
    elif cmd == "report":
        cmd_report()
    elif cmd == "abort":
        cmd_abort()
    else:
        raise SystemExit(f"未知命令 {cmd}。用法见: python retest.py --help")


if __name__ == "__main__":
    main()
