"""
LeetCode 547. Number of Provinces / 省份数量  (Medium)
Link: https://leetcode.cn/problems/number-of-provinces/

题目描述
--------
给定 n 个城市的连接矩阵 isConnected，isConnected[i][j] = 1 表示城市 i, j 直接相连。
省份 = 一组直接或间接相连的城市的集合。返回省份数量。

约束
----
- 1 <= n <= 200
- isConnected[i][i] == 1
- isConnected[i][j] == isConnected[j][i]

提示
----
卡住超过 25 分钟再去看 13_union_find/NOTES.md 的「并查集模板 + 计数连通分量」。
也可以用 DFS / BFS 求连通分量。

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
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # TODO: 在这里写你的解法
        # 提示：可以在文件内手写一个 UnionFind 类，或者用 DFS 染色。
        pass


def test():
    sol = Solution()
    cases = [
        ([[1, 1, 0], [1, 1, 0], [0, 0, 1]], 2),
        ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3),
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 1),
        ([[1]], 1),
    ]
    passed = 0
    for i, (mat, expected) in enumerate(cases, 1):
        actual = sol.findCircleNum(mat)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
