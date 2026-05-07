"""
LeetCode 300. Longest Increasing Subsequence / 最长递增子序列  (Medium)
Link: https://leetcode.cn/problems/longest-increasing-subsequence/

题目描述
--------
给定整数数组 nums，返回最长**严格递增**子序列的长度。
子序列：在不改变原顺序的前提下任选若干元素（可以不连续）。

约束
----
- 1 <= nums.length <= 2500
- -10^4 <= nums[i] <= 10^4
- 进阶：能否做到 O(n log n)?

提示
----
卡住超过 25 分钟再去看 09_dp/NOTES.md 的「LIS」模板。
（O(n^2) DP 或 O(n log n) 二分 + tails 数组）

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
    def lengthOfLIS(self, nums: List[int]) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7, 7, 7, 7], 1),
        ([1], 1),
        ([1, 3, 6, 7, 9, 4, 10, 5, 6], 6),
    ]
    passed = 0
    for i, (nums, expected) in enumerate(cases, 1):
        actual = sol.lengthOfLIS(nums)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: nums={nums!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
