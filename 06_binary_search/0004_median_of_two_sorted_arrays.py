"""
LeetCode 4. Median of Two Sorted Arrays / 寻找两个正序数组的中位数  (Hard)
Link: https://leetcode.cn/problems/median-of-two-sorted-arrays/

题目描述
--------
给定两个非递减数组 nums1 和 nums2，返回它们合并后的中位数。要求 O(log(m+n))。

约束
----
- nums1.length == m, nums2.length == n
- 0 <= m, n <= 1000
- 1 <= m + n <= 2000
- -10^6 <= nums1[i], nums2[i] <= 10^6

提示
----
卡住超过 25 分钟再去看 06_binary_search/NOTES.md。
（思路：对较短数组二分切割位置；一种常见思路是「找第 k 小」递归）

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
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        (([1, 3], [2]), 2.0),
        (([1, 2], [3, 4]), 2.5),
        (([], [1]), 1.0),
        (([2], []), 2.0),
        (([1, 3, 5], [2, 4, 6]), 3.5),
        (([0, 0], [0, 0]), 0.0),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = sol.findMedianSortedArrays(*args)
        ok = actual is not None and abs(actual - expected) < 1e-9
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: args={args!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
