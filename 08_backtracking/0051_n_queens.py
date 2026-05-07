"""
LeetCode 51. N-Queens / N 皇后  (Hard)
Link: https://leetcode.cn/problems/n-queens/

题目描述
--------
在 n x n 棋盘上放置 n 个皇后，使得任意两个皇后不在同一行、列或对角线。
返回所有不同的合法摆法。每种摆法用一组字符串表示，'Q' 表示皇后位置，'.' 表示空格。

约束
----
- 1 <= n <= 9

提示
----
卡住超过 25 分钟再去看 08_backtracking/NOTES.md 的「N 皇后 / 三对角线集合」模板。

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
    def solveNQueens(self, n: int) -> List[List[str]]:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        (1, 1),
        (4, 2),
        (5, 10),
        (6, 4),
        (8, 92),
    ]
    passed = 0
    for i, (n, expected_count) in enumerate(cases, 1):
        actual = sol.solveNQueens(n)
        cnt = len(actual) if actual else 0
        # 校验：数量正确，且每个解格式合法（n 行 × n 列、每行恰好一个 Q）
        valid_format = all(
            isinstance(sol_, list) and len(sol_) == n and all(len(row) == n and row.count('Q') == 1 for row in sol_)
            for sol_ in (actual or [])
        )
        ok = cnt == expected_count and valid_format
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: n={n}  expected_count={expected_count}  actual_count={cnt}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
