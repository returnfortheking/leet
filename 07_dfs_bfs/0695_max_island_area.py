"""
LeetCode 695. Max Area of Island / 岛屿的最大面积  (Medium)
Link: https://leetcode.cn/problems/max-area-of-island/

题目描述
--------
给定 m x n 的 0/1 网格，1 表示陆地，0 表示水。
四联通的 1 构成一个岛屿；返回所有岛屿中面积（格子数）的最大值。
不存在岛屿则返回 0。

约束
----
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 50
- grid[i][j] in {0, 1}

提示
----
卡住超过 25 分钟再去看 07_dfs_bfs/NOTES.md 的「网格 DFS」模板。

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
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        ], 6),
        ([[0, 0, 0, 0, 0]], 0),
        ([[1]], 1),
        ([[1, 1], [1, 1]], 4),
        ([[1, 0, 1], [0, 0, 0], [1, 0, 1]], 1),
    ]
    passed = 0
    for i, (grid, expected) in enumerate(cases, 1):
        copy = [row[:] for row in grid]
        actual = sol.maxAreaOfIsland(copy)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
