"""
LeetCode 136. Single Number / 只出现一次的数字  (Easy)
Link: https://leetcode.cn/problems/single-number/

题目描述
--------
给定非空整数数组 nums，除了**某个元素只出现一次**外，其余每个元素均出现两次。
找出那个只出现一次的元素。要求 O(n) 时间，O(1) 额外空间。

约束
----
- 1 <= nums.length <= 3 * 10^4
- -3 * 10^4 <= nums[i] <= 3 * 10^4

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
    def singleNumber(self, nums: List[int]) -> int:
        # TODO: 在这里写你的解法
        res = 0
        for num in nums:
            res ^= num
        return res


def test():
    sol = Solution()
    cases = [
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4),
        ([1], 1),
        ([7, 3, 7], 3),
        ([-1, -1, 5], 5),
    ]
    passed = 0
    for i, (nums, expected) in enumerate(cases, 1):
        actual = sol.singleNumber(list(nums))
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(
            f"[{status}] Case {i}: nums={nums!r}  expected={expected!r}  actual={actual!r}"
        )
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
