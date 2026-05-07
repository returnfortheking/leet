"""
LeetCode 31. Next Permutation / 下一个排列  (Medium)
Link: https://leetcode.cn/problems/next-permutation/

题目描述
--------
将整数数组 nums 重新排列成下一个**字典序更大**的排列。
若已是最大排列，则重排为升序（最小）。要求**原地**修改、O(1) 额外空间。

约束
----
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 100

提示
----
卡住超过 25 分钟再去看 01_array_string/NOTES.md。
（思路：从右往左找第一个 nums[i] < nums[i+1]；再从右往左找第一个 nums[j] > nums[i]；
  swap(i, j)；reverse nums[i+1:]）

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
    def nextPermutation(self, nums: List[int]) -> None:
        """原地修改 nums。"""
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([1, 2, 3], [1, 3, 2]),
        ([3, 2, 1], [1, 2, 3]),
        ([1, 1, 5], [1, 5, 1]),
        ([1], [1]),
        ([1, 3, 2], [2, 1, 3]),
        ([2, 3, 1], [3, 1, 2]),
    ]
    passed = 0
    for i, (nums, expected) in enumerate(cases, 1):
        n = nums[:]
        sol.nextPermutation(n)
        ok = n == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: nums={nums!r}  expected={expected!r}  actual={n!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
