"""
LeetCode 48. Rotate Image / 旋转图像  (Medium)
Link: https://leetcode.cn/problems/rotate-image/

题目描述
--------
给定 n x n 二维矩阵 matrix，将其顺时针**原地**旋转 90 度。

约束
----
- n == matrix.length == matrix[i].length
- 1 <= n <= 20
- -1000 <= matrix[i][j] <= 1000

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
    def rotate(self, matrix: List[List[int]]) -> None:
        """原地修改 matrix。"""
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
         [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
        ([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
         [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]),
        ([[1]], [[1]]),
        ([[1, 2], [3, 4]], [[3, 1], [4, 2]]),
    ]
    passed = 0
    for i, (matrix, expected) in enumerate(cases, 1):
        m = [row[:] for row in matrix]
        sol.rotate(m)
        ok = m == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: expected={expected!r}  actual={m!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
