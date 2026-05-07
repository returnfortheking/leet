"""
LeetCode 63. Unique Paths II / 不同路径 II  (Medium)
Link: https://leetcode.cn/problems/unique-paths-ii/

题目描述
--------
m x n 网格 obstacleGrid，1 表示障碍，0 表示可走。
机器人从左上角到右下角，每步只能向右或向下。返回不同路径总数；
若起点或终点被障碍占据，返回 0。

约束
----
- m == obstacleGrid.length
- n == obstacleGrid[i].length
- 1 <= m, n <= 100
- obstacleGrid[i][j] in {0, 1}

提示
----
卡住超过 25 分钟再去看 09_dp/NOTES.md。
（在 #62 的 DP 上加一条：遇到障碍 dp[i][j] = 0）

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
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 2),
        ([[0, 1], [0, 0]], 1),
        ([[1]], 0),
        ([[0]], 1),
        ([[0, 0], [1, 1], [0, 0]], 0),
    ]
    passed = 0
    for i, (grid, expected) in enumerate(cases, 1):
        actual = sol.uniquePathsWithObstacles([row[:] for row in grid])
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
