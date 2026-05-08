"""
LeetCode 42. Trapping Rain Water / 接雨水  (Hard)
Link: https://leetcode.cn/problems/trapping-rain-water/

题目描述
--------
给定 n 个非负整数 height，每位代表宽度为 1 的柱子。
计算下雨之后能接多少雨水。

约束
----
- n == height.length
- 1 <= n <= 2 * 10^4
- 0 <= height[i] <= 10^5

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
    def trap(self, height: List[int]) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
        ([1], 0),
        ([], 0),
        ([3, 0, 0, 2, 0, 4], 10),
        ([0, 0, 0], 0),
    ]
    passed = 0
    for i, (h, expected) in enumerate(cases, 1):
        actual = sol.trap(h)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: height={h!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
