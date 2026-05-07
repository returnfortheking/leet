"""
LeetCode 90. Subsets II / 子集 II  (Medium)
Link: https://leetcode.cn/problems/subsets-ii/

题目描述
--------
给定可能含重复元素的整数数组 nums，返回所有可能的不重复子集（解集中不能含重复的子集）。
返回顺序任意。

约束
----
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10

提示
----
卡住超过 25 分钟再去看 08_backtracking/NOTES.md 的「含重复元素去重」模板。

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
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([1, 2, 2], [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]),
        ([0], [[], [0]]),
        ([4, 4, 4, 1, 4], [[], [1], [4], [1, 4], [4, 4], [1, 4, 4], [4, 4, 4], [1, 4, 4, 4], [4, 4, 4, 4], [1, 4, 4, 4, 4]]),
    ]
    passed = 0
    for i, (nums, expected) in enumerate(cases, 1):
        actual = sol.subsetsWithDup(list(nums))
        norm_a = sorted(sorted(s) for s in actual) if actual else []
        norm_e = sorted(sorted(s) for s in expected)
        ok = norm_a == norm_e
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: nums={nums!r}  count_e={len(expected)}  count_a={len(actual) if actual else 0}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
