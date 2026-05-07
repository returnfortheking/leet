"""
LeetCode 312. Burst Balloons / 戳气球  (Hard)
Link: https://leetcode.cn/problems/burst-balloons/

题目描述
--------
n 个气球排成一排，第 i 个气球上有数字 nums[i]。每次戳破一个气球 i，
你将得到 nums[i-1] * nums[i] * nums[i+1] 的硬币（越界视作 1）。
戳破后两侧气球变得相邻。返回戳破所有气球能获得的最大硬币数。

约束
----
- n == nums.length
- 1 <= n <= 300
- 0 <= nums[i] <= 100

提示
----
卡住超过 25 分钟再去看 09_dp/NOTES.md 的「区间 DP」模板。
（关键转换：枚举"最后被戳的气球 k"，划分为 (i,k) 与 (k,j) 两段独立子问题）

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
    def maxCoins(self, nums: List[int]) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([3, 1, 5, 8], 167),
        ([1, 5], 10),
        ([1], 1),
        ([5], 5),
        ([7, 9, 8, 0, 7, 1, 3, 5, 5, 2, 3], 4806),
    ]
    passed = 0
    for i, (nums, expected) in enumerate(cases, 1):
        actual = sol.maxCoins(list(nums))
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: nums={nums!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
