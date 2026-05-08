"""
LeetCode 20. Valid Parentheses / 有效的括号  (Easy)
Link: https://leetcode.cn/problems/valid-parentheses/

题目描述
--------
给定只含 '()[]{}' 6 种字符的字符串 s，判断是否合法配对：
- 左括号必须用相同类型右括号闭合
- 必须以正确顺序闭合（嵌套结构合法）

约束
----
- 1 <= s.length <= 10^4
- s[i] 仅来自 "()[]{}"

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
    def isValid(self, s: str) -> bool:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("(", False),
        ("]", False),
        ("", True),
    ]
    passed = 0
    for i, (s, expected) in enumerate(cases, 1):
        actual = sol.isValid(s)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: s={s!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
