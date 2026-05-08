"""
LeetCode 714. Best Time to Buy and Sell Stock with Transaction Fee / 含手续费的买卖股票  (Medium)
Link: https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

题目描述
--------
prices[i] 为第 i 天股价，每完成一笔交易需要支付 fee 手续费。
可多次交易，任何时候只能持有不超过一股。返回最大利润。

约束
----
- 1 <= prices.length <= 5 * 10^4
- 1 <= prices[i] < 5 * 10^4
- 0 <= fee < 5 * 10^4

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
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        (([1, 3, 2, 8, 4, 9], 2), 8),
        (([1, 3, 7, 5, 10, 3], 3), 6),
        (([1], 1), 0),
        (([5, 4, 3, 2, 1], 1), 0),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = sol.maxProfit(*args)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: args={args!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
