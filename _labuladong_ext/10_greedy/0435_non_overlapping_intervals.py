"""
LeetCode 435. Non-overlapping Intervals / 无重叠区间  (Medium)
Link: https://leetcode.cn/problems/non-overlapping-intervals/

题目描述
--------
给定区间数组 intervals[i] = [start_i, end_i]，返回需要移除的最少区间数量，
使剩余区间互不重叠（端点相邻不算重叠）。

约束
----
- 1 <= intervals.length <= 10^5
- intervals[i].length == 2
- -5*10^4 <= start_i < end_i <= 5*10^4

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
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([[1, 2], [2, 3], [3, 4], [1, 3]], 1),
        ([[1, 2], [1, 2], [1, 2]], 2),
        ([[1, 2], [2, 3]], 0),
        ([[1, 100], [11, 22], [1, 11], [2, 12]], 2),
        ([[1, 2]], 0),
    ]
    passed = 0
    for i, (intervals, expected) in enumerate(cases, 1):
        actual = sol.eraseOverlapIntervals([row[:] for row in intervals])
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: intervals={intervals!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
