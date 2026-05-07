"""
LeetCode 215. Kth Largest Element in an Array / 数组中的第 K 个最大元素  (Medium)
Link: https://leetcode.cn/problems/kth-largest-element-in-an-array/

题目描述
--------
给定整数数组 nums 和整数 k，返回数组中第 k 大的元素。

约束
----
- 1 <= k <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

提示
----
卡住超过 25 分钟再去看 12_heap_topk/NOTES.md 的「TopK 堆」模板。

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
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        (([3, 2, 1, 5, 6, 4], 2), 5),
        (([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4),
        (([1], 1), 1),
        (([7, 6, 5, 4, 3, 2, 1], 7), 1),
        (([2, 1], 2), 1),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = sol.findKthLargest(*args)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: args={args!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
