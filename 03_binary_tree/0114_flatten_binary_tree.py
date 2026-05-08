"""
LeetCode 114. Flatten Binary Tree to Linked List / 二叉树展开为链表  (Medium)
Link: https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/

题目描述
--------
给定二叉树根 root，将其**原地**展开成一个"链表"：
- 展开后的链表使用 right 指针串联，left 指针全部置为 None
- 节点顺序与原树的**前序遍历**一致

约束
----
- 节点数 0 <= n <= 2000
- -100 <= Node.val <= 100

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
    def flatten(self, root: Optional[TreeNode]) -> None:
        """原地修改 root 为前序展开的"链表"。"""
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


def to_right_chain(root):
    """走 right 指针的链；同时检查所有 left 都为 None。"""
    out, node = [], root
    while node:
        if node.left is not None:
            return None         # 不合规
        out.append(node.val)
        node = node.right
    return out


def test():
    sol = Solution()
    cases = [
        ([1, 2, 5, 3, 4, None, 6], [1, 2, 3, 4, 5, 6]),
        ([], []),
        ([0], [0]),
        ([1, None, 2, None, 3], [1, 2, 3]),
        ([1, 2, 3, 4, 5, 6, 7], [1, 2, 4, 5, 3, 6, 7]),
    ]
    passed = 0
    for i, (vals, expected) in enumerate(cases, 1):
        root = build_tree(vals)
        sol.flatten(root)
        actual = to_right_chain(root) if root else []
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: vals={vals!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
