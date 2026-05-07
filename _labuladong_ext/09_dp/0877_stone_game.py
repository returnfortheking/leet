"""
LeetCode 877. Stone Game / 石子游戏  (Medium)
Link: https://leetcode.cn/problems/stone-game/

题目描述
--------
偶数堆石子排成一行，piles[i] 是第 i 堆的数量。Alice 和 Bob 轮流取，Alice 先手。
每次只能从行的两端任选一堆全部拿走。两人都最优策略下，判断 Alice 能否赢得比赛。

约束
----
- 2 <= piles.length <= 500
- piles.length 是偶数
- 1 <= piles[i] <= 500
- sum(piles) 是奇数

提示
----
卡住超过 25 分钟再去看 09_dp/NOTES.md 的「区间 DP」模板。
（dp[i][j] = 从 piles[i..j] 出发先手能比对手多得多少；面试小技巧：先手必胜，可直接 return True）

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
    def stoneGame(self, piles: List[int]) -> bool:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([5, 3, 4, 5], True),
        ([3, 7, 2, 3], True),
        ([1, 2], True),
        ([1, 100, 1, 100], True),
    ]
    passed = 0
    for i, (piles, expected) in enumerate(cases, 1):
        actual = sol.stoneGame(piles)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: piles={piles!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
