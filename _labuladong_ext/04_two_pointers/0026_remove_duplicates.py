"""
LeetCode 26. Remove Duplicates from Sorted Array / 删除有序数组中的重复项  (Easy)
Link: https://leetcode.cn/problems/remove-duplicates-from-sorted-array/

题目描述
--------
给定一个非递减数组 nums，**原地**去重使每个元素只出现一次，并返回新长度 k。
nums 的前 k 个位置为去重后元素（顺序保持）；超出 k 的部分内容不重要。

约束
----
- 1 <= nums.length <= 3 * 10^4
- -100 <= nums[i] <= 100
- nums 非递减

提示
----
卡住超过 25 分钟再去看 04_two_pointers/NOTES.md 的「原地修改：快慢指针」模板。

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
    def removeDuplicates(self, nums: List[int]) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([1, 1, 2], 2, [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
        ([1], 1, [1]),
        ([1, 2, 3], 3, [1, 2, 3]),
        ([1, 1, 1, 1], 1, [1]),
    ]
    passed = 0
    for i, (nums, expected_k, expected_prefix) in enumerate(cases, 1):
        nums_copy = nums[:]
        k = sol.removeDuplicates(nums_copy)
        ok = k == expected_k and nums_copy[:k] == expected_prefix
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: nums={nums!r}  expected k={expected_k} prefix={expected_prefix}  actual k={k} prefix={nums_copy[:k] if k else []}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
