"""
LeetCode 72. Edit Distance / 编辑距离  (Hard)
Link: https://leetcode.cn/problems/edit-distance/

题目描述
--------
给定两个字符串 word1, word2，返回将 word1 转换成 word2 所需的最少操作次数。
每次操作可以：插入、删除、替换一个字符。

约束
----
- 0 <= word1.length, word2.length <= 500
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
    def minDistance(self, word1: str, word2: str) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        (("horse", "ros"), 3),
        (("intention", "execution"), 5),
        (("", ""), 0),
        (("a", ""), 1),
        (("", "abc"), 3),
        (("abc", "abc"), 0),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = sol.minDistance(*args)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: args={args!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
