"""
LeetCode 378. Kth Smallest Element in a Sorted Matrix / 有序矩阵中第 K 小的元素  (Medium)
Link: https://leetcode.cn/problems/kth-smallest-element-in-a-sorted-matrix/

题目描述
--------
n x n 矩阵 matrix，每行每列均按非递减排序。返回矩阵中第 k 小的元素。
要求空间复杂度优于 O(n^2)。

约束
----
- n == matrix.length == matrix[i].length
- 1 <= n <= 300
- -10^9 <= matrix[i][j] <= 10^9
- 1 <= k <= n^2

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
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        (([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8), 13),
        (([[-5]], 1), -5),
        (([[1, 2], [1, 3]], 2), 1),
        (([[1, 2], [1, 3]], 4), 3),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = sol.kthSmallest(*args)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: args={args!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
