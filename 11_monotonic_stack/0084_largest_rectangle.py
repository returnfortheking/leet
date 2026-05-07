"""
LeetCode 84. Largest Rectangle in Histogram / 柱状图中最大的矩形  (Hard)
Link: https://leetcode.cn/problems/largest-rectangle-in-histogram/

题目描述
--------
给定柱形图的每根柱子高度 heights[i]（柱宽 1）。
求由相邻若干柱子构成的最大矩形面积。

约束
----
- 1 <= heights.length <= 10^5
- 0 <= heights[i] <= 10^4

提示
----
卡住超过 25 分钟再去看 11_monotonic_stack/NOTES.md 的「柱状图最大矩形」模板。
（前后加 0 哨兵；单调递增栈，破坏单调性时弹出并结算面积）

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
    def largestRectangleArea(self, heights: List[int]) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([2, 1, 5, 6, 2, 3], 10),
        ([2, 4], 4),
        ([1], 1),
        ([0], 0),
        ([2, 1, 2], 3),
        ([5, 4, 1, 2], 8),
    ]
    passed = 0
    for i, (h, expected) in enumerate(cases, 1):
        actual = sol.largestRectangleArea(h)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: heights={h!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
