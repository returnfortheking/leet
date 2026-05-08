"""
LeetCode 739. Daily Temperatures / 每日温度  (Medium)
Link: https://leetcode.cn/problems/daily-temperatures/

题目描述
--------
给定整数数组 temperatures，对于每一天，返回还需要等几天才会有更高的温度。
若不存在则填 0。

约束
----
- 1 <= temperatures.length <= 10^5
- 30 <= temperatures[i] <= 100

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
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
        ([30, 60, 90], [1, 1, 0]),
        ([90, 80, 70], [0, 0, 0]),
        ([42], [0]),
    ]
    passed = 0
    for i, (nums, expected) in enumerate(cases, 1):
        actual = sol.dailyTemperatures(nums)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: nums={nums!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
