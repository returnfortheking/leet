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

提示
----
卡住超过 25 分钟再去看 09_dp/NOTES.md 的「完全背包」模板。

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
        pass


def test():
    sol = Solution()
    cases = [
        (([1, 2, 5], 11), 3),
        (([2], 3), -1),
        (([1], 0), 0),
        (([1], 2), 2),
        (([186, 419, 83, 408], 6249), 20),
        (([2, 5, 10, 1], 27), 4),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = sol.coinChange(*args)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: args={args!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
