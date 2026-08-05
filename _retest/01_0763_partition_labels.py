"""
LeetCode 763. Partition Labels / 划分字母区间  (Medium)
Link: https://leetcode.cn/problems/partition-labels/

题目描述
--------
给定字符串 s，将其划分为尽可能多的片段，使得**同一字母最多出现在一个片段中**。
返回每个片段的长度。片段拼接后必须等于 s。

约束
----
- 1 <= s.length <= 500
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
from collections import defaultdict


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        l = [n + 1] * 26
        r = [-1] * 26
        ans = []
        for i in range(n):
            pos = ord(s[i]) - ord("a")
            l[pos] = min(l[pos], i)
            r[pos] = max(l[pos], i)
        res = [(l[i], r[i]) for i in range(26)]
        res.sort()
        prevx = res[0][0]
        prevy = res[0][1]
        flag = False
        for i in range(1, 26):
            if prevy < res[i][0]:
                ans.append(prevy - prevx)
                prevx = res[i][0]
                prevy = res[i][1]
                flag = False
            else:
                prevy = res[i][1]
                flag = True
        if flag:
            ans.append(prevy - prevx)
        return ans


def test():
    sol = Solution()
    cases = [
        ("ababcbacadefegdehijhklij", [9, 7, 8]),
        ("eccbbbbdec", [10]),
        ("a", [1]),
        ("abc", [1, 1, 1]),
        ("abba", [4]),
    ]
    passed = 0
    for i, (s, expected) in enumerate(cases, 1):
        actual = sol.partitionLabels(s)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: s={s!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
