"""
LeetCode 994. Rotting Oranges / 腐烂的橘子  (Medium)
Link: https://leetcode.cn/problems/rotting-oranges/

题目描述
--------
给定 m x n 网格 grid：0=空、1=新鲜橘子、2=腐烂橘子。
每分钟，所有四邻接到腐烂橘子的新鲜橘子会一并腐烂。
返回让所有新鲜橘子腐烂所需的最少分钟数；若有橘子无法腐烂返回 -1。

约束
----
- 1 <= m, n <= 10
- grid[i][j] in {0, 1, 2}

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
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4),
        ([[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1),
        ([[0, 2]], 0),
        ([[0]], 0),
        ([[1]], -1),
        ([[2]], 0),
    ]
    passed = 0
    for i, (grid, expected) in enumerate(cases, 1):
        copy = [row[:] for row in grid]
        actual = sol.orangesRotting(copy)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
