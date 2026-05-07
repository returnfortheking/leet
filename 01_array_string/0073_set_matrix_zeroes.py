"""
LeetCode 73. Set Matrix Zeroes / 矩阵置零  (Medium)
Link: https://leetcode.cn/problems/set-matrix-zeroes/

题目描述
--------
给定 m x n 整数矩阵 matrix，若某元素为 0，则将其所在整行和整列的所有元素都置为 0。
要求**原地修改**。进阶：O(1) 额外空间（不计输入输出）。

约束
----
- m == matrix.length
- n == matrix[0].length
- 1 <= m, n <= 200
- -2^31 <= matrix[i][j] <= 2^31 - 1

提示
----
卡住超过 25 分钟再去看 01_array_string/NOTES.md。
（O(m+n) 空间：用两个数组记录哪些行/列要清零；O(1) 空间：用第一行第一列当标记位）

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
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """原地修改 matrix。"""
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([[1, 1, 1], [1, 0, 1], [1, 1, 1]],
         [[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
        ([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
         [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]),
        ([[1]], [[1]]),
        ([[0]], [[0]]),
        ([[1, 2], [3, 4]], [[1, 2], [3, 4]]),
    ]
    passed = 0
    for i, (matrix, expected) in enumerate(cases, 1):
        m = [row[:] for row in matrix]
        sol.setZeroes(m)
        ok = m == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: expected={expected!r}  actual={m!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
