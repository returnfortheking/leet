"""
LeetCode 494. Target Sum / 目标和  (Medium)
Link: https://leetcode.cn/problems/target-sum/

题目描述
--------
给定非负整数数组 nums 和整数 target。
对每个元素加 '+' 或 '-' 号后求总和等于 target 的方案数。

约束
----
- 1 <= nums.length <= 20
- 0 <= nums[i] <= 1000
- 0 <= sum(nums) <= 1000
- -1000 <= target <= 1000

提示
----
卡住超过 25 分钟再去看 09_dp/NOTES.md。
（转化：设正号子集和 P，负号子集和 N，P - N = target；P = (target + sum)/2，转 0-1 背包计数）

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
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        (([1, 1, 1, 1, 1], 3), 5),
        (([1], 1), 1),
        (([1], -1), 1),
        (([1, 2, 3], 0), 2),
        (([0, 0, 0, 0, 0, 0, 0, 0, 1], 1), 256),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = sol.findTargetSumWays(*args)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: args={args!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
