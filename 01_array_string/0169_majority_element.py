"""
LeetCode 169. Majority Element / 多数元素  (Easy)
Link: https://leetcode.cn/problems/majority-element/

题目描述
--------
给定数组 nums，找出其中的**多数元素**——出现次数严格大于 n/2 的元素。
保证一定存在。要求 O(n) 时间，O(1) 额外空间。

约束
----
- 1 <= nums.length <= 5 * 10^4
- -10^9 <= nums[i] <= 10^9

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
    def majorityElement(self, nums: List[int]) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([3, 2, 3], 3),
        ([2, 2, 1, 1, 1, 2, 2], 2),
        ([1], 1),
        ([1, 1, 2], 1),
        ([6, 5, 5], 5),
    ]
    passed = 0
    for i, (nums, expected) in enumerate(cases, 1):
        actual = sol.majorityElement(list(nums))
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: nums={nums!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
