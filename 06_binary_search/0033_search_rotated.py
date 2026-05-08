"""
LeetCode 33. Search in Rotated Sorted Array / 搜索旋转排序数组  (Medium)
Link: https://leetcode.cn/problems/search-in-rotated-sorted-array/

题目描述
--------
原本严格升序的数组在某未知下标处被旋转，得到 nums。
给定 target，返回其下标，不存在返回 -1。要求 O(log n)。

约束
----
- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4
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
    def search(self, nums: List[int], target: int) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        (([4, 5, 6, 7, 0, 1, 2], 0), 4),
        (([4, 5, 6, 7, 0, 1, 2], 3), -1),
        (([1], 0), -1),
        (([1, 3], 3), 1),
        (([5, 1, 3], 3), 2),
        (([1, 2, 3, 4, 5], 4), 3),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = sol.search(*args)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: args={args!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
