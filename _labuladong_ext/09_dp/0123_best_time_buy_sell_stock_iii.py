"""
LeetCode 123. Best Time to Buy and Sell Stock III / 买卖股票的最佳时机 III  (Hard)
Link: https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/

题目描述
--------
prices[i] 为第 i 天股价。最多完成两笔交易（买-卖算一笔），返回最大利润。
任意时刻只能持有不超过一股。

约束
----
- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^5

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
        ([3, 3, 5, 0, 0, 3, 1, 4], 6),
        ([1, 2, 3, 4, 5], 4),
        ([7, 6, 4, 3, 1], 0),
        ([1], 0),
        ([6, 1, 3, 2, 4, 7], 7),
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
