"""
LeetCode 152. Maximum Product Subarray / 乘积最大子数组  (Medium)
Link: https://leetcode.cn/problems/maximum-product-subarray/

题目描述
--------
给定整数数组 nums，找一个连续子数组使其乘积最大，返回该最大乘积。
保证最终结果是 32 位整数。

约束
----
- 1 <= nums.length <= 2 * 10^4
- -10 <= nums[i] <= 10
- 任何前缀积都在 32 位整数范围内

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
    def maxProduct(self, nums: List[int]) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([2, 3, -2, 4], 6),
        ([-2, 0, -1], 0),
        ([-2, 3, -4], 24),
        ([0, 2], 2),
        ([-2], -2),
        ([-1, -2, -3, 0], 6),
    ]
    passed = 0
    for i, (nums, expected) in enumerate(cases, 1):
        actual = sol.maxProduct(nums)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: nums={nums!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
