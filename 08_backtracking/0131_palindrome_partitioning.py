"""
LeetCode 131. Palindrome Partitioning / 分割回文串  (Medium)
Link: https://leetcode.cn/problems/palindrome-partitioning/

题目描述
--------
给定字符串 s，将其切割成若干段使每一段都是回文串。返回所有可能的分割方案。
返回顺序任意。

约束
----
- 1 <= s.length <= 16
- s 仅由小写英文字母组成

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
    def partition(self, s: str) -> List[List[str]]:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ("aab", [["a", "a", "b"], ["aa", "b"]]),
        ("a", [["a"]]),
        ("ab", [["a", "b"]]),
        ("aaa", [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]]),
    ]
    passed = 0
    for i, (s, expected) in enumerate(cases, 1):
        actual = sol.partition(s)
        ok = actual is not None and sorted(actual) == sorted(expected)
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: s={s!r}  count_e={len(expected)}  count_a={len(actual) if actual else 0}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
