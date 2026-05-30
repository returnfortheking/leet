"""
LeetCode 438. Find All Anagrams in a String / 找到字符串中所有字母异位词  (Medium)
Link: https://leetcode.cn/problems/find-all-anagrams-in-a-string/

题目描述
--------
给定字符串 s 和 p，找到 s 中所有 p 的字母异位词的起始下标，返回下标数组。
异位词：字母组成与 p 完全相同（含每个字母出现次数）。

约束
----
- 1 <= s.length, p.length <= 3 * 10^4
- s, p 仅由小写字母组成

复杂度（解完后填）
------
时间：O(?)    空间：O(?)

复盘要点（解完后填）
--------
- 卡在哪一步？
- 触发器：什么样的题面应该让我立刻想到这个套路？
"""

from typing import List
from collections import Counter, defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n = len(p), len(s)
        need = Counter(p)
        window = Counter(s[:m])
        ans = []
        if need == window:
            ans.append(0)
        for i in range(0, n - m):
            window[s[i]] -= 1
            if window[s[i]] == 0:
                del window[s[i]]
            window[s[i + m]] += 1
            if need == window:
                ans.append(i + 1)
        return ans

    def findAnagrams2(self, s: str, p: str) -> List[int]:

        lenP = len(p)
        lenS = len(s)
        if lenS < lenP:
            return []
        ans = []
        mapS = defaultdict(int)
        mapP = defaultdict(int)
        for i in range(lenP):
            mapP[p[i]] += 1
        for i in range(lenP):
            mapS[s[i]] += 1

        def equa(a, b) -> bool:
            for k in b:
                if a[k] != b[k]:
                    return False
            for k in a:
                if a[k] != b[k]:
                    return False
            return True

        l = 0
        r = lenP - 1
        while r < lenS:
            if equa(mapS, mapP):
                ans.append(l)
            if mapS[s[l]] > 1:
                mapS[s[l]] -= 1
            else:
                mapS.pop(s[l])
            l += 1
            r += 1
            if r < lenS:
                mapS[s[r]] += 1
        return ans


def test():
    sol = Solution()
    cases = [
        (("cbaebabacd", "abc"), [0, 6]),
        (("abab", "ab"), [0, 1, 2]),
        (("aaaaaa", "aa"), [0, 1, 2, 3, 4]),
        (("a", "ab"), []),
        (("ab", "ab"), [0]),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = sol.findAnagrams(*args)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(
            f"[{status}] Case {i}: args={args!r}  expected={expected!r}  actual={actual!r}"
        )
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
