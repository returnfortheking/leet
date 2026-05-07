"""
LeetCode 875. Koko Eating Bananas / 爱吃香蕉的珂珂  (Medium)
Link: https://leetcode.cn/problems/koko-eating-bananas/

题目描述
--------
有 n 堆香蕉，第 i 堆有 piles[i] 根。珂珂选定一个固定的小时速度 k 根/小时：
每小时挑一堆吃，若该堆少于 k 根则当小时只吃完该堆并结束本小时。
给定上限 h 小时，返回能吃完所有香蕉的最小整数 k。

约束
----
- 1 <= piles.length <= 10^4
- piles.length <= h <= 10^9
- 1 <= piles[i] <= 10^9

提示
----
卡住超过 25 分钟再去看 06_binary_search/NOTES.md 的「二分答案」模板。
（feasible(k) 单调：k 越大耗时越少；找最小可行 k）

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
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        (([3, 6, 7, 11], 8), 4),
        (([30, 11, 23, 4, 20], 5), 30),
        (([30, 11, 23, 4, 20], 6), 23),
        (([1], 1), 1),
        (([1000000000], 2), 500000000),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = sol.minEatingSpeed(*args)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: args={args!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
