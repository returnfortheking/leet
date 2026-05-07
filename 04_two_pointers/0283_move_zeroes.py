"""
LeetCode 283. Move Zeroes / 移动零  (Easy)
Link: https://leetcode.cn/problems/move-zeroes/

题目描述
--------
给定数组 nums，**原地**将所有 0 移到数组末尾，同时保持非零元素的相对顺序。
要求最少操作次数，O(1) 额外空间。

约束
----
- 1 <= nums.length <= 10^4
- -2^31 <= nums[i] <= 2^31 - 1

提示
----
卡住超过 25 分钟再去看 04_two_pointers/NOTES.md 的「快慢指针」模板。

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
    def moveZeroes(self, nums: List[int]) -> None:
        """原地修改 nums。"""
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0], [0]),
        ([1], [1]),
        ([0, 0, 1], [1, 0, 0]),
        ([1, 0, 1], [1, 1, 0]),
        ([1, 2, 3], [1, 2, 3]),
    ]
    passed = 0
    for i, (nums, expected) in enumerate(cases, 1):
        nums_copy = nums[:]
        sol.moveZeroes(nums_copy)
        ok = nums_copy == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: nums={nums!r}  expected={expected!r}  actual={nums_copy!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
