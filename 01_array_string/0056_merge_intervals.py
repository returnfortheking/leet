"""
LeetCode 56. Merge Intervals / 合并区间  (Medium)
Link: https://leetcode.cn/problems/merge-intervals/

题目描述
--------
给定多组区间 intervals[i] = [start_i, end_i]，合并所有重叠的区间，
返回不重叠的区间列表（覆盖所有输入区间的最小集合）。

约束
----
- 1 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= start_i <= end_i <= 10^4

提示
----
卡住超过 25 分钟再去看 01_array_string/NOTES.md。
（思路：按起点排序，扫描时合并相邻可重叠区间）

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
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
        ([[1, 4], [2, 3]], [[1, 4]]),
        ([[1, 4]], [[1, 4]]),
        ([[1, 4], [0, 4]], [[0, 4]]),
        ([[1, 4], [0, 0]], [[0, 0], [1, 4]]),
    ]
    passed = 0
    for i, (intervals, expected) in enumerate(cases, 1):
        actual = sol.merge([row[:] for row in intervals])
        ok = actual is not None and sorted(actual) == sorted(expected)
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: intervals={intervals!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
