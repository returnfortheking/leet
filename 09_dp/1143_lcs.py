"""
LeetCode 1143. Longest Common Subsequence / 最长公共子序列  (Medium)
Link: https://leetcode.cn/problems/longest-common-subsequence/

题目描述
--------
给定两个字符串 text1 和 text2，返回它们最长公共子序列的长度；不存在则返回 0。
子序列：在不改变原顺序的前提下任选若干字符。

约束
----
- 1 <= text1.length, text2.length <= 1000
- 仅小写英文字母

提示
----
卡住超过 25 分钟再去看 09_dp/NOTES.md 的「LCS」模板。

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
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        (("abcde", "ace"), 3),
        (("abc", "abc"), 3),
        (("abc", "def"), 0),
        (("a", "a"), 1),
        (("ezupkr", "ubmrapg"), 2),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = sol.longestCommonSubsequence(*args)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: args={args!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
