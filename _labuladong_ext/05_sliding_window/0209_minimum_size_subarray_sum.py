"""
LeetCode 209. Minimum Size Subarray Sum / 长度最小的子数组  (Medium)
Link: https://leetcode.cn/problems/minimum-size-subarray-sum/

题目描述
--------
给定正整数数组 nums 和正整数 target，返回总和 >= target 的最短连续子数组长度；
若不存在则返回 0。

约束
----
- 1 <= target <= 10^9
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^4

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
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ((7, [2, 3, 1, 2, 4, 3]), 2),
        ((4, [1, 4, 4]), 1),
        ((11, [1, 1, 1, 1, 1, 1, 1, 1]), 0),
        ((15, [1, 2, 3, 4, 5]), 5),
        ((6, [10, 2, 3]), 1),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = sol.minSubArrayLen(*args)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: args={args!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
