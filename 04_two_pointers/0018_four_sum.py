"""
LeetCode 18. 4Sum / 四数之和  (Medium)
Link: https://leetcode.cn/problems/4sum/

题目描述
--------
给定整数数组 nums 和目标值 target，返回所有不重复的四元组 [a, b, c, d]，
满足下标互不相同且 a + b + c + d == target。
四元组本身的顺序不限，但结果中不能有重复的四元组。

约束
----
- 1 <= nums.length <= 200
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9

提示
----
卡住超过 25 分钟再去看 04_two_pointers/NOTES.md。
（思路：排序 + 双层 for + 内层左右双指针；四层去重）

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
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        (([1, 0, -1, 0, -2, 2], 0), [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
        (([2, 2, 2, 2, 2], 8), [[2, 2, 2, 2]]),
        (([1, 2, 3, 4], 100), []),
        (([0, 0, 0, 0], 0), [[0, 0, 0, 0]]),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = sol.fourSum(list(args[0]), args[1])
        norm_actual = sorted(sorted(q) for q in actual) if actual else []
        norm_expected = sorted(sorted(q) for q in expected)
        ok = norm_actual == norm_expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: args={args!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
