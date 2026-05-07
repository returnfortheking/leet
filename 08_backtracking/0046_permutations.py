"""
LeetCode 46. Permutations / 全排列  (Medium)
Link: https://leetcode.cn/problems/permutations/

题目描述
--------
给定一个不含重复数字的数组 nums，返回其所有可能的全排列。

约束
----
- 1 <= nums.length <= 6
- -10 <= nums[i] <= 10
- nums 中元素互不相同

提示
----
卡住超过 25 分钟再去看 08_backtracking/NOTES.md 的「排列型回溯」模板。

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
    def permute(self, nums: List[int]) -> List[List[int]]:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([1, 2, 3], [
            [1, 2, 3], [1, 3, 2], [2, 1, 3],
            [2, 3, 1], [3, 1, 2], [3, 2, 1],
        ]),
        ([0, 1], [[0, 1], [1, 0]]),
        ([1], [[1]]),
    ]
    passed = 0
    for i, (nums, expected) in enumerate(cases, 1):
        actual = sol.permute(nums)
        ok = actual is not None and sorted(actual) == sorted(expected)
        status = "PASS" if ok else "FAIL"
        n_actual = len(actual) if actual is not None else 0
        print(f"[{status}] Case {i}: nums={nums!r}  count_expected={len(expected)}  count_actual={n_actual}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
