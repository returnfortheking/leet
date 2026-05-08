"""
LeetCode 34. Find First and Last Position / 在排序数组中查找元素的第一和最后位置  (Medium)
Link: https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/

题目描述
--------
给定一个非递减数组 nums 和一个目标值 target，找到 target 在数组中的开始位置和
结束位置。如果不存在则返回 [-1, -1]。

约束
----
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i], target <= 10^9
- 必须 O(log n)

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
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # TODO: 在这里写你的解法
        pass


def test():
    s = Solution()
    cases = [
        (([5, 7, 7, 8, 8, 10], 8), [3, 4]),
        (([5, 7, 7, 8, 8, 10], 6), [-1, -1]),
        (([], 0), [-1, -1]),
        (([1], 1), [0, 0]),
        (([2, 2], 2), [0, 1]),
        (([1, 2, 3], 4), [-1, -1]),
        (([1, 2, 3], 0), [-1, -1]),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = s.searchRange(*args)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: args={args!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
