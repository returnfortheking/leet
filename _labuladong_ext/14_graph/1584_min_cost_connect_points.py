"""
LeetCode 1584. Min Cost to Connect All Points / 连接所有点的最小费用  (Medium)
Link: https://leetcode.cn/problems/min-cost-to-connect-all-points/

题目描述
--------
points[i] = [x_i, y_i] 表示二维平面上 n 个点。两点 (xi, yi) 和 (xj, yj) 之间
的连接费用为曼哈顿距离 |xi - xj| + |yi - yj|。返回连通所有点的最小总费用。

约束
----
- 1 <= n <= 1000
- -10^6 <= x_i, y_i <= 10^6
- 所有点不重复

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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]], 20),
        ([[3, 12], [-2, 5], [-4, 1]], 18),
        ([[0, 0], [1, 1], [1, 0], [-1, 1]], 4),
        ([[-1000000, -1000000], [1000000, 1000000]], 4000000),
        ([[0, 0]], 0),
    ]
    passed = 0
    for i, (points, expected) in enumerate(cases, 1):
        actual = sol.minCostConnectPoints([row[:] for row in points])
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
