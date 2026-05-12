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
        n = len(nums)
        if n == 0:
            return 0
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = nums[0]
        for i in range(1, n):
            if i > 1:
                dp[i][0] = max(dp[i - 2][0], dp[i - 1][1]) + nums[i]
                dp[i][1] = max(dp[i - 1][0], dp[i - 1][1])
            else:
                dp[i][0] = nums[i]
                dp[i][1] = nums[i - 1]
        return max(dp[n - 1][0], dp[n - 1][1])


def test():
    sol = Solution()
    cases = [
        # LeetCode 题面 example
        ([1, 2, 3, 1], 4),  # 1+3
        ([2, 7, 9, 3, 1], 12),  # 2+9+1
        # 尺寸边界
        ([1], 1),
        ([0], 0),
        # 两户：必须二选一
        ([3, 1], 3),
        ([1, 3], 3),
        ([3, 3], 3),  # 等值二选一
        # 全相同
        ([3, 3, 3], 6),  # 偷 0+2
        ([5, 5, 5, 5], 10),  # 0+2 或 1+3
        # 严格升
        ([1, 2, 3, 4, 5], 9),  # 1+3+5
        # 全 0
        ([0, 0, 0], 0),
        # 高低交替（贪心可能错）
        ([100, 1, 100, 1, 100], 300),
        # 隔一个的高值更优（DP 必须）
        ([2, 1, 1, 2], 4),  # 偷 0+3 = 4，不是 0+2 = 3
        # 大约束（约束 length <= 100, val <= 400）
        ([400] * 100, 20000),  # 所有偶数下标 = 50 户 × 400
    ]
    passed = 0
    for i, (nums, expected) in enumerate(cases, 1):
        actual = sol.rob(nums)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(
            f"[{status}] Case {i}: nums={nums!r}  expected={expected!r}  actual={actual!r}"
        )
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
