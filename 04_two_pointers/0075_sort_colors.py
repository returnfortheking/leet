"""
LeetCode 75. Sort Colors / 颜色分类  (Medium)
Link: https://leetcode.cn/problems/sort-colors/

题目描述
--------
给定数组 nums，元素值仅为 0、1、2，**原地**对其排序使相同颜色相邻、按 0/1/2 顺序排列。
进阶：要求 O(n) 时间、O(1) 空间，单遍扫描。

约束
----
- n == nums.length
- 1 <= n <= 300
- nums[i] in {0, 1, 2}

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
    def sortColors(self, nums: List[int]) -> None:
        """原地修改 nums。"""
        # TODO: 在这里写你的解法
        n = len(nums)
        l = 0
        r = n - 1
        while l < r:
            while l < r and nums[l] == 0:
                l += 1
            while r > l and nums[r] != 0:
                r -= 1
            if l < r:
                nums[l], nums[r] = nums[r], nums[l]
        l = 0
        r = n - 1
        while l < r:
            while l < r and nums[l] != 2:
                l += 1
            while l < r and nums[r] == 2:
                r -= 1
            if l < r:
                nums[l], nums[r] = nums[r], nums[l]


def test():
    sol = Solution()
    cases = [
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
        ([2, 0, 1], [0, 1, 2]),
        ([0], [0]),
        ([1], [1]),
        ([2, 2, 2], [2, 2, 2]),
        ([1, 0], [0, 1]),
    ]
    passed = 0
    for i, (nums, expected) in enumerate(cases, 1):
        nums_copy = nums[:]
        sol.sortColors(nums_copy)
        ok = nums_copy == expected
        status = "PASS" if ok else "FAIL"
        print(
            f"[{status}] Case {i}: nums={nums!r}  expected={expected!r}  actual={nums_copy!r}"
        )
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
