"""
LeetCode 221. Maximal Square / 最大正方形  (Medium)
Link: https://leetcode.cn/problems/maximal-square/

题目描述
--------
m x n 的 0/1 矩阵 matrix，找其中只含 1 的最大正方形子矩阵，返回其面积。

约束
----
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 300
- matrix[i][j] in {'0', '1'}

提示
----
卡住超过 25 分钟再去看 09_dp/NOTES.md。
（dp[i][j] = 以 (i,j) 为右下角的最大正方形边长 = 1 + min(上, 左, 左上)）

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
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([["1", "0", "1", "0", "0"],
          ["1", "0", "1", "1", "1"],
          ["1", "1", "1", "1", "1"],
          ["1", "0", "0", "1", "0"]], 4),
        ([["0", "1"], ["1", "0"]], 1),
        ([["0"]], 0),
        ([["1"]], 1),
        ([["0", "0"], ["0", "0"]], 0),
    ]
    passed = 0
    for i, (matrix, expected) in enumerate(cases, 1):
        actual = sol.maximalSquare([row[:] for row in matrix])
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
