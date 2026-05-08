"""
LeetCode 692. Top K Frequent Words / 前 K 个高频单词  (Medium)
Link: https://leetcode.cn/problems/top-k-frequent-words/

题目描述
--------
给定单词列表 words 和整数 k，返回出现次数最多的前 k 个单词。
排序规则：先按频次降序；频次相同则按字典序升序。

约束
----
- 1 <= words.length <= 500
- 1 <= words[i].length <= 10
- words[i] 仅由小写字母组成
- 1 <= k <= words 中不同单词的数量

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
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ((["i", "love", "leetcode", "i", "love", "coding"], 2), ["i", "love"]),
        ((["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4),
         ["the", "is", "sunny", "day"]),
        ((["a"], 1), ["a"]),
        ((["a", "aa", "aaa"], 3), ["a", "aa", "aaa"]),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = sol.topKFrequent(*args)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: args={args!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
