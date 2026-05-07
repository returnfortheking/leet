"""
LeetCode 704. Binary Search / 二分查找  (Easy)
Link: https://leetcode.cn/problems/binary-search/

题目描述
--------
给定升序数组 nums 和目标值 target，若 target 存在则返回其下标；否则返回 -1。
要求 O(log n) 时间。

约束
----
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i], target <= 10^4
- nums 严格升序

提示
----
卡住超过 25 分钟再去看 06_binary_search/NOTES.md 的「普通二分」模板。

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
    def search(self, nums: List[int], target: int) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        (([-1, 0, 3, 5, 9, 12], 9), 4),
        (([-1, 0, 3, 5, 9, 12], 2), -1),
        (([5], 5), 0),
        (([5], -5), -1),
        (([1, 2, 3, 4, 5], 1), 0),
        (([1, 2, 3, 4, 5], 5), 4),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = sol.search(*args)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: args={args!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
