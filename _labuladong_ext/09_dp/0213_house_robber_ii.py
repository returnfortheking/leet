"""
LeetCode 213. House Robber II / 打家劫舍 II  (Medium)
Link: https://leetcode.cn/problems/house-robber-ii/

题目描述
--------
n 户人家围成一圈（首尾相邻视为相邻）。规则同 #198：不能偷相邻两户。
返回能偷到的最大金额。

约束
----
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 1000

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
    def rob(self, nums: List[int]) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([2, 3, 2], 3),
        ([1, 2, 3, 1], 4),
        ([1, 2, 3], 3),
        ([1], 1),
        ([1, 2], 2),
        ([200, 3, 140, 20, 10], 340),
    ]
    passed = 0
    for i, (nums, expected) in enumerate(cases, 1):
        actual = sol.rob(nums)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: nums={nums!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
