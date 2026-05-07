"""
LeetCode 54. Spiral Matrix / 螺旋矩阵  (Medium)
Link: https://leetcode.cn/problems/spiral-matrix/

题目描述
--------
给定 m x n 矩阵，按**顺时针螺旋顺序**返回矩阵中所有元素。

约束
----
- m == matrix.length
- n == matrix[0].length
- 1 <= m, n <= 10
- -100 <= matrix[i][j] <= 100

提示
----
卡住超过 25 分钟再去看 01_array_string/NOTES.md。
（思路：维护四个边界 top/bottom/left/right，按"右 → 下 → 左 → 上"循环往内收缩）

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
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
        ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
         [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
        ([[1]], [1]),
        ([[1, 2], [3, 4]], [1, 2, 4, 3]),
        ([[1, 2, 3]], [1, 2, 3]),
        ([[1], [2], [3]], [1, 2, 3]),
    ]
    passed = 0
    for i, (matrix, expected) in enumerate(cases, 1):
        actual = sol.spiralOrder([row[:] for row in matrix])
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
