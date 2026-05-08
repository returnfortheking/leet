"""
LeetCode 11. Container With Most Water / 盛最多水的容器  (Medium)
Link: https://leetcode.cn/problems/container-with-most-water/

题目描述
--------
给定 n 个非负整数 height[i]，把每个数看作一根垂直线段（坐标 i, 高度 height[i]）。
任选两根线段构成容器（与 x 轴围成矩形），返回能盛最多水的体积。

约束
----
- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4

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
    def maxArea(self, height: List[int]) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 1], 2),
        ([2, 3, 4, 5, 18, 17, 6], 17),
    ]
    passed = 0
    for i, (h, expected) in enumerate(cases, 1):
        actual = sol.maxArea(h)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: height={h!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
