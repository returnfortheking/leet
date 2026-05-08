"""
LeetCode 200. Number of Islands / 岛屿数量  (Medium)
Link: https://leetcode.cn/problems/number-of-islands/

题目描述
--------
给定一个 m x n 的二维网格，'1' 表示陆地，'0' 表示水域。
计算岛屿数量（陆地连通分量数）。相邻指上下左右。

约束
----
- 1 <= m, n <= 300
- grid[i][j] in {'1', '0'}

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
    def numIslands(self, grid: List[List[str]]) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ], 1),
        ([
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ], 3),
        ([["1"]], 1),
        ([["0"]], 0),
        ([], 0),
    ]
    passed = 0
    for i, (grid, expected) in enumerate(cases, 1):
        copy = [row[:] for row in grid]   # 拷贝避免污染
        actual = sol.numIslands(copy)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
