"""
LeetCode 438. Find All Anagrams in a String / 找到字符串中所有字母异位词  (Medium)
Link: https://leetcode.cn/problems/find-all-anagrams-in-a-string/

题目描述
--------
给定字符串 s 和 p，找到 s 中所有 p 的字母异位词的起始下标，返回下标数组。
异位词：字母组成与 p 完全相同（含每个字母出现次数）。

约束
----
- 1 <= s.length, p.length <= 3 * 10^4
- s, p 仅由小写字母组成

提示
----
卡住超过 25 分钟再去看 05_sliding_window/NOTES.md 的「定长滑窗」模板。
（思路：维护长度为 len(p) 的窗口，比较两个 26 字母数组）

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
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        (("cbaebabacd", "abc"), [0, 6]),
        (("abab", "ab"), [0, 1, 2]),
        (("aaaaaa", "aa"), [0, 1, 2, 3, 4]),
        (("a", "ab"), []),
        (("ab", "ab"), [0]),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = sol.findAnagrams(*args)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: args={args!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
