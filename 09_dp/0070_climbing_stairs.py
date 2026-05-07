"""
LeetCode 70. Climbing Stairs / 爬楼梯  (Easy)
Link: https://leetcode.cn/problems/climbing-stairs/

题目描述
--------
有 n 级台阶，每次可以跨 1 步或 2 步。返回到达第 n 级有多少种不同方法。

约束
----
- 1 <= n <= 45

提示
----
卡住超过 25 分钟再去看 09_dp/NOTES.md。
（最经典的入门 DP；递推关系等同于斐波那契）

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
    def climbStairs(self, n: int) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        (1, 1),
        (2, 2),
        (3, 3),
        (5, 8),
        (10, 89),
        (45, 1836311903),
    ]
    passed = 0
    for i, (n, expected) in enumerate(cases, 1):
        actual = sol.climbStairs(n)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: n={n}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
