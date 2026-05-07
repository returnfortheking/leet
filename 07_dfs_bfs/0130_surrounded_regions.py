"""
LeetCode 130. Surrounded Regions / 被围绕的区域  (Medium)
Link: https://leetcode.cn/problems/surrounded-regions/

题目描述
--------
给定 m x n 的字符网格 board，元素只有 'X' 和 'O'。
将所有**完全被 X 包围**的 O 区域翻为 X；与边界相连的 O 区域保留。
原地修改 board。

约束
----
- m == board.length
- n == board[i].length
- 1 <= m, n <= 200
- board[i][j] in {'X', 'O'}

提示
----
卡住超过 25 分钟再去看 07_dfs_bfs/NOTES.md。
（思路：从边界的 O 开始 DFS / BFS，把它们临时标成 '#'；
  最后 O→X，#→O）

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
    def solve(self, board: List[List[str]]) -> None:
        """原地修改 board。"""
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([["X", "X", "X", "X"],
          ["X", "O", "O", "X"],
          ["X", "X", "O", "X"],
          ["X", "O", "X", "X"]],
         [["X", "X", "X", "X"],
          ["X", "X", "X", "X"],
          ["X", "X", "X", "X"],
          ["X", "O", "X", "X"]]),
        ([["X"]], [["X"]]),
        ([["O"]], [["O"]]),
        ([["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]],
         [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]]),
    ]
    passed = 0
    for i, (board, expected) in enumerate(cases, 1):
        b = [row[:] for row in board]
        sol.solve(b)
        ok = b == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: expected={expected!r}  actual={b!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
