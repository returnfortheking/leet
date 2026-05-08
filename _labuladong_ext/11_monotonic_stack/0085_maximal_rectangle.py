"""
LeetCode 85. Maximal Rectangle / 最大矩形  (Hard)
Link: https://leetcode.cn/problems/maximal-rectangle/

题目描述
--------
给定 m x n 的二进制矩阵 matrix（'0' 或 '1'），求其中只含 '1' 的最大矩形面积。

约束
----
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 200
- matrix[i][j] in {'0', '1'}

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
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([["1", "0", "1", "0", "0"],
          ["1", "0", "1", "1", "1"],
          ["1", "1", "1", "1", "1"],
          ["1", "0", "0", "1", "0"]], 6),
        ([], 0),
        ([["0"]], 0),
        ([["1"]], 1),
        ([["0", "0"]], 0),
        ([["1", "1", "1"], ["1", "1", "1"]], 6),
    ]
    passed = 0
    for i, (matrix, expected) in enumerate(cases, 1):
        actual = sol.maximalRectangle([row[:] for row in matrix])
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
