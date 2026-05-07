"""
LeetCode 45. Jump Game II / 跳跃游戏 II  (Medium)
Link: https://leetcode.cn/problems/jump-game-ii/

题目描述
--------
给定非负整数数组 nums，最初位于 nums[0]。nums[i] 表示在该位置可向前跳跃的最大长度。
保证总能到达终点 nums[n-1]，返回到达终点所需的最少跳跃次数。

约束
----
- 1 <= nums.length <= 10^4
- 0 <= nums[i] <= 1000
- 总能到达终点

提示
----
卡住超过 25 分钟再去看 10_greedy/NOTES.md 的「跳跃游戏 II」模板。
（思路：维护当前能到的最远位置 far、当前层边界 end；i == end 时步数 +1）

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
    def jump(self, nums: List[int]) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([2, 3, 1, 1, 4], 2),
        ([2, 3, 0, 1, 4], 2),
        ([1], 0),
        ([1, 2, 3], 2),
        ([5, 1, 1, 1, 1, 1], 1),
    ]
    passed = 0
    for i, (nums, expected) in enumerate(cases, 1):
        actual = sol.jump(nums)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: nums={nums!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
