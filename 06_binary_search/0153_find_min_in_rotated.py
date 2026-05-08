"""
LeetCode 153. Find Minimum in Rotated Sorted Array / 寻找旋转排序数组中的最小值  (Medium)
Link: https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/

题目描述
--------
原本严格升序的数组在某未知下标处被旋转，得到 nums。返回其中最小元素。
要求 O(log n)。

约束
----
- n == nums.length
- 1 <= n <= 5000
- -5000 <= nums[i] <= 5000
- nums 中元素互不相同
- nums 是某升序数组的旋转

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
    def findMin(self, nums: List[int]) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([3, 4, 5, 1, 2], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([11, 13, 15, 17], 11),     # 没旋转
        ([2, 1], 1),
        ([1], 1),
        ([5, 1, 2, 3, 4], 1),
    ]
    passed = 0
    for i, (nums, expected) in enumerate(cases, 1):
        actual = sol.findMin(nums)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: nums={nums!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
