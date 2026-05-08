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
        pass


def test():
    sol = Solution()
    cases = [
        ([1, 5, 11, 5], True),
        ([1, 2, 3, 5], False),
        ([1, 1], True),
        ([2], False),
        ([1, 2, 3, 4, 5, 6, 7], True),
    ]
    passed = 0
    for i, (nums, expected) in enumerate(cases, 1):
        actual = sol.canPartition(nums)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: nums={nums!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
