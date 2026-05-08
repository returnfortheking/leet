"""
LeetCode 287. Find the Duplicate Number / 寻找重复数  (Medium)
Link: https://leetcode.cn/problems/find-the-duplicate-number/

题目描述
--------
给定整数数组 nums，长度为 n+1，所有元素在 [1, n] 范围内（含端点）。
保证至少有一个重复数字，找出**那个**重复的数（答案唯一）。
要求：不能修改 nums，O(1) 额外空间，时间优于 O(n^2)。

约束
----
- 1 <= n <= 10^5
- nums.length == n + 1
- 1 <= nums[i] <= n
- 仅有一个重复整数（可能重复多次）

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
    def findDuplicate(self, nums: List[int]) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([1, 3, 4, 2, 2], 2),
        ([3, 1, 3, 4, 2], 3),
        ([1, 1], 1),
        ([1, 1, 2], 1),
        ([2, 5, 9, 6, 9, 3, 8, 9, 7, 1], 9),
    ]
    passed = 0
    for i, (nums, expected) in enumerate(cases, 1):
        actual = sol.findDuplicate(list(nums))
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: nums={nums!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
