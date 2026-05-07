"""
LeetCode 121. Best Time to Buy and Sell Stock / 买卖股票的最佳时机  (Easy)
Link: https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/

题目描述
--------
给定数组 prices，prices[i] 是某股票第 i 天的价格。
最多买入一次、卖出一次（必须先买后卖），返回能获得的最大利润；不能盈利返回 0。

约束
----
- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4

提示
----
卡住超过 25 分钟再去看 09_dp/NOTES.md。
（思路：扫描时维护历史最低价，当前利润 = price - 历史最低）

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
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([1], 0),
        ([2, 4, 1], 2),
        ([3, 2, 6, 5, 0, 3], 4),
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
