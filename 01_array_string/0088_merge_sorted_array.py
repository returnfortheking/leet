"""
LeetCode 88. Merge Sorted Array / 合并两个有序数组  (Easy)
Link: https://leetcode.cn/problems/merge-sorted-array/

题目描述
--------
给定两个非递减数组 nums1 和 nums2，长度分别为 m+? 和 n。
nums1 的实际容量为 m+n，前 m 个为有效元素，后 n 个为占位 0。
将 nums2 合并进 nums1，使 nums1 整体仍非递减；要求**原地**修改 nums1（不返回值）。

约束
----
- 0 <= m, n <= 200
- 1 <= m + n <= 200
- -10^9 <= nums1[i], nums2[i] <= 10^9

提示
----
卡住超过 25 分钟再去看 01_array_string/NOTES.md。
（思路：从尾部往前的双指针；正序合并要额外空间，倒序合并 O(1) 空间）

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
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """原地修改 nums1。"""
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        # (nums1, m, nums2, n, expected_nums1)
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ([1], 1, [], 0, [1]),
        ([0], 0, [1], 1, [1]),
        ([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6]),
        ([2, 0], 1, [1], 1, [1, 2]),
    ]
    passed = 0
    for i, (nums1, m, nums2, n, expected) in enumerate(cases, 1):
        nums1_copy = nums1[:]
        sol.merge(nums1_copy, m, nums2[:], n)
        ok = nums1_copy == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: m={m} n={n}  expected={expected!r}  actual={nums1_copy!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
