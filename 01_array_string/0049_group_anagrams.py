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

复杂度（解完后填）
------
时间：O(?)    空间：O(?)

复盘要点（解完后填）
--------
- 卡在哪一步？
- 触发器：什么样的题面应该让我立刻想到这个套路？
"""

import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # TODO: 在这里写你的解法
        dic = {}
        res = []
        for str in strs:
            tmp = tuple(sorted(str))
            if tmp not in dic:
                dic[tmp] = len(res)
                res.append([str])
            else:
                res[dic[tmp]].append(str)
        return res

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        # TODO: 在这里写你的解法
        mp = collections.defaultdict(list)
        res = []
        for str in strs:
            key = "".join(sorted(str))
            mp[key].append(str)
        return list(mp.values())


def test():
    sol = Solution()
    cases = [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
        ),
        ([""], [[""]]),
        (["a"], [["a"]]),
        (["abc", "bca", "cab", "xyz", "zyx"], [["abc", "bca", "cab"], ["xyz", "zyx"]]),
    ]
    passed = 0
    for i, (strs, expected) in enumerate(cases, 1):
        actual = sol.groupAnagrams(list(strs))
        # 顺序无关：把每组排序，再把组排序
        norm_a = sorted(sorted(g) for g in (actual or []))
        norm_e = sorted(sorted(g) for g in expected)
        ok = norm_a == norm_e
        status = "PASS" if ok else "FAIL"
        print(
            f"[{status}] Case {i}: strs={strs!r}  expected={expected!r}  actual={actual!r}"
        )
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
