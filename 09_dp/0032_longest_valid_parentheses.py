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
        # LeetCode 题面 example
        ("(()", 2),
        (")()())", 4),
        # 尺寸边界
        ("", 0),
        ("(", 0),
        (")", 0),
        # 全开 / 全闭（无配对）
        ("(((", 0),
        (")))", 0),
        # 嵌套 / 并列
        ("(())", 4),
        ("()()", 4),
        ("(())()", 6),
        ("()(())", 6),
        # 中段失败但局部有解
        ("()(()", 2),
        ("(()()(", 4),                      # 中段 "()()" valid 长 4
        # 嵌套深层
        ("(((())))", 8),
        # 前导 ) 不影响后续整段配对
        (")(((((()))", 6),
        # 复合 (常见 off-by-one)
        ("()(()()", 4),                     # 中段 "(()()" 内 "()()" 长 4
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
