"""
LeetCode XXXX. <题目英文名> / <题目中文名>  (Easy | Medium | Hard)
Link: https://leetcode.cn/problems/<slug>/

题目描述
--------
<把题目用自己的话简述一遍，方便回顾时不用切回浏览器>

约束
----
- 1 <= n <= 10^5
- ...

示例
----
输入：...
输出：...

思路
----
<一两句话讲清楚选哪个套路。例如：滑动窗口 + 哈希表统计字符出现次数>

复杂度
------
时间：O(?)    空间：O(?)

复盘要点
--------
- 卡在哪一步？
- 触发器：什么样的题面应该让我立刻想到这个套路？
"""

from typing import List, Optional


# 如果用到链表 / 二叉树，去掉下面的注释：
# class ListNode:
#     def __init__(self, val=0, nxt=None):
#         self.val = val
#         self.next = nxt
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def solve(self, *args, **kwargs):
        """改成 LeetCode 题目要求的方法名和签名。"""
        raise NotImplementedError


# ----------------------------------------------------------------------------
# 测试框架（无需第三方依赖；直接 `python <本文件>` 即可跑）
# ----------------------------------------------------------------------------
def test():
    s = Solution()

    # 用例：(args_tuple, expected)
    cases = [
        # ((nums, target), [0, 1]),
    ]

    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = s.solve(*args)  # ← 改成实际方法名
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: args={args!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases), "存在失败用例"


if __name__ == "__main__":
    test()
