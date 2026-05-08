"""
LeetCode 240. Search a 2D Matrix II / 搜索二维矩阵 II  (Medium)
Link: https://leetcode.cn/problems/search-a-2d-matrix-ii/

题目描述
--------
给定 m x n 矩阵 matrix，**每一行从左到右非递减**，**每一列从上到下非递减**。
判断 target 是否存在。要求时间优于 O(m*n)。

约束
----
- m == matrix.length
- n == matrix[0].length
- 1 <= m, n <= 300
- -10^9 <= matrix[i][j], target <= 10^9

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
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    cases = [
        ((matrix, 5), True),
        ((matrix, 20), False),
        ((matrix, 1), True),
        ((matrix, 30), True),
        ((matrix, 31), False),
        (([[1]], 1), True),
        (([[1]], 0), False),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        m = [row[:] for row in args[0]]
        actual = sol.searchMatrix(m, args[1])
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: target={args[1]}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
