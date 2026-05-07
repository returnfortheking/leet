"""
LeetCode 188. Best Time to Buy and Sell Stock IV / 买卖股票的最佳时机 IV  (Hard)
Link: https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/

题目描述
--------
prices[i] 为第 i 天股价。最多完成 k 笔交易，返回最大利润。
任意时刻只能持有不超过一股。

约束
----
- 1 <= k <= 100
- 1 <= prices.length <= 1000
- 0 <= prices[i] <= 1000

提示
----
卡住超过 25 分钟再去看 09_dp/NOTES.md 的「股票状态机」模板。
（k >= n//2 时退化为 #122 任意次交易；否则用二维 DP）

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
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ((2, [2, 4, 1]), 2),
        ((2, [3, 2, 6, 5, 0, 3]), 7),
        ((1, [1, 2]), 1),
        ((1, []), 0),
        ((100, [1, 2, 3, 4, 5]), 4),
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
