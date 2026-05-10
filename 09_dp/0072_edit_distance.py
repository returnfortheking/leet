"""
LeetCode 72. Edit Distance / 编辑距离  (Hard)
Link: https://leetcode.cn/problems/edit-distance/

题目描述
--------
给定两个字符串 word1, word2，返回将 word1 转换成 word2 所需的最少操作次数。
每次操作可以：插入、删除、替换一个字符。

约束
----
- 0 <= word1.length, word2.length <= 500
- 仅小写英文字母

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
    def minDistance(self, word1: str, word2: str) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        # LeetCode 题面 example
        (("horse", "ros"), 3),
        (("intention", "execution"), 5),
        # 尺寸边界
        (("", ""), 0),                      # 都为空
        (("a", ""), 1),                     # 一边为空，等于另一边长度
        (("", "abc"), 3),
        (("abc", "abc"), 0),                # 完全相同
        # 单字符
        (("a", "a"), 0),
        (("a", "b"), 1),                    # 单次替换
        # 仅插入 / 仅删除
        (("ab", "abc"), 1),                 # 插入末尾
        (("abc", "ab"), 1),                 # 删除末尾
        (("ac", "abc"), 1),                 # 插入中间
        # 全替换
        (("abc", "def"), 3),
        # 经典示例
        (("kitten", "sitting"), 3),
        # 长度差异大
        (("a", "abcdef"), 5),
        (("abcdef", "a"), 5),
        # 顺序敏感（公共字符不在对应位置）
        (("ab", "ba"), 2),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = sol.minDistance(*args)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: args={args!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
