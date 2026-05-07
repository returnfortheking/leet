"""
LeetCode 162. Find Peak Element / 寻找峰值  (Medium)
Link: https://leetcode.cn/problems/find-peak-element/

题目描述
--------
峰值定义为严格大于左右相邻元素的位置。给定整数数组 nums，返回**任意一个**峰值的下标。
约定 nums[-1] = nums[n] = -∞（边界视作负无穷）。要求 O(log n)。

约束
----
- 1 <= nums.length <= 1000
- -2^31 <= nums[i] <= 2^31 - 1
- 任意相邻元素不相等

提示
----
卡住超过 25 分钟再去看 06_binary_search/NOTES.md。
（思路：朝着 nums[mid] < nums[mid+1] 的那一侧二分，必能找到峰值）

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
    def findPeakElement(self, nums: List[int]) -> int:
        # TODO: 在这里写你的解法
        pass


def is_peak(nums, i):
    n = len(nums)
    left = nums[i - 1] if i > 0 else float('-inf')
    right = nums[i + 1] if i < n - 1 else float('-inf')
    return left < nums[i] > right


def test():
    sol = Solution()
    cases = [
        [1, 2, 3, 1],
        [1, 2, 1, 3, 5, 6, 4],
        [1],
        [1, 2],
        [2, 1],
        [3, 1, 2],
    ]
    passed = 0
    for i, nums in enumerate(cases, 1):
        actual = sol.findPeakElement(nums)
        ok = isinstance(actual, int) and 0 <= actual < len(nums) and is_peak(nums, actual)
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: nums={nums!r}  actual_idx={actual}  is_peak={ok}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
