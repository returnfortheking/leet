"""
LeetCode 309. Best Time to Buy and Sell Stock with Cooldown / 含冷冻期的买卖股票  (Medium)
Link: https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/

题目描述
--------
prices[i] 为第 i 天股价。可多次交易，但卖出后必须冷却 1 天才能再买。返回最大利润。

约束
----
- 1 <= prices.length <= 5000
- 0 <= prices[i] <= 1000

提示
----
卡住超过 25 分钟再去看 09_dp/NOTES.md。
（三状态 DP：持有 / 不持有今天卖出 / 不持有今天没卖（含冷冻期））

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
    def maxProfit(self, prices: List[int]) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([1, 2, 3, 0, 2], 3),
        ([1], 0),
        ([1, 2], 1),
        ([6, 1, 3, 2, 4, 7], 6),
        ([2, 1, 4, 5, 2, 9, 7], 11),
    ]
    passed = 0
    for i, (prices, expected) in enumerate(cases, 1):
        actual = sol.maxProfit(prices)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: prices={prices!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
