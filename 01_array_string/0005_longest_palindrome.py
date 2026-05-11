"""
LeetCode 5. Longest Palindromic Substring / 最长回文子串  (Medium)
Link: https://leetcode.cn/problems/longest-palindromic-substring/

题目描述
--------
给定字符串 s，返回其中最长的回文子串。

约束
----
- 1 <= s.length <= 1000
- s 仅由数字和英文字母组成

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
    def longestPalindrome(self, s: str) -> str:
        # TODO: 在这里写你的解法
        if not s:
            return ""

        def expand(l: int, r: int) -> tuple[int, int]:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l = l - 1
                r = r + 1
            return [l + 1, r - 1]

        i = 0
        res_l = 0
        res_r = 0
        for i in range(len(s)):
            l1, r1 = expand(i, i)
            l2, r2 = expand(i, i + 1)
            if r1 - l1 > res_r - res_l:
                res_l = l1
                res_r = r1
            if r2 - l2 > res_r - res_l:
                res_l = l2
                res_r = r2
        return s[res_l : res_r + 1]

    #     i = (int)(0)
    #     max = 0
    #     res = ""
    #     for i in range(s.__len__):
    #         str1 = self.Odd(s, i)
    #         if max < str1.__len__:
    #             res = str1
    #             max = str1.__len__
    #         str2 = self.Oven(s, i)
    #         if max < str2.__len__:
    #             res = str2
    #             max = str2.__len__
    #     return res

    # def Odd(s: str, pos: int) -> str:
    #     res = s[pos]
    #     i = 1
    #     while pos - i > -1 | pos + i < s.__len__:
    #         if s[pos - i] == s[pos + i]:
    #             res.append(s[pos + i])
    #             res.insert(s[pos + i], 0)
    #         else:
    #             return res
    #     return res

    # def Oven(s: str, pos: int) -> str:
    #     res = ""
    #     i = 0
    #     while pos - 1 - i > -1 | pos + i < s.__len__:
    #         if s[pos - 1 - i] == s[pos + i]:
    #             res.append(s[pos + i])
    #             res.insert(s[pos + i], 0)
    #         else:
    #             return res
    #     return res


def test():
    sol = Solution()
    # 多个有效答案：用 (输入, 期望长度) 验证；并校验 actual 是 s 的回文子串
    cases = [
        ("babad", 3),  # "bab" 或 "aba"
        ("cbbd", 2),  # "bb"
        ("a", 1),
        ("ac", 1),  # "a" 或 "c"
        ("racecar", 7),
        ("abba", 4),
    ]
    passed = 0
    for i, (s, expected_len) in enumerate(cases, 1):
        actual = sol.longestPalindrome(s)
        ok = (
            isinstance(actual, str)
            and len(actual) == expected_len
            and actual == actual[::-1]
            and actual in s
        )
        status = "PASS" if ok else "FAIL"
        print(
            f"[{status}] Case {i}: s={s!r}  expected_len={expected_len}  actual={actual!r}"
        )
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()


# ============================================================================
# 复盘笔记（做完题再看；避免提前剧透）
# ============================================================================
# # 0005 最长回文子串 — 复盘
#
# > 题：[0005_longest_palindrome.py](../01_array_string/0005_longest_palindrome.py)
# > 日期：2026-04-30
# > 套路：中心扩展（详见 [01_array_string/NOTES.md](../01_array_string/NOTES.md)）
#
# ## 我的第一版踩了哪些坑
#
# 按"致命"→"逻辑"分级。括号里链接到 [pitfalls.md](pitfalls.md) 的主题归类。
#
# ### 致命（让代码跑不起来）
#
# 1. **`s.__len__` 当成数字用** → `TypeError`。Python 里取长度永远 `len(s)`。`__len__` 不加括号是方法对象。  〔[Python 取长度](pitfalls.md#长度--大小)〕
# 2. **类内方法忘了 `self`**：`def Odd(s, pos):` 调用 `self.Odd(...)` 时 self 实例会被错误绑给 s 参数。Python 不像 TS / Java 隐式注入 this，必须显式声明 `self`。  〔[OOP/方法定义](pitfalls.md#类与方法)〕
# 3. **`|` 当逻辑或用**：`pos - i > -1 | pos + i < ...` 里的 `|` 是按位或，且优先级比 `<` `>` 高，整句解析错。Python 的逻辑或是 `or`、与是 `and`，不是 TS 的 `||` `&&`。  〔[逻辑运算符](pitfalls.md#逻辑运算符)〕
# 4. **while 没递增 `i`** → 死循环（任何语言通病，但加 `i += 1` 即可）。
# 5. **字符串当 list 用**：`res = s[pos]; res.append(...)` —— 字符串**不可变**，没有 append/insert。要积字符要么用 `list` + `"".join(...)`，要么直接维护下标做切片。  〔[字符串不可变](pitfalls.md#字符串不可变)〕
#
# ### 逻辑/风格
#
# 6. `i = (int)(0)` → C/TS 风格 cast 不存在。Python 是 `int(0)`（函数）；这里直接 `i = 0` 就够。  〔[类型转换](pitfalls.md#类型转换)〕
# 7. `max = 0` 覆盖了 Python 内置 `max()` 函数。同名变量不会立即报错，但等你想 `max(a, b)` 时会拿到一个 int 不可调用，调试很费劲。建议永远不要用 `max` `min` `sum` `list` `dict` `set` `id` `type` `input` `open` 这些当变量名。  〔[内置名遮蔽](pitfalls.md#变量名遮蔽内置)〕
# 8. `res.insert(s[pos + i], 0)` 参数顺序反了。`list.insert(index, value)`，第一个是位置，第二个是值。  〔[list API 参数顺序](pitfalls.md#list-api)〕
# 9. `Oven` → `Even`（拼写）。
# 10. 中心扩展的实现思路绕了：**正确套路是只记录 (l, r) 区间，扩展结束后切片 s[l:r+1]**。不要一个一个字符积。
#
# ## 这次学到的
#
# - TS 写惯了，最容易"自动"写出来的错都集中在 **取长度（`.length` → `len()`）** 和 **逻辑运算符（`||` → `or`）** 上，把这两条肌肉记忆改过来能省一半 bug。
# - Python 字符串和列表的不可变区别要刻进脑子。看到题面里"要修改字符序列"立刻 `s = list(s)`。
# - 写实例方法时，**一开始就先打 `def f(self, ...):` 再写参数**——别等调用时才想起来。
# - **切片左闭右开**：`s[l : r + 1]` 里的 `+1` 不是 hack——Python 切片 `[a, b)` 不含 b，要把下标 r 这个字符包进来 stop 必须 = r+1。详见 [pitfalls.md § 切片左闭右开](pitfalls.md#切片左闭右开)。
#
# ## 修复后的关键片段（中心扩展标准写法）
#
# ```python
# def expand(l: int, r: int) -> tuple[int, int]:
#     while l >= 0 and r < len(s) and s[l] == s[r]:
#         l -= 1
#         r += 1
#     return l + 1, r - 1
# ```
#
# 整体结构在 [01_array_string/NOTES.md](../01_array_string/NOTES.md) 里有完整模板。
