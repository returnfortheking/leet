"""
LeetCode 127. Word Ladder / 单词接龙  (Hard)
Link: https://leetcode.cn/problems/word-ladder/

题目描述
--------
给定起始单词 beginWord、目标单词 endWord、单词字典 wordList。
每次只能修改一个字母（且修改后必须仍是 wordList 中的单词，含 endWord）。
返回从 beginWord 转换到 endWord 的最短转换序列长度（包含两端点）；
不可达返回 0。注意 beginWord 不要求在 wordList 中。

约束
----
- 1 <= beginWord.length <= 10
- endWord.length == beginWord.length
- 1 <= wordList.length <= 5000
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
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        (("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 5),
        (("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0),       # endWord 不在
        (("a", "c", ["a", "b", "c"]), 2),
        (("hot", "dog", ["hot", "dog"]), 0),                            # 两词差太多
        (("hot", "dog", ["hot", "dog", "dot"]), 3),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = sol.ladderLength(*args)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: args={args!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
