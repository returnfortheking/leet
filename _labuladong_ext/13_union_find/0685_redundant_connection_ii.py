"""
LeetCode 685. Redundant Connection II / 冗余连接 II  (Hard)
Link: https://leetcode.cn/problems/redundant-connection-ii/

题目描述
--------
原本是一棵以某节点为根的有向树（每个非根节点都有恰好一个父节点）。
现在添加了一条额外有向边导致它不再是树。给定 n 条有向边，
返回最后出现的那条多余的边（删除它能使图重新成为合法的有向树）。

约束
----
- n == edges.length
- 3 <= n <= 1000
- edges[i].length == 2

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
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([[1, 2], [1, 3], [2, 3]], [2, 3]),
        ([[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]], [4, 1]),
        ([[2, 1], [3, 1], [4, 2], [1, 4]], [2, 1]),
    ]
    passed = 0
    for i, (edges, expected) in enumerate(cases, 1):
        actual = sol.findRedundantDirectedConnection([row[:] for row in edges])
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: edges={edges!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
