"""
LeetCode 516. Longest Palindromic Subsequence / 最长回文子序列  (Medium)
Link: https://leetcode.cn/problems/longest-palindromic-subsequence/

题目描述
--------
给定字符串 s，返回其最长回文子序列的长度。
子序列：在不改变顺序前提下任选若干字符（可不连续）。

约束
----
- 1 <= s.length <= 1000
- 仅小写英文字母

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
    def longestPalindromeSubseq(self, s: str) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ("bbbab", 4),
        ("cbbd", 2),
        ("a", 1),
        ("ac", 1),
        ("racecar", 7),
        ("abcdefg", 1),
    ]
    passed = 0
    for i, (s, expected) in enumerate(cases, 1):
        actual = sol.longestPalindromeSubseq(s)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: s={s!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
