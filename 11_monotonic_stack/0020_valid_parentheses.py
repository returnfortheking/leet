"""
LeetCode 20. Valid Parentheses / 有效的括号  (Easy)
Link: https://leetcode.cn/problems/valid-parentheses/

题目描述
--------
给定只含 '()[]{}' 6 种字符的字符串 s，判断是否合法配对：
- 左括号必须用相同类型右括号闭合
- 必须以正确顺序闭合（嵌套结构合法）

约束
----
- 1 <= s.length <= 10^4
- s[i] 仅来自 "()[]{}"

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
    def isValid(self, s: str) -> bool:
        # TODO: 在这里写你的解法
        stack = []
        pair = {")": "(", "]": "[", "}": "{"}
        for i in range(len(s)):
            if s[i] == ")" or s[i] == "]" or s[i] == "}":
                if not stack or pair[s[i]] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(s[i])
        return len(stack) == 0
        # for i, chr in enumerate(s):
        #     stack.append(chr)
        #     while stack:
        #         if chr == ")":
        #             if stack[-1] != "(":
        #                 return False
        #             else:
        #                 stack.pop()
        #                 i += 1
        #         elif chr == "]":
        #             if stack[-1] != "[":
        #                 return False
        #             else:
        #                 stack.pop()
        #                 i += 1
        #             i += 1
        #         elif chr == "}":
        #             if stack[-1] != "{":
        #                 return False
        #             else:
        #                 stack.pop()
        #                 i += 1
        #         else:
        #             break
        # if stack:
        #     return False
        return True


def test():
    sol = Solution()
    cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("(", False),
        ("]", False),
        ("", True),
    ]
    passed = 0
    for i, (s, expected) in enumerate(cases, 1):
        actual = sol.isValid(s)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: s={s!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()


# ============================================================================
# 复盘笔记（做完题再看；避免提前剧透）
# ============================================================================
# # 0020 有效括号 — 语法踩坑
#
# 主要是 Python 语法/语义层面三个错。算法思路（栈匹配）本身没问题。
#
# ## 1. `{(a,b), (c,d)}` 写成了 set 而不是 dict
#
# **错误写法**：
#
# ```python
# pair = {(")", "("), ("]", "["), ("}", "{")}   # ❌ 这是 set，装了 3 个 tuple
# pair[s[i]]                                    # TypeError: 'set' object is not subscriptable
# ```
#
# **根因**：`{a, b, c}` 是 **set**，`{k: v, k: v}` 才是 **dict**。区别就在**冒号**——脑子里想的是"`)`→`(`"，但手写成"两个一组用括号包起来"，结果变成 set of tuples。
#
# **改法**：
#
# ```python
# pair = {")": "(", "]": "[", "}": "{"}    # ✅ dict
# ```
#
# ## 2. `stack[-1]` 没防空栈
#
# **错误写法**：
#
# ```python
# if pair[s[i]] != stack[-1]:    # 输入 ")" 这种以右括号开头时，stack 空，IndexError
#     return False
# ```
#
# **根因**：访问 `[-1]` 前没判 stack 是否为空。算法层面的边界遗漏，不是 Python 特有的。
#
# **改法**：
#
# ```python
# if not stack or stack[-1] != pair[s[i]]:
#     return False
# ```
#
# `or` 短路保证只在 stack 非空时才访问 `[-1]`。
#
# ## 3. `return stack == None` 永远为 False
#
# **错误写法**：
#
# ```python
# return stack == None    # ❌ stack 是 list，[] == None 永远 False
# ```
#
# **根因**：空 list `[]` 和 `None` 是两个不同对象。`[] == None` 永远 False，所以函数会对所有"完美匹配"的输入返回 False。
#
# **改法**：
#
# ```python
# return not stack    # ✅ 空 list 是 falsy
# ```
#
# ## 修好后的完整代码
#
# ```python
# def isValid(self, s: str) -> bool:
#     stack = []
#     pair = {")": "(", "]": "[", "}": "{"}
#     for c in s:
#         if c in pair:                              # 右括号
#             if not stack or stack[-1] != pair[c]:
#                 return False
#             stack.pop()
#         else:                                      # 左括号
#             stack.append(c)
#     return not stack
# ```
#
# ## 触发器（什么题该想到栈）
#
# **"最近匹配 / 嵌套配对 / 撤销"** → 栈。括号匹配、表达式求值、撤销操作、"最近一个未配对的 X"，都是栈的信号。
