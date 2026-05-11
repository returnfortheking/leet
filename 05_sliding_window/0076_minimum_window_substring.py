"""
LeetCode 76. Minimum Window Substring / 最小覆盖子串  (Hard)
Link: https://leetcode.cn/problems/minimum-window-substring/

题目描述
--------
给定字符串 s 和 t，在 s 中找一个最短子串，覆盖 t 中所有字符（含重复次数）。
若不存在则返回空串；若有多个最短，返回任意一个。

约束
----
- m == s.length, n == t.length
- 1 <= m, n <= 10^5
- s 和 t 仅由英文字母组成

复杂度（解完后填）
------
时间：O(?)    空间：O(?)

复盘要点（解完后填）
--------
- 卡在哪一步？
- 触发器：什么样的题面应该让我立刻想到这个套路？
"""

from typing import List


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict

        dic_s = defaultdict(int)
        dic_t = defaultdict(int)

        for c in t:
            dic_t[c] += 1
        l = 0
        res = ""
        min_len = len(s) + 1

        def contain(a: dict, b: dict) -> bool:
            for k in b:
                if a[k] < b[k]:
                    return False
            return True

        for r in range(len(s)):
            dic_s[s[r]] += 1
            while contain(dic_s, dic_t):
                if r - l + 1 < min_len:
                    res = s[l : r + 1]
                    min_len = r - l + 1
                dic_s[s[l]] -= 1
                l += 1
        return res


def test():
    sol = Solution()
    # 多个有效答案：用 (s, t, 期望长度) 验证；并校验 actual 含 t 全部字符
    from collections import Counter

    cases = [
        ("ADOBECODEBANC", "ABC", 4),  # "BANC"
        ("a", "a", 1),
        ("a", "aa", 0),
        ("ab", "b", 1),
        ("aaflslflsldkalskaaa", "aaa", 3),
    ]
    passed = 0
    for i, (s, t, expected_len) in enumerate(cases, 1):
        actual = sol.minWindow(s, t)
        if expected_len == 0:
            ok = actual == ""
        else:
            ok = (
                isinstance(actual, str)
                and len(actual) == expected_len
                and not (Counter(t) - Counter(actual))  # 覆盖
                and actual in s  # 是 s 的子串
            )
        status = "PASS" if ok else "FAIL"
        print(
            f"[{status}] Case {i}: s={s!r} t={t!r}  expected_len={expected_len}  actual={actual!r}"
        )
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()


# ============================================================================
# 复盘笔记（做完题再看；避免提前剧透）
# ============================================================================
# # 0076 最小覆盖子串 — 复盘
#
# > 题：[0076_minimum_window_substring.py](../05_sliding_window/0076_minimum_window_substring.py)
# > 日期：2026-05-09
# > 套路：滑动窗口
#
# ## 我的第一版踩了哪些坑
#
# ### 致命
#
# 1. **窗口长度 `min_len` 更新错误**：更新最优解时用了 `r - l`，但 `[l, r]` 闭区间的长度是 `r - l + 1`。而 `min_len` 初始化为 `len(s) + 1`，两者不统一，导致比较和记录的结果都错。
#    - 症状：Case 1 输出 `'ADOBECO'`（长度 7）而非 `'BANC'`（长度 4）。
#
# 2. **初始窗口未填入字符**：原版用 `while l <= r < len(s)` + `if/else` 分支。`l = r = 0` 时窗口 `[0, 0]` 是空的（`dic_s` 里还没加 `s[0]`），进入 else 后先 `dic_s[s[r]] += 1; r += 1`，导致 `r` 从 0 直接跳到 1，**漏掉了仅含 `s[0]` 的情况**。
#    - 症状：Case 2 (`s="a", t="a"`) 和 Case 4 (`s="ab", t="b"`) 返回空串。
#    - 根因：滑动窗口的右指针扩展时机不对——应该在每轮循环**先加入 `s[r]`，再判断是否满足条件**。
#
# ### 风格 / 习惯
#
# 3. **手动预填 52 个字母 key**：用 `for i in range(26)` 循环给 `dic_s` 和 `dic_t` 各初始化 26×2 个 key 为 0。完全可以用 `defaultdict(int)` 替代——访问不存在的 key 自动返回 0，省掉整个初始化循环。
#
# 4. **`if contain / else` 结构不适合滑动窗口**：原版把"满足条件收缩"和"不满足扩展"分成 if/else 两个分支，逻辑容易混乱。标准写法是 `for r` 遍历右指针 + 内层 `while` 收缩左指针，结构更清晰，不容易漏元素。
#
# ## 这次学到的
#
# - 滑动窗口的标准模板：
#   ```python
#   for r in range(len(s)):
#       dic_s[s[r]] += 1          # 先把右端字符加入窗口
#       while 满足条件:            # 再判断要不要收缩
#           更新最优解
#           dic_s[s[l]] -= 1       # 收缩左端
#           l += 1
#   ```
#   关键：**先加右端，再判断，再收缩左端**。不要把"加右端"放在 else 分支里。
#
# - 窗口长度始终用 `r - l + 1`（闭区间），和初始化 `min_len = len(s) + 1` 统一比较。
#
# - `defaultdict(int)` 可以替代手动初始化字典默认值，写法更简洁。
#
# ## 修复后的关键片段
#
# ```python
# from collections import defaultdict
#
# dic_s = defaultdict(int)
# dic_t = defaultdict(int)
# for c in t:
#     dic_t[c] += 1
#
# l = 0
# res = ""
# min_len = len(s) + 1
#
# for r in range(len(s)):
#     dic_s[s[r]] += 1
#     while contain(dic_s, dic_t):
#         if r - l + 1 < min_len:
#             res = s[l : r + 1]
#             min_len = r - l + 1
#         dic_s[s[l]] -= 1
#         l += 1
# ```
