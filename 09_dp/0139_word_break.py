"""
LeetCode 139. Word Break / 单词拆分  (Medium)
Link: https://leetcode.cn/problems/word-break/

题目描述
--------
给定字符串 s 和单词列表 wordDict，判断 s 能否被空格拆分成一个或多个 wordDict 中
的单词序列（每个单词可重复使用）。

约束
----
- 1 <= s.length <= 300
- 1 <= wordDict.length <= 1000
- 1 <= wordDict[i].length <= 20
- s 与 wordDict[i] 仅由小写字母组成
- wordDict 中所有词互不相同

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
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        (("leetcode", ["leet", "code"]), True),
        (("applepenapple", ["apple", "pen"]), True),
        (("catsandog", ["cats", "dog", "sand", "and", "cat"]), False),
        (("a", ["a"]), True),
        (("ab", ["a"]), False),
        (("aaaaaaa", ["aaaa", "aaa"]), True),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = sol.wordBreak(args[0], list(args[1]))
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: args={args!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
