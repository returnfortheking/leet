"""
LeetCode 787. Cheapest Flights Within K Stops / K 站中转内最便宜的航班  (Medium)
Link: https://leetcode.cn/problems/cheapest-flights-within-k-stops/

题目描述
--------
有 n 个城市（0..n-1）。flights[i] = [from, to, price] 表示一条单向航线。
求从 src 到 dst **最多经过 k 站中转**的最便宜价格；不存在返回 -1。

约束
----
- 1 <= n <= 100
- 0 <= flights.length <= n * (n - 1) / 2
- 0 <= src, dst < n; src != dst
- 1 <= price <= 10^4
- 0 <= k <= n - 1

提示
----
卡住超过 25 分钟再去看 14_graph/NOTES.md 的「Bellman-Ford」模板。
（中转 k 次 = 最多 k+1 条边；做 k+1 轮松弛；注意每轮基于上一轮的 dist）

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
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ((4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1), 700),
        ((3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1), 200),
        ((3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0), 500),
        ((2, [[0, 1, 1]], 0, 1, 0), 1),
        ((2, [], 0, 1, 0), -1),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = sol.findCheapestPrice(*args)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: args={args!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
