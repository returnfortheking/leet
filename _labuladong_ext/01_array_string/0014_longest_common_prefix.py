"""
LeetCode 14. Longest Common Prefix / 最长公共前缀  (Easy)
Link: https://leetcode.cn/problems/longest-common-prefix/

题目描述
--------
给定字符串数组 strs，返回所有字符串的最长公共前缀。如果不存在，返回空串。

约束
----
- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] 仅由小写英文字母组成

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
    def longestCommonPrefix2(self, strs: List[str]) -> str:
        # TODO: 在这里写你的解法
        # 前缀树？{char, list[char]}字典+按长度排序
        min_len = 10000
        for str in strs:
            if len(str) < min_len:
                min_len = len(str)
        i = 0
        j = 0
        for i in range(min_len):
            chr = strs[0][i]
            for j in range(len(strs)):
                if strs[j][i] != chr:
                    return strs[0][:i]
        return strs[0][:min_len]

    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        for chars in zip(
            *strs
        ):  # 按"列"打包：(s[0][0], s[1][0], ...), (s[0][1], s[1][1], ...) ...
            if len(set(chars)) == 1:  # 这一列全相同
                res.append(chars[0])
            else:
                break
        return "".join(res)


def test():
    sol = Solution()
    cases = [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        (["a"], "a"),
        ([""], ""),
        (["abc", "abc", "abc"], "abc"),
        (["abab", "aba", ""], ""),
    ]
    passed = 0
    for i, (strs, expected) in enumerate(cases, 1):
        actual = sol.longestCommonPrefix(strs)
        ok = actual == expected
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
