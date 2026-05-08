"""
LeetCode 189. Rotate Array / 轮转数组  (Medium)
Link: https://leetcode.cn/problems/rotate-array/

题目描述
--------
给定整数数组 nums 和非负整数 k，将数组中的元素整体向右轮转 k 个位置。
要求**原地**修改数组（进阶要求 O(1) 额外空间）。

约束
----
- 1 <= nums.length <= 10^5
- -2^31 <= nums[i] <= 2^31 - 1
- 0 <= k <= 10^5

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
    def rotate(self, nums: List[int], k: int) -> None:
        """原地修改 nums。"""
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
        ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
        ([1, 2], 3, [2, 1]),
        ([1], 0, [1]),
        ([1, 2, 3], 0, [1, 2, 3]),
        ([1, 2, 3, 4], 4, [1, 2, 3, 4]),
    ]
    passed = 0
    for i, (nums, k, expected) in enumerate(cases, 1):
        nums_copy = nums[:]
        sol.rotate(nums_copy, k)
        ok = nums_copy == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: nums={nums!r} k={k}  expected={expected!r}  actual={nums_copy!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
