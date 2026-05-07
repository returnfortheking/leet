"""
LeetCode 974. Subarray Sums Divisible by K / 和可被 K 整除的子数组  (Medium)
Link: https://leetcode.cn/problems/subarray-sums-divisible-by-k/

题目描述
--------
给定整数数组 nums 和正整数 k，统计连续子数组中和能被 k 整除的子数组个数。

约束
----
- 1 <= nums.length <= 3 * 10^4
- -10^4 <= nums[i] <= 10^4
- 2 <= k <= 10^4

提示
----
卡住超过 25 分钟再去看 15_prefix_sum/NOTES.md。
（思路：前缀和 mod k 同余 → 哈希计数；初始 {0:1} 处理整段子数组）

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
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        (([4, 5, 0, -2, -3, 1], 5), 7),
        (([5], 9), 0),
        (([5], 5), 1),
        (([-1, 2, 9], 2), 2),
        (([1, 2, 3, 4, 5], 5), 4),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = sol.subarraysDivByK(*args)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: args={args!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
