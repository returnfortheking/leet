"""
LeetCode 106. Construct Binary Tree from Inorder and Postorder Traversal / 从中序与后序遍历序列构造二叉树  (Medium)
Link: https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

题目描述
--------
给定二叉树的中序遍历 inorder 和后序遍历 postorder（节点值互不相同），
构造并返回该二叉树的根节点。

约束
----
- 1 <= inorder.length == postorder.length <= 3000
- -3000 <= Node.val <= 3000

提示
----
卡住超过 25 分钟再去看 03_binary_tree/NOTES.md。
（思路：postorder 末尾是根；在 inorder 中定位根后切分两段；右子树先构建）

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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # TODO: 在这里写你的解法
        pass


def to_levels(root):
    if not root: return []
    from collections import deque
    out, q = [], deque([root])
    while q:
        node = q.popleft()
        if node is None:
            out.append(None)
        else:
            out.append(node.val)
            q.append(node.left); q.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out


def test():
    sol = Solution()
    cases = [
        (([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]), [3, 9, 20, None, None, 15, 7]),
        (([-1], [-1]), [-1]),
        (([2, 1], [2, 1]), [1, 2]),
        (([1, 2], [2, 1]), [1, None, 2]),
    ]
    passed = 0
    for i, ((ino, post), expected) in enumerate(cases, 1):
        actual = to_levels(sol.buildTree(ino, post))
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: in={ino!r} post={post!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
