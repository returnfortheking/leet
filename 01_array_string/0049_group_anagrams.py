"""
LeetCode 49. Group Anagrams / 字母异位词分组  (Medium)
Link: https://leetcode.cn/problems/group-anagrams/

题目描述
--------
给定字符串数组 strs，将字母异位词组合在一起。
异位词：所含字母相同但排列不同。返回顺序任意，每组内顺序也任意。

约束
----
- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- 仅小写英文字母

提示
----
卡住超过 25 分钟再去看 01_array_string/NOTES.md。
（思路：取一个"规范键"作为 dict 的 key —— 排序后字符串、或长度 26 的字母频次元组）

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
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        (["eat", "tea", "tan", "ate", "nat", "bat"],
         [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]),
        ([""], [[""]]),
        (["a"], [["a"]]),
        (["abc", "bca", "cab", "xyz", "zyx"],
         [["abc", "bca", "cab"], ["xyz", "zyx"]]),
    ]
    passed = 0
    for i, (strs, expected) in enumerate(cases, 1):
        actual = sol.groupAnagrams(list(strs))
        # 顺序无关：把每组排序，再把组排序
        norm_a = sorted(sorted(g) for g in (actual or []))
        norm_e = sorted(sorted(g) for g in expected)
        ok = norm_a == norm_e
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: strs={strs!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
