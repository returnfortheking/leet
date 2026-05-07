"""
LeetCode 64. Minimum Path Sum / 最小路径和  (Medium)
Link: https://leetcode.cn/problems/minimum-path-sum/

题目描述
--------
给定 m x n 的非负整数网格 grid，从左上角走到右下角，每步只能向右或向下。
返回路径上所有数字之和的最小值。

约束
----
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 200
- 0 <= grid[i][j] <= 200

提示
----
卡住超过 25 分钟再去看 09_dp/NOTES.md。
（dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])）

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
    def minPathSum(self, grid: List[List[int]]) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([[1, 3, 1], [1, 5, 1], [4, 2, 1]], 7),
        ([[1, 2, 3], [4, 5, 6]], 12),
        ([[1]], 1),
        ([[5, 1], [2, 3]], 9),
    ]
    passed = 0
    for i, (grid, expected) in enumerate(cases, 1):
        actual = sol.minPathSum([row[:] for row in grid])
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
