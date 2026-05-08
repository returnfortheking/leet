"""
LeetCode 503. Next Greater Element II / 下一个更大元素 II  (Medium)
Link: https://leetcode.cn/problems/next-greater-element-ii/

题目描述
--------
给定循环数组 nums（最后一个元素的下一个是第一个），对每个元素返回循环意义下
右边第一个比它大的元素；不存在填 -1。

约束
----
- 1 <= nums.length <= 10^4
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
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([1, 2, 1], [2, -1, 2]),
        ([1, 2, 3, 4, 3], [2, 3, 4, -1, 4]),
        ([5, 4, 3, 2, 1], [-1, 5, 5, 5, 5]),
        ([1], [-1]),
        ([1, 1, 1], [-1, -1, -1]),
    ]
    passed = 0
    for i, (nums, expected) in enumerate(cases, 1):
        actual = sol.nextGreaterElements(nums)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: nums={nums!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
