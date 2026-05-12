"""
LeetCode 94. Binary Tree Inorder Traversal / 二叉树的中序遍历  (Easy)
Link: https://leetcode.cn/problems/binary-tree-inorder-traversal/

题目描述
--------
给定二叉树的根节点 root，返回中序遍历（左 → 根 → 右）的节点值列表。

约束
----
- 节点数 0 <= n <= 100
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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # TODO: 在这里写你的解法
        res = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)

        dfs(root)
        return res


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
            node.left = TreeNode(vals[i])
            q.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            q.append(node.right)
        i += 1
    return root


def test():
    sol = Solution()
    cases = [
        # LeetCode 题面 example
        ([1, None, 2, 3], [1, 3, 2]),
        # 尺寸边界
        ([], []),
        ([1], [1]),
        # 完整二叉树
        ([1, 2, 3, 4, 5, 6, 7], [4, 2, 5, 1, 6, 3, 7]),
        # BST 中序 = 升序（自动验证遍历方向正确）
        ([5, 3, 8, 1, 4, 7, 9], [1, 3, 4, 5, 7, 8, 9]),
        # 左斜链（仅左孩子，深递归压栈测试）
        ([3, 2, None, 1], [1, 2, 3]),
        # 右斜链（仅右孩子）
        ([1, None, 2, None, 3], [1, 2, 3]),
        # 不规则深嵌套
        ([1, None, 2, 3, None], [1, 3, 2]),
        # 负值
        ([-1, -2, -3], [-2, -1, -3]),
    ]
    passed = 0
    for i, (vals, expected) in enumerate(cases, 1):
        actual = sol.inorderTraversal(build_tree(vals))
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(
            f"[{status}] Case {i}: tree={vals!r}  expected={expected!r}  actual={actual!r}"
        )
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
