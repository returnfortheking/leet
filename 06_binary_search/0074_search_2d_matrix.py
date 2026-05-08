"""
LeetCode 74. Search a 2D Matrix / 搜索二维矩阵  (Medium)
Link: https://leetcode.cn/problems/search-a-2d-matrix/

题目描述
--------
给定 m x n 整数矩阵 matrix，每行非递减；且每一行的第一个数大于上一行的最后一个数
（整体可视作一维有序数组）。判断 target 是否存在。要求 O(log(m*n))。

约束
----
- m == matrix.length
- n == matrix[0].length
- 1 <= m, n <= 100
- -10^4 <= matrix[i][j], target <= 10^4

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
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        (([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3), True),
        (([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13), False),
        (([[1]], 1), True),
        (([[1]], 2), False),
        (([[1, 3]], 3), True),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        matrix = [row[:] for row in args[0]]
        actual = sol.searchMatrix(matrix, args[1])
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: target={args[1]}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
