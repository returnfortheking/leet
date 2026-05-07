"""
LeetCode 236. Lowest Common Ancestor of a Binary Tree / 二叉树的最近公共祖先  (Medium)
Link: https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/

题目描述
--------
给定二叉树根 root 和两个节点 p、q（保证都在树中），返回它们的最近公共祖先。
LCA 定义：在二叉树中同时拥有 p 和 q 作为后代的最深节点（一个节点也可以是它自己的祖先）。

约束
----
- 节点数 2 <= n <= 10^5
- -10^9 <= Node.val <= 10^9
- Node.val 互不相同
- p, q 一定存在于树中

提示
----
卡住超过 25 分钟再去看 03_binary_tree/NOTES.md 的「LCA」模板。

复杂度（解完后填）
------
时间：O(?)    空间：O(?)

复盘要点（解完后填）
--------
- 卡在哪一步？
- 触发器：什么样的题面应该让我立刻想到这个套路？
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # TODO: 在这里写你的解法
        pass


def build_tree(vals):
    if not vals:
        return None
    from collections import deque
    root = TreeNode(vals[0])
    q = deque([root])
    i = 1
    while q and i < len(vals):
        node = q.popleft()
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i]); q.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i]); q.append(node.right)
        i += 1
    return root


def find(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    return find(root.left, val) or find(root.right, val)


def test():
    sol = Solution()
    cases = [
        # (tree, p_val, q_val, expected_val)
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1, 3),
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4, 5),
        ([1, 2], 1, 2, 1),
        ([1, 2, 3, 4, 5], 4, 5, 2),
    ]
    passed = 0
    for i, (vals, pv, qv, expected) in enumerate(cases, 1):
        root = build_tree(vals)
        p = find(root, pv); q = find(root, qv)
        ans = sol.lowestCommonAncestor(root, p, q)
        actual = ans.val if ans else None
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: p={pv} q={qv}  expected={expected}  actual={actual}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
