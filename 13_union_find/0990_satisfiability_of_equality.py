"""
LeetCode 990. Satisfiability of Equality Equations / 等式方程的可满足性  (Medium)
Link: https://leetcode.cn/problems/satisfiability-of-equality-equations/

题目描述
--------
给定字符串数组 equations，每个串形如 "a==b" 或 "a!=b"（变量名是单字母）。
判断是否能给所有变量赋整数值，使得所有方程同时成立；可以返回 True，否则返回 False。

约束
----
- 1 <= equations.length <= 500
- equations[i].length == 4
- equations[i][0], equations[i][3] 是小写字母
- equations[i][1:3] in {"==", "!="}

提示
----
卡住超过 25 分钟再去看 13_union_find/NOTES.md。
（思路：先 union 所有 == 关系，再扫描 !=，若两端已 connected 则矛盾）

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
    def equationsPossible(self, equations: List[str]) -> bool:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        (["a==b", "b!=a"], False),
        (["b==a", "a==b"], True),
        (["a==b", "b==c", "a==c"], True),
        (["a==b", "b!=c", "c==a"], False),
        (["c==c", "b==d", "x!=z"], True),
    ]
    passed = 0
    for i, (eqs, expected) in enumerate(cases, 1):
        actual = sol.equationsPossible(list(eqs))
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: eqs={eqs!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
