"""
LeetCode 416. Partition Equal Subset Sum / 分割等和子集  (Medium)
Link: https://leetcode.cn/problems/partition-equal-subset-sum/

题目描述
--------
判断给定正整数数组 nums 是否可以被划分为两个和相等的子集。

约束
----
- 1 <= nums.length <= 200
- 1 <= nums[i] <= 100

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
    def canPartition(self, nums: List[int]) -> bool:
        # TODO: 在这里写你的解法
        total = sum(x for x in nums) / 2
        if total != int(total):
            return False
        total = (int)(total)
        dp = [False] * ((int)(total) + 1)
        dp[0] = True
        for j, num in enumerate(nums):
            for i in range(total, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[total]


def test():
    sol = Solution()
    cases = [
        # LeetCode 题面 example
        ([1, 5, 11, 5], True),                  # sum=22 target=11, {11} 或 {1,5,5}
        ([1, 2, 3, 5], False),                  # sum=11 奇数，直接 False
        # 尺寸边界
        ([1], False),                           # 单元素无法分两组
        ([1, 1], True),                         # 最简对称
        # 奇数和早退
        ([1, 2], False),                        # sum=3
        # ★ 杀手用例：0-1 写成正序会误判 True
        ([1, 2, 5], False),                     # sum=8 target=4，没有子集和=4
        ([2, 2, 3, 5], False),                  # sum=12 target=6，没有子集和=6
        # 0-1 vs 完全的核心区分（同一个数不能反复用）
        ([2], False),                           # 单 2 不能凑 1
        ([1, 1, 1, 1], True),                   # sum=4 target=2={1,1}
        # 复杂解空间
        ([3, 3, 3, 4, 5], True),                # sum=18 target=9={4,5} 或 {3,3,3}
        ([1, 2, 3, 4, 5, 6, 7], True),          # sum=28 target=14
        # 大约束
        ([1] * 100, True),                      # 100 个 1，target=50
        ([100, 100, 100, 100], True),           # target=200={100,100}
        ([1, 1, 1, 1, 100], False),             # sum=104 target=52，凑不出
    ]
    passed = 0
    for i, (nums, expected) in enumerate(cases, 1):
        actual = sol.canPartition(nums)
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
