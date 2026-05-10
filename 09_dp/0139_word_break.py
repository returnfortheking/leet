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
    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #     # TODO: 在这里写你的解法
    #     n = len(s)
    #     dp = [False] * (n + 1)
    #     dp[0] = True
    #     for i in range(1, n + 1):
    #         for w in wordDict:
    #             wl = len(w)
    #             if wl <= i and s[i - wl : i] == w:
    #                 dp[i] = dp[i - wl] or dp[i]
    #     return dp[n]
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # TODO: 在这里写你的解法
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for w in wordDict:
                wl = len(w)
                if wl <= i:
                    flag = s[i - wl : i] == w
                    dp[i] = dp[i] or (flag and dp[i - wl])
        return dp[n]


def test():
    sol = Solution()
    cases = [
        # LeetCode 题面 example
        (("leetcode", ["leet", "code"]), True),
        (("applepenapple", ["apple", "pen"]), True),
        (("catsandog", ["cats", "dog", "sand", "and", "cat"]), False),
        # 尺寸边界
        (("a", ["a"]), True),
        (("a", ["b"]), False),
        (("a", ["aa"]), False),                    # word 比 s 长
        # ★ 杀手用例：dp[i] 误用 OR（and/or 嵌套写错）会错答 True
        (("ab", ["a"]), False),                    # 前缀能拆但末段 'b' 不在 dict
        (("ab", ["a", "c"]), False),               # 同上更明显
        (("aaab", ["a"]), False),                  # 多步前缀拆通但末段 'b' 不在
        # word 整段
        (("abc", ["abc"]), True),
        (("abc", ["abcd"]), False),
        # word 重复使用（完全背包特性）
        (("aaaaaaa", ["aaaa", "aaa"]), True),      # 4+3
        (("aaa", ["a"]), True),                    # 同 word 三次
        (("aaa", ["aa"]), False),                  # 长度对不上
        (("aaaa", ["aa"]), True),                  # 长度对得上
        # 多 word 必须组合
        (("ab", ["a", "b"]), True),
        # 长答案需要回溯（贪心选错短词会失败）
        (("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]), True),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = sol.wordBreak(args[0], list(args[1]))
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
