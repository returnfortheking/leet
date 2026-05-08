"""
LeetCode 53. Maximum Subarray / 最大子数组和  (Medium)
Link: https://leetcode.cn/problems/maximum-subarray/

题目描述
--------
给定整数数组 nums，找一个具有最大和的连续子数组，返回该最大和。

约束
----
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

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
    def maxSubArray(self, nums: List[int]) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),   # [4,-1,2,1]
        ([1], 1),
        ([5, 4, -1, 7, 8], 23),
        ([-1], -1),
        ([-2, -1], -1),
        ([1, 2, 3, 4, 5], 15),
    ]
    passed = 0
    for i, (nums, expected) in enumerate(cases, 1):
        actual = sol.maxSubArray(nums)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: nums={nums!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
