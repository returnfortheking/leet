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


# ============================================================================
# 复盘笔记（做完题再看；避免提前剧透）
# ============================================================================
# # 0014 最长公共前缀 — 复盘
#
# > 题：[0014_longest_common_prefix.py](../01_array_string/0014_longest_common_prefix.py)
# > 日期：2026-04-30
# > 套路：纵向扫描（详见 [01_array_string/NOTES.md](../01_array_string/NOTES.md)）
#
# ## 我这版踩了哪些坑
#
# ### 致命
#
# 1. **循环变量 `str` 漏出来污染了后续代码** —— 主 bug 来源。
#    ```python
#    for str in strs:           # 这个 str 在循环结束后仍 = strs 的最后一个字符串
#        ...
#    ...
#    chr = str[0][i]            # 此时 str 不是数组而是单字符串；str[0][1] 就越界
#    ```
#    错误：`IndexError: string index out of range`。
#    〔[for / while 循环变量会"漏"到循环外](pitfalls.md#for--while-循环变量会漏到循环外)〕
#
# 2. **inner break 没有跳出 outer**：双层 for 中，内层不匹配时只 break 内层，外层 i 还会继续递增。改用 **sentinel return**（找到第一个不匹配就直接 return）最干净。
#    〔[break 只跳出最内层循环](pitfalls.md#break-只跳出最内层循环)〕
#
# ### 风格 / 习惯
#
# 3. **`str`、`chr` 都覆盖了 Python 内置**（`str()` 类型转换、`chr()` 整数转字符）。这次没立即出错只是因为没用到这两个内置。下回写题：永远用 `s`、`ch`、`text`、`word` 这种命名，避开内置名。
#    〔[变量名遮蔽内置](pitfalls.md#变量名遮蔽内置)〕
#
# 4. **手写 `min_len = 10000; for s in strs: if len(s) < min_len: ...`** 太啰嗦。一行内置就能搞定：
#    ```python
#    min_len = min(len(s) for s in strs)
#    ```
#    生成器表达式在 Python 比手写循环更 Pythonic，而且**变量 `s` 局限于生成器作用域，不会泄漏到外层**——一举两得。
#
# 5. 末尾 `pass` 在 `return` 之后是死代码，可删。
#
# 6. 返回切片用了 `str[0][:j]`，但 j 是字符串下标（外层 strs 的索引），用错了变量。**列号 `i` 才是要切的位置**。
#
# ## 这次学到的
#
# - TS 的 `for (let x of xs)` 是块作用域，循环变量出循环就消失。**Python 不是**——循环跑完 `x` 还在，且等于最后一次迭代值。改肌肉记忆：循环变量起短名（`s` / `i` / `_`），但**循环外不要再读这个变量名**。
# - 双层 for 想"任一不满足就整体停"，**优先想 sentinel return**，比 flag 干净 3 倍。
# - 看到题面里有"求最小长度"、"取每个元素的某属性后聚合"这种动词，立刻条件反射 `min(... for ... in ...)` 之类的内置 + 生成器，比 for 循环短而且没循环变量泄漏问题。
#
# ## 修复后的关键片段（纵向扫描）
#
# ```python
# def longestCommonPrefix(self, strs: List[str]) -> str:
#     if not strs:
#         return ""
#     min_len = min(len(s) for s in strs)
#     for i in range(min_len):
#         ch = strs[0][i]
#         for s in strs:
#             if s[i] != ch:
#                 return strs[0][:i]
#     return strs[0][:min_len]
# ```
