"""
LeetCode 394. Decode String / 字符串解码  (Medium)
Link: https://leetcode.cn/problems/decode-string/

题目描述
--------
编码规则 k[encoded_string] 表示 encoded_string 重复 k 次（k 是正整数；可嵌套）。
给定符合规则的编码字符串 s，返回解码后的字符串。
原始数据不包含数字；所有数字仅作为重复次数。

例如 "3[a2[c]]" → "accaccacc"。

约束
----
- 1 <= s.length <= 30
- 1 <= 重复次数 <= 300
- s 由小写英文字母、数字、'[' 和 ']' 组成

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
    def decodeString(self, s: str) -> str:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ("3[a]2[bc]", "aaabcbc"),
        ("3[a2[c]]", "accaccacc"),
        ("2[abc]3[cd]ef", "abcabccdcdcdef"),
        ("abc3[cd]xyz", "abccdcdcdxyz"),
        ("a", "a"),
        ("100[leetcode]", "leetcode" * 100),
    ]
    passed = 0
    for i, (s, expected) in enumerate(cases, 1):
        actual = sol.decodeString(s)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        # 长串只打印前 40 字符避免噪音
        e_show = expected if len(expected) <= 40 else expected[:40] + "...({}chars)".format(len(expected))
        a_show = (actual if isinstance(actual, str) and len(actual) <= 40
                  else (actual[:40] + "...({}chars)".format(len(actual))) if isinstance(actual, str) else actual)
        print(f"[{status}] Case {i}: s={s!r}  expected={e_show!r}  actual={a_show!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
