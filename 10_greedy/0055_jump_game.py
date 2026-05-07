"""
LeetCode 55. Jump Game / 跳跃游戏  (Medium)
Link: https://leetcode.cn/problems/jump-game/

题目描述
--------
给定非负整数数组 nums，最初位于数组第一个下标。
nums[i] 表示在该位置可以跳跃的最大长度。判断是否能到达最后一个下标。

约束
----
- 1 <= nums.length <= 10^4
- 0 <= nums[i] <= 10^5

提示
----
卡住超过 25 分钟再去看 10_greedy/NOTES.md 的「跳跃游戏」模板。

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
    def canJump(self, nums: List[int]) -> bool:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
        ([0], True),
        ([2, 0, 0], True),
        ([1, 0, 1, 0], False),
        ([1, 2], True),
    ]
    passed = 0
    for i, (nums, expected) in enumerate(cases, 1):
        actual = sol.canJump(nums)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: nums={nums!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
