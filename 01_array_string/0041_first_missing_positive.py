"""
LeetCode 41. First Missing Positive / 缺失的第一个正数  (Hard)
Link: https://leetcode.cn/problems/first-missing-positive/

题目描述
--------
给定未排序整数数组 nums，找出其中没有出现过的最小正整数。
要求 O(n) 时间，O(1) 额外空间。

约束
----
- 1 <= nums.length <= 10^5
- -2^31 <= nums[i] <= 2^31 - 1

提示
----
卡住超过 25 分钟再去看 01_array_string/NOTES.md。
（思路：原地哈希——把 nums[i] 放到下标 nums[i]-1 处；最后扫一遍找第一个不匹配的位置）

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
    def firstMissingPositive(self, nums: List[int]) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([1, 2, 0], 3),
        ([3, 4, -1, 1], 2),
        ([7, 8, 9, 11, 12], 1),
        ([1], 2),
        ([2], 1),
        ([1, 2, 3], 4),
    ]
    passed = 0
    for i, (nums, expected) in enumerate(cases, 1):
        actual = sol.firstMissingPositive(list(nums))
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: nums={nums!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
