"""
LeetCode 518. Coin Change II / 零钱兑换 II  (Medium)
Link: https://leetcode.cn/problems/coin-change-ii/

题目描述
--------
给定不同面额的硬币 coins（每种无限多）和总金额 amount，
返回凑成 amount 的不同组合数（组合不计顺序）。

约束
----
- 1 <= coins.length <= 300
- 1 <= coins[i] <= 5000
- 0 <= amount <= 5000
- 各 coin 互不相同

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
    def change(self, amount: int, coins: List[int]) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ((5, [1, 2, 5]), 4),
        ((3, [2]), 0),
        ((10, [10]), 1),
        ((0, [1, 2, 3]), 1),
        ((4, [1, 2, 3]), 4),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = sol.change(*args)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: args={args!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
