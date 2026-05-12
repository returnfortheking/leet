"""
LeetCode 1. Two Sum / 两数之和  (Easy)
Link: https://leetcode.cn/problems/two-sum/

题目描述
--------
给定一个整数数组 nums 和一个目标值 target，
找出数组中和为 target 的两个数，返回它们的下标。
假设每种输入只对应一个答案，且不能使用同一个元素两次。

约束
----
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i], target <= 10^9
- 只存在一个有效答案

思路
----
一遍哈希。遍历 nums，对每个 x 检查 target - x 是否在哈希里：
  在 → 找到答案，返回两个下标
  不在 → 把 (x, i) 存进哈希
单次遍历即可，因为答案对若存在，第二次遇到时第一个一定已经入表。

复杂度
------
时间：O(n)    空间：O(n)

复盘要点
--------
- 触发器：「数组里找两个元素满足 X 关系」+「无序」+「O(n) 期望」→ 哈希
- 比 brute-force O(n²) 强在哪：用空间换时间，记下"曾经见过谁"
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, num in enumerate(nums):
            if map.get(target - num, None) is not None:
                return [map[target - num], i]
            map[num] = i
            i += 1
        return []  # 题目保证有解；这行只是让类型检查器闭嘴


def test():
    s = Solution()
    cases = [
        (([2, 7, 11, 15], 9), [0, 1]),
        (([3, 2, 4], 6), [1, 2]),
        (([3, 3], 6), [0, 1]),
        (([-3, 4, 3, 90], 0), [0, 2]),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = s.twoSum(*args)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(
            f"[{status}] Case {i}: args={args!r}  expected={expected!r}  actual={actual!r}"
        )
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
