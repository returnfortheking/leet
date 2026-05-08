"""
LeetCode 410. Split Array Largest Sum / 分割数组的最大值  (Hard)
Link: https://leetcode.cn/problems/split-array-largest-sum/

题目描述
--------
给定非负整数数组 nums 和正整数 k，将 nums 划分为 k 个连续非空子数组，
使各子数组的和的最大值尽量小，返回这个最小化后的最大值。

约束
----
- 1 <= nums.length <= 1000
- 0 <= nums[i] <= 10^6
- 1 <= k <= min(50, nums.length)

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
    def splitArray(self, nums: List[int], k: int) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        (([7, 2, 5, 10, 8], 2), 18),
        (([1, 2, 3, 4, 5], 2), 9),
        (([1, 4, 4], 3), 4),
        (([10], 1), 10),
        (([1, 2, 3, 4, 5], 5), 5),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = sol.splitArray(*args)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: args={args!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
