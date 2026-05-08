"""
LeetCode 5. Longest Palindromic Substring / 最长回文子串  (Medium)
Link: https://leetcode.cn/problems/longest-palindromic-substring/

题目描述
--------
给定字符串 s，返回其中最长的回文子串。

约束
----
- 1 <= s.length <= 1000
- s 仅由数字和英文字母组成

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
    def longestPalindrome(self, s: str) -> str:
        # TODO: 在这里写你的解法
        if not s:
            return ""

        def expand(l: int, r: int) -> tuple[int, int]:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l = l - 1
                r = r + 1
            return [l + 1, r - 1]

        i = 0
        res_l = 0
        res_r = 0
        for i in range(len(s)):
            l1, r1 = expand(i, i)
            l2, r2 = expand(i, i + 1)
            if r1 - l1 > res_r - res_l:
                res_l = l1
                res_r = r1
            if r2 - l2 > res_r - res_l:
                res_l = l2
                res_r = r2
        return s[res_l : res_r + 1]

    #     i = (int)(0)
    #     max = 0
    #     res = ""
    #     for i in range(s.__len__):
    #         str1 = self.Odd(s, i)
    #         if max < str1.__len__:
    #             res = str1
    #             max = str1.__len__
    #         str2 = self.Oven(s, i)
    #         if max < str2.__len__:
    #             res = str2
    #             max = str2.__len__
    #     return res

    # def Odd(s: str, pos: int) -> str:
    #     res = s[pos]
    #     i = 1
    #     while pos - i > -1 | pos + i < s.__len__:
    #         if s[pos - i] == s[pos + i]:
    #             res.append(s[pos + i])
    #             res.insert(s[pos + i], 0)
    #         else:
    #             return res
    #     return res

    # def Oven(s: str, pos: int) -> str:
    #     res = ""
    #     i = 0
    #     while pos - 1 - i > -1 | pos + i < s.__len__:
    #         if s[pos - 1 - i] == s[pos + i]:
    #             res.append(s[pos + i])
    #             res.insert(s[pos + i], 0)
    #         else:
    #             return res
    #     return res


def test():
    sol = Solution()
    # 多个有效答案：用 (输入, 期望长度) 验证；并校验 actual 是 s 的回文子串
    cases = [
        ("babad", 3),  # "bab" 或 "aba"
        ("cbbd", 2),  # "bb"
        ("a", 1),
        ("ac", 1),  # "a" 或 "c"
        ("racecar", 7),
        ("abba", 4),
    ]
    passed = 0
    for i, (s, expected_len) in enumerate(cases, 1):
        actual = sol.longestPalindrome(s)
        ok = (
            isinstance(actual, str)
            and len(actual) == expected_len
            and actual == actual[::-1]
            and actual in s
        )
        status = "PASS" if ok else "FAIL"
        print(
            f"[{status}] Case {i}: s={s!r}  expected_len={expected_len}  actual={actual!r}"
        )
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
