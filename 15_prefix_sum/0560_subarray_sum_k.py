"""
LeetCode 560. Subarray Sum Equals K / 和为 K 的子数组  (Medium)
Link: https://leetcode.cn/problems/subarray-sum-equals-k/

题目描述
--------
给定整数数组 nums 和整数 k，统计连续子数组中和等于 k 的个数。

约束
----
- 1 <= nums.length <= 2 * 10^4
- -1000 <= nums[i] <= 1000
- -10^7 <= k <= 10^7

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
    def subarraySum(self, nums: List[int], k: int) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        (([1, 1, 1], 2), 2),
        (([1, 2, 3], 3), 2),
        (([1], 0), 0),
        (([1, -1, 0], 0), 3),
        (([3, 4, 7, 2, -3, 1, 4, 2], 7), 4),
        (([0, 0, 0], 0), 6),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = sol.subarraySum(*args)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: args={args!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
