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
        ((3, 7), 28),
        ((3, 2), 3),
        ((7, 3), 28),
        ((1, 1), 1),
        ((1, 10), 1),
        ((23, 12), 193536720),
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
