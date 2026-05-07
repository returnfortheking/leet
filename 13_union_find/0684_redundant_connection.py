"""
LeetCode 684. Redundant Connection / 冗余连接  (Medium)
Link: https://leetcode.cn/problems/redundant-connection/

题目描述
--------
原本是一棵 n 节点树（节点编号 1..n），现在多加了一条边形成一个环。
给定 n-1+1 = n 条边的列表 edges（无向）。返回那条多余的边
（如果存在多个，返回在 edges 中**最后**出现的那条）。

约束
----
- n == edges.length
- 3 <= n <= 1000
- edges[i].length == 2
- 1 <= edges[i][0], edges[i][1] <= n
- 无自环

提示
----
卡住超过 25 分钟再去看 13_union_find/NOTES.md。
（思路：一边加边一边并查集；首次发现两端已在同一连通块时，这条边就是多余的）

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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([[1, 2], [1, 3], [2, 3]], [2, 3]),
        ([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]], [1, 4]),
        ([[1, 2], [2, 3], [1, 3]], [1, 3]),
    ]
    passed = 0
    for i, (edges, expected) in enumerate(cases, 1):
        actual = sol.findRedundantConnection([row[:] for row in edges])
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: edges={edges!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
