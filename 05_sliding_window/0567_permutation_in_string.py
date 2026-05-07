"""
LeetCode 567. Permutation in String / 字符串的排列  (Medium)
Link: https://leetcode.cn/problems/permutation-in-string/

题目描述
--------
给定两个字符串 s1 和 s2，判断 s2 是否包含 s1 的某个排列作为子串。
等价于：s2 是否存在一个长度等于 len(s1) 的子串，其字母频次与 s1 完全相同。

约束
----
- 1 <= s1.length, s2.length <= 10^4
- 仅小写英文字母

提示
----
卡住超过 25 分钟再去看 05_sliding_window/NOTES.md 的「定长滑窗」模板。

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
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        (("ab", "eidbaooo"), True),
        (("ab", "eidboaoo"), False),
        (("a", "a"), True),
        (("abc", "ab"), False),
        (("hello", "ooolleoooleh"), False),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = sol.checkInclusion(*args)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: args={args!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
