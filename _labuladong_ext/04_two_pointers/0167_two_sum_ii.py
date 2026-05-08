"""
LeetCode 167. Two Sum II - Input Array Is Sorted / 两数之和 II - 输入有序数组  (Medium)
Link: https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/

题目描述
--------
给定 1-indexed 的非递减数组 numbers 和目标值 target，找出唯一一对元素使其和等于 target，
返回 [index1, index2]（1-based）。要求 O(1) 额外空间。

约束
----
- 2 <= numbers.length <= 3 * 10^4
- -1000 <= numbers[i] <= 1000
- numbers 非递减
- -1000 <= target <= 1000
- 仅存在一个有效答案

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
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        (([2, 7, 11, 15], 9), [1, 2]),
        (([2, 3, 4], 6), [1, 3]),
        (([-1, 0], -1), [1, 2]),
        (([1, 2, 3, 4, 4, 9, 56, 90], 8), [4, 5]),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = sol.twoSum(*args)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: args={args!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
