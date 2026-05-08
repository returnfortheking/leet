"""
LeetCode 496. Next Greater Element I / 下一个更大元素 I  (Easy)
Link: https://leetcode.cn/problems/next-greater-element-i/

题目描述
--------
给定两个**互不相同**的数组 nums1 和 nums2，且 nums1 是 nums2 的子集。
对 nums1 中每个元素 x，找它在 nums2 中右侧第一个比 x 大的元素；不存在则填 -1。
返回长度等于 nums1 的答案数组。

约束
----
- 1 <= nums1.length <= nums2.length <= 1000
- 0 <= nums[i] <= 10^4
- nums1, nums2 各自元素互不相同
- nums1 中元素都出现在 nums2 中

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
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        (([4, 1, 2], [1, 3, 4, 2]), [-1, 3, -1]),
        (([2, 4], [1, 2, 3, 4]), [3, -1]),
        (([1], [1]), [-1]),
        (([1, 2], [3, 1, 2]), [2, -1]),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = sol.nextGreaterElement(*args)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: args={args!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
