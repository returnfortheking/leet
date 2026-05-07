"""
LeetCode 198. House Robber / 打家劫舍  (Medium)
Link: https://leetcode.cn/problems/house-robber/

题目描述
--------
沿街排列着 n 户人家，每家有钱 nums[i]。你不能同时偷相邻两户（会触发警报）。
返回不触发警报情况下能偷到的最大金额。

约束
----
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 400

提示
----
卡住超过 25 分钟再去看 09_dp/NOTES.md 的「一维线性 DP」模板。

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
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
        ([2, 1, 1, 2], 4),
        ([1], 1),
        ([0], 0),
        ([100, 1, 100, 1, 100], 300),
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
