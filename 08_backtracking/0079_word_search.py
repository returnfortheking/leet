"""
LeetCode 79. Word Search / 单词搜索  (Medium)
Link: https://leetcode.cn/problems/word-search/

题目描述
--------
给定 m x n 字符网格 board 和单词 word。判断 word 能否由网格中相邻（上下左右）字母
拼接得到，且每个格子至多使用一次。

约束
----
- m == board.length
- n == board[i].length
- 1 <= m, n <= 6
- 1 <= word.length <= 15
- 仅大小写英文字母

提示
----
卡住超过 25 分钟再去看 08_backtracking/NOTES.md。
（DFS + 回溯：访问后临时改成占位字符，回溯时恢复）

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
    def exist(self, board: List[List[str]], word: str) -> bool:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        (([
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"],
        ], "ABCCED"), True),
        (([
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"],
        ], "SEE"), True),
        (([
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"],
        ], "ABCB"), False),
        (([["A"]], "A"), True),
        (([["A"]], "B"), False),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        board = [row[:] for row in args[0]]
        actual = sol.exist(board, args[1])
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: word={args[1]!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
