"""
LeetCode 105. Construct Binary Tree from Preorder and Inorder Traversal / 从前序与中序遍历序列构造二叉树  (Medium)
Link: https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

题目描述
--------
给定二叉树的前序遍历 preorder 和中序遍历 inorder（节点值互不相同），
构造并返回该二叉树的根节点。

约束
----
- 1 <= preorder.length == inorder.length <= 3000
- -3000 <= Node.val <= 3000
- preorder, inorder 由同一棵二叉树的不同遍历得到

提示
----
卡住超过 25 分钟再去看 03_binary_tree/NOTES.md。
（思路：preorder 第一个是根；在 inorder 里找到根的位置后，左右两段递归构造）

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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
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
        (([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]), [3, 9, 20, None, None, 15, 7]),
        (([-1], [-1]), [-1]),
        (([1, 2], [2, 1]), [1, 2]),
        (([1, 2], [1, 2]), [1, None, 2]),
    ]
    passed = 0
    for i, ((pre, ino), expected) in enumerate(cases, 1):
        actual = to_levels(sol.buildTree(pre, ino))
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: pre={pre!r} in={ino!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
