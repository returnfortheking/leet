"""
LeetCode 128. Longest Consecutive Sequence / 最长连续序列  (Medium)
Link: https://leetcode.cn/problems/longest-consecutive-sequence/

题目描述
--------
给定无序整数数组 nums，找出最长连续元素序列的长度（值连续，不要求在原数组中相邻）。
要求 O(n) 时间。

约束
----
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

提示
----
卡住超过 25 分钟再去看 13_union_find/NOTES.md。
（最简思路：用 set；只从"序列起点"（即 x-1 不在 set 中的 x）开始向上数。也可用并查集。）

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
    def longestConsecutive(self, nums: List[int]) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([], 0),
        ([1], 1),
        ([1, 2, 0, 1], 3),
    ]
    passed = 0
    for i, (nums, expected) in enumerate(cases, 1):
        actual = sol.longestConsecutive(list(nums))
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: nums={nums!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
