"""
LeetCode 279. Perfect Squares / 完全平方数  (Medium)
Link: https://leetcode.cn/problems/perfect-squares/

题目描述
--------
给定正整数 n，返回**和为 n 的完全平方数的最少个数**。
（完全平方数 = 1, 4, 9, 16, ...，可重复使用同一个数）

约束
----
- 1 <= n <= 10^4

提示
----
卡住超过 25 分钟再去看 09_dp/NOTES.md。
（完全背包：dp[i] = 1 + min(dp[i - k*k] for k*k <= i)。
  也可数学解：四平方和定理（拉格朗日）+ 余数分类）

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
    def numSquares(self, n: int) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        (12, 3),    # 4 + 4 + 4
        (13, 2),    # 4 + 9
        (1, 1),
        (4, 1),
        (7, 4),     # 1+1+1+4
        (100, 1),
    ]
    passed = 0
    for i, (n, expected) in enumerate(cases, 1):
        actual = sol.numSquares(n)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: n={n}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
