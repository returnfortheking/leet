"""
LeetCode 62. Unique Paths / 不同路径  (Medium)
Link: https://leetcode.cn/problems/unique-paths/

题目描述
--------
m x n 的网格，机器人从左上角走到右下角，每步只能向右或向下。
返回不同路径总数。

约束
----
- 1 <= m, n <= 100

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
    def uniquePaths(self, m: int, n: int) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        # LeetCode 题面 example
        ((3, 7), 28),
        ((3, 2), 3),
        # 尺寸边界
        ((1, 1), 1),                        # 起点 = 终点
        ((1, 10), 1),                       # 单行只有一种走法
        ((10, 1), 1),                       # 单列同上
        ((2, 2), 2),                        # 最简 2x2
        # 对称性验证（C(m+n-2, m-1) 对称）
        ((7, 3), 28),                       # = (3, 7)
        ((12, 23), 193536720),              # = (23, 12)
        # 中等大小
        ((10, 10), 48620),                  # C(18, 9)
        ((23, 12), 193536720),
        # 大网格（Python 任意精度，DP 不会溢出）
        ((20, 20), 35345263800),            # C(38, 19)
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = sol.uniquePaths(*args)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: args={args!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
