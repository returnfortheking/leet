"""
LeetCode 32. Longest Valid Parentheses / 最长有效括号  (Hard)
Link: https://leetcode.cn/problems/longest-valid-parentheses/

题目描述
--------
给定只含 '(' 和 ')' 的字符串 s，返回**最长有效括号子串**的长度。
有效：每个 ')' 都能匹配前面的 '('。

约束
----
- 0 <= s.length <= 3 * 10^4
- s[i] in {'(', ')'}

提示
----
卡住超过 25 分钟再去看 09_dp/NOTES.md（也可用栈解法，参见 11_monotonic_stack）。
（DP：dp[i] = 以 s[i] 结尾的最长有效长度；分 s[i]==')' 且 s[i-1]=='(' / s[i-1]==')' 两种情况）

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
    def longestValidParentheses(self, s: str) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ("(()", 2),
        (")()())", 4),
        ("", 0),
        ("(", 0),
        (")", 0),
        ("()(()", 2),
        ("()(())", 6),
    ]
    passed = 0
    for i, (s, expected) in enumerate(cases, 1):
        actual = sol.longestValidParentheses(s)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: s={s!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
