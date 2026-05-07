"""
LeetCode 304. Range Sum Query 2D - Immutable / 二维区域和检索 - 矩阵不可变  (Medium)
Link: https://leetcode.cn/problems/range-sum-query-2d-immutable/

题目描述
--------
设计 NumMatrix 类：
- __init__(matrix): 给定 m x n 整数矩阵 matrix
- sumRegion(row1, col1, row2, col2): 返回左上 (row1,col1) 右下 (row2,col2) 的子矩阵元素之和

要求 sumRegion 单次 O(1)。

约束
----
- 1 <= m, n <= 200
- -10^5 <= matrix[i][j] <= 10^5
- 调用次数 <= 10^4

提示
----
卡住超过 25 分钟再去看 15_prefix_sum/NOTES.md 的「二维前缀和」模板。

复杂度（解完后填）
------
init：O(?)    query：O(?)    空间：O(?)

复盘要点（解完后填）
--------
- 卡在哪一步？
- 触发器：什么样的题面应该让我立刻想到这个套路？
"""

from typing import List, Tuple, Any


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        # TODO: 在这里初始化数据结构
        pass

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # TODO: 在这里写你的解法
        pass


def run_ops(ops: List[Tuple[str, Any]]) -> List[Any]:
    out: List[Any] = []
    obj = None
    for name, args in ops:
        if name == 'init':
            obj = NumMatrix(*args)
            out.append(None)
        elif name == 'sumRegion':
            out.append(obj.sumRegion(*args))
    return out


def test():
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5],
    ]
    cases = [
        (
            [('init', ([row[:] for row in matrix],)),
             ('sumRegion', (2, 1, 4, 3)),
             ('sumRegion', (1, 1, 2, 2)),
             ('sumRegion', (1, 2, 2, 4))],
            [None, 8, 11, 12],
        ),
        (
            [('init', ([[1]],)),
             ('sumRegion', (0, 0, 0, 0))],
            [None, 1],
        ),
    ]
    passed = 0
    for i, (ops, expected) in enumerate(cases, 1):
        actual = run_ops(ops)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: expected={expected}  actual={actual}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
