"""
LeetCode 47. Permutations II / 全排列 II  (Medium)
Link: https://leetcode.cn/problems/permutations-ii/

题目描述
--------
给定可能包含重复元素的数组 nums，按任意顺序返回所有不重复的全排列。

约束
----
- 1 <= nums.length <= 8
- -10 <= nums[i] <= 10

提示
----
卡住超过 25 分钟再去看 08_backtracking/NOTES.md 的「排列去重」模板。
（关键：排序后跳过同层重复——nums[i]==nums[i-1] 且 used[i-1] 未使用 → continue）

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
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([1, 1, 2], [[1, 1, 2], [1, 2, 1], [2, 1, 1]]),
        ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
        ([1], [[1]]),
        ([1, 1], [[1, 1]]),
    ]
    passed = 0
    for i, (nums, expected) in enumerate(cases, 1):
        actual = sol.permuteUnique(list(nums))
        ok = actual is not None and sorted(actual) == sorted(expected)
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: nums={nums!r}  count_e={len(expected)}  count_a={len(actual) if actual else 0}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
