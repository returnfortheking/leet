"""
LeetCode 3. Longest Substring Without Repeating Characters / 无重复字符的最长子串  (Medium)
Link: https://leetcode.cn/problems/longest-substring-without-repeating-characters/

题目描述
--------
给定一个字符串 s，找出其中不含有重复字符的最长子串的长度。

约束
----
- 0 <= s.length <= 5 * 10^4
- s 由英文字母、数字、符号和空格组成

复杂度（解完后填）
------
时间：O(?)    空间：O(?)

复盘要点（解完后填）
--------
- 卡在哪一步？
- 触发器：什么样的题面应该让我立刻想到这个套路？
"""

from typing import List
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # TODO: 在这里写你的解法
        letters = defaultdict(int)
        l = r = 0
        ans = 0

        def isRepeated() -> bool:
            for n in letters.values():
                if n > 1:
                    return True
            return False

        while r < len(s):
            while r < len(s) and not isRepeated():
                ans = max(r - l, ans)
                letters[s[r]] += 1
                r += 1
            while l < r and isRepeated():
                letters[s[l]] -= 1
                l += 1
        if not isRepeated():
            ans = max(r - l, ans)
        return ans


def test():
    sol = Solution()
    cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
        ("au", 2),
        ("dvdf", 3),
    ]
    passed = 0
    for i, (s, expected) in enumerate(cases, 1):
        actual = sol.lengthOfLongestSubstring(s)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: s={s!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
