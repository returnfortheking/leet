"""
LeetCode 1109. Corporate Flight Bookings / 航班预订统计  (Medium)
Link: https://leetcode.cn/problems/corporate-flight-bookings/

题目描述
--------
有 n 个航班（编号 1..n）。bookings[i] = [first, last, seats] 表示在 first..last
（含端点）每个航班预订 seats 个座位。
返回长度为 n 的数组 answer，answer[i] 是航班 i+1 的总预订数。

约束
----
- 1 <= n <= 2 * 10^4
- 1 <= bookings.length <= 2 * 10^4
- bookings[i].length == 3
- 1 <= first <= last <= n
- 1 <= seats <= 10^4

提示
----
卡住超过 25 分钟再去看 15_prefix_sum/NOTES.md 的「差分」模板。

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
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        (([[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5), [10, 55, 45, 25, 25]),
        (([[1, 2, 10], [2, 2, 15]], 2), [10, 25]),
        (([[1, 1, 5]], 1), [5]),
        (([], 3), [0, 0, 0]),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = sol.corpFlightBookings(*args)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: args={args!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
