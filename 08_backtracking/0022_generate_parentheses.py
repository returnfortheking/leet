"""
LeetCode 22. Generate Parentheses / 括号生成  (Medium)
Link: https://leetcode.cn/problems/generate-parentheses/

题目描述
--------
给定整数 n，生成所有由 n 对括号组成的合法（有效配对）字符串列表。
顺序任意，每个串只出现一次。

约束
----
- 1 <= n <= 8

提示
----
卡住超过 25 分钟再去看 08_backtracking/NOTES.md 的「括号生成」模板。
（关键约束：right < left 时才能放右括号）

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
    def generateParenthesis(self, n: int) -> List[str]:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
        (1, ["()"]),
        (2, ["(())", "()()"]),
    ]
    passed = 0
    for i, (n, expected) in enumerate(cases, 1):
        actual = sol.generateParenthesis(n)
        ok = actual is not None and sorted(actual) == sorted(expected)
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: n={n}  count_e={len(expected)}  count_a={len(actual) if actual else 0}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
