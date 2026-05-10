"""
LeetCode 322. Coin Change / 零钱兑换  (Medium)
Link: https://leetcode.cn/problems/coin-change/

题目描述
--------
给定不同面额的硬币 coins（每种无限多）和总金额 amount，
求凑成总金额所需的最少硬币个数。如果不可能，返回 -1。

约束
----
- 1 <= coins.length <= 12
- 1 <= coins[i] <= 2^31 - 1
- 0 <= amount <= 10^4

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
    def coinChange(self, coins: List[int], amount: int) -> int:
        # TODO: 在这里写你的解法
        # c
        n = len(coins)
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if c > i:
                    continue
                else:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1


def test():
    sol = Solution()
    cases = [
        # LeetCode 题面 example
        (([1, 2, 5], 11), 3),                  # 5+5+1
        (([2], 3), -1),                        # 凑不出
        (([1], 0), 0),                         # amount=0
        # ★ amount=0 的多 coin 形式（dp[0] 必须 = 0，不少人会忘）
        (([1, 2, 5], 0), 0),
        # 单 coin 边界
        (([1], 2), 2),
        (([7], 7), 1),                         # 单 coin 恰好 = amount
        (([7], 14), 2),                        # 单 coin 整除 amount
        (([10], 5), -1),                       # 单 coin > amount
        # 完全背包特性（同 coin 可反复用）
        (([2], 6), 3),                         # 用 2 三次
        # 平价但凑不出（奇偶性）
        (([2, 4], 7), -1),                     # 偶数 coin 凑不出奇数 amount
        # ★ 贪心错例（必须 DP）
        (([1, 7, 10], 14), 2),                 # 7+7=2 优于 10+4*1=5
        # LeetCode 隐藏 case 风格的较复杂输入
        (([186, 419, 83, 408], 6249), 20),
        (([2, 5, 10, 1], 27), 4),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = sol.coinChange(*args)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(
            f"[{status}] Case {i}: args={args!r}  expected={expected!r}  actual={actual!r}"
        )
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
