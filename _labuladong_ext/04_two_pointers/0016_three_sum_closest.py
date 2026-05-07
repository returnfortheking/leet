"""
LeetCode 16. 3Sum Closest / 最接近的三数之和  (Medium)
Link: https://leetcode.cn/problems/3sum-closest/

题目描述
--------
给定整数数组 nums 和目标值 target，从 nums 中选 3 个数使其和最接近 target，返回这三个数之和。
保证答案唯一。

约束
----
- 3 <= nums.length <= 500
- -1000 <= nums[i] <= 1000
- -10^4 <= target <= 10^4

提示
----
卡住超过 25 分钟再去看 04_two_pointers/NOTES.md。
（思路：排序 + 固定 i + 左右双指针；维护当前最接近的 sum）

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
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        (([-1, 2, 1, -4], 1), 2),
        (([0, 0, 0], 1), 0),
        (([1, 1, 1, 0], -100), 2),
        (([1, 1, 1, 1], 4), 3),
        (([-1, 0, 1, 1, 55], 3), 2),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = sol.threeSumClosest(*args)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: args={args!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
