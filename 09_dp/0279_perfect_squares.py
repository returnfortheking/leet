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
        sq = []
        for i in range(1, n + 1):
            if i * i > n:
                break
            sq.append(i * i)
        dp = [n + 1] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for s in sq:
                if s <= i:
                    dp[i] = min(dp[i], dp[i - s] + 1)
        return dp[n]


def test():
    sol = Solution()
    cases = [
        # LeetCode 题面 example
        (12, 3),                        # 4+4+4
        (13, 2),                        # 9+4
        # 尺寸边界
        (1, 1),                         # 单平方数
        (2, 2),                         # 1+1
        (3, 3),                         # 1+1+1
        # 完全平方（一步到位）
        (4, 1),
        (16, 1),
        (25, 1),
        (100, 1),
        # ★ 拉格朗日四平方和定理：n = 4^k * (8m+7) 必须 4 个
        (7, 4),                         # 8*0+7：1+1+1+4
        (15, 4),                        # 8*1+7：9+4+1+1
        (23, 4),                        # 8*2+7：9+9+4+1
        (28, 4),                        # 4*(8*0+7)：16+4+4+4
        # 3 个平方足够（边界对照）
        (5, 2),                         # 4+1
        (6, 3),                         # 4+1+1
        (8, 2),                         # 4+4
        (32, 2),                        # 16+16
        # 大约束
        (9999, 4),                      # 8*1249+7
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
