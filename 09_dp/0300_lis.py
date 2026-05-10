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
        # LeetCode 题面 example
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7, 7, 7, 7], 1),         # 全相同（严格递增长度仅 1）
        # 尺寸边界
        ([1], 1),
        ([5], 1),
        # 严格升 / 严格降
        ([1, 2, 3, 4, 5], 5),
        ([5, 4, 3, 2, 1], 1),
        # ★ 严格 vs 非严格区分（重复值不算递增）
        ([1, 1, 2, 2, 3, 3], 3),            # 严格上升只能取 1,2,3
        # 经典
        ([1, 3, 6, 7, 9, 4, 10, 5, 6], 6),  # 1,3,6,7,9,10
        # 多解（有多条等长 LIS）
        ([4, 10, 4, 3, 8, 9], 3),           # {4,8,9} 或 {3,8,9}
        # 含负数
        ([-1, -2, 0, 1], 3),                # -2,0,1
        # 长串多跳跃
        ([3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12], 6),  # 2,4,5,6,7,12
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
