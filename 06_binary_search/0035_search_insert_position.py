"""
LeetCode 35. Search Insert Position / 搜索插入位置  (Easy)
Link: https://leetcode.cn/problems/search-insert-position/

题目描述
--------
给定升序整数数组 nums 和目标值 target，若存在则返回其下标；
不存在则返回应**插入位置**的下标（保持数组有序）。要求 O(log n)。

约束
----
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- nums 严格升序
- -10^4 <= target <= 10^4

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
    def searchInsert(self, nums: List[int], target: int) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        (([1, 3, 5, 6], 5), 2),
        (([1, 3, 5, 6], 2), 1),
        (([1, 3, 5, 6], 7), 4),
        (([1, 3, 5, 6], 0), 0),
        (([1], 0), 0),
        (([1], 2), 1),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = sol.searchInsert(*args)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: args={args!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
