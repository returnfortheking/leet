"""
LeetCode 15. 3Sum / 三数之和  (Medium)
Link: https://leetcode.cn/problems/3sum/

题目描述
--------
给定一个整数数组 nums，返回所有不重复的三元组 [nums[i], nums[j], nums[k]]，
满足 i != j != k 且三个数之和为 0。

约束
----
- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5

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
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # TODO: 在这里写你的解法
        pass


def test():
    s = Solution()
    cases = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([0, 0, 0, 0], [[0, 0, 0]]),
        ([], []),
    ]
    passed = 0
    for i, (nums, expected) in enumerate(cases, 1):
        actual = s.threeSum(list(nums))  # 拷贝，避免 sort 污染输入
        # 答案顺序无关，比较时排序
        ok = actual is not None and sorted(actual) == sorted(expected)
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: nums={nums!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
