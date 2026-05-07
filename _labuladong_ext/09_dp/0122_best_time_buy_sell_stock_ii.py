"""
LeetCode 122. Best Time to Buy and Sell Stock II / 买卖股票的最佳时机 II  (Medium)
Link: https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/

题目描述
--------
prices[i] 为第 i 天股价。每天你可以买、卖，但任意时刻只能持有不超过一股
（卖出后可以立刻在同一天再买）。返回最大利润。

约束
----
- 1 <= prices.length <= 3 * 10^4
- 0 <= prices[i] <= 10^4

提示
----
卡住超过 25 分钟再去看 09_dp/NOTES.md。
（最简：每段上升区间都吃掉——sum(max(0, prices[i] - prices[i-1])))

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
        ([7, 1, 5, 3, 6, 4], 7),
        ([1, 2, 3, 4, 5], 4),
        ([7, 6, 4, 3, 1], 0),
        ([1], 0),
        ([2, 1, 4], 3),
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
