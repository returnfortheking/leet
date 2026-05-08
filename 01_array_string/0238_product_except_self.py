"""
LeetCode 238. Product of Array Except Self / 除自身以外数组的乘积  (Medium)
Link: https://leetcode.cn/problems/product-of-array-except-self/

题目描述
--------
给定整数数组 nums，返回长度相同的数组 answer，其中 answer[i] 等于 nums 中
除 nums[i] 之外所有元素的乘积。
要求 O(n) 时间，**不能使用除法**。进阶：O(1) 额外空间（输出数组不计）。

约束
----
- 2 <= nums.length <= 10^5
- -30 <= nums[i] <= 30
- 任何前缀/后缀积都在 32 位整数范围内

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
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
        ([2, 3], [3, 2]),
        ([1, 1], [1, 1]),
        ([0, 0], [0, 0]),
    ]
    passed = 0
    for i, (nums, expected) in enumerate(cases, 1):
        actual = sol.productExceptSelf(list(nums))
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: nums={nums!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
