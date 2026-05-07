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

提示
----
卡住超过 25 分钟再去看 05_sliding_window/NOTES.md 的「最短型滑窗」模板。

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
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    # 多个有效答案：用 (s, t, 期望长度) 验证；并校验 actual 含 t 全部字符
    from collections import Counter
    cases = [
        ("ADOBECODEBANC", "ABC", 4),    # "BANC"
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
                and not (Counter(t) - Counter(actual))     # 覆盖
                and actual in s                            # 是 s 的子串
            )
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: s={s!r} t={t!r}  expected_len={expected_len}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
