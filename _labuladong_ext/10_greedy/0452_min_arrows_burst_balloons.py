"""
LeetCode 452. Minimum Number of Arrows to Burst Balloons / 用最少数量的箭引爆气球  (Medium)
Link: https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/

题目描述
--------
有一组气球，每个用区间 points[i] = [x_start, x_end] 表示水平延伸。
弓箭手从 x 轴朝上射箭：射在 x 处的箭会引爆所有 x_start <= x <= x_end 的气球。
返回引爆所有气球所需的最少箭数。

约束
----
- 1 <= points.length <= 10^5
- points[i].length == 2
- -2^31 <= x_start <= x_end <= 2^31 - 1

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
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([[10, 16], [2, 8], [1, 6], [7, 12]], 2),
        ([[1, 2], [3, 4], [5, 6], [7, 8]], 4),
        ([[1, 2], [2, 3], [3, 4], [4, 5]], 2),
        ([[1, 2]], 1),
        ([[-2147483648, 2147483647]], 1),
    ]
    passed = 0
    for i, (points, expected) in enumerate(cases, 1):
        actual = sol.findMinArrowShots([row[:] for row in points])
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: points={points!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
