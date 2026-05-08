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

复杂度（解完后填）
------
时间：O(?)    空间：O(?)

复盘要点（解完后填）
--------
- 卡在哪一步？
- 触发器：什么样的题面应该让我立刻想到这个套路？

题解
--------
- 遇到边界转向，vis矩阵
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # TODO: 在这里写你的解法
        if not matrix:
            return []
        ori = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        w = len(matrix[0])
        h = len(matrix)
        vis = [[False] * w for _ in range(h)]
        count = 0
        oration = 0
        i = 0
        j = 0
        res = []
        while count < w * h:
            res.append(matrix[i][j])
            vis[i][j] = True
            i_next = i + ori[oration][0]
            j_next = j + ori[oration][1]
            if (
                i_next >= h
                or i_next < 0
                or j_next >= w
                or j_next < 0
                or vis[i_next][j_next]
            ):
                oration = (oration + 1) % len(ori)
            i = i + ori[oration][0]
            j = j + ori[oration][1]
            count += 1
        return res


class SolutionLean:
    """
    改进版 A：保持你的方向数组 + vis 标记思路，但裁掉冗余变量。

    主要变化：
    - for _ in range(m*n)  替代  while count < w*h + count += 1
    - r = c = di = 0       一行三个变量初始化
    - dirs 用 tuple，比 list 更轻量（不可变）
    - nr, nc 只算一次：转向后重算并就地更新
    - 边界判断用链式比较 0 <= nr < m，比 nr>=0 and nr<m 短

    手动测试：把下面 test() 里的 sol = Solution() 改成 sol = SolutionLean()。
    """

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]   # 右 下 左 上
        visited = [[False] * n for _ in range(m)]
        res = []
        r = c = di = 0
        for _ in range(m * n):
            res.append(matrix[r][c])
            visited[r][c] = True
            nr, nc = r + dirs[di][0], c + dirs[di][1]
            if not (0 <= nr < m and 0 <= nc < n) or visited[nr][nc]:
                di = (di + 1) % 4
                nr, nc = r + dirs[di][0], c + dirs[di][1]
            r, c = nr, nc
        return res


def test():
    sol = Solution()
    cases = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
        (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
        ),
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
