"""
LeetCode 17. Letter Combinations of a Phone Number / 电话号码的字母组合  (Medium)
Link: https://leetcode.cn/problems/letter-combinations-of-a-phone-number/

题目描述
--------
给定一串数字字符串 digits（仅含 2-9），按九宫格映射返回所有可能的字母组合。
映射约定：2→abc, 3→def, 4→ghi, 5→jkl, 6→mno, 7→pqrs, 8→tuv, 9→wxyz。
空输入返回空列表，结果顺序任意。

约束
----
- 0 <= digits.length <= 4
- digits[i] in {2..9}

提示
----
卡住超过 25 分钟再去看 08_backtracking/NOTES.md。
（思路：经典回溯，按位推进）

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
    def letterCombinations(self, digits: str) -> List[str]:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
        ("", []),
        ("2", ["a", "b", "c"]),
        ("7", ["p", "q", "r", "s"]),
    ]
    passed = 0
    for i, (digits, expected) in enumerate(cases, 1):
        actual = sol.letterCombinations(digits)
        ok = actual is not None and sorted(actual) == sorted(expected)
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: digits={digits!r}  count_e={len(expected)}  count_a={len(actual) if actual else 0}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
