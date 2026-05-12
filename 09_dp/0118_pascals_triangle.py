"""
LeetCode 118. Pascal's Triangle / 杨辉三角  (Easy)
Link: https://leetcode.cn/problems/pascals-triangle/

题目描述
--------
给定非负整数 numRows，生成杨辉三角的前 numRows 行。
每行从 1 开始、以 1 结束；中间元素 = 上一行的左+右两数之和。

约束
----
- 1 <= numRows <= 30

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
    def generate(self, numRows: int) -> List[List[int]]:
        # TODO: 在这里写你的解法
        pre = [1]
        res = [pre]
        for i in range(1, numRows):
            l = [0] * (i + 1)
            l[0] = l[-1] = 1
            for j in range(1, i):
                l[j] = pre[j - 1] + pre[j]
            res.append(l)
            pre = l
        return res


def test():
    sol = Solution()
    cases = [
        # LeetCode 题面 example
        (1, [[1]]),
        (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
        # 尺寸边界
        (2, [[1], [1, 1]]),
        (3, [[1], [1, 1], [1, 2, 1]]),
        (4, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]),
        # 较深（验证递推无误）
        (
            6,
            [
                [1],
                [1, 1],
                [1, 2, 1],
                [1, 3, 3, 1],
                [1, 4, 6, 4, 1],
                [1, 5, 10, 10, 5, 1],
            ],
        ),
        (
            7,
            [
                [1],
                [1, 1],
                [1, 2, 1],
                [1, 3, 3, 1],
                [1, 4, 6, 4, 1],
                [1, 5, 10, 10, 5, 1],
                [1, 6, 15, 20, 15, 6, 1],
            ],
        ),
    ]
    passed = 0
    for i, (n, expected) in enumerate(cases, 1):
        actual = sol.generate(n)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: n={n}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
